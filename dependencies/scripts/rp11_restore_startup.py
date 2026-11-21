#!/usr/bin/env python3
"""Start installed G1 runtimes against a disposable, network-isolated restore copy."""

import argparse
from contextlib import ExitStack, closing
import json
import os
from pathlib import Path
import pwd
import shutil
import sqlite3
import subprocess
import sys
from tempfile import TemporaryDirectory
import time
from urllib.error import URLError
from urllib.request import ProxyHandler, Request, build_opener
from uuid import uuid4

from rp11_backup import ROOT, inventory, verify

MODEL = "ollama/qwen3:4b-instruct-2507-q4_K_M"
RUNTIMES = ROOT / "development/venvs"


def docker(*args):
    return subprocess.run(
        ["/usr/bin/docker", *args], check=True, capture_output=True, text=True, timeout=30
    ).stdout.strip()


def read_task(directory):
    database = directory / "checkpoints.sqlite"
    with closing(sqlite3.connect(database.as_uri() + "?mode=ro&immutable=1", uri=True)) as db:
        db.row_factory = sqlite3.Row
        if db.execute(
            "SELECT 1 FROM localai_tasks WHERE state IN ('queued','running','cancelling') LIMIT 1"
        ).fetchone():
            raise RuntimeError("Recovered snapshot contains unfinished work")
        if db.execute("SELECT 1 FROM localai_delivery WHERE state='pending' LIMIT 1").fetchone():
            raise RuntimeError("Recovered snapshot has pending deliveries")
        rows = db.execute(
            """SELECT t.id,t.actor,t.chat,t.message,t.result FROM localai_tasks t
               JOIN localai_delivery d ON t.id=d.task_id
               WHERE t.state='completed' AND d.state='delivered' ORDER BY t.rowid DESC"""
        ).fetchall()
        return rows


def request(base, path, headers=None, decode=True):
    opener = build_opener(ProxyHandler({}))
    with opener.open(Request(base + path, headers=headers or {}), timeout=4) as response:
        return json.load(response) if decode else response.status


def await_ready(base, path):
    deadline = time.monotonic() + 75
    while time.monotonic() < deadline:
        try:
            if request(base, path, decode=False) == 200:
                return
        except (URLError, TimeoutError):
            time.sleep(0.5)
    raise RuntimeError("Restored service readiness did not pass for " + base)


def probe(scratch):
    langgraph = scratch / "langgraph"
    with closing(sqlite3.connect(
        (scratch / "webui/data/webui.db").as_uri() + "?mode=ro", uri=True
    )) as chats:
        eligible = {row[0] for row in chats.execute("SELECT id FROM chat")}
    tasks = [task for task in read_task(langgraph) if task["chat"] in eligible]
    if not tasks:
        raise RuntimeError("Restore has no completed task correlated to a saved WebUI chat")
    task = tasks[0]
    await_ready("http://127.0.0.1:8080", "/health")
    print("RESTORED_BIFROST_HEALTH=PASS", flush=True)
    await_ready("http://127.0.0.1:3000", "/ready")
    webui_key = (langgraph / "webui-api-key").read_text().strip()
    chat = request("http://127.0.0.1:3000", "/api/v1/chats/" + task["chat"],
                   {"Authorization": "Bearer " + webui_key})
    slot = chat["chat"]["history"]["messages"][task["message"]]
    if chat["user_id"] != task["actor"] or not slot["content"].endswith("\n\n" + task["result"]):
        raise RuntimeError("Restored WebUI chat and task result did not match")
    print("RESTORED_WEBUI_AUTHENTICATED_CHAT_READBACK=PASS", flush=True)
    await_ready("http://127.0.0.1:8010", "/ready")
    pipe_key = (langgraph / "pipe-api-key").read_text().strip()
    status = request("http://127.0.0.1:8010", "/tasks/" + task["id"],
                     {"Authorization": "Bearer " + pipe_key, "X-LocalAI-Actor": task["actor"]})
    if status["state"] != "completed" or status["result"] != task["result"]:
        raise RuntimeError("Restored LangGraph task status or result did not match")
    print("RESTORED_LANGGRAPH_TASK_READBACK=PASS", flush=True)


def stop_process(process):
    if process.poll() is not None:
        return
    process.terminate()
    try:
        process.wait(timeout=12)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait()


def stop_container(name):
    subprocess.run(
        ["/usr/bin/docker", "stop", "--time", "5", name],
        check=False, capture_output=True, timeout=20,
    )


def rehearse(bundle, recovered, destination, runtimes=RUNTIMES, supervisor=None):
    if os.geteuid() != 0 or "SUDO_UID" not in os.environ:
        raise RuntimeError("Run through sudo to access the private restore and Docker")
    if not ROOT.is_mount():
        raise RuntimeError("The installed Local AI application mount is unavailable")
    bundle = bundle.resolve(strict=True)
    recovered = recovered.resolve(strict=True)
    destination = destination.resolve(strict=True)
    runtimes = runtimes.resolve(strict=True)
    if supervisor is None:
        script = Path(__file__).resolve()
        supervisor = script.with_name("supervisor.py")
        if not supervisor.is_file():
            supervisor = script.parents[2] / "localai/supervisor.py"
    supervisor = supervisor.resolve(strict=True)
    if any(source == destination or source in destination.parents for source in (bundle, recovered)):
        raise ValueError("Choose a scratch destination outside both verification inputs")
    verify(bundle)
    verify(recovered)
    entries = inventory(recovered)
    if entries != inventory(bundle) or any("symlink" in item for item in entries.values()):
        raise ValueError("Restore copy differs from its backup or includes a symlink")
    operator = pwd.getpwuid(int(os.environ["SUDO_UID"]))
    inspect = json.loads((recovered / "bifrost/container.private.json").read_text())
    image = inspect["Image"]
    if not image.startswith("sha256:") or docker("image", "inspect", "--format", "{{.Id}}", image) != image:
        raise ValueError("The backed-up Bifrost image is not installed locally")
    config = inspect["Config"]
    env = config.get("Env") or []
    if any("=" not in item or "\r" in item or "\n" in item for item in env):
        raise ValueError("A Bifrost environment value cannot be replayed via an env file")
    live_id = docker("inspect", "--format", "{{.Id}}/{{.State.Running}}", "bifrost-g1")

    with TemporaryDirectory(prefix="rp11-runtime-", dir=destination) as temp, ExitStack() as stack:
        scratch = Path(temp)
        os.chown(scratch, 0, operator.pw_gid)
        scratch.chmod(0o710)
        for component in ("bifrost", "webui", "langgraph"):
            target = scratch / component
            shutil.copytree(recovered / component, target)
            for path in [target, *target.rglob("*")]:
                if component == "bifrost":
                    source = (bundle / path.relative_to(scratch)).stat()
                    os.chown(path, source.st_uid, source.st_gid)
                else:
                    os.chown(path, operator.pw_uid, operator.pw_gid)
        env_file = scratch / "bifrost.env"
        env_file.write_text("\n".join(env) + "\n")
        name = "localai-rp11-" + uuid4().hex[:12]
        options = []
        if config.get("User"):
            options.extend(("--user", config["User"]))
        if config.get("WorkingDir"):
            options.extend(("--workdir", config["WorkingDir"]))
        docker("run", "--detach", "--rm", "--pull=never", "--network=none", "--name", name,
               "--env-file", str(env_file), "--mount",
               f"type=bind,src={scratch / 'bifrost/data'},dst=/app/data",
               "--entrypoint", inspect["Path"], *options, image, *inspect["Args"])
        stack.callback(stop_container, name)
        pid = int(docker("inspect", "--format", "{{.State.Pid}}", name))
        if pid <= 0:
            raise RuntimeError("Restored Bifrost process did not start")
        namespace = ["/usr/bin/nsenter", "--target", str(pid), "--net"]
        user = [*namespace, "--setuid", str(operator.pw_uid), "--setgid", str(operator.pw_gid)]
        child_env = {"HOME": str(scratch / "webui"), "PATH": "/usr/bin:/bin",
                     "OFFLINE_MODE": "true", "DO_NOT_TRACK": "true",
                     "ANONYMIZED_TELEMETRY": "false", "LANGSMITH_TRACING": "false",
                     "DATA_DIR": str(scratch / "webui/data")}
        langgraph = scratch / "langgraph"
        for component, command, cwd in (
            ("webui", [str(runtimes / "open-webui/bin/open-webui"), "serve",
                       "--host", "127.0.0.1", "--port", "3000"], scratch / "webui"),
            ("langgraph", [str(runtimes / "langgraph/bin/python"), "-B", str(supervisor),
                          "--checkpoint-db", str(langgraph / "checkpoints.sqlite"),
                          "--gateway-key-file", str(langgraph / "bifrost-api-key"),
                          "--pipe-key-file", str(langgraph / "pipe-api-key"),
                          "--webui-key-file", str(langgraph / "webui-api-key"), "--model", MODEL], langgraph),
        ):
            log = stack.enter_context((scratch / (component + ".log")).open("w"))
            process = subprocess.Popen([*user, *command], cwd=cwd, env=child_env,
                                       stdout=log, stderr=subprocess.STDOUT, umask=0o077)
            stack.callback(stop_process, process)
        subprocess.run([*namespace, sys.executable, "-B", __file__, "--probe", str(scratch)],
                       check=True, timeout=250)
    if docker("inspect", "--format", "{{.Id}}/{{.State.Running}}", "bifrost-g1") != live_id:
        raise RuntimeError("The live Bifrost container changed during rehearsal")
    print("RP11_ISOLATED_STARTUP_AND_READBACK=PASS")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path)
    parser.add_argument("--recovered", type=Path)
    parser.add_argument("--scratch-in", type=Path)
    parser.add_argument("--runtimes", type=Path, default=RUNTIMES)
    parser.add_argument("--supervisor", type=Path)
    parser.add_argument("--probe", type=Path, help=argparse.SUPPRESS)
    args = parser.parse_args()
    os.umask(0o077)
    if args.probe:
        probe(args.probe)
    elif all((args.bundle, args.recovered, args.scratch_in)):
        rehearse(args.bundle, args.recovered, args.scratch_in, args.runtimes, args.supervisor)
    else:
        parser.error("--bundle, --recovered, and --scratch-in are required")


if __name__ == "__main__":
    main()

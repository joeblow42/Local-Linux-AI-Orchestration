#!/usr/bin/python3
"""Prepare the pinned Local AI Python environments for an existing G1 install."""

import argparse
import hashlib
import os
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import tarfile
import tempfile

MOUNT = Path("/mnt/local-ai-storage")
TRANSPORT_SHA256 = "db384cde5a107740d3f8dc0cdfb7e87f1e6e0f84cd3480b20e09d87b37c9d413"
COMPONENTS = ("langgraph", "open-webui")


def verify_transport(stream):
    digest = hashlib.sha256()
    for block in iter(lambda: stream.read(1024 * 1024), b""):
        digest.update(block)
    if digest.hexdigest() != TRANSPORT_SHA256:
        raise ValueError("Offline transport SHA-256 does not match this package")
    stream.seek(0)


def extract_inputs(stream, staging):
    with tarfile.open(fileobj=stream) as archive:
        for member in archive:
            path = PurePosixPath(member.name)
            if not (
                member.name == "runtime/python.tar.gz"
                or member.name in {f"evidence/{name}.lock.txt" for name in COMPONENTS}
                or len(path.parts) == 3 and path.parts[0] == "wheels"
                and path.parts[1] in COMPONENTS and path.suffix == ".whl"
            ):
                continue
            if not member.isfile() or path.name in {".", ".."}:
                raise ValueError("Unexpected member in the offline installation inputs")
            output = staging.joinpath(*path.parts)
            output.parent.mkdir(parents=True, exist_ok=True)
            with archive.extractfile(member) as source, output.open("xb") as target:
                shutil.copyfileobj(source, target)
    # The transport hash pins the nested upstream Python archive.
    subprocess.run(
        ["tar", "-xzf", str(staging / "runtime/python.tar.gz"), "-C", str(staging)],
        check=True,
    )


def stage(transport, parent):
    with transport.open("rb") as stream:
        verify_transport(stream)
        staging = Path(tempfile.mkdtemp(prefix="localai-fat-", dir=parent))
        try:
            extract_inputs(stream, staging)
            python = staging / "python/bin/python3.12"
            env = {
                **os.environ,
                "TMPDIR": str(staging),
                "PIP_CONFIG_FILE": os.devnull,
                "PIP_DISABLE_PIP_VERSION_CHECK": "1",
                "PIP_NO_CACHE_DIR": "1",
            }
            for name in COMPONENTS:
                runtime = staging / name
                subprocess.run([python, "-I", "-m", "venv", runtime], env=env, check=True)
                pip = [runtime / "bin/python", "-I", "-m", "pip", "--isolated",
                       "--no-cache-dir", "--disable-pip-version-check"]
                subprocess.run(
                    [*pip, "install", "--no-index", "--only-binary=:all:", "--require-hashes",
                     "--find-links", staging / "wheels" / name, "-r",
                     staging / "evidence" / f"{name}.lock.txt"],
                    env=env,
                    check=True,
                )
                subprocess.run([*pip, "check"], env=env, check=True)
            subprocess.run(
                [staging / "langgraph/bin/python", "-B",
                 Path(__file__).resolve().with_name("supervisor.py"), "--help"],
                stdout=subprocess.DEVNULL,
                check=True,
            )
            (staging / "TRANSPORT_SHA256").write_text(TRANSPORT_SHA256 + "\n")
        except BaseException:
            shutil.rmtree(staging)
            raise
    return staging


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("transport", type=Path)
    parser.add_argument("--stage-in", type=Path, required=True)
    args = parser.parse_args()
    parent = args.stage_in.resolve(strict=True)
    if os.geteuid() == 0:
        parser.error("Run staging as the operator, without sudo")
    if not MOUNT.is_mount() or MOUNT not in parent.parents or parent.stat().st_dev != MOUNT.stat().st_dev:
        parser.error("Stage in an existing directory on the mounted G1 application storage")
    if not parent.is_dir() or shutil.disk_usage(parent).free < 5 * 1024**3:
        parser.error("Staging requires an existing directory with at least 5 GiB free")
    try:
        result = stage(args.transport, parent)
    except (OSError, ValueError, subprocess.CalledProcessError, tarfile.TarError) as error:
        parser.exit(1, f"Offline staging failed: {error}\n")
    print(f"OFFLINE_STAGE_READY={result}")


if __name__ == "__main__":
    main()

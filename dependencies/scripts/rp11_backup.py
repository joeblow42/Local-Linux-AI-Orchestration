#!/usr/bin/env python3
"""Create and verify the private RP-11 backup of the three running G1 data owners."""

import argparse
from contextlib import closing
import json
import os
from pathlib import Path
import pwd
import shutil
import sqlite3
import stat
import tempfile

from rp05_g1_checkpoint import DATA, ROOT, docker, online_sqlite_copy, safe_copy_data, sha256, sqlite_format


def inventory(root):
    entries = {}
    for parent, dirs, files in os.walk(root, followlinks=False):
        for name in sorted(dirs + files):
            path = Path(parent) / name
            relative = path.relative_to(root).as_posix()
            if relative == "manifest.json":
                continue
            if path.is_symlink():
                entries[relative] = {"symlink": os.readlink(path)}
            elif path.is_file():
                entries[relative] = {"bytes": path.stat().st_size, "sha256": sha256(path)}
            elif not path.is_dir():
                raise ValueError("Backup contains an unsupported filesystem object")
    return entries


def verify(bundle):
    manifest = json.loads((bundle / "manifest.json").read_text())
    if manifest.get("format") != 1 or manifest.get("files") != inventory(bundle):
        raise ValueError("Backup manifest does not match the stored objects")
    required = {
        "bifrost/container.private.json",
        "webui/data/webui.db",
        "webui/.webui_secret_key",
        "langgraph/checkpoints.sqlite",
        "langgraph/webui-api-key",
        "langgraph/pipe-api-key",
        "langgraph/bifrost-api-key",
        "units/localai-open-webui.service",
        "units/localai-langgraph.service",
    }
    if not required <= manifest["files"].keys() or not any(
        name.startswith("bifrost/data/") for name in manifest["files"]
    ):
        raise ValueError("A required backup component is missing")
    return len(manifest["files"])


def copy_private(source, target):
    if source.is_symlink() or not stat.S_ISREG(source.stat().st_mode):
        raise ValueError("Expected a regular private configuration file")
    shutil.copy2(source, target)


def create(destination):
    if os.geteuid() != 0 or "SUDO_UID" not in os.environ:
        raise ValueError("Run as the Local AI operator through sudo")
    if not ROOT.is_mount():
        raise ValueError("The Local AI application mount is unavailable")
    destination = destination.resolve(strict=True)
    if not destination.is_dir() or destination.stat().st_dev == ROOT.stat().st_dev:
        raise ValueError("Choose a destination on independent backup storage")
    uid = int(os.environ["SUDO_UID"])
    home = Path(pwd.getpwuid(uid).pw_dir)
    development = ROOT / "development"
    webui = development / "open-webui"
    langgraph = development / "langgraph" / "data"
    inspect = json.loads(docker(["inspect", "--type", "container", "bifrost-g1"]))[0]
    mounts = inspect.get("Mounts", [])
    if not inspect.get("State", {}).get("Running") or len(mounts) != 1 or not any(
        mount.get("Source") == str(DATA) and mount.get("Destination") == "/app/data" for mount in mounts
    ):
        raise ValueError("Existing Bifrost mount or service state differs from the approved G1 layout")

    staging = Path(tempfile.mkdtemp(prefix="rp11-g1-", dir=destination))
    if staging.stat().st_uid != 0 or stat.S_IMODE(staging.stat().st_mode) != 0o700:
        raise ValueError("The backup filesystem cannot enforce a root-owned private directory")
    print(f"BACKUP_LOCATION={staging}", flush=True)
    for name in ("bifrost", "webui", "langgraph", "units"):
        (staging / name).mkdir(mode=0o700)
    (staging / "bifrost/container.private.json").write_text(json.dumps(inspect) + "\n")
    safe_copy_data(DATA, staging / "bifrost/data")
    safe_copy_data(webui / "data", staging / "webui/data")
    copy_private(webui / ".webui_secret_key", staging / "webui/.webui_secret_key")
    online_sqlite_copy(langgraph / "checkpoints.sqlite", staging / "langgraph/checkpoints.sqlite")
    for name in ("bifrost-api-key", "pipe-api-key", "webui-api-key"):
        copy_private(langgraph / name, staging / "langgraph" / name)

    units = home / ".config/systemd/user"
    for name in ("localai-open-webui.service", "localai-langgraph.service"):
        copy_private(units / name, staging / "units" / name)
        dropins = units / (name + ".d")
        for config in sorted(dropins.glob("*.conf")):
            target = staging / "units" / dropins.name
            target.mkdir(exist_ok=True, mode=0o700)
            copy_private(config, target / config.name)

    (staging / "manifest.json").write_text(json.dumps({
        "format": 1, "components": ["bifrost", "webui", "langgraph"], "files": inventory(staging)
    }, indent=2) + "\n")
    return verify(staging)


def restore(bundle, destination):
    bundle = bundle.resolve(strict=True)
    destination = destination.resolve(strict=True)
    if destination == bundle or bundle in destination.parents:
        raise ValueError("Restore destination must be outside the backup bundle")
    verify(bundle)
    recovered = Path(tempfile.mkdtemp(prefix="rp11-restore-", dir=destination))
    if recovered.stat().st_uid != os.geteuid() or stat.S_IMODE(recovered.stat().st_mode) != 0o700:
        raise ValueError("The restore filesystem cannot enforce a private directory")
    print(f"RESTORE_LOCATION={recovered}", flush=True)
    shutil.copytree(bundle, recovered, symlinks=True, dirs_exist_ok=True)
    count = verify(recovered)
    for component in ("bifrost", "webui", "langgraph"):
        inspected = 0
        for parent, _, files in os.walk(recovered / component, followlinks=False):
            for name in files:
                path = Path(parent) / name
                if path.is_symlink() or not path.is_file() or not sqlite_format(path):
                    continue
                # Verified snapshots already include committed WAL state.
                uri = path.as_uri() + "?mode=ro&immutable=1"
                with closing(sqlite3.connect(uri, uri=True)) as db:
                    if db.execute("PRAGMA quick_check").fetchone() != ("ok",):
                        raise ValueError(f"Restored {component} SQLite integrity check failed")
                    if component == "webui" and path.name == "webui.db":
                        db.execute("SELECT 1 FROM chat LIMIT 1").fetchone()
                    if component == "langgraph":
                        db.execute("SELECT 1 FROM checkpoints LIMIT 1").fetchone()
                        db.execute("SELECT 1 FROM localai_tasks LIMIT 1").fetchone()
                inspected += 1
        if not inspected:
            raise ValueError(f"No restored SQLite snapshots found for {component}")
        print(f"RESTORE_COMPONENT={component} SQLITE_VERIFIED={inspected}")
    print("RESTORE_LIMIT=FRESH_DIRECTORY_NO_SERVICE_START")
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--create", type=Path, metavar="BACKUP_DIRECTORY")
    mode.add_argument("--verify", type=Path, metavar="BUNDLE")
    mode.add_argument("--restore", type=Path, metavar="BUNDLE")
    parser.add_argument("--into", type=Path, metavar="EXISTING_RESTORE_DIRECTORY")
    args = parser.parse_args()
    if bool(args.restore) != bool(args.into):
        parser.error("--restore and --into must be used together")
    os.umask(0o077)
    if args.restore:
        count = restore(args.restore, args.into)
    elif args.create:
        count = create(args.create)
    else:
        count = verify(args.verify)
    print(f"RP11_BACKUP_MANIFEST_VERIFIED={count}")


if __name__ == "__main__":
    main()

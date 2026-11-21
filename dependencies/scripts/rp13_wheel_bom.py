#!/usr/bin/env python3
"""Inventory the two Release 1 wheel sets and collect embedded license notices."""

import argparse
from email import message_from_bytes
import json
from pathlib import Path, PurePosixPath
import shutil
import zipfile

from license_inventory import inspect_wheel

COMPONENTS = ("open-webui", "langgraph")


def notice_paths(archive):
    for member in archive.infolist():
        path = PurePosixPath(member.filename)
        name = path.name.upper()
        if member.is_dir() or path.is_absolute() or ".." in path.parts or "\\" in member.filename:
            continue
        if (any(part.lower() == "licenses" for part in path.parts[:-1])
                or name.startswith(("LICENSE", "LICENCE", "COPYING", "NOTICE"))
                or name in {"THIRD_PARTY_LICENSES.TXT", "THIRD-PARTY-NOTICES.TXT"}):
            yield member


def build(wheelhouse, output):
    artifacts = {}
    for component in COMPONENTS:
        wheels = sorted((wheelhouse / component).glob("*.whl"))
        if not wheels:
            raise ValueError(f"No locked wheels found for {component}")
        for wheel in wheels:
            info = inspect_wheel(wheel)
            if "error" in info:
                raise ValueError(info["error"])
            digest = info["sha256"]
            if digest not in artifacts:
                artifacts[digest] = (wheel, {**info, "components": [], "notices": []})
            artifacts[digest][1]["components"].append(component)

    output.mkdir()
    with zipfile.ZipFile(output / "wheel-notices.zip", "x", compression=zipfile.ZIP_DEFLATED) as notices:
        for digest, (wheel, item) in artifacts.items():
            with zipfile.ZipFile(wheel) as source:
                metadata = [name for name in source.namelist() if name.endswith(".dist-info/METADATA")]
                top_level = next(name for name in metadata if name.count("/") == 1)
                package = message_from_bytes(source.read(top_level))
                item["project_urls"] = [
                    str(value) for value in package.get_all("Project-URL", [])
                ]
                if package.get("Home-page"):
                    item["home_page"] = str(package["Home-page"])
                item["vendored_metadata"] = [
                    name for name in metadata if name != top_level
                ]
                for member in notice_paths(source):
                    target = f"{digest}/{member.filename}"
                    with source.open(member) as original, notices.open(target, "w") as copy:
                        shutil.copyfileobj(original, copy)
                    item["notices"].append(target)
    items = sorted((item for _, item in artifacts.values()), key=lambda item: item["artifact"])
    with (output / "wheel-bom.json").open("x") as stream:
        json.dump({"format": 1, "scope": "R1 Python wheels", "artifacts": items}, stream, indent=2)
        stream.write("\n")
    with zipfile.ZipFile(output / "wheel-notices.zip") as archive:
        if archive.testzip() is not None:
            raise ValueError("Notice archive failed readback")
        expected = {notice for item in items for notice in item["notices"]}
        if set(archive.namelist()) != expected:
            raise ValueError("Notice archive does not match the inventory")
    print(f"UNIQUE_WHEELS={len(items)}")
    print(f"EMBEDDED_NOTICE_FILES={len(expected)}")
    print(f"NO_RECOGNIZED_EMBEDDED_NOTICE={sum(not item['notices'] for item in items)}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("wheelhouse", type=Path)
    parser.add_argument("output", type=Path, help="New directory for the BOM and notice archive")
    args = parser.parse_args()
    build(args.wheelhouse, args.output)


if __name__ == "__main__":
    main()

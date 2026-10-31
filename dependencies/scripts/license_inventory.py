#!/usr/bin/env python3
"""Read metadata and license files from acquired wheels, without executing wheel code."""
import argparse
import csv
import email
import hashlib
import json
import pathlib
import zipfile

FLAG_TERMS = ("proprietary", "commercial", "unknown", "non-commercial", "business source", "sspl", "agpl")
def inspect_wheel(path):
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        metadata_names = [n for n in names if n.endswith(".dist-info/METADATA")]
        if len(metadata_names) != 1:
            return dict(artifact=path.name, error="Expected one METADATA")
        msg = email.message_from_bytes(z.read(metadata_names[0]))
        license_names = [n for n in names if ".dist-info/licenses/" in n or
                         n.upper().endswith(("/LICENSE", "/COPYING", "/NOTICE"))]
        license_expression = msg.get("License-Expression", "")
        license_text = msg.get("License", "")
        classifiers = [c for c in msg.get_all("Classifier", []) if c.startswith("License ::")]
        descriptor = " | ".join([license_expression, license_text, "; ".join(classifiers)])
        status = "REVIEW" if not descriptor.strip(" |;") or any(t in descriptor.lower() for t in FLAG_TERMS) else "CHECK_NOTICES"
        return dict(artifact=path.name, package=msg.get("Name", ""), version=msg.get("Version", ""),
                    license_expression=license_expression, license_metadata=license_text[:500],
                    license_classifiers="; ".join(classifiers), license_files="; ".join(license_names),
                    sha256=hashlib.file_digest(open(path, "rb"), "sha256").hexdigest(),
                    status=status)
def main():
    p = argparse.ArgumentParser()
    p.add_argument("wheelhouse", type=pathlib.Path)
    p.add_argument("--output", required=True, type=pathlib.Path)
    a = p.parse_args()
    if not a.wheelhouse.is_dir():
        p.error("wheelhouse is not a directory")
    rows = []
    for whl in sorted(a.wheelhouse.rglob("*.whl")):
        try:
            rows.append(inspect_wheel(whl))
        except (OSError, zipfile.BadZipFile) as ex:
            rows.append(dict(artifact=whl.name, error=str(ex), status="REVIEW"))
    a.output.parent.mkdir(parents=True, exist_ok=True)
    keys = ["artifact","package","version","license_expression","license_metadata",
            "license_classifiers","license_files","sha256","status","error"]
    with a.output.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(rows)
    print(json.dumps(dict(wheels=len(rows), flagged=sum(x.get("status") == "REVIEW" for x in rows), output=str(a.output))))
if __name__ == "__main__":
    main()

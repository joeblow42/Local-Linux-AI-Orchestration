#!/usr/bin/env python3
"""Offline IF-02 candidate fixture consistency checker; NOT a product or runtime test.

No network calls, no Open WebUI/LangGraph/Bifrost imports and no deployed service access.
The classifier below represents a *proposed oracle model*, not application code.
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

CONTROL = re.compile(r"task (status|cancel) ([A-Za-z0-9_-]{1,128})", re.ASCII)
ALLOWED_STATES = {
    "accepted", "running", "cancel_requested", "completed",
    "cancelled", "failed", "incomplete", "recovery_error",
}
TERMINAL = {"completed", "cancelled", "failed", "incomplete", "recovery_error"}


def classify(origin: str, text: str) -> tuple[str, str | None]:
    """An illustrative *strict* contract parser, not a deployable Pipe."""
    if origin != "user":
        return ("no_dispatch", None)
    match = CONTROL.fullmatch(text)
    if match:
        return (match.group(1), match.group(2))
    if text.lower().startswith(("task ", "/task ")) or text.lower() in {"task", "/task"}:
        return ("syntax_error", None)
    return ("submit", None)


def lifecycle(before: str, operation: str) -> tuple[str, bool | None, bool]:
    """Provisional externally visible cancellation semantics."""
    if before not in ALLOWED_STATES:
        raise ValueError("Unrecognized candidate state")
    if operation == "status":
        return (before, None, False)
    if operation != "cancel":
        raise ValueError("Unknown operation")
    if before in {"accepted", "running", "cancel_requested"}:
        return ("cancel_requested", True, False)
    return (before, False, False)


def verify(path: Path) -> dict:
    catalog = json.loads(path.read_text(encoding="utf-8"))
    failures = []
    seen = set()
    counts = {}
    cases = (
        ("command_cases", 23),
        ("lifecycle_cases", 11),
        ("fault_scenarios", 14),
    )
    for key, expected_count in cases:
        records = catalog.get(key)
        if not isinstance(records, list) or len(records) != expected_count:
            failures.append(f"{key}: expected {expected_count} fixtures")
            continue
        counts[key] = len(records)
        for item in records:
            name = item.get("id")
            if name in seen:
                failures.append(f"{key}: duplicate ID {name}")
            seen.add(name)
            if item.get("execution_status") != "NOT_RUN":
                failures.append(f"{name}: executable or passed status prohibited")
            if key == "fault_scenarios" and not (
                item.get("interface_id") in {"IF-02", "IF-06"}
                and item.get("independent_acceptance_predicate")
            ):
                failures.append(f"{name}: missing fault provenance or oracle")
    for item in catalog.get("command_cases", []):
        name = item.get("id")
        if not item.get("source_anchors"):
            failures.append(f"{name}: missing requirement/interface provenance")
        got = classify(item.get("message_origin", ""), item.get("input_text", ""))
        want = (item.get("expected_intent"), item.get("expected_task_id"))
        if got != want:
            failures.append(f"{name}: command model {got!r} != {want!r}")
    for item in catalog.get("lifecycle_cases", []):
        name = item.get("id")
        if not item.get("source_anchors"):
            failures.append(f"{name}: missing requirement/interface provenance")
        try:
            got = lifecycle(item["before"], item["operation"])
            want = (
                item["expected_after"], item["expected_cancel_accepted"],
                item["expected_new_step_allowed"],
            )
            if got != want:
                failures.append(f"{name}: lifecycle model {got!r} != {want!r}")
        except (KeyError, ValueError) as exc:
            failures.append(f"{name}: malformed lifecycle fixture: {exc}")
    for key, want in (
        ("owner_approved_direction", "LAI-OD-20261117-04"),
        ("schema_authority", "NOT_G_A_APPROVED"),
        ("requirements_authority", "NOT_G_R_APPROVED"),
        ("target_execution_state", "NOT_RUN"),
        ("g1_runtime", "OWNER_HOLD"),
        ("actual_pipe_implementation", "NOT_IMPLEMENTED"),
    ):
        if catalog.get(key) != want:
            failures.append(f"authority constraint {key}: required {want!r}")
    return {
        "status": "DESIGN_SELF_CONSISTENCY_PASS" if not failures else "FAIL",
        "counts": counts,
        "checked_command_cases": len(catalog.get("command_cases", [])),
        "checked_lifecycle_cases": len(catalog.get("lifecycle_cases", [])),
        "checked_fault_scenario_records": len(catalog.get("fault_scenarios", [])),
        "independently_observed_product_behavior": False,
        "installed_system_FAT": "NOT_RUN",
        "G_R": "NOT_APPROVED",
        "G_A": "NOT_APPROVED",
        "G1": "OWNER_HOLD",
        "failures": failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "catalog", nargs="?", type=Path,
        default=Path(__file__).with_name(
            "IF02_TASK_COMMAND_AND_LIFECYCLE_FIXTURES_CANDIDATE_20261117.json"
        ),
    )
    result = verify(parser.parse_args().catalog)
    print(json.dumps(result, sort_keys=True, indent=2))
    return 0 if result["status"] == "DESIGN_SELF_CONSISTENCY_PASS" else 1


if __name__ == "__main__":
    sys.exit(main())

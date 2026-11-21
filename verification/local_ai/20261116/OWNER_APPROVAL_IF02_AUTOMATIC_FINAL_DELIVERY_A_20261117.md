# IF-02 — Owner-approved Alternative A: automatic final-result delivery

**Decision ID (administrative new reference):** `LAI-OD-20261117-06`  
**Owner statement:** “A is approved,” responding to the explicit Release 1 IF-02 outcome question in [the bounded G-R/G-A review packet](./RP03_IF02_GR_GA_MINIMUM_REVIEW_PACKET_AND_FINAL_DELIVERY_DECISION_CANDIDATE_20261117.md).  
**Date:** 2026-11-17 (conversation continuation). **Authority level: owner-approved Release 1 acceptance direction only.**

## Approved Release 1 user experience

After the operator submits a delegated LangGraph task through the single trusted Open WebUI Pipe, the supervisor should promptly acknowledge its **durably accepted task ID**. When the task finishes, its terminal **synthesized result appears automatically in the original Open WebUI conversation**, without requiring the operator to issue a status/retrieval command. The previously approved `task status <id>` and `task cancel <id>` text controls remain available as fallback and for independent operator control.

The result must reflect actual terminal outcome; failure/cancellation/incompleteness is not a successful synthesized answer. The supervisor owns task identity/checkpoints; Open WebUI owns its conversation history. No additional Stop button or unnecessary dashboard is approved.

**Interpretation A, rather than B, is now selected.** On-demand-only final result retrieval is **not** an acceptable complete Release 1 outcome. This selection resolves the earlier IF-02 / `LAI-R1-N004-03` user-facing acceptance ambiguity.

## No implied technical certification

The owner has chosen the **outcome**, not an implementation. Tagged Open WebUI source has conditional message/event update pathways but **no verified guarantee** that a callback survives a closed Pipe response or UI/supervisor restart. Engineering must prove the automatic completion-to-original-conversation delivery path and recovery behavior in isolated, source-pinned tests before requesting G-R/G-A baseline approval and first-article acceptance.

Provisional implementation direction: first evaluate reuse of the pinned Open WebUI message/event mechanism with a narrowly scoped authorized completion delivery and a restart reconciliation strategy. Do not equate UI events with supervisor task durability, or add a second history database or uncontrolled polling daemon merely to make notification appear successful.

## Unchanged authorizations

- Earlier owner directions `LAI-OD-20261117-04` (single-Pipe text-control Alternative A) and `LAI-OD-20261117-05` (six provisional stop/self-termination directions) remain in force.
- G-R requirement text, controlled witness and baseline remain **NOT APPROVED**; G-A 19 original interface schemas, callback/HTTP/auth/status contracts remain **NOT APPROVED**. This decision is one accepted operator-facing acceptance direction.
- G1 runtime/data collection remains **OWNER HOLD**. No existing service should be contacted or changed.
- No Release 2 external API calls, hosted inference, Release 3 autonomy, additional Stop button, product deployment, or original FAT oracle execution authorized.
- PR #1 remains **open/draft/unmerged**. No merge, release, or CI success inferred from this approval.

## Immediate bounded next engineering action

Source-review and document the minimum **automatic final-result delivery** contract: task-ID to originating chat/assistant-message correlation; authenticated update path; delivery following Pipe response closure; idempotent final result; duplicate/stale update suppression; reconnection, restart, and checkpoint error outcomes. Keep the exact interface, retry/retention policy and runtime viability as verification subjects, not invented certainties.

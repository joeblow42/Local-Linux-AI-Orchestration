# Local AI Development — bounded RP-02 / RP-03 owner decision docket

**2026-11-16 — DRAFT FOR OWNER DIRECTION, NOT APPROVED G-R OR G-A.** Built after source-first independent review of all 136 original requirements and exact 28 candidate rewrites, deeper review of the 12 no-reword reported FAILs and targeted challenge of several QUESTIONED-only requirements. Original source text/hashes and historical IDs remain preserved. This docket is the controlled review path to avoid repeated candidate cycles or unjustified runtime infrastructure.

## Decision 1 — Release assignment for original requirements

**Question:** May the candidate release allocation of the **original 136** requirements be accepted as a controlled release-ownership direction, pending requirements wording/verification approval?

- **A (recommended):** R1 = 104, R2 = 17, R3 = 15. Keep original historical IDs (e.g., `LAI-R1-N014-01` retains its ID but its *current* assignment is R2). Treat release assignment separately from exact statement approval.
- **B:** Do not authorize candidate 104/17/15; owner identifies exceptions by original ID and intended release before G-R.
- **Material rationale:** A aligns the already approved R1 local-only, R2 two provider APIs and R3 unattended operation. Historical source says 121 R1 / 15 R2, but that predates the three-release decision.

**If A chosen:** update controlled release-assignment register only with owner decision reference; **do not** declare G-R accepted merely from allocation approval.

## Decision 2 — Unnecessary product subsystem elimination / requirement classification

**Question:** For Release 1, should qualified product obligations be verified through existing components and first-article instrumentation rather than new dedicated planner, profiler, edition detector and duplicated policy brokers?

- **A (recommended):** Retain validated resource, packaging, licensing, privacy and tool-authorization outcomes, but verify capacity/performance with existing FAT instrumentation; use installer preflight for storage budget, actual gateway/Ollama concurrency controls when supported, and one active tool grant gate. Propose retirement of `LAI-R1-N022-05` optional licensed-edition detection; move `LAI-R1-N023-05` acceptance thresholds to FAT specification; preserve `LAI-R1-N021-03` interface declaration and put separate redistribution-license clearance into package-release compliance. Preserve IDs/trace and review exact replacements at G-R.
- **B:** Retain original product-level module obligations, but require a source-specific implementation-necessity justification for each additional module before coding.
- **Material rationale:** Owner approved Bifrost OSS and a single-operator personal/family R1. Additional autonomous/billing/security infrastructure is not implicit. No legal clearance or basic FAT measurement is waived.

**If A chosen:** record classification and disposition as owner direction; the actual retirement/split/reclassification of original requirements still needs controlled text and trace approval at G-R.

## Decision 3 — Release 1 delegated UI-to-supervisor entry boundary

**Question:** Which interface should be the provisional integration target for the independently executable LangGraph supervisor, subject to pinned-version source/fixture verification?

- **A (recommended):** **One thin trusted Open WebUI Pipe** as the user-initiated delegated-model entry, calling a separate **localhost LangGraph HTTP service**. Pipe only translates request, displays status and final result; supervisor alone owns task IDs, checkpoints and cancellation. Direct model route remains Open WebUI → Bifrost → Ollama. This is an interface-selection direction, **not** approval to implement or freeze API.
- **B:** OpenAI-compatible endpoint of the independent LangGraph service presented as a model, **only** if exact target-version evidence establishes the required task status, cancellation and recovery controls with no additional custom UI or redundant adapter.
- **C:** Defer interface selection until source pin and an independent minimal experimental compatibility fixture. Does not imply both are required.
- **Material rationale:** Official Open WebUI documentation supports a Pipe as a selectable custom model and a trusted in-process extension. A generic chat-completions endpoint does not by itself prove a durable task-control plane. Open WebUI/LangGraph installed versions remain **Data unavailable**. Bifrost version 2.4.0 docs were read, but G1 is on hold.

**If A chosen:** carry as conditional G-A design direction; review the exact Pipe/event arguments under pinned Open WebUI version and supervisor API/status/cancel semantics before implementation.

## Outstanding evidence-dependent technical approvals (not requests for guessing)

- **26 remaining candidate rewrites:** 21 sustained, five refined; two earlier rewrites were judged unnecessary; targeted N023-02/N024-02 questioned-only anomalies may also need controlled amendments. This is **not yet** a final 136-row G-R acceptance package.
- **Verification parameters:** task state machine (including cancel/restart), 30-day sanitized metadata expiration without exceeding owner-approved retention, service readiness/health observations, rollback-supported scope and realistic host resource/storage/concurrency budgets. Fix exact criteria using pinned sources and measured evidence, not invented numbers.
- **G-A and FAT:** all 19 original interface IDs preserved; no field schema frozen. All 26 original oracles remain NOT RUN. G1 runtime OWNER HOLD active. FAT Alternative B requires an installed system demonstration and owner acceptance.
- **Current software baseline:** historic LiteLLM references in the main repository are superseded by owner-approved **Bifrost OSS**; no deployed service modifications or public distribution of original historical source archives.

## Proposed action sequence if owner chooses recommended alternatives

1. Record release assignment, nonessential-subsystem exclusion and one provisional IF-02 integration direction as owner decisions **without** automatic G-R/G-A baseline promotion.
2. Complete residual 96 QUESTIONED-only source/need quality review, explicitly reconcile two new targeted text candidates, and submit controlled 136-row exact wording/applicability/verification register for actual G-R approval.
3. Read/pin exact Open WebUI, LangGraph, Bifrost OCI and Ollama source/config versions **offline**, then refine IF-01/02/03/06 first and all other R1 IFs for G-A; defer R2/R3 implementation.
4. After independent G-R/G-A approval and explicit release of G1 hold, resume implementation and conduct genuine installed-system FAT; no hosted inference or paid calls in R1.

**OWNER DECISIONS UNRECORDED.** This text itself authorizes no release change, requirement deletion, integration implementation, runtime test, merge or spending.

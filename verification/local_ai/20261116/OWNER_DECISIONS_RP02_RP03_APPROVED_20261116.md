# Owner-approved engineering directions — RP-02/RP-03 (2026-11-16)

**Authority:** Owner explicitly responded **"A is approved for each"** to the three alternatives presented in [the candidate decision docket](./RP02_RP03_OWNER_DECISION_DOCKET_CANDIDATE_20261116.md). These are **approved directions**, *not* a G-R requirements baseline, G-A frozen interface schema, deployed implementation, or release of the G1 runtime hold. All previous owner approvals remain in force.

## LAI-OD-20261116-01 — Release assignment of 136 original requirements

**Decision: Alternative A — APPROVED.**

- **Release 1: 104** original requirements.
- **Release 2: 17** original requirements.
- **Release 3: 15** original requirements.
- Preserve **all historical requirement IDs** and original source bytes/hashes. An ID with `LAI-R1-` can have an approved **current release assignment R2**; a historical `LAI-R2-` requirement can be **R3**.
- This authorizes the **release-ownership assignment direction** for the 136 originals. It does **not** authorize the 26 remaining revised statements, classify all original statements as adequate, approve derived requirements, waive acceptance criteria, or declare G-R complete.
- Controlled scope index: [136 requirement ID/allocation index](./RP02_136_REQUIREMENT_SCOPE_INDEX_CANDIDATE_20261116.csv). Its contents represent now-approved **release assignment only**, while its old filename and the quality/rewrite annotations remain *candidate* historical engineering records; do not retitle or rewrite earlier evidence.

## LAI-OD-20261116-02 — Avoid unjustified Release 1 subsystems

**Decision: Alternative A — APPROVED.**

- Meet validated resource and capacity needs primarily through **existing toolchain, installer preflight and first-article verification**, not a new standalone resource planner/profiler/monitor daemon without separate demonstrated need.
- Use supported **Bifrost/Ollama concurrency controls** where verified to meet the target acceptance outcome, and **one active tool-capability admission gate** satisfying multiple trace IDs where appropriate.
- Retain packaging/licensing compliance: `LAI-R1-N021-03` interface declaration remains traceable, with redistribution permissions/notices verified as a **package-release compliance obligation**, rather than implementing a new runtime licensing subsystem.
- **Proposed at G-R, not yet retired:** `LAI-R1-N022-05` optional licensed-edition feature detection. **Proposed at G-R, not yet formally reclassified:** `LAI-R1-N023-05` FAT acceptance thresholds as verification specification. Preserve all original IDs and traceability.
- This decision does **not** waive necessary installation checks, capacity/resource acceptance, license terms, access-control/privacy requirements or independent FAT measurements.

## LAI-OD-20261116-03 — Provisional independent LangGraph entry point

**Decision: Alternative A — APPROVED AS PROVISIONAL ARCHITECTURAL DIRECTION.**

- A **single thin trusted Open WebUI Pipe** is the preferred user-initiated delegated entry, contacting a **separately executable localhost LangGraph HTTP service**. The Pipe is translation/presentation only; it does not own task scheduling, durable state, checkpoints, cancellation, or chat history.
- The independent LangGraph supervisor owns stable task IDs, workflow and role execution, truthful status, cancellation/recovery, and checkpoints. Open WebUI continues to own user-facing conversation history.
- The direct-chat path remains **Open WebUI → Bifrost OSS → Ollama** and must bypass the supervisor. Delegated inference goes via **Open WebUI → Pipe → independent LangGraph → Bifrost OSS → Ollama**.
- **Provisional** means subject to version-pinned source/API/Pipe compatibility, independent interface/oracle review and G-A authorization. **No competing second entry mechanism is required**, no implementation of the Pipe is authorized by this choice alone, and no claim of a tested target installation is implied.
- Protect Release 2 architectural seams AC-01 through AC-04 without creating R2 external-provider mocks/APIs in R1.

## Unchanged engineering gates

| Gate | Current status |
| --- | --- |
| Owner release-assignment direction | **APPROVED, 104 / 17 / 15** |
| Owner minimal-subsystem direction | **APPROVED** |
| Provisional IF-02 architecture choice | **APPROVED AS DIRECTION, subject to pinned-version proof** |
| G-R — exact wording/acceptance/trace baseline | **NOT APPROVED** |
| G-A — concrete interface producer/consumer schemas | **NOT APPROVED** |
| G1 gateway data collection and runtime verification | **OWNER HOLD** |
| External OpenAI/Anthropic paid API calls | **NOT AUTHORIZED** |
| RP-04 executed oracles / actual operational FAT | **NOT RUN** |
| Draft PR merge | **NOT AUTHORIZED** |

**Next permitted engineering increment:** independently adjudicate residual original QUESTIONED-only requirements, reconcile the *controlled* complete 136-row proposed wording/verification metadata, inspect version-pinned upstream source and historical evidence for IF-02 without touching the held runtime, and submit only genuinely material decisions to owner. Preserve original source artifacts unchanged.

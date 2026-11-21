# IF-02 — owner-approved interaction direction (2026-11-17)
**Decision ID:** `LAI-OD-20261117-04` (new continuation decision reference; administrative identifier only, not a requirement or interface ID).  
**Owner direction, verbatim:** "For Local AI Development IF-02, I approve Alternative A for the operator-visible task status and cancellation interaction direction. Preserve the pending G-R/G-A approval gates, G1 hold, and draft/unmerged PR restrictions. Proceed with the next bounded verification increment."

## Approved scope — control commands through one trusted Pipe
The selected alternative is **A** from [the RP-02–RP-04 continuation decision docket](./RP02_RP04_CONTINUATION_CHECKPOINT_20261116.md): use explicit text commands within the *single* trusted Open WebUI delegated Pipe for a user to query task status or request cancellation by stable task identifier. The Pipe translates user-initiated commands and invokes a separate local supervisor HTTP control plane. The independent LangGraph supervisor retains authority over task identity, committed state, cancellation acknowledgement, specialist execution, checkpoints and recovery. Open WebUI remains owner of conversation history. No mandatory additional graphical status/cancel adapter or duplicate scheduler/control subsystem is introduced.

**The examples** `/task status <task-id>` and `/task cancel <task-id>` were illustrative. Exact command spelling, parser, dispatch mechanism, endpoint schema, authentication, UI slash-command interaction and operator task visibility remain candidates for independent G-A review; they were not frozen by this approval. The model's generated or retrieved text must not acquire authority to issue task controls.

The "Stop generating" control in Open WebUI is *not* thereby proven equivalent to accepted LangGraph cancellation. A successfully submitted cancel request must be distinguishable from terminal `cancelled` state. Task status must be recovered from supervisor-owned durable data, not transient chat-status events.

## Unchanged gates and exclusions
- **G-R** exact requirements, 28 replacement texts, classifications and acceptance criteria: NOT APPROVED.
- **G-A** 19 concrete interface contracts, selected field names, statuses, error semantics and version compatibility: NOT APPROVED.
- **G1 runtime and data collection:** OWNER HOLD; no contact with deployed services or service changes.
- **RP-04** 26 original oracles (including one R1 conditional) and 13 draft falsification cases: NOT RUN; FAT Alternative B not performed or accepted.
- **Current R1** remains local-only Open WebUI → Bifrost OSS → Ollama, with delegated Open WebUI → one trusted Pipe → independently managed LangGraph → Bifrost → Ollama; no billable external requests or R2/R3 implementation.
- **PR #1** must remain open/draft/unmerged. This approval authorizes bounded **source/fixture design verification** only, not an implementation or G-A baseline promotion.

## Next bounded increment
Source-inspect Open WebUI v0.12.5 command-suggestion/pipe behavior and LangGraph 1.2.19 checkpoint semantics, then prepare a minimum candidate command/HTTP control contract with falsifiable offline fixture cases. Treat slash-command interference and cancellation/acknowledgement races as explicit risks. Maintain original IF-02 and oracle IDs.

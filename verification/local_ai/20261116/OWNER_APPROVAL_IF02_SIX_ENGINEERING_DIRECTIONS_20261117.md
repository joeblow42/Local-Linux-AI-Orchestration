# Owner approval — IF-02 six provisional engineering directions

**Owner approval:** 2026-11-17, owner reply **"approved, continue"** after assistant explained that the six listed items were provisional engineering recommendations, **not** a G-R requirements baseline, G-A interface baseline, release authorization or G1 hold release.
**Administrative reference:** `LAI-OD-20261117-05` (new approval-record label only; not a historical requirement/interface/oracle ID).
**Preapproval source:** [IF-02 stop/cancellation/self-termination candidate](./RP03_IF02_STOP_CANCEL_SELF_TERMINATION_G_R_G_A_REVIEW_CANDIDATE_20261117.md), prior source checkpoint [2026-11-17](./RP03_IF02_SELF_TERMINATION_REVIEW_CHECKPOINT_20261117.md).
**Earlier decision remains in force:** [LAI-OD-20261117-04](./OWNER_DECISION_IF02_TASK_CONTROL_A_APPROVED_20261117.md) — one trusted Open WebUI Pipe, text commands for operator-visible delegated-task status and cancellation.

## Six approved directions — authority limited to engineering review

| # | Direction | Interpretation |
| --- | --- | --- |
| 1 | Retain the single delegated Open WebUI Pipe and operator text controls | Existing approved Alternative A; no new task dashboard or second adapter |
| 2 | Use LangGraph's native graph completion/conditional END for task self-termination | Handle successful early completion and truthful failed/incomplete outcomes without a separate self-cancel service; no R3 unattended scheduler |
| 3 | Prefer a sequential two-specialist R1 workflow | Valid minimum happy path if both configured specialist roles actually execute; parallel execution is not required |
| 4 | Fence new work after durable cancellation acceptance | Do not imply an in-flight Ollama request instantly aborts; only later truthful terminal disposition may say cancelled |
| 5 | Do not require existing WebUI Stop→supervisor-cancel integration in R1 | Reuse WebUI Stop for its native response purpose; explicit task-ID command covers supervisor tasks; possible optional UI bridge needs later proof |
| 6 | Keep truthful distinct completion, cancellation, failure and incompleteness outcomes | Exact enum, partial-result definition, transition ordering and wire schema remain for G-R/G-A adjudication |

## Controls and exclusions

- **G-R:** 136 original requirement IDs/hashes and 28 rewording candidates remain **NOT APPROVED AS BASELINE**. No automatic acceptance of new requirements or changed historical records.
- **G-A:** 19 original interface IDs remain **UNFROZEN / NOT APPROVED**. These directions do not approve HTTP paths, status codes, syntax, task-ID encoding, checkpoint schema, saver implementation or terminal state vocabulary.
- **G1 runtime/data collection:** OWNER HOLD remains in effect; no target contact, restart, configuration changes or installed first-article test.
- **Original RP-04 oracle identities:** all 26 remain NOT_RUN; candidate checks are not evidence of actual product compliance.
- **GitHub PR #1:** open, draft, unmerged; no CI pass inferred; no merge or release baseline promotion.
- **Scope:** Release 1 local Ollama/Bifrost/Open WebUI + independent LangGraph, direct-chat bypass and delegated two-specialist operator workflow; no external provider calls (R2) or autonomous scheduling (R3).

## Next authorized work

Produce a compact, traceable IF-02 G-R/G-A **candidate approval packet** from original indexed requirements and interface identities, showing only unresolved concrete decisions and missing independent evidence. Do not proliferate unsupported mocks, implement an unfrozen protocol or demand redundant approvals for these six directions. Baseline sign-off requires a separately explicit owner decision.

# Local AI Development — RP-03 / IF-02 stop-vs-self-termination checkpoint

**Date label:** 2026-11-17. **Work completed:** source-anchored review and bounded G-R/G-A candidate reconciliation; no runtime/G1/product change.
**Base/source:** Previous validated PR #1 head `f3ab1188b199c93f252a694a7f4ea2f1735e83e4`; approved UX direction `LAI-OD-20261117-04` from [owner record](./OWNER_DECISION_IF02_TASK_CONTROL_A_APPROVED_20261117.md).
**New complete review candidate:** [IF-02 stop, cancellation and self-termination](./RP03_IF02_STOP_CANCEL_SELF_TERMINATION_G_R_G_A_REVIEW_CANDIDATE_20261117.md), commit `5d6a56c77093b27c342f662b4e0519d11ca6b108`.

## Source-verified distinctions

1. Open WebUI `Stop` terminates UI-managed response/stream; independent supervisor task cancellation is not thereby established. The approved single trusted Pipe already supplies a user-facing text mechanism for separate task-ID status/cancel requests, including after the initial response ends. No extra Stop button required in R1.
2. LangGraph 1.2.19 `StateGraph.add_conditional_edges` routes to `END`, and `set_finish_point` attaches END. For an already user-initiated R1 delegated task, native conditional branch-to-END meets the *self-termination mechanism* need without adding another REST self-cancel command or R3 unattended scheduler.
3. LangGraph `interrupt()` is for resumable pause, requires checkpointing and re-executes the node on resume. It is not the correct primitive for normal early completion or owner cancellation.
4. An early END does not by itself prove task success; supervisor-controlled outcome classification must distinguish satisfied work (`completed`), invalid prerequisites (`failed`/`incomplete`), and accepted operator stop (`cancelled`). Do not assert graph END kills parallel/in-flight work: R1 minimum may use a sequential two-specialist workflow and check exit conditions before starting each subsequent role.
5. Distinguish task-specific cancellation from stopping the LangGraph service. Service must remain running, and other tasks unchanged.

## Independent pinned-source static checks

Open-source immutable LangGraph target source: `langchain-ai/langgraph@5bd231cbfd913e05ebc662f519eb9a655bc766df`.

| Exact source / blob | Claims checked | Result |
| --- | --- | --- |
| `libs/langgraph/langgraph/graph/state.py` / `9a87f16fa91a794b2e9be09352c1cb03ae89a90d` | Conditional END routing, finish-point edge to END | 2/2 source guards PASS |
| `libs/langgraph/langgraph/types.py` / `8fba752a1d20d98721d2afcdfff8ee92dfa4c84b` | Resumable interrupt, node reexecution, saver requirement | 3/3 source guards PASS |
| `libs/checkpoint-sqlite/langgraph/checkpoint/sqlite/aio.py` / `a62a35473c05c4cf93b77e5fc787c890521d2bd0` | Saver existence, production-write cautions | 2/2 source guards PASS |

**Total 7/7 matched source claims.** Static source text checked, **no** LangGraph/SQLite/HTTP runtime tests, UI integration, deployed G1 verification or original FAT oracles performed. Earlier standalone fake-model 20/20 PASS is unchanged and does not become a product test.

## Requirements/interfaces and owner gate

The document contains exactly **six tightly scoped recommended G-R/G-A review directions**, not a frozen baseline: (1) existing single-Pipe text interaction, (2) native END self-termination, (3) minimal sequential R1 two-specialist happy path, (4) cancellation fence without promising immediate Ollama abort, (5) no mandatory WebUI Stop to supervisor bridge, (6) distinct truthful terminal outcomes. This recommendation set does not add R1 autonomy scheduling, another Stop button, another management service or a separate authorization subsystem.

Linked existing original requirement identities include `LAI-R1-N004-01/03/04`, `LAI-R1-N005-01`, `LAI-R1-N006-03/04`, `LAI-R1-N007-01/03`, `LAI-R1-N008-01/02/03/04`, `IF-02`, `IF-06`, and derived (unapproved) `GAP-R1-01/02`. The original 136 requirements, 19 interfaces, 26 original FAT oracle identities, 28 candidate rewrites and source hashes are unchanged. Original oracle statuses remain **NOT_RUN**.

**G-R requirements/acceptance:** NOT APPROVED. **G-A pinned interface/wire/supervisor status schema:** NOT APPROVED. Candidate `failed` versus `incomplete` distinction, WebUI Pipe actual command delivery, HTTP field semantics and stop/in-flight model cancellation require approval and real isolated verification; not established by this increment.

## Engineering stop point / authorized continuation

No new owner decision needed to preserve this source review. **Do not treat this candidate as owner approval of exact G-R or G-A.** The next meaningful work is an owner review of the six recommended directions, then a small isolated real frontend/Pipe/supervisor test after the relevant interface approval. Additional mock scenarios without real installed FAT evidence have diminishing value. G1 runtime/data-collection hold remains in force and needs separate owner release if required for deployment tests. PR #1 must remain DRAFT, OPEN, UNMERGED.

**Conversation safety:** safe to continue; all new findings, approvals and prior verified checkpoint are indexed in GitHub. Verify actual exact PR head and base before further changes.

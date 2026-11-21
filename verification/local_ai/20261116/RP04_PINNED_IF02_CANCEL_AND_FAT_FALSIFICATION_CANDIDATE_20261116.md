# RP-04 — source-pinned IF-02 cancellation and installed FAT falsification review
**2026-11-16 continuity date. CANDIDATE / NO TEST EXECUTION / NOT OWNER ACCEPTED.**  
**Starting PR HEAD:** `aca4a5171fae276c5ba1b9e72e4f570977ea07dd`. G-R/G-A not approved; G1 owner hold active; no paid provider call, installed-service change or first-article FAT.

## Original oracle identity accounting (all 26 preserved)
Derived from [original oracle identity index](./RP04_26_ORACLE_SCOPE_INDEX_CANDIDATE_20261116.csv) and [prior R1 positive/negative/recovery predicates](./RP04_R1_OPERATIONAL_FIRST_ARTICLE_ORACLES_CANDIDATE_20261116.md). **18 R1 unconditional, one R1_CONDITIONAL (F17 native tool call), six R2, one R3**; R1 total including conditional = 19.

| Original oracle ID | Original requirement trace | Target release | Review disposition | Execution |
|---|---|---|---|---|
| `GRGA07-F01` | `LAI-R1-N003-01` | R1 | Existing source-linked positive/negative witness | NOT RUN |
| `GRGA07-F02` | `LAI-R1-N003-03` | R1 | Existing source-linked positive/negative witness | NOT RUN |
| `GRGA07-F03` | `LAI-R1-N009-01` | R2 | Deferred to owner-assigned R2 release; no R1 test | NOT RUN |
| `GRGA07-F04` | `LAI-R1-N009-02` | R2 | Deferred to owner-assigned R2 release; no R1 test | NOT RUN |
| `GRGA07-F05` | `LAI-R1-N009-03` | R2 | Deferred to owner-assigned R2 release; no R1 test | NOT RUN |
| `GRGA07-F06` | `LAI-R1-N010-01` | R1 | Existing source-linked positive/negative witness | NOT RUN |
| `GRGA07-F07` | `LAI-R1-N010-02` | R1 | Existing source-linked positive/negative witness | NOT RUN |
| `GRGA07-F08` | `LAI-R1-N010-03` | R1 | Existing source-linked positive/negative witness | NOT RUN |
| `GRGA07-F09` | `LAI-R1-N011-03` | R1 | Existing source-linked positive/negative witness | NOT RUN |
| `GRGA07-F10` | `LAI-R1-N011-04` | R1 | Existing source-linked positive/negative witness | NOT RUN |
| `GRGA07-F11` | `LAI-R1-N012-04` | R1 | Existing source-linked positive/negative witness | NOT RUN |
| `GRGA07-F12` | `LAI-R1-N013-01` | R2 | Deferred to owner-assigned R2 release; no R1 test | NOT RUN |
| `GRGA07-F13` | `LAI-R1-N013-02` | R2 | Deferred to owner-assigned R2 release; no R1 test | NOT RUN |
| `GRGA07-F14` | `LAI-R1-N013-05` | R2 | Deferred to owner-assigned R2 release; no R1 test | NOT RUN |
| `GRGA07-F15` | `LAI-R1-N015-03` | R1 | Existing source-linked positive/negative witness | NOT RUN |
| `GRGA07-F16` | `LAI-R1-N016-02` | R1 | Existing source-linked positive/negative witness | NOT RUN |
| `GRGA07-F17` | `LAI-R1-N016-03` | R1_CONDITIONAL | Existing source-linked positive/negative witness | NOT RUN |
| `GRGA07-F18` | `LAI-R1-N016-05` | R1 | Existing source-linked positive/negative witness | NOT RUN |
| `GRGA07-F19` | `LAI-R1-N018-02` | R1 | Existing source-linked positive/negative witness | NOT RUN |
| `GRGA07-F20` | `LAI-R1-N008-01` | R1 | Existing source-linked positive/negative witness | NOT RUN |
| `GRGA07-F21` | `LAI-R1-N020-03` | R1 | Existing source-linked positive/negative witness | NOT RUN |
| `GRGA07-F22` | `LAI-R1-N020-04` | R1 | Existing source-linked positive/negative witness | NOT RUN |
| `GRGA07-F23` | `LAI-R1-N019-05` | R1 | Existing source-linked positive/negative witness | NOT RUN |
| `GRGA07-F24` | `LAI-R1-N021-02` | R1 | Existing source-linked positive/negative witness | NOT RUN |
| `GRGA07-F25` | `LAI-R1-N024-02` | R1 | Existing source-linked positive/negative witness | NOT RUN |
| `GRGA07-F26` | `LAI-R2-N026-03` | R3 | Deferred to owner-assigned R3 release; no R1 test | NOT RUN |

## Independent falsification specimens — draft labels, NOT new original oracle IDs
These extend the owner-approved R1 status/cancellation/checkpoint/restore outcome and are **not** executable acceptance baselines until G-R/G-A approval. The seven GAP-R1 derived gap witnesses remain separately unapproved. In particular, WebUI UI-cancel events are not evidence that LangGraph accepted or completed cancellation.

| Candidate fixture | Trigger | Expected observable outcome | Independent observer |
|---|---|---|---|
| `IF02-N01` | Supervisor stopped before submit | Reject without generated task ID or fabricated result | supervisor task store |
| `IF02-N02` | UI status event lost after accepted task | Same stable ID and durable status after reload | supervisor task ledger |
| `IF02-N03` | Cancel accepted during in-flight model generation | No next specialist/tool starts; acknowledged cancel not falsely called terminal | role-step log and task record |
| `IF02-N04` | Cancel arrives after task completed | Return prior completed state; do not retrospectively claim cancellation | committed task status/version |
| `IF02-N05` | Open WebUI Stop clicked while supervisor task active | No unproven LangGraph cancellation inferred; explicit true task status remains accessible | UI stop observation vs supervisor state |
| `IF02-N06` | Same Pipe receives a status/cancel task-ID control message (candidate UX) | Operator identity, known-ID gating and typed control result; unknown ID denied | pinned Pipe request signature and supervisor fixture |
| `IF02-N07` | HTTP status delayed/out of order | Older state cannot overwrite newer committed status | supervisor state version |
| `IF02-N08` | Connection drops after accepted task before acknowledgment | Retry does not create duplicate task; idempotency rule explicit | task records and retry correlation |
| `IF02-N09` | Pipe SSE error or truncated stream | No normal completed task without committed supervisor success | pinned stream path and state store |
| `IF03-N10` | Missing virtual key / model disallowed / backend unavailable | Zero unauthorized Ollama dispatch and no external fallback | gateway and upstream evidence after G1 hold release |
| `IF06-N11` | Supervisor restart after acknowledged checkpoint | Same task and graph thread recover last committed state | durable saver and task record |
| `IF06-N12` | Corrupt/missing checkpoint or incompatible saver revision | Explicit recovery error, no fabricated success or silent overwrite | isolated checkpoint fixture |
| `FAT-N13` | Clean target three-owner backup restore | History, delegated task/checkpoint and Bifrost local route independently usable | three persistent stores and operational local task |

All 13 fixtures are **NOT RUN**. For 12 source/fixture-only cases, no deployed G1 access is needed. IF03-N10's **target-gateway** claim cannot be tested while G1 is held; source/fixture review only until authorization. FAT-N13 requires an installed supported target and clean independent restore later; simulation cannot substitute for installed first-article evidence.

## Source-supported verification boundaries
- [Open WebUI v0.12.5 Pipe invocation](https://github.com/open-webui/open-webui/blob/f7ac7ee10962ddec0017f5c29b6740d9b9c5faca/backend/open_webui/functions.py) at commit `f7ac7ee10962ddec0017f5c29b6740d9b9c5faca` supports a single model-selectable trusted Pipe. Its emitted UI status and streaming data do **not** demonstrate durable task state or reliable cancel-by-ID.
- [Open WebUI v0.12.5 chat middleware](https://github.com/open-webui/open-webui/blob/f7ac7ee10962ddec0017f5c29b6740d9b9c5faca/backend/open_webui/utils/middleware.py) handles UI cancellation. Exact propagation to a separate LangGraph HTTP service must be independently specified; cannot presume generation Stop does it.
- [LangGraph 1.2.19 pinned graph checkpointer](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/graph/state.py) documents `thread_id` and saver; it does not create a task lifecycle HTTP API. Exact durable saver and `langgraph-checkpoint` dependency revision are not yet frozen.
- Bifrost tagged v2.4.0 documentation supports candidate gateway contract only. OCI source matching, installed configuration, SSE, error response and authorization behaviors need held-runtime release for an operational verdict.
- Integrated FAT Alternate B requires a real supported Bodhi 7 AMD64 offline `.deb`/complete transport install, direct local chat, two-specialist delegated task with status/cancel/restart, and independent three-owner local offline backup/restore readback. No external inference or R3 scheduler required.

## Owner decision and verification boundaries
**Not ready for G-R/G-A approval.** Exact IF-02 operator-visible task-control UX (same Pipe text command vs source-backed UI affordance), supervisor wire fields and idempotency, accepted-cancel race/terminal policy, concrete checkpoint saver, Bifrost source/deployed parity, original source authority and data-supported numeric thresholds remain. Do not infer arbitrary timeout/resource limits, execute a test, report PASS or merge draft PR.

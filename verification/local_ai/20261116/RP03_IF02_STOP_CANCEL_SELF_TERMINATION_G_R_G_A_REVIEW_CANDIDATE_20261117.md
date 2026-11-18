# RP-03 / IF-02 — Minimal stop, cancellation and self-termination G-R/G-A review candidate

**Date:** 2026-11-17. **Status:** SOURCE-REVIEWED CANDIDATE, NOT G-R/G-A APPROVED, NOT IMPLEMENTED, NOT FAT-EXECUTED.  
**Owner-approved interaction direction:** [LAI-OD-20261117-04](./OWNER_DECISION_IF02_TASK_CONTROL_A_APPROVED_20261117.md), one trusted Open WebUI Pipe with operator-visible status and cancellation text commands.  
**Starting exact verified PR head:** `f3ab1188b199c93f252a694a7f4ea2f1735e83e4`; current PR #1 must remain DRAFT/UNMERGED. **G1 owner hold** active.  
**Continuity:** [prior verified IF-02 source checkpoint](./RP03_IF02_FRONTEND_DELIVERY_AND_FAKE_SUPERVISOR_CHECKPOINT_20261117.md); [previous minimum HTTP draft](./RP03_IF02_TASK_COMMAND_HTTP_MINIMUM_CONTRACT_CANDIDATE_20261117.md). All historical source IDs and hashes retained.

## 1. Engineering disposition — reuse rather than duplicate

One verb, **stop**, describes different mechanisms and must not be implemented as an undifferentiated button/service.

| Initiator / action | Requested outcome | Owner of decision and durable evidence | Correct status implication | R1 implementation disposition |
| --- | --- | --- | --- | --- |
| User presses existing **Open WebUI Stop** during a direct chat | Stop active WebUI-managed generation | WebUI / original Bifrost and Ollama chat transport | No independent delegated-task cancellation inferred | **Reuse as is**, no duplicate UI |
| User selects delegated Pipe and enters an explicit **task cancel by ID** | Cancel an independently running or queued delegated task after WebUI response has finished | LangGraph supervisor control plane | `cancel_requested` on durable acceptance; `cancelled` only after final disposition | **Required candidate operator mechanism** under approved Alternative A |
| User presses existing **Open WebUI Stop** while delegated Pipe is replying | Stop WebUI-managed response; may or may not propagate to independent supervisor | WebUI initially, then only supervisor if a separately verified bridge exists | **Never infer supervisor cancellation** from UI Stop alone | **Optional integration** for R1, not substitute for task-ID control and not a separate button |
| **Delegated workflow determines objective is already satisfied** | Do not run unnecessary additional nodes; finish | LangGraph graph routing to `END`; supervisor records terminal disposition | `completed` only when completion predicates are met | **Native graph ending**, no cancel HTTP call |
| **Delegated workflow detects invalid/missing essential input or violated execution limit** | Do not continue defective work; preserve reason | LangGraph branch to `END` or internal failure handling; supervisor records reason | `failed` or `incomplete`, not `cancelled`; exact enum still G-A candidate | **Native graph termination + truthful terminal outcome**, no new management service |
| **Human approval/pause** (future if required) | Pause and later resume, not terminate | LangGraph `interrupt()` / checkpointer | Paused/interrupt state, **not terminal or cancelled** | Do **not** add mandatory R1 pause feature without separate need/authority |
| **Unattended future schedules** | Start tasks without a current user request | Release 3 persistent autonomous-operation control | Distinct from a condition that stops an already authorized R1 delegated task | **Excluded from R1**, no scheduler |

**Avoid unjustified hostile-actor complexity.** Required integrity here means a real operator command must reach the right task, and an actual failing specialist must not be shown as a successful completed task. R1 remains the owner-approved single-operator, locally administered trust perimeter; no duplicate authorization server, daemon or UI framework.

## 2. Pinned LangGraph source findings (not a running-product proof)

Exact upstream tag commit: [`langchain-ai/langgraph@5bd231cbfd913e05ebc662f519eb9a655bc766df`](https://github.com/langchain-ai/langgraph/tree/5bd231cbfd913e05ebc662f519eb9a655bc766df), candidate LangGraph 1.2.19.

- [`libs/langgraph/langgraph/graph/state.py`](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/graph/state.py), blob `9a87f16fa91a794b2e9be09352c1cb03ae89a90d`: `StateGraph.add_conditional_edges` (approximately lines 982–1016) documents routing to `END` to stop graph execution; `set_finish_point` (around 1114–1128) adds an edge to `END`. These are **normal graph-control primitives**, not a REST task cancellation API. For a simple sequential two-specialist R1 candidate, ensure a conditional guard selects the finish node/END **before launching another specialist**.
- [`libs/langgraph/langgraph/types.py`](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/types.py), blob `8fba752a1d20d98721d2afcdfff8ee92dfa4c84b`: `Command` around 833–860 can direct graph transitions; `interrupt()` around 896–920 explicitly raises a resumable graph interruption, requires a checkpointer and **reexecutes the node upon resume**. Do not implement normal completion or cancellation by conflating either with `interrupt()`.
- [`libs/checkpoint-sqlite/langgraph/checkpoint/sqlite/aio.py`](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/checkpoint-sqlite/langgraph/checkpoint/sqlite/aio.py), blob `a62a35473c05c4cf93b77e5fc787c890521d2bd0`: `AsyncSqliteSaver` implements asynchronous checkpoint persistence, but documentation cautions about high-throughput production writes. Single-user R1 SQLite remains **provisional**, requiring FAT write/restart/backup verification, not automatic PostgreSQL escalation.

**Boundary caveat:** Graph `END` routing is **not** a general process kill or cancellation of already running independent/parallel nodes. Use a simple serial R1 graph if it meets the two-role FAT; if any parallelism later exists, define precise fencing and join/termination behavior separately. The supervisor service must remain alive for unrelated tasks.

## 3. Minimal R1 task-lifecycle semantics for G-A review

Keep the previously approved *direction*; the names below are **provisional** and not a frozen wire schema.

1. **Submit:** owner-initiated request, one trusted Pipe → independent supervisor. Supervisor commits the task ID, operator identity, accepted state and correlation before the Pipe returns an acknowledgement. Do not keep the Pipe stream open for the entire workflow; pinned WebUI queues prompts during active generation. Distinguish supervisor task ID from WebUI generation/task IDs.
2. **Status:** an explicit status command queries supervisor-owned committed state and terminal reason, including restart/reconnect. WebUI chat history is a view, not a checkpoint store.
3. **Operator cancel:** one authenticated user task-control command → supervisor. Durable `cancel_requested` acknowledgement means new work is fenced; it does **not** prove an in-flight Ollama request was aborted, or claim terminal `cancelled` prematurely. A separately observable final disposition follows.
4. **Self-termination:** an already authorized workflow evaluates **bounded local stop conditions** at node boundaries, and routes to END (or failure handling) without issuing a user-level cancel command. Supervisor classifies outcome by cause: objective satisfied → completed; unsatisfied essential prerequisites → failed/incomplete. It records reason with task ID and committed revision.
5. **Service stop vs task stop:** stopping supervisor process is not a valid per-task cancel mechanism; restart must recover task records accurately. Task control must not stop unrelated tasks, Open WebUI, Bifrost or Ollama.
6. **No extra mandatory GUI:** WebUI's Stop remains for active generated responses, while the existing same-Pipe text command addresses background tasks. Optional future WebUI Stop→supervisor mapping needs its own source/fixture proof; no duplicate button.
7. **No R3 scope:** self-termination of a user-initiated R1 workflow does not imply persistent unattended scheduling or self-created tasks.

### Candidate mutually exclusive terminal classifications

| Condition observed | Proposed terminal disposition | Must never claim |
| --- | --- | --- |
| All required task acceptance criteria met; graph ends normally, possibly early | `completed` | That a missing required specialist's output was produced |
| Required source invalid, specialist failed, or work could not meet acceptance | `failed` or `incomplete`, reason retained | `completed`, absent actual validated result |
| Accepted operator cancellation fences successors; in-flight work resolved | `cancelled` | Instantaneous abort at time of cancel HTTP response |
| Completion committed before cancel request | Original terminal outcome remains; cancel not accepted | Retroactive cancellation |
| Merely `interrupt()` paused awaiting human response | Nonterminal interrupted/awaiting-input if supported by later baseline | `cancelled`, `failed`, or `completed` by default |
| UI Stop was pressed on separate WebUI response without supervisor propagation proof | Supervisor status unchanged/unconfirmed | A terminal supervisor cancellation |

**Not yet resolved by source-only evidence:** deterministic distinction `failed` versus `incomplete`; early END routing when concurrent roles are active; precisely what constitutes accepted cancellation during an already-in-flight inference; preservation of source/user identity through selected Pipe; exact HTTP response fields and status codes. These belong in G-R/G-A approval with explicit acceptance tests.

## 4. Candidate G-R acceptance predicates linked to *existing* identities

All are **candidate witnesses**, **not new historical requirements or approved baseline replacements**.

| Existing requirement / derived scope | Minimum positive witness | Negative/early-stop witness |
| --- | --- | --- |
| `LAI-R1-N004-01`, `N004-03/04` | WebUI delegated turn produces a supervisor-accepted stable ID, and completed two-specialist result is displayed via the same Pipe | Service down → explicit unavailable, no fabricated task ID/completion; stopped response does not silently claim supervisor cancellation |
| `LAI-R1-N005-01` and `N006-03/04` | A successful user-initiated workflow actually exercises at least **two different specialist roles**, preserving each result/failure | A deliberate internal early-exit before role 2 must **not** masquerade as a successful two-role FAT; failure/incomplete reason visible |
| `LAI-R1-N007-01/03` | Task ID persists across status, end, restart; second submitted task has a distinct ID | UI and supervisor task IDs never incorrectly substituted; unknown task fails cleanly |
| `LAI-R1-N008-01/02/03/04` | Committed checkpoint and final disposition survive supervisor restart/backup readback | Missing/corrupt checkpoint and paused vs ended states never falsely reported completed |
| Derived `GAP-R1-01` status, `GAP-R1-02` cancellation | Status and operator cancellation available through one selected Pipe, even after original submit response ends | Cancel accepted ≠ terminal; in-flight call cannot allow new specialist steps after acknowledged cancel |
| `IF-02`, `IF-06` interfaces | Separate supervisor status/cancel vs native END/pause; no second durable owner | Open WebUI Stop and LangGraph `interrupt()` not silently treated as per-task cancellation |

**Original oracle inventory:** 26 IDs retained: 18 unconditional R1, one conditional R1, six R2 and one R3. All NOT_RUN and NOT_APPROVED. Supplemental cases are not replacements for those oracle identities.

## 5. Narrow G-R/G-A reviewer choices — proposed, not approved

| Review question | Recommended candidate | Alternative and reason to defer |
| --- | --- | --- |
| **R1 operator interaction** | Retain approved Alternative A: status/cancel through one selected Pipe, text commands without mandatory new graphical control | Mandating a new UI button/modification adds version-specific complexity without proved user need |
| **R1 self-termination** | Graph native conditional END / finish point; supervisor publishes truthful end reason; no HTTP self-cancel round trip | Reentering same supervisor cancellation API from within graph to represent success/failure conflates semantics |
| **R1 graph execution** | Minimum sequential two-specialist happy path; inspect stop conditions before next step | Parallel specialist cancellation/write race burden unnecessary unless needed for a requirement |
| **R1 model request cancellation** | Fence subsequent workflow steps immediately after durable cancel acknowledgement, record in-flight inference as unresolved until safe terminal disposition | Promise instant force-abort of all Ollama inference requests before pinned API/runtime proof |
| **Existing Open WebUI Stop** | Reuse for active direct chat and stream Stop; leave mapping to independent task cancel **optional**, subject to later evidence | Automatically mapping Stop to supervisor task cancel without verified linkage could cancel wrong task or claim cancellation incorrectly |
| **Status taxonomy** | Maintain clear completed / cancelled / failed (and incomplete as needed), backed by durable reason/version; exact enum and response format require G-A | Single generic `stopped` obscures difference between operator cancel and defective work |

**No new owner direction is required to continue source-only documentation.** Approval of this table as the *controlled G-R/G-A baseline* **does** require the designated owner review. Do not implement, merge, freeze schema, release G1 or promote requirement texts based on this candidate document.

## 6. Next justified engineering action

Present this as the single **IF-02 G-R/G-A micro-approval docket**, with source limits and explicit owner decisions before building more mocks. When approved, build one tiny isolated **real** pinned UI/Pipe/supervisor/checkpointer fixture (not G1) and test a normal two-specialist task, early successful END, early incomplete END, status, cancel and restart. Confirm first-party dependency locks and offline packaging before release.

**Current verdict:** The approved single-Pipe Alternative A remains sound; it already provides the operator UI for background task cancellation. Graph self-termination is a separate ordinary graph-flow responsibility, not a new Stop button or supervisor service. G1 hold, G-R/G-A gates and draft/unmerged PR boundaries remain intact.

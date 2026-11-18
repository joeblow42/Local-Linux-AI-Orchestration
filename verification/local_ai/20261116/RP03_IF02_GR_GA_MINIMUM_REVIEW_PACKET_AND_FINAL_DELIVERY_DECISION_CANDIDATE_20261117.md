# RP-03 / IF-02 — Minimum G-R/G-A review packet and final-result delivery decision

**Date:** 2026-11-17. **Authority:** CANDIDATE PACKET ONLY; **NO** G-R or G-A baseline approval, G1 release, target-system test, external provider integration, release acceptance or PR merge.  
**Current owner engineering directions:** [LAI-OD-20261117-05](./OWNER_APPROVAL_IF02_SIX_ENGINEERING_DIRECTIONS_20261117.md) approves six provisional engineering directions; [LAI-OD-20261117-04](./OWNER_DECISION_IF02_TASK_CONTROL_A_APPROVED_20261117.md) approved a single trusted Pipe with operator text controls.  
**Read-back trace:** [Six-direction crosswalk](./RP03_IF02_SIX_APPROVED_DIRECTIONS_GR_GA_CROSSWALK_CANDIDATE_20261117.json), independently resolved to existing 136 original requirement identities, 19 original interface identities, 26 original FAT oracle identities and the 136 owner-approved release assignments. The six directions reference 14 unique original requirements, **not** 14 new requirements.  
**Last verified pre-packet PR HEAD:** `80841c73fb401a46ca4f96482e520f7add1ab7e4`.

## 1. What is settled, and what is not

**Approved as engineering direction:** one trusted Open WebUI Pipe; explicit operator text status/cancel commands; independent LangGraph service owns task IDs, durable state and cancellation; sequential two-specialist R1 normal path; LangGraph native conditional `END` for internally decided completion/failure; cancellation acceptance fences successor steps; Open WebUI Stop is not required to cancel an independent LangGraph task; distinct truthful task dispositions.

**Still unapproved:** G-R replacement wording, full owner-approved acceptance predicates, IF-02 / IF-06 exact message schemas, status/error codes and terminal enum, actual pinned-install compatibility, and any new R1 obligation beyond existing needs. Do not interpret these approvals as authority to create a new Stop button, duplicate scheduler, privilege-management daemon, a R3 autonomous initiator or any paid API integration.

**Self-termination is not a second cancellation service.** Already running, operator-authorized workflows may route to `END` based on their internal stop condition. Validated outcome achieved → completed; invalid essential input or missing specialist evidence → failed/incomplete (disposition rules still G-R/G-A candidate). LangGraph `interrupt()` is a **resumable pause** and must not automatically mean cancelled. Graph `END` does not force-abort already running parallel model requests.

## 2. An actual unresolved G-R acceptance interpretation: final answer delivery

The [RP-02 136-row acceptance matrix](./RP02_136_ACCEPTANCE_AND_APPLICABILITY_REVIEW_CANDIDATE_20261116.csv) associates `LAI-R1-N004-03` with a *candidate* witness that the synthesized delegated response reaches the **initiating Open WebUI conversation**, while the independently managed LangGraph service retains the durable task data. This statement does **not** explicitly determine **when** or **whether automatically** the final result must appear.

The approved first-turn architecture also needs the Pipe to finish its initial answer promptly with a durable task ID, because pinned Open WebUI may queue subsequent task status/cancel commands while an assistant response is still generating. These create two meaningfully different experiences:

| Owner interpretation | Operator experience | R1 technical implications | Recommendation |
| --- | --- | --- | --- |
| **A — Automatic final-result delivery, with manual status fallback** | Submit delegated task; receive task ID promptly; completed synthesized answer subsequently appears in the originating chat without needing a status request; `task status`/cancel commands remain available | Requires **separately verified** safe, durable asynchronous completion→WebUI message delivery or update without creating another UI or ownership store. Must truthfully handle UI/connector restart and duplicate/late completion. Existing event emitter source supports some chat-message updates but **does not prove** reliable post-response or post-restart delivery. | **Preferred for end-user usability if a narrow pinned mechanism is demonstrably reliable**; has higher integration and recovery cost |
| **B — On-demand result retrieval using existing text controls** | Submit delegated task, receive stable task ID; operator enters `task status <id>` (or final retrieval command, if accepted) when ready and the final result is displayed **in that chat** | Simple existing Pipe→supervisor lookup; no independent callback into WebUI history; task state persists across disconnect. Operator must remember to check and might miss a finished result. | **Lowest complexity**, but materially less convenient for a fully functioning first article |

**This choice is not authorized by the six approved directions.** Do not quietly interpret B as equivalent to A. Option A is not already technically proven and must not be promised as automatic after service restart absent an independent callback/replay mechanism. A dedicated graphical Stop button is **not** a consequence of choosing A.

**Owner decision requested only for the intended Release 1 acceptance behavior, not an implementation permission**: choose A, B, or explicitly defer until the source/fixture feasibility analysis is complete. Until selected, treat `LAI-R1-N004-03` witness as **G-R OPEN**.

## 3. Pinned Open WebUI evidence on message updates

Target source candidate: `open-webui/open-webui` tag `v0.12.5`, immutable commit `f7ac7ee10962ddec0017f5c29b6740d9b9c5faca`.

- [`backend/open_webui/socket/main.py`](https://github.com/open-webui/open-webui/blob/f7ac7ee10962ddec0017f5c29b6740d9b9c5faca/backend/open_webui/socket/main.py), source blob `1338308fb6d77f96532229b5d3444bcb3c5605d7`: `get_event_emitter(request_info, update_db=True)` supplies message-related UI events and, when a valid saved chat/message is present and DB updating is enabled, `message`/`replace` branches can update stored Open WebUI message content (approx. lines 1596–1724). **This proves conditional handler behavior in source, not a guaranteed durable asynchronous return path after the Pipe response ends.**
- [`backend/open_webui/functions.py`](https://github.com/open-webui/open-webui/blob/f7ac7ee10962ddec0017f5c29b6740d9b9c5faca/backend/open_webui/functions.py), blob `20601fee7e42e69f7d21bb452c740ec4c3df96f9`: Pipe gets `__event_emitter__` only for eligible request metadata and a declared Pipe signature. The emitter is not, by itself, an independently persisted callback subscription or delivery ledger.
- [`src/lib/components/chat/Chat.svelte`](https://github.com/open-webui/open-webui/blob/f7ac7ee10962ddec0017f5c29b6740d9b9c5faca/src/lib/components/chat/Chat.svelte), blob `438c173eb91833192d822d15d6ecaa76f3b99e15`: queue behavior while a prior response generates (approx. lines 4001–4028) and WebUI Stop behavior (4621–4672).
- A fresh independent source-snippet verification of these three immutable blobs matched **13/13 expected snippets**. **Source-guard only:** not UI testing, not callback execution, not API integration, not an installed system FAT.

Do not design automatic delivery by silently creating a background polling daemon, copying entire chat history into supervisor state, or treating transient UI emitter events as the durable task source of truth. If A is selected, start with one bounded prototype using existing source-supported message update facilities and independently test lost/late/duplicated deliveries.

## 4. Minimal G-A candidate semantics after the outcome decision

| Contract | Producer / consumer | Minimum invariant | Status |
| --- | --- | --- | --- |
| `IF-02` submit acknowledgement | Open WebUI selected Pipe → independent supervisor | Server-authenticated actor + bounded request; supervisor commits stable task ID/state/version before the Pipe acknowledges and finishes the WebUI response; no duplicate accepted task on safe retry | CANDIDATE; real UI/Pipe fixture NOT RUN |
| `IF-02` status and final | Pipe → supervisor authoritative task state; Pipe → WebUI presentation | Unknown ID or unavailable checkpoint never yields completed; final synthesized response must reach initiating conversation according to owner-selected A or B | **MATERIAL G-R CHOICE OPEN**; no actual delivery test |
| `IF-02` cancellation | One user-issued task-ID control → supervisor | Durable cancellation acceptance distinct from eventual terminal; prevent new specialist steps; unrelated task unaffected; WebUI Stop not automatically mapped | CANDIDATE; real cancel race NOT RUN |
| `IF-02` normal self-end | LangGraph configured node/conditional edge → END; supervisor classifies outcome | Objective achieved can be completed early; invalid essential input yields failed/incomplete; incomplete two-specialist FAT cannot be falsely counted passed | APPROVED ENGINEERING DIRECTION; G-R/G-A enum and acceptance still unapproved |
| `IF-06` persistence | LangGraph saver + supervisor-owned metadata | Acknowledged durable state/restart readback, no invented success on corrupt checkpoint; control ID distinct from Open WebUI generation task | CANDIDATE; actual saver and restart NOT RUN |
| `IF-01` direct bypass | Open WebUI → Bifrost OSS → Ollama | Open WebUI native Stop for direct mode; supervisor not invoked in direct chat; no paid provider fallback | OWNER SCOPE APPROVED; target tests NOT RUN |

**Authorization/source boundaries:** only the real authenticated user and present user turn can initiate task-control side effects. The model's assistant output, retrieved text and client-provided actor fields are not control authority. Single-operator local-only R1 does not require a separately administered enterprise authorization service.

## 5. FAT and source trace

- Original requirement IDs untouched. The crosswalk links all six directions to 14 existing R1 requirements with original source hashes and candidate positive/negative witnesses. Release 1 allocation remains 104 of 136 original requirements, R2 17, R3 15.
- All 19 original interface IDs retained, statuses `UNFROZEN_CANDIDATE`, G-A `NOT_APPROVED`.
- All 26 original FAT oracle IDs retained, `NOT_RUN`, with original R1 vs R2 vs R3 classifications. **`GRGA07-F20` traces to `LAI-R1-N008-01` (durable checkpoint) and is not an original cancellation oracle.** Supplemental derived cancellation `GAP-R1-02` still awaits G-R controlled acceptance; do not invent a new historical ID or report it executed.
- Pinned Open WebUI, LangGraph and Bifrost source reviews are **not** evidence that the deployed offline image, actual selected Pipe, checkpoint saver or installed Bodhi 7 R1 app passes. G1 hold remains active; no false CI result.
- Real isolated non-G1 integration testing is the next justified source-to-implementation verification after **appropriate G-A authority**, not more in-memory mocks.

## 6. Gate disposition

**IF-02 micro-review: evidence sufficient to expose one material owner-level acceptance interpretation; not sufficient for G-R or G-A baseline promotion.** Present only that user-facing final-result delivery question for owner decision. The six earlier approved directions do **not** need another approval. No need to request control over generic task self-termination conditions or a new Stop UI.

**Owner decision is pending only on A vs B for final-result delivery**; do not block other lawful source-only analysis. Once settled, reconcile `LAI-R1-N004-03` G-R witness and minimal IF-02 response presentation contract, then seek formal G-R/G-A baseline approval when evidence is sufficient. Preserve G1 hold and draft/unmerged PR #1.

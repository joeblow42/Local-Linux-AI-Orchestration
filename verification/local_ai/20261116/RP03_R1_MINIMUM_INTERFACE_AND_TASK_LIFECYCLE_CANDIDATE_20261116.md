# RP-03 — bounded Release 1 direct/delegated interface contract and decision readiness

**2026-11-16, CANDIDATE / NOT G-A APPROVED.** This is a *logical* interface data dictionary and failure-semantics preparation record. It **does not** select an Open WebUI or LangGraph version, freeze API payloads, implement adapters, amend the approved architecture, test G1, or authorize hosted inference.

## Exact source and supplemental research

- Original `interface_contracts_original_candidate_rev0_3.csv` inside 2026-11-14 Phase I v3 controlled input: **19 interface IDs**, R1 direct/supervisor/chat/checkpoint boundaries and originally proposed request/response/negative semantics. Original IF-04/IF-BUDGET hosted and IF-SCHED/IF-AGENT autonomous release labeling is superseded **for scope only** by later owner R1/R2/R3 decisions. Preserve all original records and IDs.
- Owner-approved R1 direct chat `Open WebUI → Bifrost OSS → Ollama`; delegated `Open WebUI → independent LangGraph → Bifrost OSS → Ollama`; UI owns chat history; supervisor owns durable tasks/checkpoints; at least one operator-initiated two-specialist useful workflow with status/cancellation/recovery.
- **Versioned Bifrost source**, `maximhq/bifrost` commit `e869c3f9adc96ea53c38694a21bb04a8e1085487`, [virtual-key documentation](https://github.com/maximhq/bifrost/blob/e869c3f9adc96ea53c38694a21bb04a8e1085487/docs/features/governance/virtual-keys.mdx) exact blob `8024a9d008ade34b547979142b290c3940b04a03`: documents `x-bf-vk`, OSS inference auth enforcement, permitted-provider model enumeration, and `/v1/chat/completions`. This is **documentary support**, not a successfully observed call on the target pinned OCI image.
- **Unpinned Open WebUI docs**: [Functions](https://docs.openwebui.com/features/extensibility/plugin/functions/), [Pipe](https://docs.openwebui.com/features/extensibility/plugin/functions/pipe/), [events](https://docs.openwebui.com/features/extensibility/plugin/development/events/). A Pipe appears as a model; a Pipe can relay requests to an independent service; status events are ephemeral UI aids, not durable task data. The docs also warn that Functions execute trusted Python inside Open WebUI. **Version-specific compatibility unverified**.
- LangGraph [persistence](https://docs.langchain.com/oss/python/langgraph/persistence) and [interrupt](https://docs.langchain.com/oss/python/langgraph/interrupts) docs: checkpoints require an identity such as `thread_id`; interruption/pause semantics do **not** automatically implement an external cancellation endpoint or task-status API. **Version and saver not pinned**.

## Minimum producer/consumer contract — IF-01, IF-02, IF-03, IF-06

| Boundary | Producer responsibility | Consumer responsibility | Data ownership and hard negative |
| --- | --- | --- | --- |
| **IF-01 direct** | Open WebUI submits a selected local model, session-scoped authorized messages and request correlation through documented Bifrost inference interface; UI saves user-facing messages | Bifrost verifies local virtual key and allowed model route, then dispatches to Ollama or returns explicit typed denial | Direct mode **must not invoke LangGraph**. A blocked request must not trigger silent alternate provider, synthetic completion or hosted fallback |
| **IF-02 submit** | An operator-selected delegated UI entry submits permitted request projection, UI conversation *reference*, client correlation, and requested task intent; the adapter contains no independent scheduler | Independent LangGraph **allocates** stable task ID, persists accepted task identity, and acknowledges it | Supervisor owns task/role status and checkpoints; UI owns chat history. No fabricated task ID or full chat archive replication. A transient Pipe completion is not a durable supervisor acceptance |
| **IF-02 status** | UI adapter asks using stable task ID; optional status events improve responsiveness only | Supervisor returns current **durably derived** task state and evidence of progress/version | UI is a viewer; it must not overwrite recorded supervisor state based on stale event. Unknown task returns explicit not-found/error, never completed |
| **IF-02 cancel** | Authenticated operator requests cancel by task ID | Supervisor decides whether task is still nonterminal, records a cancellation request/ack, and prevents initiation of later specialist/tool steps once accepted | Acceptance of cancellation is **not** proof that an in-flight Ollama generation immediately stopped. Do not report normal task success after accepted cancellation |
| **IF-02 final** | UI fetches/displays the supervisor's terminal outcome and optional synthesized response | Supervisor returns consolidated successful roles, traceable incompleteness, or typed failure/cancel/recovery error | Chat transcript is stored by UI; final supervisor result is not a second conversation archive |
| **IF-03 delegated model call** | Supervisor specialist supplies bounded task/role correlation, requested allowed Bifrost model identity and context | Bifrost performs key/model admission and local Ollama routing, reports measured or UNKNOWN usage and error | LangGraph must not call Ollama directly or treat a model's self-reported policy clearance as trusted; denied key/model = **zero upstream dispatch** |
| **IF-06 checkpoint** | LangGraph commits task/thread mapping, state transitions and checkpoint version in a selected durable local saver | Checkpoint store acknowledges persistence before supervisor marks data durable; recovered task resumes/reconciles according to approved transition contract | Unreadable/missing checkpoint is **recovery error**, not completed. A UI message or uncommitted event never substitutes for persistence |

**Candidate identity dictionary**, semantically required but **not** frozen field names: `conversation_reference` (UI-owned; opaque, do not copy entire archive), `task_id` (supervisor-issued stable public identifier), `thread_id` (LangGraph checkpoint mapping, possibly internal), `request_correlation` (cross-boundary safe metadata), `specialist_role_id` (task role), `selected_model`, `gateway_dispatched_model`, `backend_resolved_model` (model IDs; distinguish UNKNOWN), `task_status` (supervisor-owned), `state_version` or committed record identity (for stale-state detection), `cancel_request_id` (idempotent operator request correlation), `sanitized_error_code` (typed, not a traceback).

## Candidate task lifecycle — not a frozen enum

1. Operator requests delegated task; if accepted, supervisor durably assigns a task ID in an **accepted/nonterminal** state.
2. Supervisor enters **running** and executes a bounded multi-step workflow of at least two configured local specialist roles; each Bifrost request references its task and role.
3. Successful run yields **completed** with a synthesized response; specialist failure yields a truthful **failed** or explicitly **partial/incomplete** disposition according to a future accepted state contract. **Do not invent partial-as-success policy.**
4. Cancel request to a nonterminal task receives an acknowledgement distinct from a terminal **cancelled** state. Once accepted, no subsequent specialist/tool step starts. An upstream model call already in flight may finish or be aborted if supported, but its return cannot silently finalize the cancelled task as normally complete.
5. Supervisor restart must recover committed state and resume/reconcile safely; missing/corrupt checkpoint => **recovery error**. For a repeated step, record durable step identity and avoid duplicating permitted local tool side effects through a bounded replay policy. No general transactional execution framework is authorized.
6. Terminal task status does not create autonomous background scheduling for R1. A live accepted task may outlive one UI session due to recovery; this is **not** an R3 recurring scheduler.

**Open design decisions needing proof, not guessing:** exact status vocabulary; cancel-race ordering; task ID / thread ID mapping; permitted partial response; retry bounds; in-flight stream termination; checkpoint saver and migration; schema fields and wire error envelopes. Until clarified, **do not freeze** G-A or claim implementation.

## Minimum Open WebUI entry-point choice

**Recommended candidate:** **one thin project-owned Pipe → separate localhost LangGraph HTTP service** for delegated tasks, *plus* the existing direct Open WebUI-to-Bifrost path. The Pipe acts only as translation/presentation; LangGraph remains independently executable and testable. It should contain no business workflow engine, durable task store, provider billing machinery or separate conversation history. The project must review trusted Pipe source since it executes inside Open WebUI.

**Alternative:** OpenAI-compatible LangGraph endpoint presented as a model. It may simplify basic message exchange, but independently supported task status, cancellation, background in-session recovery and durable acknowledgement are **not documented as automatically provided** by generic chat completions. No obligation to implement *both* alternatives.

**Selection remains provisional** pending pinned Open WebUI version/source, an independent status/cancel adapter contract review and owner G-A authorization. Avoid building a custom task dashboard when Open WebUI controls and modest status events suffice.

## Independent negative/recovery oracle docket — NOT RUN

| ID | Falsification case | Independent observation needed |
| --- | --- | --- |
| IF02-N01 | Supervisor down during submit | No fake task ID, result or success; UI displays failure |
| IF02-N02 | Status event received but checkpoint not durable | Persisted supervisor status must win over transient UI event |
| IF02-N03 | Cancel accepted while model call running | No later specialist/tool step starts; eventual task state is truthful, never false success |
| IF02-N04 | Cancel arrives after terminal commit | Cancellation not silently marked accepted; original terminal state retained |
| IF02-N05 | UI refresh/disconnect during task | Same task ID and actual state accessible when UI reconnects |
| IF06-N06 | Checkpoint unavailable/corrupted | Explicit recovery error; no invented completion or silent creation of a duplicate task |
| IF06-N07 | Restart during step with local tool | Replay decision traceable; do not automatically duplicate tool side effect |
| IF03-N08 | Gateway key or model unauthorized | Error and **zero** Ollama dispatch; no hosted fallback |
| IF01-N09 | Direct chat request | No LangGraph task creation or supervisor invocation |
| IF03-N10 | Backend unavailable or SSE truncated | Explicit provider/stream failure; never report normal completed response |

These are verification **design obligations** requiring source-supported parameter limits and later controlled execution; they do not establish a mock-only external provider implementation or an installed-system test PASS.

## Gate disposition

- **R1 design:** AC-01 Bifrost common route, AC-02 model identity, AC-03 future external secret boundary, AC-04 future policy insertions are owner-approved directions. R2 adapters and R3 schedulers are not R1 implementation prerequisites.
- **IF-04/IF-BUDGET** hosted paid API integration is R2; **IF-SCHED/IF-AGENT** autonomous/external agent implementation is R3. Historical interface IDs remain unchanged.
- **G-A remains BLOCKED** pending exact pinned Open WebUI/LangGraph versions, concrete transport/status/cancel fields and error semantics, independently reviewed oracles and owner approval.
- **G1 runtime OWNER HOLD** remains active. No service change, gateway call, paid provider call, or installed-system assertion occurred in this review.

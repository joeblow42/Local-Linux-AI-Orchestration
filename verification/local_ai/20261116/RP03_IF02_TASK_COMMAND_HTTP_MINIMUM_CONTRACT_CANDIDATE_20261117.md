# RP-03 / IF-02 — minimum single-Pipe task-command and HTTP control-plane contract
**Date:** 2026-11-17. **State:** CANDIDATE DESIGN ONLY; NOT G-A APPROVED / NOT G-R APPROVED / NOT DEPLOYED.  
**Owner direction:** [LAI-OD-20261117-04](./OWNER_DECISION_IF02_TASK_CONTROL_A_APPROVED_20261117.md): operator-visible text commands through **one trusted Pipe**, separate local LangGraph HTTP service. **Exact syntax and endpoint fields remain unapproved.**  
**Starting verified PR head:** `fecffc700d959d8c4be83ce0447b4a7181203469`; PR #1 stays draft/unmerged. G1 runtime/data-collection OWNER HOLD.

## 1. Source-first command-delivery finding (material)
- The owner-approved alternative used *illustrative* syntax `/task status <task-id>` and `/task cancel <task-id>`. Source at [Open WebUI v0.12.5 tag commit `f7ac7ee10962...`](https://github.com/open-webui/open-webui/tree/f7ac7ee10962ddec0017f5c29b6740d9b9c5faca) shows a frontend slash-command suggestion mechanism:
  - [`src/lib/components/chat/MessageInput.svelte`](https://github.com/open-webui/open-webui/blob/f7ac7ee10962ddec0017f5c29b6740d9b9c5faca/src/lib/components/chat/MessageInput.svelte), blob `bafec0644a19cb993e52227e266fa1747ddb08c8`, checks slash-style suggestion handling and may consume selected commands.
  - [`src/lib/components/chat/MessageInput/Commands/SlashCommands.svelte`](https://github.com/open-webui/open-webui/blob/f7ac7ee10962ddec0017f5c29b6740d9b9c5faca/src/lib/components/chat/MessageInput/Commands/SlashCommands.svelte), blob `92b6d92aef8dbae70e33b145b1d8b3bdf74d9b26`, lists built-in slash commands including `/status`. This **does not** prove `/task ...` is consumed, but means sending it unchanged is not established.
  - [`backend/open_webui/functions.py`](https://github.com/open-webui/open-webui/blob/f7ac7ee10962ddec0017f5c29b6740d9b9c5faca/backend/open_webui/functions.py), blob `20601fee7e42e69f7d21bb452c740ec4c3df96f9`: registers active Pipes as selectable models and invokes `pipe(**params)`, passing only signature-requested special arguments. `__user__`, `__chat_id__`, `__message_id__`, and `__event_emitter__` may be supplied; emitter is conditional on metadata.
- **Smallest candidate refinement consistent with owner A:** provide plain text controls **without slash**, namely `task status <opaque-id>` and `task cancel <opaque-id>` when the delegated Pipe model is selected. The exact parser and frontend passage still need fixture verification; this is **not** a new owner decision or a frozen G-A command schema.
- If `/task ...` reaches the Pipe during future source/fixture tests, it must fail with an explicit syntax/help response rather than be submitted as a new delegated inference task; do not assume that every UI slash suggestion is a Pipe command.

## 2. Minimal parser and scope (CANDIDATE, not implementation)
**Source of control authority:** a *direct, authenticated operator* user turn in Open WebUI selected delegated mode. The Pipe must not parse instructions from prior assistant/tool content, retrieval results, model completions, the full conversation history, or untrusted input metadata as task-control commands. Only the immediate last user message is eligible and must exactly match the reserved grammar.

- Canonical *proposed* exact-match grammar: `task (status|cancel) <task_id>`, where `<task_id>` is an opaque token of 1–128 ASCII letters, digits, underscore or hyphen. These character/length limits are **test candidates**, not owner-approved requirements.
- No mixed command+prompt text, trailing whitespace, embedded newline, case-insensitive alias or multiple actions in one message. Reserved `task ...` and `/task ...` malformed/unsupported forms cause a syntax error, **never** an accidental newly accepted supervisor workflow.
- All other direct user prompts in the delegated mode follow the ordinary **submit** path; resulting model-generated text cannot invoke the supervisor control endpoint. The Pipe routes control commands separately from inference/worker orchestration.
- Open WebUI retains user-facing chat history; only the supervisor stores its task/role/checkpoint records. Pipe status display can use a plain assistant response or supported ephemeral UI events, but events cannot substitute for authoritative supervisor status.

## 3. Minimal logical HTTP interactions (not frozen URLs, status codes or field names)
These are suggested **logical** operations between one Pipe and one independently managed local supervisor service; no extra adapter, dashboard, scheduler or service registry.

| Operation | Candidate transport | Producer | Required independent consumer fact | Critical negative |
| --- | --- | --- | --- | --- |
| **Submit** | `POST /tasks` | Trusted Pipe translates one explicit user task and bounded authorized context, opaque chat reference, stable request identity and user identity supplied by WebUI server | Supervisor durably accepts task, allocates stable `task_id`, committed state/version, returns acknowledgement | Supervisor unavailable, malformed input or lost acceptance acknowledgement cannot fabricate success or a second task |
| **Status / result** | `GET /tasks/{task_id}` | Pipe sends authenticated task lookup | Supervisor responds with committed state and `state_version`; includes final result only if that terminal outcome actually exists | Unknown ID or unavailable/checkpoint-corrupt task cannot yield completed |
| **Request cancellation** | `POST /tasks/{task_id}/cancel` | Pipe forwards direct operator control with idempotent request identity | Supervisor atomically resolves cancel vs terminal commit ordering; reports **cancel accepted** separately from eventual `cancelled` | UI Stop, transport disconnect or cancel request sent is *not* proof of cancellation accepted, model abort or terminal cancellation |

**Local administration:** use the existing single-operator Open WebUI authenticated identity plus a narrowly held local service credential/IPC boundary where required; no duplicate enterprise permission system. Never trust a user-supplied `actor_id` in the message or expose gateway/UI keys in chat or diagnostics. If deployed as containers, verify the actual service namespace/address: `localhost` inside a container is not automatically the host's loopback; only approved local-only connectivity is permitted.

**Candidate response semantic fields**, not wire-format approval: `task_id` stable, `task_state`, `state_version` from committed supervisor record, `request_id` for retry/idempotency, `source_conversation_ref` opaque, `result` if truly terminal successful, sanitized `error_code` if failed. The supervisor may map its stable task ID directly to LangGraph `thread_id` or store one small durable association. Do not recreate the UI's whole chat archive. Logged usage absent from producer remains **UNKNOWN**, not invented.

## 4. Cancel/terminal race and restart invariants (NOT G-A FROZEN)
- **State candidates:** `accepted`, `running`, `cancel_requested`, `completed`, `cancelled`, `failed`, `incomplete`, `recovery_error`; final enums and partial-result policy remain for G-A/G-R.
- A successful **cancel acknowledgement** requires a durable supervisor decision; it does not mean the in-flight Ollama call stopped. Once cancellation accepted, no subsequent specialist/tool step is started. Its eventual terminal `cancelled` is only reported after a true final disposition, not upon HTTP receipt.
- **Linearization:** if the terminal completion commit precedes cancellation, cancellation is rejected/not accepted and terminal result preserved. If cancellation commits first, normal completed finalization is prohibited, even if the already-in-flight inference returns. Duplicate cancel returns recorded status, with no duplicate side effect or regressed state.
- Status lookup is a read of the supervisor's committed version. Stale UI status events and delayed HTTP responses may not overwrite a later state. A missing/corrupt checkpoint must not appear as `completed`.
- Retry-after-lost-submit-ack must correlate to the **same** accepted task ID through a stable operator/request identity. The source of stable WebUI message and conversation IDs must be proven in selected pinned build; do not invent guaranteed persistence from one API field.
- LangGraph `thread_id` and a durable saver support checkpoints, not a built-in user-facing task-control HTTP API. Tagged LangGraph 1.2.19 source and same-tree `langgraph-checkpoint==4.3.1`/`langgraph-checkpoint-sqlite==3.1.3` are only **compatible source candidates**, not a chosen deployment configuration.

## 5. Candidate error and privacy outcomes
- Unknown/missing task: explicit not-found or invalid-control response; no new task.
- Unauthorized operator/task control: denied with no task state mutation. No generic second authorization service.
- Supervisor down/timeout: clear unavailability; never normal completion.
- Stale revision/terminal cancel conflict: return current committed terminal status with `cancel_accepted=false`, not false successful cancellation.
- Incomplete stream/UI disconnect: operator can use status command to recover the same task; do not rely on transient Pipe stream for task identity or correctness.
- Retained diagnostic records stay sanitized; do not log source prompt, full response or keys. Enforce separate 30-day sanitized-metadata retention, not purge chat history.

## 6. Traceability and offline oracle plan
- Original requirement anchors: `LAI-R1-N004-01..04` supervised interaction; `LAI-R1-N007-01..04` task ID; `LAI-R1-N008-01..05` checkpoint/recovery; `LAI-R1-N017-01..03` data ownership. Derived cancellation `GAP-R1-02` remains **unapproved candidate**, not a new historical requirement ID.
- Original interfaces `IF-02` and `IF-06` remain unchanged; `IF-01` direct chat stays bypass, `IF-03` local gateway inference unchanged.
- [Fixture catalog](./IF02_TASK_COMMAND_AND_LIFECYCLE_FIXTURES_CANDIDATE_20261117.json): 23 command-recognition, 11 state/cancellation cases, 14 negative/recovery **scenario definitions**; [stdlib-only candidate checker](./verify_if02_candidate_fixtures.py) is an **oracle-model lint tool**, not a Pipe or an implemented service.
- Separate independent source/fixture consistency verification is recorded in [increment checkpoint](./IF02_OWNER_A_SOURCE_FIXTURE_VERIFICATION_CHECKPOINT_20261117.md). No original oracle is executed; `GRGA07-F01..F26` retain their prior scope and **NOT_RUN** states.

## 7. Gate conclusion and next testable question
**Candidate design supported, G-A blocked.** Verify one benign status/cancel operator turn passes through Open WebUI's exact pinned frontend and Pipe signatures without slash collision or response corruption, then test supervisor HTTP protocol and SQLite saver under isolated non-G1 fixtures **only after source/schema approval**. User-facing syntax, task/ack receipt visibility, stable request identity, terminal policies and persistent storage remain unapproved implementation particulars. No runtime change, G1 action, billable call, R2/R3 build or PR merge authorized.

# RP-03 pinned-source compatibility and IF-02 delegation decision preparation

**Increment checkpoint 2026-11-16 — independent documentation-only review.** No runtime inspection, API calls, service mutation, or new software versions selected. **G1 runtime hold ACTIVE; G-A UNFROZEN.** This is a candidate paper engineering assessment, not a compatibility certification.

## Source authority and limits

| Layer | Evidence read | Source status | Limits |
| --- | --- | --- | --- |
| Bifrost OSS | maximhq/bifrost commit `e869c3f9adc96ea53c38694a21bb04a8e1085487`, tag `transports/v2.4.0`; [virtual-key document](https://github.com/maximhq/bifrost/blob/e869c3f9adc96ea53c38694a21bb04a8e1085487/docs/features/governance/virtual-keys.mdx) blob SHA `8024a9d008ade34b547979142b290c3940b04a03`; [setup](https://github.com/maximhq/bifrost/blob/e869c3f9adc96ea53c38694a21bb04a8e1085487/docs/quickstart/gateway/setting-up.mdx) blob SHA `f611856f2fa385b01bb85367284c4106078f5657` | **VERSIONED SOURCE TEXT READ** | This proves documentation at a tagged source commit, **not** that the pinned deployed Docker image necessarily matches all docs or that local G1 works now |
| Deployed gateway provenance | Owner's historical pinned `maximhq/bifrost@sha256:a1c906…`; old G1 recovered source archives | **HISTORICAL EVIDENCE**, no new deployment verification | Image digest is abbreviated in summary; inspect original unabridged pinned evidence before treating exact OCI identity as verified |
| Open WebUI | [official Pipe guide](https://docs.openwebui.com/features/extensibility/plugin/functions/pipe/) and [official Functions overview](https://docs.openwebui.com/features/extensibility/plugin/functions/) | **CURRENT UNPINNED DOCUMENTATION** | No exact Open WebUI version/image commit is independently established by this continuation; cannot freeze field names, event-stream behavior, or adapter support at target |
| LangGraph | [official checkpointer reference](https://docs.langchain.com/oss/python/langgraph/persistence) and [official interrupt documentation](https://docs.langchain.com/oss/python/langgraph/interrupts); docs source [checkpointer](https://github.com/langchain-ai/docs/blob/main/src/oss/langgraph/checkpointers.mdx) | **CURRENT UNPINNED DOCUMENTATION** | No approved LangGraph package version, concrete saver, migration contract or service implementation verified here |

## Source-supported Bifrost boundary findings

1. At tag `transports/v2.4.0`, documented inference path is OpenAI-compatible `/v1/chat/completions`. Virtual keys can be supplied using `x-bf-vk`, and documentation also lists `Authorization: Bearer sk-bf-*` and other headers under specific key formats. **Do not assume any arbitrary or historical key format works in Authorization.**
2. Virtual-key enforcement is a **configuration choice**, not guaranteed by endpoint compatibility; tagged OSS documentation identifies **Enforce Virtual Keys on Inference**. Historical G1 observations suggest enforcement was enabled, but current state is unverified. **IF-01/IF-03 must not omit actual auth handling.**
3. Tagged docs describe `GET /v1/models` scoped by virtual-key allowed providers. A model visible to the UI is not automatically proven usable until its exact ID, model allowlist, mapping and Ollama dispatch are checked.
4. Tagged docs discuss expired/inactive keys and typed rejections, but **actual HTTP statuses, body formats and routing metadata are not frozen**. Earlier error observations may inform oracle candidates, not replace current pinned runtime proof.
5. Bifrost docs describe generic OpenAI-compatible streaming support; no definitive byte-for-byte SSE/cancellation or error-envelope contract is hereby proven for the exact image digest and selected Ollama model. **IF-01/IF-03/IF-LOCAL streaming and failure vocabulary remain UNFROZEN.**
6. A provider/model alias used in Bifrost may differ among UI-selected, gateway-dispatched, and backend-resolved identifiers. **AC-02 demands each identity be observable or explicitly UNKNOWN; it does not require inventing a vendor-agnostic alias registry in R1.**

## IF-02 integration: smallest justified alternatives

**Alternative A — thin Open WebUI Pipe → separate LangGraph local HTTP service (provisional candidate).** A Pipe can appear in the model selector and process a chat request according to Open WebUI's *current* official documentation. The Pipe would only translate operator-initiated requests, display status and relay results; all task execution, role scheduling, durable checkpoints and cancellation belong to the separately managed LangGraph service. A local HTTP endpoint is an integration transport, not a second supervisor. **Risks:** Pipe runs arbitrary Python in the Open WebUI process (admin-controlled, trusted code only); version-specific special arguments and event emitter behavior are not pinned; UI events must not be mistaken for durable task state.

**Alternative B — independent supervisor exposes an OpenAI-compatible endpoint to Open WebUI.** This might avoid a Pipe and preserve a model-chooser experience, but compatibility for durable user-visible task status, explicit task-ID cancellation and recovery has not been established. A chat-completion response alone is **not** evidence that the supervisor control plane is usable. Avoid creating a parallel task UI merely to rescue a too-thin interface.

**Candidate engineering recommendation:** keep **A as the leading design hypothesis**, not a G-A selection. It satisfies the owner-required separate supervisor and provides an explicit user-initiated entry point while minimizing custom UI. Before selecting it, establish exact Open WebUI version plus request and progress/cancellation behavior through authorized non-G1 source/fixture review. If B can demonstrably supply the same controls with fewer moving parts, prefer B. **Do not implement both as mandatory routes.**

## Semantic task/status/checkpoint contract (NOT wire schema)

| Semantic operation | Producer/owner | Required observable result | Critical rejection/edge |
| --- | --- | --- | --- |
| Submit delegated task | Operator via Open WebUI adapter; supervisor accepts | Stable task ID correlated to originating conversation without copying the whole conversation archive | Unauthorized, malformed or unavailable supervisor => no fabricated completed task |
| Retrieve task status | Supervisor's durable task-state owner | Truthful accepted/running/completed/failed/cancellation-requested/cancelled/recovery-error distinction (exact enum pending) | Stale UI event cannot overwrite durable state; unknown task must not appear completed |
| Cancel task | Operator via adapter; supervisor controls task lifecycle | Cancel acknowledgment distinct from actual downstream stop and final durable disposition | In-flight Ollama call may not be instantly cancellable; after accepted cancel do not start another specialist step; no false success |
| Retrieve final result | Supervisor final state to initiating Open WebUI conversation | Synthesized specialist result and explicit incompleteness/failure | A failed or cancelled workflow does not return normal successful completion |
| Durable checkpoint/restart | LangGraph worker/checkpointer | Acknowledged state is retrievable after controlled restart via stable workflow-thread mapping | Missing/corrupt state => recovery error; retry/replay may re-execute steps and should not silently double-execute local actions |
| Direct chat bypass | Open WebUI directly to Bifrost OSS | Local Ollama completion without invoking supervisor | If gateway auth/routing denies, UI displays error instead of secretly invoking supervisor |

**LangGraph distinction:** the documented checkpointer uses `thread_id` to store/retrieve graph state; it does **not** prove a user-facing `task_id` control-plane service exists automatically. Map task ID to a stable thread deliberately. LangGraph's `interrupt()` is a pause/resume mechanism, **not a substitute for user-requested cancellation and eventual terminal disposition**. Restarting a node or replaying may cause actions to run again, so tests must compare durable state and step counters without assuming exactly-once execution from the library.

## Proposed offline verification gates (no runtime hold violation)

1. **SRC-PIN-01:** record immutable Open WebUI and LangGraph versions/source commits and actual selected API/Pipe integration signatures. Current state: **OPEN**.
2. **SRC-PIN-02:** validate Bifrost `transports/v2.4.0` tagged documentation against the exact intended Docker OCI digest and provisioned configuration **using archived evidence or authorized source inspection only**. Current state: **PARTIAL**, no live G1 call.
3. **IF02-ORACLE-01:** independently review an adapter contract carrying task ID, poll/status, cancellation accepted vs completed, and final result. Current state: **DESIGN CANDIDATE**, no endpoint verified.
4. **IF06-ORACLE-02:** source/fixture review of checkpoint identity, committed-state acknowledgement, and restart/replay semantics, including failed/cancelled states. Current state: **DESIGN CANDIDATE**, not executed.
5. **IF01-ORACLE-03:** document exact auth/model-list/SSE behavior and negative paths from versioned source, then later execute on target only after G1 hold release. Current state: **PARTIAL**, not executed.
6. **G-A submission:** owner chooses/finalizes adapter, field semantics and supported versions only after independent evidence. Current state: **BLOCKED**.

**No new G1 evidence collected.** This assessment does not authorize G1 runtime inspection, paid calls, service changes, release allocation freeze or an unapproved external provider adapter.

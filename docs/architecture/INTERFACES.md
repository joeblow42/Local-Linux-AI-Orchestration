# Logical interfaces — Phase 0 Sprint A

Status: proposed interface specification; the dual-path decision is accepted.

| ID | Source | Destination | Purpose |
|---|---|---|---|
| IF-01 | Open WebUI | LiteLLM | Direct operator-selected model requests |
| IF-02 | Open WebUI | LangGraph service | Supervisor-delegated tasks |
| IF-03 | LangGraph | LiteLLM | Model calls from supervisory workflows |
| IF-04 | LiteLLM | External provider APIs | Controlled outbound requests |
| IF-05 | Open WebUI | Local conversation store | Authoritative user-facing history |
| IF-06 | LangGraph | Local checkpoint store | Workflow state and recovery |

Design constraints:
- Open WebUI owns authoritative user-facing conversation history.
- LangGraph has an independent service/process boundary, with stable task identifiers separate from chat identifiers.
- Context sent to providers must be bounded by an enforceable outbound policy; local storage does not guarantee confidentiality of transmitted payloads.
- Provider-specific API behavior and actual integration compatibility remain unverified until tested.
- Future queue/scheduler/workers are extension points, not Release 1 runtime dependencies.

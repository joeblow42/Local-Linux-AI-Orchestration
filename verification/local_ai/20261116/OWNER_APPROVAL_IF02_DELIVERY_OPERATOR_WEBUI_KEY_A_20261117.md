# IF-02 — Owner approval: operator-owned WebUI API-key delivery direction

**Decision record:** `LAI-OD-20261117-07` (new administrative reference, not a requirement/interface/oracle identifier).  
**Date:** 2026-11-17.  
**Owner response:** “A” to the choice in [IF-02 delivery authorization and message integrity](./RP03_IF02_DELIVERY_AUTH_AND_MESSAGE_INTEGRITY_GA_DECISION_CANDIDATE_20261117.md): **A — let the independent LangGraph supervisor use a locally protected operator-owned Open WebUI API key** for automatic final-result updates to the original conversation, subject to independent verification and controlled G-A review.

## Approved — engineering direction only

- Prefer **reuse** of Open WebUI's existing authenticated chat-message update facility over modifying its backend or creating a second UI/service.
- The LangGraph supervisor, not a resident Pipe worker, may maintain the bounded pending-delivery status in its **existing** durable task data; Open WebUI owns the actual chat history.
- A local, access-controlled operator-owned WebUI credential may be used as a candidate supervisor-to-WebUI integration mechanism. The owner accepts this *direction* for the approved single-operator local-only R1 trust perimeter. Do not construe this as a narrow task-only token; the pinned API key grants broader user authority.
- Automatic delivery to the original saved chat is required by owner `LAI-OD-20261117-06`; on-demand task status/cancel controls from `LAI-OD-20261117-04`, and six technical directions `-05`, remain intact.

## Not approved or performed

- **No API key creation, rotation, disclosure, retrieval, copying from a session, or installation**; especially no replacement of an existing one-key-per-user credential.
- **No enable/disable/change to API-key availability, endpoint restriction settings or Open WebUI configuration**; no target host contact, including deployed G1 while under owner hold.
- **No specific credential-storage path, exact HTTP field schema, prototype write, production patch, G-R or G-A baseline freeze, PR merge or release authorization.** These require controlled evidence, source review and any subsequent material owner decisions.
- **No relaxation of message identity/integrity:** pinned Open WebUI update behaves as an upsert and can create missing messages. Read-before-write is not atomic; verify deletion-race behavior. Do not promise zero accidental recreation without first proving it.

## Next authorized bounded engineering work

1. Finish a source-grounded IF-02 candidate contract for task ID → original chat ID → existing assistant-message ID; least broad feasible API-key reuse; terminal result → WebUI message update → independent readback/ack; no extra service.
2. Prepare a **read-only, explicitly invoked isolated-fixture preflight** checking an already-provisioned key and an existing saved chat/message without printing tokens or conversation content. Do not run it against G1. A real integration write/restart test must await the applicable G-A/runtime authorization.
3. Seek owner decision **only** if a concrete discovered incompatibility demands key rotation/global configuration changes, extra permissions, backend modifications, or an expanded R1 scope.

**Control state:** 136 requirement IDs, 19 interfaces and 26 original FAT oracles unchanged; G-R NOT APPROVED; G-A NOT APPROVED; original oracles NOT_RUN; G1 OWNER HOLD; PR #1 open, draft, unmerged; R1 Ollama local-only, R2 provider APIs deferred, R3 autonomy deferred.

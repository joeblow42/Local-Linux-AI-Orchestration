# Local AI — IF-02 Alternative A automatic-delivery direction and source checkpoint

**Date:** 2026-11-17. **Status:** owner outcome approved, bounded source review completed, exact wire/protocol/runtime not approved.
**Starting verified PR HEAD:** `58589cf00c06aed5de34d9bde850dec7f5944918`; subsequent commits listed below. Verify current branch head before next work.

## 1. Owner authority

- Owner responded **"A is approved"** to the previously isolated A-versus-B Release 1 final-result delivery question. [Recorded as `LAI-OD-20261117-06`](./OWNER_APPROVAL_IF02_AUTOMATIC_FINAL_DELIVERY_A_20261117.md), commit `e5c88de09fb1aa74043afa32d7adc0995ccc8004`.
- The completed delegated task result must appear automatically in the **originating Open WebUI conversation** without needing a manual status retrieval. Existing task status/cancel by ID remain available.
- This is an approved user-visible **acceptance direction**. It is **NOT** approval of G-R requirement wording, G-A interface schema, any app implementation, G1 hold release, PR merge or external API calls.
- Preserve previously approved Alternative A single trusted Pipe and six provisional engineering directions. No duplicate Stop button, separate dashboard, autonomous scheduler, extra durable history owner or unnecessary subsystem.

## 2. Bounded source finding

[Pinned automatic-delivery and recovery review](./RP03_IF02_AUTO_DELIVERY_PINNED_INTERFACE_AND_RECOVERY_REVIEW_CANDIDATE_20261117.md), commit `6b1272a52cbcffee594c1aa0f241e2f8a729be1c`, amended with auth review `9d54c9f8aab4fd847edbb057341502ea0c3eefc8`.

- **Existing WebUI update endpoint** at upstream Open WebUI v0.12.5 pinned commit `f7ac7ee10962ddec0017f5c29b6740d9b9c5faca`: `backend/open_webui/main.py` mounts `/api/v1/chats` (blob `a1abf80e7980c25cfc1d7dbf2dd76c290fd7de7d`); `routers/chats.py` offers authenticated `POST /{id}/messages/{message_id}` to update message content (blob `59c769b584ac0d4c758caab18d4836b0f6b8458b`).
- `socket/main.py` emitter (blob `1338308fb6d77f96532229b5d3444bcb3c5605d7`) supports conditional saved-message and event updating; frontend `Chat.svelte` (blob `438c173eb91833192d822d15d6ecaa76f3b99e15`) handles `chat:message`/replace event. `models/chats.py` (blob `3391c000eb6385cdd9352c584d86f25ccb05086a`) persists update transactionally. **18/18 selected pinned source checks matched.** No run/CI proof.
- `utils/auth.py` (blob `44d0c8c460603d3e44f5f2f42cf541991004a48e`) supports authenticated user keys and optional API-key path-prefix restrictions, but does not establish a **task-scoped** credential. Existing message edit enforces chat owner authorization; unrelated service identity cannot inherently write to an operator's chat. Prefix allowlisting of `/api/v1/chats` is broader than only a designated assistant-result message.
- No evidence that the Pipe emitter can deliver after Pipe response completion and process crash, or that a supervisor can write after restart with safe least privilege. Do not treat callback availability as durability.

## 3. Candidate positive and negative witness scope

- Supervisor durably accepts and promptly acknowledges task ID; a saved chat has a stable existing assistant-message reference correlated with that task; LangGraph remains task/checkpoint owner and WebUI remains history owner.
- Without further operator messages, terminal result is automatically written into the **original** WebUI chat, not a new chat/message stream; verified after page reload. UI disconnect, WebUI outage and supervisor restart must not silently lose the result. Repeated terminal delivery must not duplicate messages or overwrite an unrelated message.
- Failure or cancellation must be truthfully displayed, not a fabricated successful synthesis. Supervisor task completion is distinct from pending or failed **delivery**.
- Stop remains WebUI response Stop; task-ID cancellation remains through the approved Pipe. Do not promise same Stop control cancels independent supervisor task.
- Supplemental falsification cases `IF02-DEL-01..10` are specified in the candidate review; **ALL NOT_RUN** and NOT controlled original oracle IDs. The 26 original FAT oracle identities and 136 requirement IDs remain unchanged and **NOT_RUN / G-R NOT APPROVED**.

## 4. One concrete unresolved G-A design boundary

**Trusted post-Pipe supervisor→Open-WebUI final-result write authorization.** Source supplies an existing authenticated message-edit facility, but safe delivery from a separately managed background supervisor is **not established**. The final G-A review must choose an authorized pathway that does not persist a broad browser user token, bypass chat ownership, or create redundant subsystems. Verify path, message ID ownership, idempotency and restart reconciliation before any implementation. If only a broad privilege token or a new custom service can satisfy it, stop and present a scoped owner decision rather than silently increasing trust perimeter.

Other unfrozen particulars: exact persisted placeholder correlation, task completion vs delivery acknowledgements, failure classification, retry bounds, disconnected/temporary chat applicability, and pinned-image/lock compatibility.

## 5. Engineering and governance status

- **G-R:** NOT APPROVED; [LAI-R1-N004-03](./RP02_136_ACCEPTANCE_AND_APPLICABILITY_REVIEW_CANDIDATE_20261116.csv) candidate witness is now constrained to **automatic** result delivery, but the historical requirement statement/hash is unchanged.
- **G-A:** NOT APPROVED; `IF-02`, `IF-05`, `IF-06`, `IF-UI` presentation and update contracts candidate only. All 19 original interface identities preserved.
- **G1 runtime/data collection:** OWNER HOLD; no target services or billed providers contacted or modified.
- **FAT:** original 26 oracles NOT_RUN; no real UI/HTTP/SQLite/provider integration executed; no CI success claimed.
- **PR #1:** must remain open/draft/unmerged; no baseline promotion.

**Next bounded step:** Resolve exact user-approved update path and secret-ownership architecture from pinned Open WebUI source/packaging, then prepare one real isolated non-G1 functional test **after requisite G-A authority**, rather than generating further hypothetical mocks. The owner decision on **A** is settled; do not reopen or ask again.

**Conversation safety:** safe to continue; the owner approval, evidence, limitation and next gate are persisted in this GitHub checkpoint.

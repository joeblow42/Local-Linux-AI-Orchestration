# IF-02 — Automatic final-result delivery: pinned interface and recovery review
**Date:** 2026-11-17. **Status:** CANDIDATE DESIGN / PINNED SOURCE INSPECTION ONLY. NOT G-R/G-A APPROVED; NOT IMPLEMENTED; NO RUNTIME TEST.  
**Owner:** [LAI-OD-20261117-06](./OWNER_APPROVAL_IF02_AUTOMATIC_FINAL_DELIVERY_A_20261117.md) approves **Alternative A**: when a delegated task finishes, the final result automatically appears in its **originating Open WebUI chat**, without operator polling. Previously approved task status/cancel text controls remain as fallback. Approval is **of the required result**, not of any HTTP credential scheme, callback or baseline.
**Earlier approvals:** LAI-OD-20261117-04/05 remain intact: one Pipe; native END for self-ending; truthful status; no second Stop button or R3 scheduler.  
**Starting verified PR HEAD:** `e5c88de09fb1aa74043afa32d7adc0995ccc8004`; PR #1 remains draft/unmerged. G1 owner hold in effect.

## 1. Concrete existing WebUI capabilities — grounded source findings

Pinned source: `open-webui/open-webui` `v0.12.5` at exact commit `f7ac7ee10962ddec0017f5c29b6740d9b9c5faca`.

| Exact source | Immutable blob | Source-supported function / limitation |
| --- | --- | --- |
| [`backend/open_webui/routers/chats.py`](https://github.com/open-webui/open-webui/blob/f7ac7ee10962ddec0017f5c29b6740d9b9c5faca/backend/open_webui/routers/chats.py), lines approximately 1503–1574 | `59c769b584ac0d4c758caab18d4836b0f6b8458b` | Existing authenticated `POST /{id}/messages/{message_id}` handler updates existing conversation message content and emits a `chat:message` event. Checks `get_verified_user`, chat ownership (unless explicit admin access). **Absolute mounted API prefix and exact auth token format require deployment/route review**. No demonstration of autonomous background user credential or retry authorization. |
| [`backend/open_webui/socket/main.py`](https://github.com/open-webui/open-webui/blob/f7ac7ee10962ddec0017f5c29b6740d9b9c5faca/backend/open_webui/socket/main.py), approx. 1596–1724 | `1338308fb6d77f96532229b5d3444bcb3c5605d7` | User-specific event emitter and conditional database `message`/`replace` updates exist when saved-chat/message metadata is valid. It does not prove stored callback subscription across process restart or closed Pipe calls. |
| [`src/lib/components/chat/Chat.svelte`](https://github.com/open-webui/open-webui/blob/f7ac7ee10962ddec0017f5c29b6740d9b9c5faca/src/lib/components/chat/Chat.svelte), approx. 1570–1640 | `438c173eb91833192d822d15d6ecaa76f3b99e15` | Frontend recognizes `chat:message` and `replace` and updates displayed message content while present. It does not guarantee a disconnected/restarted UI receives an event; persisted message readback must be independently checked. |
| [`backend/open_webui/models/chats.py`](https://github.com/open-webui/open-webui/blob/f7ac7ee10962ddec0017f5c29b6740d9b9c5faca/backend/open_webui/models/chats.py), approx. 1391–1435 | `3391c000eb6385cdd9352c584d86f25ccb05086a` | Conversation message update runs in a transaction and is stored in WebUI-owned chat history. The visible endpoint does not itself provide a supervisor-task `state_version` compare-and-swap invariant or completed-task delivery idempotency. |
| [`backend/open_webui/functions.py`](https://github.com/open-webui/open-webui/blob/f7ac7ee10962ddec0017f5c29b6740d9b9c5faca/backend/open_webui/functions.py), approx. 234–261 | `20601fee7e42e69f7d21bb452c740ec4c3df96f9` | Pipe `__event_emitter__` can be injected for eligible metadata and only if signature asks for it. Being available during a Pipe call does not establish durable post-return/power-loss delivery. |

**Independent static source verification:** 18/18 selected source-fragment checks matched the four identified immutable source blobs (plus functions.py previous read). This is **not** a WebUI, supervisor, HTTP, renderer, DB or first-article runtime test.

## 2. Minimal candidate design — no new runtime service

A **single Open WebUI Pipe** starts the delegated operation, returns a **persisted task ID and acknowledgement promptly**, and completes its chat response. A **single independent LangGraph supervisor** runs the sequential two-specialist workflow and owns only the task's execution state/checkpoint. The original Open WebUI conversation must receive and persist the final result after the task finishes.

**Candidate integration to verify first:** reuse the **existing authenticated Open WebUI message-update facility**, targeting a pre-existing assistant message placeholder created in the initiating conversation. A task-to-conversation/message reference is recorded only as limited correlation metadata in supervisor-owned task records. The supervisor's completion delivery may update that placeholder via a properly authorized local API route, or an equivalent existing WebUI-native mechanism; exact producer and token-handling boundary is **not yet authorized/frozen**.

Critical separation:
- **LangGraph owns** `task_id`, outcome, final synthesis, terminal state, checkpoint, and any bounded pending-delivery marker/correlation necessary for restart reconciliation.
- **Open WebUI owns** actual chat message content and persistence. The Pipe does **not** store a second copy of the whole conversation or maintain an autonomous task worker.
- **Delivery acknowledgement** is separate from **task completion**. If a task is terminal but its chat write fails, status accurately reports completed with **delivery pending/error**, not a fabricated delivery success.
- **No new daemon, scheduler, dashboard or independent delivery database** is authorized. Bounded restart reconciliation should run within the already-required supervisor service (if independently justified by persistence/FAT evidence). No uncontrolled infinite retry.
- **No storage of operator's browser bearer token** in LangGraph. The existing endpoint authenticates as an authorized WebUI user; a safe, scoped server-side authorization method for supervisor-origin delivery is **still unproven**. Neither a privileged admin token with broad history access nor bypassing Open WebUI ownership checks is justified. If no narrow safe option is verifiable in pinned source, do not silently implement one.

## 3. Candidate acceptance invariants and negative cases

| Fixture ID (new supplemental case label, NOT historical oracle) | Observable positive behavior | Failure / falsification |
| --- | --- | --- |
| `IF02-DEL-01` | New delegated task returns committed `task_id` and saves a correlation to an **existing** originating chat/message placeholder | Acceptance and placeholder cannot be fabricated; nonexistent placeholder not silently created by write path |
| `IF02-DEL-02` | Normal two-specialist task completes; final synthesized result arrives automatically in the original chat even though original Pipe stream already ended | No operator status request; delivered content matches supervisor terminal outcome |
| `IF02-DEL-03` | Completion while browser disconnected persists original chat message; reconnect/reload retrieves it | A transient socket event alone is insufficient |
| `IF02-DEL-04` | Delivery attempt fails while WebUI unavailable; terminal task state persists with truthful pending-delivery disposition and can reconcile after restart | No lost final answer, false `delivered`, indefinite duplicate messages or uncontrolled retry |
| `IF02-DEL-05` | Duplicate completion notification or retry updates **only the same correlated assistant message** and preserves committed final outcome | A repeated callback must not create second answer or rewrite an unrelated chat |
| `IF02-DEL-06` | Operator cancels during running task; the originating conversation ultimately shows the cancellation or failed/incomplete outcome with accurate status | No successful synthesized answer for an incomplete/cancelled task |
| `IF02-DEL-07` | Correct authenticated local update is accepted only for the target owner's existing chat/message | Wrong chat, stale/wrong message ref, missing/expired credential, wrong user denied; no generic admin token bypass |
| `IF02-DEL-08` | Original chat history remains in WebUI; supervisor holds task/correlation only; restored independent WebUI + supervisor can reconcile pending deliveries | No duplicate chat ownership, no missing message after clean restore |
| `IF02-DEL-09` | Task-ID status remains usable regardless of delivery state | Delivery failure does not replace task status with fabricated failure/completion |
| `IF02-DEL-10` | Existing native WebUI Stop behavior remains independent of supervisor task cancellation; task-ID text cancel works after initial ack | Pressing Stop on UI alone cannot generate a false supervisor cancellation |

All tests **NOT RUN**, all API fields/paths used here are **design candidates**. No original controlled 26-oracle ID was added or changed.

## 4. Material caveats before G-A approval

1. **Credential boundary is the key remaining security/architecture problem.** The existing endpoint checks `get_verified_user` and ownership. A supervisor operating after the original browser request has ended cannot assume it possesses an authorized end-user credential or safe capability to update the chat. An engineer must demonstrate narrowly authorized server-to-server delivery without keeping a user's broad WebUI bearer token, bypassing ownership, or creating an unnecessary service. Document exact pinned supported mechanism; if none exists, present one bounded alternative and its cost for owner adjudication.
2. **UI lifetime and saved-chat semantics:** late delivery requires a persisted originating chat and a stable existing assistant message reference. In-memory/temporary chat is **not proven** capable of durable post-restart delivery. Do not silently promise it for a temporary chat. Explicitly identify test applicability before formal G-R wording.
3. **Delivery once and integrity:** message update is apparently an existing route, but retry under contention, missing message, stale version, and side effect of overlapping UI writes are **not** shown to satisfy exactly-once outcomes. For R1, propose an idempotent full-message replacement into the one designated placeholder with source task identity and delivery version; verify correctness before freezing. Never append to a random latest chat message.
4. **Notification vs persistent content:** UI socket events improve live visibility; acceptance must be grounded in **persisted chat readback** and after-restart/reconnect usability. Terminal supervisor state alone is not a delivered final answer.
5. **Independent G-A owner gate:** `LAI-R1-N004-03` candidate acceptance may now be interpreted with automatic delivery, but the actual controlled G-R replacement and G-A IF-02/IF-05/IF-06 field, permission and recovery contracts are still **NOT APPROVED**. G1 runtime hold still active.

## 5. Gate disposition and next justified increment

**Result: owner-approved acceptance outcome is feasible enough to merit a bounded interface prototype, but exact implementation has NOT been established.** Source shows first-party Open WebUI message updates; no source proof of a least-privilege autonomous caller and post-Pipe/restart reconciliation.

Next: inspect pinned Open WebUI security/auth route and package deployment seams for an existing narrow supervisor→WebUI write path; decide if a small design adaptation is required. After G-A authorization, test with a real isolated non-G1 Open WebUI+Pipe+supervisor fixture, not another in-memory mock. Do not promote G-R/G-A, touch G1 or merge the PR.

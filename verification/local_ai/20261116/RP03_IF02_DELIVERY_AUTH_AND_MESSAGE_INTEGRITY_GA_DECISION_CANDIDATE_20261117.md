# RP-03 / IF-02 — automatic-delivery authorization and message-integrity G-A candidate

**2026-11-17. CANDIDATE; NOT G-A APPROVED; NO RUNTIME ACTION.**  
**Starting exact PR #1 HEAD:** `aa0fa82aa2e484791feac69e92de5f9deb95c33c`. PR remains draft/unmerged; G1 runtime/data collection remains on owner hold.  
**Owner requirement:** [LAI-OD-20261117-06](./OWNER_APPROVAL_IF02_AUTOMATIC_FINAL_DELIVERY_A_20261117.md) — automatically publish final delegated result into the *original* Open WebUI conversation. Preceding [04](./OWNER_DECISION_IF02_TASK_CONTROL_A_APPROVED_20261117.md) and [05](./OWNER_APPROVAL_IF02_SIX_ENGINEERING_DIRECTIONS_20261117.md) still govern one Pipe, operator cancellation and native graph self-termination.  
**Parent evidence:** [Existing WebUI post-response delivery candidate](./RP03_IF02_AUTO_DELIVERY_PINNED_INTERFACE_AND_RECOVERY_REVIEW_CANDIDATE_20261117.md); [verified prior checkpoint](./RP03_IF02_OWNER_A_AUTO_DELIVERY_VERIFICATION_CHECKPOINT_20261117.md).

## 1. BLUF and source-pinned constraints

**Best R1 candidate is reuse of the existing Open WebUI authenticated chat-message edit route with an operator-owned local API key and one supervisor-owned pending-delivery record.** That uses the existing Open WebUI installation and the already-required independent LangGraph supervisor, with **no new UI, daemon, DB owner, or custom auth server**. It is **not yet approved or proven**. The key is not a single-task capability and the existing edit operation lacks an atomic *existing-message-only* check.

Target upstream: `open-webui/open-webui@f7ac7ee10962ddec0017f5c29b6740d9b9c5faca` (tag v0.12.5 candidate; installed version **not confirmed**).

| Pinned file (Git blob) | Exact source-supported fact | Operational consequence |
| --- | --- | --- |
| `backend/open_webui/routers/auths.py` (`d9b0d01d528551bffbfbb45e260cedfa9e99ef44`) lines 1497–1558 | Creating a user API key calls `Users.update_user_api_key_by_id` | **Creating/replacing a key is not free**; do not rotate an existing user key merely for IF-02 without checking other integrations |
| `backend/open_webui/models/users.py` (`0aa6a6f167609b87117d8b746f89bc78b100947d`) lines 865–889 | Key creation **deletes prior `ApiKey` rows for that user**, then inserts one replacement | One effectively stored active key per user in this code path; no distinct per-task/supervisor key for the same user via the existing generator |
| `backend/open_webui/utils/auth.py` (`44d0c8c460603d3e44f5f2f42cf541991004a48e`) lines 389–433, 506–549 | `get_current_user` accepts API keys if enabled; `auth.api_key.endpoint_restrictions` and `auth.api_key.allowed_endpoints` are **shared configuration** with path-prefix matching, not per-key grants | A key is user-owned; enabling/changing restrictions may affect unrelated local clients and cannot grant only one message update. Do not assume current host enables API keys |
| `backend/open_webui/main.py` (`a1abf80e7980c25cfc1d7dbf2dd76c290fd7de7d`) line ~896 and `backend/open_webui/routers/chats.py` (`59c769b584ac0d4c758caab18d4836b0f6b8458b`) lines 1380–1407, 1510–1569 | Existing `GET /api/v1/chats/{id}` and `POST /api/v1/chats/{id}/messages/{message_id}` with verified-user and chat-owner permission check. Message POST updates `content` and emits `chat:message` | No new route is necessary to test full-content replacement and browser update; a **user-owned key** could authorize it if available, though GET returns broader chat history than a single-message projection |
| `backend/open_webui/models/chats.py` (`3391c000eb6385cdd9352c584d86f25ccb05086a`) lines 1134–1195, 1391–1425 | `upsert_message_to_history` **creates a message if ID absent**; the content-only POST route does not pre-check message existence | Missing/deleted target IDs risk creating an unintended assistant message. A read-before-write check is useful but **not atomic**, so cannot alone prove this failure impossible if UI deletes the message concurrently |
| `backend/open_webui/socket/main.py` (`1338308fb6d77f96532229b5d3444bcb3c5605d7`) lines 1596–1715 and `src/lib/components/chat/Chat.svelte` (`438c173eb91833192d822d15d6ecaa76f3b99e15`) lines 1570–1640 | Event relay, persisted chat update and frontend content replacement present | Reloaded chat readback, not just a live socket event, is the acceptance evidence |

**Verification method:** seven immutable pinned upstream files inspected; **14/14 code-fragment guards matched** after correcting one checker text-matching typo (initial 13/14 due solely to a guard expecting the assignment without the actual `success = await` prefix). No source file, endpoint, authentication system, browser or installed runtime executed.

## 2. Candidate minimal design — conditional, no product implementation

1. Single trusted selected Pipe receives operator request with server-authenticated `__user__` and originating saved `chat_id` plus the existing assistant acknowledgement **message ID**. It submits limited task projection to independent LangGraph supervisor. Never store whole WebUI conversation history in supervisor.
2. Supervisor *durably* commits `task_id`, actor reference, immutable originating chat ID and existing acknowledgement-message ID, task state, pending delivery marker and revision before Pipe sends task ID and closes the chat response. The Pipe is **not** an independent worker after response closure.
3. Supervisor executes the approved sequential two-specialist workflow and records final outcome. Its already-required durable loop checks terminal tasks with pending delivery; **no new background daemon or periodic independent scheduler**. This is post-completion delivery, not R3 creation of autonomous new tasks.
4. Using an operator-approved, owner-associated Open WebUI API key stored as local access-controlled secret **only in the supervisor runtime**, a bounded client first retrieves the target saved chat and checks expected assistant message ID, role, parent/conversation correlation and existence before issuing a **full content replacement**. Do not use arbitrary latest-message index, model-supplied IDs or admin cross-user impersonation.
5. After POST, independently read back the exact stored chat result and mark **delivery acknowledged** in the supervisor's existing task ledger. Retries operate on same message ID and committed final content, not append/create. If WebUI is down, key invalid, message absent or outcome conflicts, report **completed / delivery_pending** or explicit **delivery_failed** (labels provisional), never false delivered or completed task failure.
6. **Integrity limitation:** GET preflight and POST are two calls; the pinned POST upserts a missing message and has no atomic compare-and-swap. For R1 single-operator UI, a normal deletion/edit race remains plausible; this cannot be called fully resolved by source review. Real isolated test should exercise deletion during pending callback. If the acceptance requirement mandates *no recreation even in that race*, a minimal guarded update inside existing Open WebUI backend (NOT a new service) may be needed; that scope and source-maintenance cost must go through G-A approval.

**Temporary/unsaved chats:** automatic durable post-return delivery is not supported by evidence here. Candidate R1 policy is to require a saved originating WebUI chat for delegated tasks until a supported persistence mechanism is proven. Do not silently treat an ephemeral conversation as durable.

**Security framing:** Single-operator, local-only administration was owner-approved. The concern is operational reliability and accidental cross-chat edits or key invalidation, **not** an assumed hostile second user. Do not add OAuth services, enterprise KMS, complex multi-tenant policy or encrypted-at-rest mandatory backup.

## 3. Options and technical recommendation

| Choice | Implementation direction | Benefits | Real tradeoffs | Recommendation |
| --- | --- | --- | --- | --- |
| **A — Reuse existing user-owned API key and existing chat-edit route** | Operator explicitly authorizes one existing/reused key or voluntarily creates one if none; supervisor keeps access-controlled local secret and only sends verified same-chat/same-message updates; existing task ledger handles reconciliation | Smallest code/dependency change, no second Pipe or UI, aligns with one-operator trust and owner-approved automatic delivery | User key can access operator's chats, not just one result; one active key per user; global endpoint restrictions can impact other API clients; missing-ID upsert and delete race require honest tests and possible follow-up | **Preferred candidate for bounded isolated test** conditional on owner acceptance of key-sharing and no unintended existing-key rotation |
| **B — Narrowly scoped guarded write path within existing WebUI backend** | Add/modify a small pinned WebUI route or equivalent in-process trust hook that enforces an existing assistant placeholder + task correlation atomically | Could avoid broad user key stored in supervisor and block phantom result creation | Version-specific upstream fork/patch, maintenance burden, and more G-A design/testing; must not introduce new service or UI | Contingency **only if** option A fails essential acceptance or owner declines user-key sharing |
| **C — Keep Pipe stream open until LangGraph finishes** | Write final on still-open Pipe response | Avoids autonomous completion update credential | Blocks same-chat status/cancel while stream active/queued, and does not reliably persist after response closed or UI/process loss | **Reject** as a substitute for owner-approved A automatic background delivery |

**Do not choose B simply because an imaginary hostile actor might use a local key; do not claim A meets a strict atomic existing-message-only requirement until tested.**

## 4. Independent verification and G-A acceptance gate — NOT RUN

| Fixture (supplemental, not a historical oracle) | Expected witness | Explicit fail witness |
| --- | --- | --- |
| IF02-AUTH-01 | Reuse an existing key without creating/replacing it; if keys disabled, fail closed and request explicit local configuration | New key silently rotates/invalidates unrelated integration |
| IF02-AUTH-02 | Local owner-key request accesses own saved chat; wrong-owner request denied | Wrong user's message mutated |
| IF02-DEL-11 | Stable existing acknowledgement assistant message only is updated with committed terminal result | Missing/deleted ID causes a new phantom assistant message |
| IF02-DEL-12 | Browser disconnected at completion; persisted chat readback and reload show final result | Socket event sent but database still contains acknowledgement only |
| IF02-DEL-13 | WebUI restart or temporary outage: supervisor retries and eventually marks delivery acknowledged after readback | False delivered status, duplicate responses or indefinite uncontrolled writes |
| IF02-DEL-14 | Original WebUI chat deleted during pending delivery: clear delivery-failure outcome, no unrelated chat writes | Recreated message in wrong chat or fabricated success |
| IF02-DEL-15 | Operator task cancel while generation ongoing: terminal disposition and delivery reflect cancellation | Late successful model response overwrites cancelled task/result |

**All NOT RUN.** Previous original 26 oracle IDs preserved and NOT_RUN. IF-02 `LAI-R1-N004-03` source-linked candidate acceptance must now include automatic original-chat result, as approved by LAI-OD-20261117-06, but its actual controlled wording remains NOT APPROVED.

## 5. Material owner authority gate

To proceed beyond paper/source design and *configure real authentication or run a real integrated isolated prototype*, the owner should explicitly choose:

- **A (recommended):** authorize a **local, operator-owned Open WebUI API key** in the independently managed LangGraph service for *only the purpose of IF-02 automatic final-result update*, while acknowledging that Open WebUI itself does not provide a per-task API-key permission. Do **not** rotate an existing key, enable keys or change global restrictions without a separate runtime preflight of configuration impacts and owner go-ahead. No server changes or G1 contact implied.
- **B:** prohibit storing an operator-owned WebUI key in the supervisor; require a narrowly guarded WebUI-native update extension instead, subject to a separate G-A scope and maintenance review.

These are materially different trust/maintenance choices; unlike the already-approved six engineering directions, **this is not already decided** by automatic-delivery UX approval. No default product implementation or G-A baseline promotion before selection.

**Conformance status:** G-R NOT APPROVED; G-A original IF-02 / IF-05 / IF-06 contracts NOT APPROVED; 136 requirement IDs, 19 interface IDs, 26 original oracle IDs preserved; G1 OWNER HOLD; PR #1 draft/unmerged; Release 1 local-only, Release 2 external model APIs and Release 3 unattended autonomy deferred.

## 6. Next legitimate increment

After owner direction on credential boundary, define minimal IF-02 authentication/correlation/update/ack requirements as **candidate G-A** with exact source-backed fields; independently exercise real Open WebUI + single Pipe + supervisor + saved chat in a **separate, authorized non-G1 fixture**. Do not multiply mocks, add a scheduler or claim success from static checks. Keep source-sensitive credentials out of this public GitHub repository.

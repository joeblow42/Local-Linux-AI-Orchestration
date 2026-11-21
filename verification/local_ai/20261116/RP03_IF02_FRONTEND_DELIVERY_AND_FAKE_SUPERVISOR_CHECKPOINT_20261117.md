# RP-03 / IF-02 — Pinned frontend delivery and isolated supervisor checkpoint

**Date:** 2026-11-17. **Status:** CANDIDATE SOURCE AND FAKE-MODEL VERIFICATION ONLY. G-R/G-A NOT APPROVED; G1 OWNER HOLD; PR #1 draft/unmerged.
**Authority:** [Owner Alternative A — LAI-OD-20261117-04](./OWNER_DECISION_IF02_TASK_CONTROL_A_APPROVED_20261117.md).
**Source:** [Exact evidence with blobs and test results](./IF02_PINNED_SOURCE_AND_ISOLATED_MODEL_EVIDENCE_20261117.json); [reproducible JS mock cases](./verify_if02_in_memory_supervisor_candidate.js).
**Parent checkpoint:** [IF-02 prior verification](./IF02_OWNER_A_SOURCE_FIXTURE_VERIFICATION_CHECKPOINT_20261117.md).

## Findings requiring design attention

1. **Front-end slash commands.** The pinned Open WebUI v0.12.5 `Chat.svelte` intercepts built-in `/status` and selected other commands. Slash suggestions exist in the pinned `SlashCommands.svelte`. This does NOT prove that `/task` is swallowed; the non-slash candidate `task status <id>` and `task cancel <id>` avoids the unresolved collision but still needs end-to-end delivery verification.
2. **Active-stream command queuing.** `Chat.svelte` lines 4001–4028 queue later prompts when message generation is active and the chat queue setting is enabled. When the queue is disabled, the UI calls `stopResponse()` before proceeding. Neither behavior guarantees an immediate independent LangGraph cancellation. Therefore the least-complex candidate is **rapid durable submit acknowledgement with stable supervisor task ID**, ending the initial Pipe response promptly; future status/cancel turns can then be processed in ordinary chat. No actual responsiveness measurements performed.
3. **Two distinct task-identity domains.** Open WebUI chat-completion `task_ids` and `stopTasksByChatId`/`stopTask` control Open WebUI generation work. There is no source proof of equivalence with the independent supervisor `task_id`. The Pipe must not treat them as aliases or consider WebUI Stop sufficient supervisor cancellation.
4. **Authenticated operator versus client metadata.** `main.py` invokes `get_verified_user` at the chat completion endpoint, while user_message fields arrive from the client and may be used in chat persistence. `functions.py` injects `__user__` from the server user object **only if** the selected Pipe declares that parameter in its signature. Do not authorize supervisor status/cancel using arbitrary `body.messages`, user-entered actor IDs, tool output or unverified client metadata. Actual current-turn provenance must be established with the pinned integration.
5. **Pipe-selection invariant.** Source routes model instances flagged as Pipe to `generate_function_chat_completion`; ordinary direct chat bypass remains separately operational. Supervised task controls require the single selected delegated Pipe. Multi-model/side-by-side selection must not accidentally dispatch duplicate supervisor tasks; exact behavior not tested.

## Verified source identities

All upstream files fetched at immutable Open WebUI `v0.12.5` commit `f7ac7ee10962ddec0017f5c29b6740d9b9c5faca`:

| Path | Exact source blob | Relevant scope |
| --- | --- | --- |
| `src/lib/components/chat/Chat.svelte` | `438c173eb91833192d822d15d6ecaa76f3b99e15` | 3868–3915 slash intercept; 4001–4028 queue; 4170–4209 WebUI task IDs; 4420–4485 completion request; 4621–4672 Stop; 4674–4706 submitted user turn |
| `src/lib/components/chat/MessageInput.svelte` | `bafec0644a19cb993e52227e266fa1747ddb08c8` | frontend command suggestions |
| `src/lib/components/chat/MessageInput/Commands/SlashCommands.svelte` | `92b6d92aef8dbae70e33b145b1d8b3bdf74d9b26` | built-in slash suggestion list |
| `backend/open_webui/main.py` | `a1abf80e7980c25cfc1d7dbf2dd76c290fd7de7d` | authenticated endpoint and client-originating user_message metadata |
| `backend/open_webui/functions.py` | `20601fee7e42e69f7d21bb452c740ec4c3df96f9` | Pipe signature, verified-user injection, streaming/nonstreaming invocation |
| `backend/open_webui/utils/chat.py` | `c97985dde4ac281d7e87c11eb5c178d81d1b43b4` | Pipe routing |

**Static guard result:** 15/15 source-fragment presence checks matched these pinned files. These are **not functional, browser, networking, or runtime integration tests**.

## Independent isolated fake-model test

Read-back and executed the **exact committed JavaScript** [candidate runner](./verify_if02_in_memory_supervisor_candidate.js) from commit `81a957d963224e594f3580cc70946431a4f80012`, blob `b85626ab980b58132305da27e377ca1de1fe4442`, in an isolated V8 executor with mocked console and process (not Node CLI or product code).

Initial exploratory test had 16 PASS and one FAIL: T17 exposed a **test-double** bug permitting an already-completed task to be finalized as failed. Corrected terminal immutability, added three more tests, and reran the exact stored program.

**Final fake-model result: 20 PASS / 0 FAIL** covering T01–T20: request retry/idempotency and changed-payload conflict, durable state version, cancel acceptance vs terminal, both cancel/terminal orderings, no-new-step fence, terminal monotonicity, authorization, unknown task, service outage, stale UI event, checkpoint corruption, and UI Stop independence.

Limit: single-threaded **in-memory mock only**. Real HTTP, actual Open WebUI UI, LangGraph, SQLite, Bifrost, Ollama, concurrency/locking and restart recovery **NOT RUN**. Original controlled **26 oracles ALL NOT RUN**. The previous Python catalog checker is still not claimed executed.

## Material pending G-R/G-A / next narrow gate

- Independently demonstrate non-slash control message passage from the **exact selected Open WebUI frontend** into **one** trusted Pipe; do not assume static source checks prove this.
- Verify prompt first-turn acknowledgement includes supervisor-durable task ID, then completes the Pipe generation promptly enough to avoid queuing future operator control commands. No promise of instantaneous abort of a running Ollama request.
- Confirm authenticated actor and fresh user-turn provenance on the actual Pipe boundary; avoid duplicate task submit during regeneration, replay, multi-model requests, or missing acknowledgement.
- Verify cancellation/terminal race, checkpoint store atomicity and restart on an isolated approved test fixture, **after G-A interface decisions**. Do not proliferate hypothetical components or mocks as a substitute for actual FAT.
- Preserve the original IF-02/IF-06 identities, the 136 requirement IDs, the 19 interface IDs, 26 original oracle IDs, all owner approvals, and the closed nonblocking Rev0.16 historical exception.

**Conclusion:** Source-supported continuation with explicit operational gaps. Neither G-R nor G-A frozen, installed runtime uncontacted, and PR #1 remains draft/unmerged. Future source-only review is safe; defer product implementation and G1 tests until authorized.

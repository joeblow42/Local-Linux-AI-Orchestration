# IF-02 — automatic-delivery authentication and integrity checkpoint

**Date:** 2026-11-17. **Source-only bounded increment complete.** Do not treat source guards as application tests.  
**Start of increment:** PR #1 draft/unmerged at `aa0fa82aa2e484791feac69e92de5f9deb95c33c`, base `main` `46ec8e99eeb65627daa1b4296b1be32350282a67`.  
**New candidate review:** [G-A delivery authentication / message integrity options](./RP03_IF02_DELIVERY_AUTH_AND_MESSAGE_INTEGRITY_GA_DECISION_CANDIDATE_20261117.md), commit `d4c1d82eb3356a9a1451fd025ce3c9dea21ade85`. Confirm final HEAD after README index commit.  
**Owner decisions upheld:** LAI-OD-20261117-04 (single Pipe text controls), -05 (six provisional stop and self-end directions), -06 (automatic final-result delivery to originating chat). **Automatic-delivery direction A remains APPROVED** and must not be reopened without substantive incompatibility evidence.

## Relevant exact-source discoveries

At Open WebUI candidate v0.12.5 source commit `f7ac7ee10962ddec0017f5c29b6740d9b9c5faca`:
- `backend/open_webui/routers/auths.py` blob `d9b0d01d528551bffbfbb45e260cedfa9e99ef44`: user API key generation delegates to `update_user_api_key_by_id`; `backend/open_webui/models/users.py` blob `0aa6a6f167609b87117d8b746f89bc78b100947d` deletes prior key rows for that user on replacement. **One replaceable key per user via this code path**. No credentials generated or exposed.
- `backend/open_webui/utils/auth.py` blob `44d0c8c460603d3e44f5f2f42cf541991004a48e`: user key use requires enabled API-key config. Endpoint restriction settings are configured globally, with URL **path-prefix** checks; no per-task permission. An operator key used by LangGraph necessarily has more authority than a task-specific update.
- `backend/open_webui/routers/chats.py` blob `59c769b584ac0d4c758caab18d4836b0f6b8458b`: authenticated owner read of `GET /api/v1/chats/{id}` and write of `POST /api/v1/chats/{id}/messages/{message_id}`. GET yields chat not a dedicated single-message view; POST `content` path does not first require existing message.
- `backend/open_webui/models/chats.py` blob `3391c000eb6385cdd9352c584d86f25ccb05086a`: missing message ID is **inserted by upsert**. Thus deleting the originating assistant placeholder concurrently with an automatic completion update can recreate a message. Read-before-write mitigates ordinary accidental wrong target but does **not** give atomic existence checking. This is a real correctness boundary, independent of hostile-actor threats.
- Existing frontend message change handling and saved-chat persistence shown in preceding [pinned delivery source review](./RP03_IF02_AUTO_DELIVERY_PINNED_INTERFACE_AND_RECOVERY_REVIEW_CANDIDATE_20261117.md).

**Guard verification:** 14/14 selected immutable-source checks matched, after correcting one checker exact-substring expectation (initial 13/14 was an audit-script text mismatch, not source failure). **No actual Open WebUI, LangGraph, Bifrost, Ollama, HTTP, browser, API key, restart or write-race test performed.**

## Recommendation and material owner gate

**Recommended Option A:** allow the trusted, locally managed independent supervisor to use a **user-owned Open WebUI API key**, with a protected local secret, task-to-chat/message association, preflight exact role/parent check, whole-message replacement and post-write readback. Preserve one Pipe and one supervisor. Reuse rather than rotate an existing key, but do not assume API keys are enabled or alter global endpoint restrictions without checking their impact. This is most consistent with single-operator R1 scope; it still needs real tests for deleted-placeholder race and restart reconciliation.

**Option B:** decline sharing an operator WebUI key with supervisor and require a minimal **existing-WebUI-backend** conditional update/auth extension (no new service/UI), accepting pinned-version code-maintenance cost. Do not implement a second task controller or autonomous scheduler.

**The owner must choose the credential/trust-boundary direction before production configuration or G-A protocol freeze.** The approved automatic-delivery UX does not authorize extending user credential storage across the service boundary by itself. This is a substantive **operational permission** difference, not a duplicate review of previously approved stop mechanisms.

## Protection status

- Release 1 only: direct Open WebUI→Bifrost OSS→Ollama; delegated Open WebUI→one Pipe→independent LangGraph→Bifrost OSS→Ollama. No external APIs, no R3 scheduling.
- G-R original requirements and acceptance **NOT APPROVED**; G-A interface schemas/auth/HTTP/task lifecycle **NOT APPROVED**; no old ID/hash changed (136 requirements, 19 interfaces, 26 original FAT oracle IDs). All original 26 oracle executions NOT_RUN.
- G1 runtime/data **OWNER HOLD**; no deployed service contact or changes; no API key created, rotated, accessed or written.
- Draft PR #1 remains open, **DRAFT and UNMERGED**; no CI PASS asserted.
- Historical Rev0.16 source exception remains closed/nonblocking.

**Conversation safety:** safe; source, credential tradeoffs, exact next owner decision and test limitations recorded in GitHub. Stop at material owner decision without manufacturing further mock passes. After owner selection, prepare G-A candidate and a **real isolated non-G1 functional integration test** before any target runtime action or baseline acceptance.

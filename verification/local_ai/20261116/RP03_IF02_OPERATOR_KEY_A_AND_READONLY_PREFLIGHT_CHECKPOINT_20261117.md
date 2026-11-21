# Local AI Development — IF-02 operator-key direction and read-only preflight checkpoint

**Date:** 2026-11-17. **Work:** bounded source and local isolated-preflight engineering. PR remains draft/unmerged; G1 hold active.  
**Starting verified HEAD:** `19abafe632a5602148e10b1c4375c18ecfede4ad` on `handoff/localai-20261116-recovery`, base `46ec8e99eeb65627daa1b4296b1be32350282a67`. Confirm final exact head after indexing this record.

## Owner direction recorded

Owner responded “A” to **operator-owned, locally protected WebUI API key in independent LangGraph supervisor** as IF-02 delivery authorization **design direction**, not a credential-change permission. Recorded as [LAI-OD-20261117-07](./OWNER_APPROVAL_IF02_DELIVERY_OPERATOR_WEBUI_KEY_A_20261117.md), commit `511d5c8e9511d7c935da5e8ce10cbf4a6a7b3ccb`.

Earlier owner decisions still control: one selected Pipe with text task status/cancel (04), six stop/self-termination directions (05), automatic result delivery to the original WebUI conversation (06). No duplicate UI/service or R3 scheduler. The user has **not** authorized API-key creation/rotation, modifying Open WebUI settings, G1 collection or runtime deployment.

## Engineering outputs

1. [Read-only preflight script](./if02_readonly_delivery_preflight.py), commit `87bd5b9095bccb13d863c6bc314437fa5e0bb362`; exact Git blob `b2a225fa14f6d74d4fd0c8292b6d5702e0f4ad1d`. Written using Python standard library, invoked only with explicit `--confirm-isolated-fixture`, limited to numeric loopback interface, uses **GET only**, disables proxies and redirects, reads pre-existing `IF02_WEBUI_API_KEY` environment secret without printing it, checks existing saved chat assistant message and optional parent ID, sanitizes failures. Never creates/rotates keys, POSTs, or writes chat content.
2. [Minimal candidate IF-02/IF-05/IF-06 G-A delivery delta](./RP03_IF02_AUTO_DELIVERY_MINIMUM_IF02_IF05_IF06_GA_DELTA_CANDIDATE_20261117.md), commit `6bc12383daa5f574897d4b94962a2da61883a3b8`. Defines task→chat/message correlation, background terminal result delivery, pending/delivered separation, exact persisted-message readback, no novel scheduler or history database, and guard for deleted placeholder.
3. Original G-R requirement IDs and source hashes preserved. Original 19 interface IDs and 26 FAT oracle IDs preserved. No original oracle promoted from NOT_RUN; no G-A schema promotion.

## Verified script checks — **NOT an Open WebUI integration test**

The same exact 4,255-byte source was prepared and compiled locally with `python -m py_compile`. Independently obtained GitHub blob hash matched local git-object SHA-1 **byte for byte** (`b2a225fa14f6d74d4fd0c8292b6d5702e0f4ad1d`).

Tiny locally hosted isolated HTTP test fixture (not real Open WebUI) exercised:
- Existing chat + assistant message using test-only bearer value: **PASS**, exit 0, no body or token exposed in output.
- Same with correct explicit parent correlation: **PASS**, exit 0.
- Wrong parent correlation: **expected FAIL**, exit 1, `PARENT_ID_MISMATCH`.
- No explicit isolated-fixture confirmation: **expected FAIL**.
- Non-loopback URL: **expected FAIL**.
- Missing environment credential: **expected FAIL**.

**What these checks prove:** script syntax, local argument safeguards, correct use of GET and parser checks under a *synthetic* HTTP response. **What they do not prove:** real installed WebUI credentials/settings, actual authenticated read, real Pipe-originated placeholder, supervisor completion callback, automatic delivery, real DB/HTTP writes, deleted-message race, backup/recovery or end-to-end FAT. No API key was read from a live environment and no target service (including G1) was contacted. No original FAT oracle executed.

## Source-supported open risk and next gate

Pinned Open WebUI v0.12.5 source uses a per-user API-key replacement procedure; global rather than per-key URL path restrictions; authenticated owner chat read/edit; and **upsert** on `POST /api/v1/chats/{id}/messages/{message_id}`, which can insert a missing assistant message. Simple read-before-write is not atomic under a concurrent deletion. Do not falsely claim the approved A direction already guarantees message integrity.

**Next legitimate work:** verify exact installed Open WebUI version and key availability through an explicitly isolated **non-G1** fixture; subsequently a real write/readback/retry/restart/deleted-message test after requisite G-A runtime authority. If key rotation, global endpoint setting changes, a privileged backend modification, or broad credential exposure becomes necessary, seek owner review rather than silently acting. No broader mock growth justified.

**Governance:** G-R baseline **NOT APPROVED**; G-A wire/authorization baseline **NOT APPROVED**; G1 **OWNER HOLD**; Release 1 local only, no external billable models; PR #1 **DRAFT/OPEN/UNMERGED**; zero deployment changes; original FAT oracles **NOT_RUN**. Conversation safe to resume from this exact checkpoint.

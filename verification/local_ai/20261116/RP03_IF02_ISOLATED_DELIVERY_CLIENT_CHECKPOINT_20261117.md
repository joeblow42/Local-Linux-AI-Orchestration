# Local AI Development — RP-03 / IF-02 isolated result-delivery candidate checkpoint

**Date:** 2026-11-17. **Status:** candidate executable HTTP client + bounded SQLite test fixture. **Not a real Open WebUI/LangGraph integration, G-A baseline, or FAT pass.**  
**Starting authority:** GitHub draft PR #1 head `53051bebf114a632f38052f0ce7e6ea2bf0b3ff7`, base `46ec8e99eeb65627daa1b4296b1be32350282a67`. Review approved owner decisions `LAI-OD-20261117-04/05/06/07`. No existing G-R/G-A owner baseline authorization, no G1 hold release.

## Executable candidate and verification

**[Candidate delivery client](./if02_delivery_client_candidate.py)**, final source commit `4cf195153e39a751cb3d5af5d20867b5260bc369`, exact verified GitHub blob `a2989fd7b275174533c13a881c70083af4744473`, 5,902 bytes. Standalone Python standard-library module, **no CLI automatic writes**; a supervisor would need to deliberately invoke it only after appropriate G-A approval. Does not install or change services, or create credentials. Protects against redirect/proxy use and nonnumeric-loopback connections in the isolated candidate. Uses an operator-owned API key only in memory, full-content replacement of an existing verified assistant message, previous-content and parent-ID checks, and exact post-write readback. Returns `DELIVERED`, `ALREADY_PRESENT`, `PENDING`, or `REFUSED`; never treats a POST response alone as durable proof of delivery.

**[Targeted synthetic protocol test suite](./test_if02_delivery_client_candidate.py)**, final commit `d24279095803e3d977534bce312ec86267adbc45`, exact verified GitHub blob `68baf19863ee753481a953cdfe9f2e074966cc90`, 8,729 bytes. Tests invoke a real **loopback HTTP listener backed by local SQLite**, but **the server is an explicit source-informed synthetic fixture, not Open WebUI**.

**Execution performed:** Python 3.13 local environment, with `ResourceWarning` treated as an error:

```bash
cd verification/local_ai/20261116
python3 -W error::ResourceWarning -m unittest -q test_if02_delivery_client_candidate
```

**Final result: 12 tests PASS / 0 FAIL.** The 12 scenarios covered persisted final-message update over HTTP/SQLite, idempotent repeat, changed placeholder refusal, missing placeholder refusal, wrong parent refusal, wrong API key rejection, unavailable write then retry, lost HTTP response after server committed write, delete-during-write race, explicit non-loopback rejection, redirect rejection, and unsafe dot-path ID rejection.

**Verification procedure:** Local files compiled/executed and their Git-object SHA-1 computed; independently fetched GitHub blobs matched **byte for byte** for both committed sources (hashes above). The first run of the synthetic fixture had SQLite connection resource warnings, resolved by explicit connection closing; final test run passed with those warnings elevated to errors. No dynamic behavior of an actual Open WebUI build was examined.

## Material observed limitation: deletion versus update

The pinned upstream Open WebUI v0.12.5 chat-message update path is an **upsert**, not conditional "update only if existing". The isolated fixture intentionally deleted the target assistant message between the client's preflight GET and POST, then simulated upstream's missing-ID upsert. **The message was recreated.** The client reported `PENDING / postwrite_readback_mismatch` rather than falsely claiming successful verified delivery, but it **could not prevent the phantom message from being written**. This is a substantive correctness risk, not a hypothetical hostile-party exploit.

**Disposition:** Keep owner-approved authorization direction A as the leading candidate and protect its scope. Do **not** claim exact once, zero phantom-message risk, or first-article readiness from these tests. Real pinned WebUI integration must test the deletion race. If strict prevention is required, a minimal conditional-update mechanism inside existing WebUI code may be necessary and must be justified under G-A; the owner previously approved **A as a direction**, not as a guarantee every source-level race is solved.

## What cannot be tested from this workspace

The current isolated tool environment has no installed `open_webui`, `langgraph` packages, Docker engine, known isolated Open WebUI service, or approved fixture credential. No connection to G1 or unknown running service was attempted. Therefore an actual Open WebUI Pipe→LangGraph→authenticated chat-result update, operator status/cancel controls, browser reload, process restart or offline package cannot be certified in this increment.

**Next real verification gate:** obtain a **separately authorized non-G1 Open WebUI installation** and an existing saved chat/message+preexisting allowed operator key for initial **read-only** preflight; then after appropriate G-A runtime authority conduct one bounded write, saved-chat readback, reload, retry and deletion-race test. Do not rotate the operator's existing API key or change globally shared endpoint restrictions without explicit authority.

## Governance and continuation

- 136 original requirements, 19 interface IDs, 26 original FAT oracle IDs, and their historical source/hash records untouched. Original 26 oracle executions **NOT_RUN**.
- G-R acceptance wording and G-A exact task/credential/message schema **NOT APPROVED**; no controlled baseline promotion.
- G1 OWNER HOLD; no runtime collection, configuration mutation, key handling, billable external AI API, or R3 scheduling.
- PR #1 must remain **OPEN/DRAFT/UNMERGED**, exact-head CI presence must be checked and not assumed.
- This bounded increment adds **one candidate client and one focused protocol test suite**, not another management service, extra Pipe, UI control or scheduler.

**Conversation-safety assessment:** context is adequate to continue; verified source and constraints reside in GitHub. Stop at the environment/approval gate rather than claiming real integration pass or inventing target credentials.

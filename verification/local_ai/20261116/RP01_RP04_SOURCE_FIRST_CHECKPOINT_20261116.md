# RP-01 → RP-04 source-first engineering checkpoint — 2026-11-16

**Status:** verified source identity and candidate engineering reconciliation, **not** G-R/G-A approval or execution evidence. **G1 runtime hold remains active.** The owner-supplied original recovery ZIP was inspected **outside this public GitHub repository**. No historical source files were modified, no deployed services were touched, and no billable or hosted inference calls were made.

## GitHub authority and source provenance

- Verified prior PR #1 head: `3e7a1e0e141753399f9072b9bfc7227fcdaec110`; base `46ec8e99eeb65627daa1b4296b1be32350282a67`. PR was open, draft, unmerged; original comparison was 7 commits ahead / 0 behind.
- Exact original archive: `LocalAI_Engineering_Knowledge_Transfer_Recovery_20261116.zip`; **3,451,941 bytes**, SHA-256 `9a48de5fa49420e470f003b7f3417277bd3aa2a6832a7b2c968d093004c2e37e`. Supplied to the conversation as `LocalAI_Engineering_Knowledge_Transfer_Recovery_20261116(1).zip`; byte identity confirmed. ZIP CRC PASS (14 entries), outer SHA-256 manifest **13/13 PASS**.
- Original review inputs read from nested Phase I rerun-v3 source-only packet, Phase I v3 results, original source requirement/interface allocation CSV, 2026-11-15 candidate engineering package, and independent RP-02–RP-04 review package. Source material has **not** been transferred to this public GitHub branch.
- The previous independent 2026-11-15 review field `HISTORICAL_REVIEW_PACKAGES_NOT_ATTACHED` is now outdated **for this conversation**. It remains correct as a description of its original review conditions; preserve historical text unchanged.
- **Outstanding isolated exception:** `03_REV0_16_CANDIDATE_QUALITY_AND_ORACLE_SCREENS/SHA256SUMS_rev0_16.txt` references `04_Rev0_16_Source_Identity_and_Authority.json`, SHA-256 `a9a2ce478cc5cc0647e20418787f948ac8faaaf7fd491cb6e880d10d9a1eebaa`, absent from the Phase II ZIP. Other seven referenced Rev0.16 members pass; Phase II outer manifest passes **54/54**. A recursive name/digest search through the provided nested source ZIPs did not find a replacement. **DO NOT recreate or mark as recovered.** Rev0.16 authority assertions dependent on this file remain unverified, while independently witnessed exact source statements can still be analyzed.

## RP-01 and RP-02: exact source verification

| Record set | Verified outcome |
| --- | --- |
| Original requirement statements | **136/136** exact UTF-8 statement SHA-256 hashes reproduced |
| Phase I v3 reviewer hashes | **136/136** match original |
| 2026-11-15 candidate hashes | **136/136** match original |
| 2026-11-15 separate independent candidate hashes | **136/136** match original |
| Original release labels | **121 R1 / 15 R2** (historical candidate) |
| Proposed owner-strategy allocation | **104 R1 / 17 R2 / 15 R3** (still candidate) |
| Exact source allocation triples | **159/159** requirement/need/interface triples match |
| Phase I v3 quality results | **40** with any reported C1–C15 FAIL; **96** QUESTIONED-only; v3 recommended editing all 136 |
| R1 derived gap docket | **7 candidate proposals**, not accepted requirements |

**Engineering judgment:** the v3 recommendation to rewrite all 136 is not supported by its own 40/96 distinction. Keep each original ID, exact statement and hash; make *targeted* wording and acceptance-criterion corrections. Neither a QUESTIONED flag nor a generic reviewer replacement creates an approved requirement.

The following original scope discrepancies are explicitly resolved for **candidate allocation only**, not the baseline:
- N009 5 outbound-context-policy items, N012-02 provider permission, N013 6 paid-call items, N014 5 external-provider items: original R1 → proposed **R2** (17).
- N025, N026, N027 (five each): original R2 → proposed **R3** (15).
- Other 104 originals remain proposed **R1**. Historical IDs such as `LAI-R1-N014-01` stay unchanged even though corrected release scope is R2. This particular original statement incorrectly says “in Release 1 acceptance”; replacement wording needs an explicit controlled amendment.
- **Do not count R2-only consent/billing engines or hosted-provider mocks as R1 build obligations.** R1 needs only the four owner-approved design seams AC-01–AC-04.

Targeted substantive corrections include: `LAI-R1-N001-01` target Bodhi 7 AMD64 (do not hard-code the testing laptop as a product requirement); `N002-05` / `N017-01` duplicate history ownership; `N011-06` / `N018-01` duplicate tool grants; `N008-02` truthful checkpoint recovery; `N010-02` R1 telemetry is disabled, not merely restricted to an approved destination; `N010-03` 30-day retention applies to **sanitized metadata only**; `N010-04` and `N020-03` backup encryption no longer mandatory; `N020-05` must cover Open WebUI history, LangGraph checkpoints **and** Bifrost configuration; `N021-04` rollback includes durable-data compatibility; `N022-05` unnecessary licensed-edition feature detection; `N023-04` merge metrics into N023-01 evidence; `N023-05` acceptance limits are test criteria, not an extra runtime subsystem; and `N024-02` unreported local token counts must remain unknown. Do not add hostile-actor engineering solely to protect self-recalculated checksums on a single-operator host.

**Seven derived gap proposals:** task-status observability, cancellation, local-only routing/telemetry, three-owner restoration, future optional backup encryption-format seam, R2 architectural extension without core redesign, and prohibition of unattended R1 execution. These require explicit requirement-level independent review before G-R.

## RP-03: 19 interface contracts — source-first bounded resolution

**All 19 original IDs recovered and compared.** Wire-format, timeouts, selected Open WebUI integration mechanism, Bifrost behavior and source/consumer responsibility remain **UNFROZEN**; G-A is blocked. No pinned runtime proof was newly obtained.

| Interface IDs | Bounded disposition |
| --- | --- |
| `IF-01`, `IF-LOCAL` | R1 direct Open WebUI → Bifrost OSS → Ollama; LangGraph bypass; distinguish model listing, ordinary chat, SSE and selected/dispatched/resolved model identity |
| `IF-02`, `IF-03`, `IF-06` | R1 delegated Open WebUI → independent LangGraph → Bifrost; task ID, status, cancellation and durable checkpoints owned by supervisor, not by WebUI history |
| `IF-05`, `IF-UI` | Open WebUI owns conversation history and operator mode; no second conversation archive in LangGraph |
| `IF-LOG`, `IF-MGMT`, `IF-CRED`, `IF-POLICY` | R1 single-operator local-only admin, sanitized 30-day metadata, no external application telemetry; future R2 external credentials, consent and spend enforcement are **seams**, not implementations |
| `IF-TOOL`, `IF-OPS` | R1 bounded tool grants and target-service lifecycle; avoid generic enterprise tool broker or architecture-mandated service-manager product names |
| `IF-BACKUP`, `IF-PACK` | R1 local access-controlled backup and verified restore, optional future encryption envelope; **primary Debian .deb plus full dependency transport archive approved** |
| `IF-04`, `IF-BUDGET` | Defer hosted provider APIs and paid-call/budget controls to **R2** |
| `IF-SCHED`, `IF-AGENT` | Defer autonomous scheduler and external-agent protocol to **R3**. R1 internal LangGraph specialists do not require R3 agent registry |

**Specific review correction:** the prior independent IF-PACK comment “unapproved .deb format” conflicts with the subsequent owner-approved packaging method. The original IF-BACKUP draft prescribes encrypted offline backup, which is obsolete. Prior IF-02 commentary implies both a Pipe adapter and local API are necessarily required; do not mandate two integration mechanisms before validating the selected Open WebUI-supported path. A functional independent supervisor remains mandatory.

## RP-04: 26 candidate verification oracles

**26/26** candidate oracle identities link to original requirement IDs and separate reviewer source records. None was executed or independently accepted. Current provisional scope: the external consent, paid-call, and hosted-provider cases belong to **R2**; consequential unattended-action case `GRGA07-F26` belongs to **R3**. Remaining local cases are R1 candidates, with `GRGA07-F17` conditional on actual R1 native tool-call use.

Proposed independently observable R1 FAT witnesses, not test results: (1) direct chat reaches Bifrost/Ollama without invoking LangGraph; (2) delegated workflow has at least two specialist roles with visible task states, cancellation and restart persistence; (3) gateway authentication and model authorization failures do not dispatch inference; (4) malformed/cancelled SSE is not reported as completion; (5) retained diagnostics have no prompt, response or secret content; (6) no R1 hosted inference or external telemetry, **without** banning necessary LAN or authorized downloads; (7) offline .deb/dependency-archive installation and a three-owner restore succeed on an isolated target; (8) checkpoint and data-mount failures are detected without fictitious success.

An oracle is accepted only after its source requirement/interface is authorized, its positive/negative/recovery witness is independently challenged, and observed output is recorded. Mock/synthetic predicate cases are **not** installed-system FAT evidence. **All states: NOT RUN; G1 on hold.**

## Approval and next-action boundaries

- Preserve governing Standard v1.0, historical originals, owner decisions, 14 RP and 42 increment identifiers, and original requirement/interface/oracle IDs.
- Release 1 = local direct + delegated LangGraph paths, Ollama-only, .deb plus complete offline transport, verified local backup/restore. Release 2 = authorized OpenAI and Anthropic. Release 3 = persistent autonomous operation.
- AC-01 through AC-04 approved as architectural **directions** only. FAT Alternative B requires actual installed operational demonstration and recorded owner acceptance, not merely entry permission.
- FUT-001 multi-host Ollama remains exploratory, release-unassigned.
- **No requirement wording, release allocation, interface schema, or oracle predicate is hereby baselined or owner-accepted.** G-R and G-A remain blocked.
- **Next bounded increment:** complete source-sensitive semantic scrutiny of the 136 candidate dispositions, resolve explicit wording for critical owner-constrained items, independently review concrete R1 producer/consumer contracts and positive/negative/recovery predicates against pinned versions *offline*; preserve any new source provenance and take G-R/G-A owner decisions only when evidence and options are complete. Keep all PRs draft/unmerged.
- **Public-repo disclosure control:** the original 3.45 MB source bundle includes nested historical owner messages and runtime evidence. No upload of source ZIP/ODT or full source-text CSV here without explicit disclosure review/approval. The user's uploaded archive is available in the conversation for independent source-first work; it does **not** yet establish cross-conversation GitHub storage.

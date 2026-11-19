# Local AI — Full 42-increment Rev 0.2 risk-proportionality audit (candidate)

**Date:** 2026-11-18. **Status:** candidate planning recommendation, NOT an approved G-R/G-A or work-package revision.
**Source:** owner-supplied `LocalAI_Release_Strategy_Rev0_2_Candidate_Engineering_Package_20261115(2).zip`, SHA-256 `0e3c45e6d5fd5b0180264a542030c10cca8ca48c6b0ba196ab378276c214ffc1`. ZIP CRC PASS; **12/12 internal member SHA-256 checks PASS**. Actual Rev 0.2 roadmap ODT and actual 42-row source trace CSV were read. The source ZIP and its raw original requirements are NOT published in this repository.
**Scope:** 14 original RP packages, 42 increment IDs, original 136 requirements/27 validated needs, 19 interfaces/159 allocations and 26 original FAT oracle identities. These identities are unchanged; source reads and review are not execution tests.

## Summary of each retained identity

Classifications: **RETAIN 15, SIMPLIFY 12, COMBINE 12, DEFER 2, REMOVE 1**. COMBINE and REMOVE affect *separate work activities*, not approved need outcomes. DEFER may mean R1 scope still requires a non-runtime design seam or that G1 must await express hold release.

| Increment | Candidate | Minimum remaining scope and disposition |
| --- | --- | --- |
| RP-01.INC-01 | **COMBINE** | GR baseline/FAT provenance; no repeat historical searches |
| RP-01.INC-02 | **DEFER** | Live G1 runtime identity until owner releases hold; preserve repository reads |
| RP-01.INC-03 | **SIMPLIFY** | One direct, one delegated, backup, offline FAT journey; narrow no-egress claim |
| RP-02.INC-01 | **COMBINE** | Reuse completed 136-item source review; only unresolved G-R deltas |
| RP-02.INC-02 | **COMBINE** | Keep approved 104/17/15 release assignments, no second allocation cycle |
| RP-02.INC-03 | **RETAIN** | One owner-reviewed controlled G-R candidate and trace |
| RP-03.INC-01 | **SIMPLIFY** | Single 19-interface and 159-allocation matrix |
| RP-03.INC-02 | **SIMPLIFY** | Pin only used local HTTP/SSE/auth/status/error semantics |
| RP-03.INC-03 | **COMBINE** | Bifrost decision plus AC-01..04 R2 seams in one G-A review |
| RP-04.INC-01 | **SIMPLIFY** | Preserve 26 source oracle identities; shared connected test witnesses |
| RP-04.INC-02 | **COMBINE** | Use real RP12 integrated instrumentation, no separate harness framework |
| RP-04.INC-03 | **COMBINE** | Reuse common FAT receipts and independent evidence |
| RP-05.INC-01 | **RETAIN** | Pinned stack/Bodhi ABI and measured resource minimum |
| RP-05.INC-02 | **RETAIN** | Build independently managed actual R1 services and storage mounts |
| RP-05.INC-03 | **COMBINE** | Real restart and local-only witness within RP12/RP14 |
| RP-06.INC-01 | **SIMPLIFY** | Reuse WebUI/Bifrost auth; one local tool gate if used |
| RP-06.INC-02 | **REMOVE** | No standalone blanket network-denial interceptor; transfer local-only and telemetry checks to RP06/RP12 |
| RP-06.INC-03 | **RETAIN** | Basic local secret, bind and log protections |
| RP-07.INC-01 | **COMBINE** | One UI installation/history readback in RP05/RP12 |
| RP-07.INC-02 | **COMBINE** | One real model selection and alias witness in RP08 |
| RP-07.INC-03 | **RETAIN** | Actual direct local chat/stream/history/error journey |
| RP-08.INC-01 | **COMBINE** | Actual gateway virtual-key/list/timeout checks in RP07/RP12 |
| RP-08.INC-02 | **SIMPLIFY** | Real Ollama usage/timeout/restart; no custom rate engine |
| RP-08.INC-03 | **DEFER** | R2 hosted implementation; retain R1 AC-01..04 design review |
| RP-09.INC-01 | **SIMPLIFY** | One Pipe, one separate supervisor, two static roles |
| RP-09.INC-02 | **RETAIN** | Actual durable checkpoint/restart/cancel tests |
| RP-09.INC-03 | **RETAIN** | Real two-specialist synthesis and automatic same-chat final delivery |
| RP-10.INC-01 | **SIMPLIFY** | Basic sanitized correlation and observed-or-UNKNOWN counts |
| RP-10.INC-02 | **RETAIN** | Simple 30-day sanitized metadata retention and one purge witness |
| RP-10.INC-03 | **COMBINE** | Auth/timeout/redaction checks within RP06/RP12 |
| RP-11.INC-01 | **SIMPLIFY** | Offline backup manifest with optional future encryption seam |
| RP-11.INC-02 | **RETAIN** | Independent clean-host restoration of WebUI/LangGraph/Bifrost |
| RP-11.INC-03 | **COMBINE** | Representative restart/missing-target/rollback failures in RP09/11/13 |
| RP-12.INC-01 | **RETAIN** | Actual integrated dual-route and restore FAT journey |
| RP-12.INC-02 | **SIMPLIFY** | Few meaningful failures; tools conditional on R1 workflow |
| RP-12.INC-03 | **RETAIN** | Measured Bodhi host resource and usability limits |
| RP-13.INC-01 | **RETAIN** | License/redistribution BOM and notices |
| RP-13.INC-02 | **RETAIN** | Actual home-use .deb and complete offline archive |
| RP-13.INC-03 | **SIMPLIFY** | One supported upgrade and compatible rollback |
| RP-14.INC-01 | **RETAIN** | 104 R1 requirements mapped to accepted evidence/exceptions |
| RP-14.INC-02 | **SIMPLIFY** | Reuse RP12/13 evidence in one actual target rehearsal |
| RP-14.INC-03 | **RETAIN** | Correct endpoint to actual installed FAT execution and owner acceptance |

## Disposition trace and material exceptions

- **RP-01.INC-01**: evidence moves to RP-02.INC-03 / RP-14.INC-01. **RP-01.INC-02**: G1 read-only runtime observations deferred until hold release; initial repo checks can proceed.
- **RP-02.INC-01/02**: dispositions already reviewed and release allocation approved; fold residual G-R into RP-02.INC-03. **RP-03.INC-03**: fold into RP-03.INC-01 and pinned RP-05 source compatibility; no new provider abstraction subsystem.
- **RP-04.INC-02/03**: evidence collection in RP-12/RP-14, not another independent mock/test infrastructure. **RP-05.INC-03**: lifetime/egress witness in RP-12/RP-14.
- **RP-06.INC-02 REMOVE** as an independently implemented *blanket network-denial/interception control*. Local-only model dispatch, no unapproved hosted fallback, and no external app telemetry still verified in RP-06.INC-03 / RP-12.INC-01, with AC-04 future policy seam in RP-03. Allow local/LAN service traffic and authorized downloads. This is not permission for R1 hosted AI.
- **RP-07.INC-01/02**: move to RP-05/RP-08 and connected RP-12 scenario. **RP-08.INC-01**: combine with actual RP-07/RP-12 black-box runs; **RP-08.INC-03 DEFER** external provider implementation to R2, while R1 verifies AC-01..04 non-redesign design only.
- **RP-09.INC-01**: no registry or second UI; two fixed specialist roles with one trusted Pipe/independent supervisor. **RP-09.INC-03** must include approved prompt task ID and *automatic* same-conversation final-result delivery, via owner-approved operator key direction; real installed verification not yet done.
- **RP-10.INC-03**: combine privacy/error checks with RP-06/RP-12. **RP-11.INC-03**: combine crash/recovery/rollback with RP-09, RP-11 and RP-13. **RP-14.INC-02**: reuse engineering-test evidence, but still demonstrate the installed system on supported target.
- **RP-14.INC-03**: later owner-approved FAT Alternative B means the end state is **executed installed functional FAT plus independent review and owner acceptance**, not merely FAT-entry GO. This candidate corrects the original November 15 planning wording.
- **Tool-call scope**: N016-03/04 and original F17 are conditional on actual R1 use. N018 tool grant must protect actual selected nondestructive tools without a general tool-policy service. Exact G-R applicability remains unapproved.
- **Low-impact speculative race**: one deleted-message/upsert check retained for eventual real Open WebUI tests; do not fork WebUI solely for an unobserved race. **High-impact essential protections kept**: durable supervisor recovery/cancel, mount-before-write, protected credentials, 30-day sanitized metadata, offline installation/license check, independent restore of three stores.

## Compressed remaining critical path (not a renumbering)

1. Complete only material remaining G-R/G-A owner gates, pinned source versions and witnessed release applicability.
2. Run one real non-G1 local direct path and single-Pipe independent two-specialist LangGraph path, status/cancel, automatic completion delivery and restart recovery.
3. Establish measured Bodhi 7 AMD64 limits, actual local secrets/privacy/usage, and one representative negative failure per materially consequential risk.
4. Produce `.deb`, complete offline archive, license/ABI evidence, verified access-controlled offline backup and clean three-store restore.
5. Conduct the installed first article FAT, map shared real evidence to all applicable original R1 requirement/interface/oracle IDs, and record owner FAT acceptance.

**Governance:** original requirements 136 and releases 104/17/15 preserved; original interfaces 19 and oracle IDs 26 preserved; original FAT tests remain NOT_RUN; G-R/G-A NOT APPROVED; G1 owner hold active; no paid external calls, G1 changes, credential changes, original source archive upload, PR merge or owner approval inferred. Formal changes require explicit review.

# RP-02 second-pass independent requirements-quality adjudication — 2026-11-16

**Status:** independent **candidate** second pass; **NOT** owner G-R approval, product implementation or acceptance evidence. Original source records, original statements, original hashes and all 136 IDs remain unchanged. This document **qualifies**, but does not retroactively rewrite, the prior [28 proposed rewrites](./RP02_28_EXACT_WORDING_PROPOSALS_CANDIDATE_20261116.md).

## Source-first verification

- Original owner-supplied recovery package: `LocalAI_Engineering_Knowledge_Transfer_Recovery_20261116.zip`, **3,451,941 bytes**, SHA-256 `9a48de5fa49420e470f003b7f3417277bd3aa2a6832a7b2c968d093004c2e37e`.
- Independent comparison: **136/136** exact statements, SHA-256 hashes, parent needs and source identifiers match the original `02_BLIND_REVIEW_TARGETS/136_REQUIREMENT_SOURCE_ONLY.csv` from the original Phase I v3 input. All referenced parent need identifiers resolve to the original `validated_needs_original.csv`.
- All **28** earlier candidate replacement statements reviewed against the original controlled text, validated need statements, later owner-approved R1/R2/R3 strategy, and the governing Standard v1.0 quality principles (necessity, one obligation, explicit conditions, independently falsifiable verification).
- Original source-exact text and source-sensitive local 28-row review file are retained *outside this public repository*. Private local QA file SHA-256: `137a879beb96b2f10d6d0b0218ec5c004948fb7d3fbb36a34ab37d1bd2a0f6c5`. Public ID/disposition register SHA-256: `d1fa1e6c47c26b75d0c3be765b293eae898ec71f54bac7be51b96e720424e493`.
- **21 SUSTAIN_CANDIDATE**, **5 REFINE_CANDIDATE**, **2 RETAIN_ORIGINAL**. This is **not** a declaration that 21 are independently accepted: all remain source-review candidates pending G-R and exact acceptance-oracle review.

## Two unnecessary changes: recommend original wording

| Requirement | Second-pass judgment | Source-based rationale |
| --- | --- | --- |
| `LAI-R1-N005-03` | **RETAIN ORIGINAL**, no new wording needed | Original singular consolidation obligation is sufficient alongside separately retained N005-02 (specialist identity), N005-04 (contribution provenance), N005-05 (evaluation before synthesis), and N006-02 (missing response disclosure). Previous rewrite to "successful responses" narrows scope without resolving an actual duplicate requirement |
| `LAI-R1-N019-03` | **RETAIN ORIGINAL**, define verification attributes | Original required health-monitor distinction among healthy, degraded and unavailable is sound. Rewriting it as "local health view" may mandate an unnecessary new UI/dashboard. Define independently observable service-state criteria in verification data instead |

## Five candidate replacements need refinement

All text below is **newly proposed**, not historically approved. Do not replace source statements until exact G-R owner authorization.

| Requirement | Second-pass refinement | Residual acceptance predicate |
| --- | --- | --- |
| `LAI-R1-N008-02` | "After a supported supervisor restart, the supervisor shall resume each interrupted checkpointed task from its last durable workflow state or place it in a documented terminal state according to the approved task-state transition contract." | Compare durable checkpoint with resumed execution; corrupted/unavailable checkpoint belongs to existing N008-04; task-state machine must be reviewed before approval |
| `LAI-R1-N010-03` | "The log-retention process shall remove sanitized operational request and diagnostic metadata according to a 30-day maximum retention policy, excluding conversation history and backup data." | **Open detail:** disposal cadence/tolerance must be defined and approved; 30 days is owner-approved, but do not invent a midnight/24h purge tolerance |
| `LAI-R1-N010-06` | "For each Release 1 diagnostic export, the export function shall omit raw prompt content, response content and credential-secret values." | Conditional requirement applies to existing diagnostic export; not authorization to create an additional export subsystem or to export content under a general exception |
| `LAI-R1-N017-05` | "The Release 1 deployment manifest shall identify the installed version or digest and configured interface endpoint of each required deployed component." | A reproducibility/deployment-data artifact, **not** a new runtime inventory service; verify installed version/endpoint against manifest |
| `LAI-R1-N021-04` | "After failure of a supported application upgrade, the rollback procedure shall restore the last validated compatible release while retaining access to chat history and supervisor checkpoints committed before upgrade initiation." | Bound supported upgrade/rollback and storage migration; demonstrate data readback on isolated host without requiring indefinite rollback to arbitrary incompatible versions |

**Caution:** The N008-02 wording does not by itself freeze the supervisor's transition states. The N010-03 wording is not verifiably complete without an approved purge-tolerance criterion. These are explicit interface/oracle review gaps, not basis for unapproved implementation assumptions.

## Remaining 21 candidate rewrites

The bounded independent pass found no new source contradiction warranting another replacement for the following; retain **candidate-only** status pending G-R:

`LAI-R1-N001-01`, `LAI-R1-N005-01`, `LAI-R1-N006-03`, `LAI-R1-N009-02` (R2), `LAI-R1-N009-05` (R2), `LAI-R1-N010-01`, `LAI-R1-N010-02`, `LAI-R1-N011-04`, `LAI-R1-N011-05`, `LAI-R1-N012-04`, `LAI-R1-N014-01` (R2), `LAI-R1-N017-04`, `LAI-R1-N018-05`, `LAI-R1-N020-05`, `LAI-R1-N024-04`, `LAI-R1-N024-05`, `LAI-R2-N025-02` (R3), `LAI-R2-N025-04` (R3), `LAI-R2-N026-04` (R3), `LAI-R2-N027-03` (R3), `LAI-R2-N027-05` (R3).

Cross-requirement observation: N011-05, N024-05, N010-01 and N010-06 all use a shared sanitized-diagnostics implementation/verification witness where appropriate. The requirements may remain distinct as to their source and triggering condition without creating four redundant log subsystems.

## Required G-R decision docket (not submitted as owner acceptance)

1. **Exact wording:** consider **26** still viable rewrite candidates: 21 currently sustained plus five proposed refinements; preserve original text of N005-03 and N019-03. All 136 IDs remain controlled and unchanged until approval.
2. **Release allocation:** independently accept or alter provisional **104 R1 / 17 R2 / 15 R3**. Historical R1/R2 prefixes remain immutable identifiers even when current release assignment changes.
3. **Classification conflicts:** `LAI-R1-N001-04`, `LAI-R1-N023-05` are primarily FAT/host evidence items; `LAI-R1-N022-05` proposed retire unnecessary proprietary-edition discovery; `LAI-R1-N016-03` model-native tool-call fidelity conditional on actually used R1 workflow. No silent delete or implementation scope expansion.
4. **Acceptance metadata:** approve task-state transition vocabulary, service health checks, supported upgrade/rollback envelope, purging tolerance, and exact witnessed release conditions **as verification attributes or interface contracts**, not new platform services.
5. **All 108 previously unrewritten items** still require approved applicability and acceptance dispositions. This 28-row second pass does not itself certify them.

## Continuation

Next: independently review the R1 **IF-01/IF-02/IF-03/IF-06** producer/consumer boundaries, task state/cancellation, and gateway admission against versioned source before any G-A freeze. Reuse the smallest sufficient Open WebUI integration; avoid duplicating supervisor, chat history or installing extra task infrastructure.

**G-R BLOCKED / G-A BLOCKED / G1 runtime OWNER HOLD / no runtime tests / no paid API calls / PR DRAFT UNMERGED**.

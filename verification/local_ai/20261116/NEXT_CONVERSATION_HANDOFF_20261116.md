# Local AI Development — next-conversation engineering handoff
**Date:** 2026-11-16  
**Status:** GitHub-based recovery checkpoint / candidate engineering work; **NOT** a product baseline  
**Governing method:** AI-Assisted Software Engineering Governance Standard v1.0  
**Authoritative repository:** https://github.com/joeblow42/Local-Linux-AI-Orchestration  
**Draft PR:** https://github.com/joeblow42/Local-Linux-AI-Orchestration/pull/1  
**Development branch:** `handoff/localai-20261116-recovery`  
**Verified predecessor HEAD:** `71d583c960d8c471ad0ae3b1692a9dfcf22f47ff`  
**Base main:** `46ec8e99eeb65627daa1b4296b1be32350282a67`  
**This handoff:** Read at the actual PR HEAD; if updated after the predecessor, validate the new exact-head state. All PR work stays **draft/unmerged**.

## Required startup verification

1. Re-read PR #1 and branch HEAD from GitHub; verify open/draft/unmerged, exact SHA and base relation. Do not assume the predecessor SHA is still HEAD after this handoff commit.
2. Read `verification/local_ai/20261116/README.md`, `ENGINEERING_HANDOFF.md`, `OWNER_DECISIONS_RP02_RP03_APPROVED_20261116.md`, `OWNER_APPROVED_136_RELEASE_ASSIGNMENTS_20261116.csv`, `RP02_136_SOURCE_FIRST_RECONCILIATION_AFTER_OWNER_APPROVAL_20261116.md`, `RP02_136_APPROVED_SCOPE_SOURCE_REVIEW_CHECKPOINT_20261116.json`, and `RP03_R1_MINIMUM_INTERFACE_AND_TASK_LIFECYCLE_CANDIDATE_20261116.md`.
3. For the full requirements review read `RP02_96_QUESTIONED_ONLY_SOURCE_FIRST_SCREEN_CANDIDATE_20261116.csv`, `RP02_28_CONSOLIDATED_EXACT_WORDING_CANDIDATE_20261116.csv`, and supporting 28/12 second-pass candidate records.
4. For verification design read `RP04_R1_OPERATIONAL_FIRST_ARTICLE_ORACLES_CANDIDATE_20261116.md`, `RP04_26_ORACLE_SCOPE_INDEX_CANDIDATE_20261116.csv`, and `RP03_PINNED_SOURCE_AND_IF02_ADAPTER_PREPARATION_CANDIDATE_20261116.md`.
5. **Original source limitation:** The exact original `LocalAI_Engineering_Knowledge_Transfer_Recovery_20261116.zip` (3,451,941 bytes; SHA-256 `9a48de5fa49420e470f003b7f3417277bd3aa2a6832a7b2c968d093004c2e37e`) was examined in the preceding conversation but is **NOT uploaded to this public GitHub branch**. The separate local source-sensitive review CSVs are also **NOT uploaded**. For new exact-original quotation, source-sensitive independent adjudication or final authoritative G-R decision, obtain the original ZIP again in the new conversation and verify its SHA-256 before relying on content. GitHub summaries/public indexes do not substitute for original bytes. Do not publish nested archives or owner/system observations to public GitHub without disclosure review.

## Controlling owner-approved engineering direction

- **Release 1:** Single-operator local app with Open WebUI, **Bifrost OSS** gateway (approved replacement for historical LiteLLM), local Ollama, **independent LangGraph supervisor** for user-initiated multi-step specialist delegation; direct chat bypasses LangGraph. Require stable delegated task ID, observable status, durable checkpoints, cancellation and recovery. Deliver supported Bodhi Linux 7 AMD64 `.deb` and complete offline dependency transport archive. Perform access-controlled local offline backup with independently verified restoration of Open WebUI conversation history, LangGraph task/checkpoint and Bifrost configuration. Mandatory encryption **deferred**; future optional format seam permitted. No R2 hosted provider APIs/mocks, paid external inference or R3 autonomous scheduler in R1.
- **Release 2:** Independently operational OpenAI and Anthropic API integrations with explicit owner authorization, protected credentials/context and usage/spend controls; **no paid calls currently authorized**.
- **Release 3:** Persistent unattended/autonomous workflows and scheduling.
- **FAT:** Owner approved Alternative B — genuine operational installed-system first-article demonstration and recorded owner acceptance, not readiness alone.
- **Four approved design seams (AC-01..04):** common gateway boundary, selected/dispatched/resolved model identity, separate future external secret ownership, request-scoped context-consent/field-projection/spend-policy insertion points. R1 **design** obligation; no R2 provider implementation.
- **FUT-001:** Multiple LAN computers with separate Ollama backends is exploratory, unassigned and not implementation scope.

### Most recent owner approval — A/A/A

The owner explicitly approved **Alternative A for each** in the RP-02/RP-03 owner docket, now recorded in `OWNER_DECISIONS_RP02_RP03_APPROVED_20261116.md`:

1. **`LAI-OD-20261116-01`:** Current release assignment of **136 original IDs = 104 R1 / 17 R2 / 15 R3**. Preserve historical requirement ID prefixes regardless of assigned release. Release allocation approved; original wording and acceptance **NOT** G-R approved.
2. **`LAI-OD-20261116-02`:** Avoid unjustified R1 planner/profiler/monitor daemon, licensed-edition detector, redundant authorization infrastructure. Use existing component controls, installer preflight and FAT instrumentation, retaining validated outcomes. Proposed retirement/split/reclassification of individual requirements still needs controlled G-R approval; no license compliance or measurement obligations waived.
3. **`LAI-OD-20261116-03`:** **Provisional** one thin trusted Open WebUI Pipe to a separate localhost LangGraph HTTP service for delegated tasks, subject to exact version compatibility and G-A. UI owns conversation history; LangGraph owns tasks, statuses, cancellation, checkpoints and recovery; direct Open WebUI → Bifrost → Ollama bypasses supervisor. No duplicate mandatory adapter.

## Exact verified engineering status

- Original 136/136 requirement IDs, statements, SHA-256 hashes and parent validated needs independently checked; **27 validated needs**. Original source bytes not edited.
- V3 quality audit reported **40** with one or more FAIL and **96** QUESTIONED-only. All 136 received a candidate second-pass disposition. Reported FAIL != mandatory rewrite; QUESTIONED != PASS.
- 40 FAIL group: prior 28 replacement proposals independently challenged (**21 retained as candidates, 5 refined, 2 proposed to retain original**); 12 have source/duplicate/deferral/classification dispositions without rewriting.
- Remaining 96 QUESTIONED-only group: **43** retain with pending verification, **30** targeted qualifications, **2** new candidate rewrites, **21** deferred to the owner-assigned R2/R3 release. Their owner-approved release distribution is 75 R1 / 12 R2 / 9 R3.
- Final consolidated text proposal: **28 active replacement candidates** (21+5+2); **108 originals without active replacement**. Wording, retirement, technical thresholds and final verification criteria remain **G-R unapproved**. In particular, N023-02 installer storage threshold has no authorized number; N024-02 must mark absent local usage counts **UNKNOWN**, not fabricate measured values.
- Preserve all **19** original interface IDs, owner-selected tentative IF-02 Pipe direction, and **26** original oracle IDs. All test oracles **NOT RUN**. Prior RP-03 logical interface contract and RP-04 falsification design are **candidate/unfrozen**, not deployed compatibility or actual FAT results.
- Tagged Bifrost source documentation has been examined at `maximhq/bifrost` commit `e869c3f9adc96ea53c38694a21bb04a8e1085487` (`transports/v2.4.0`); this is not proof that the deployed pinned OCI gateway behaves exactly as documented. The installed Open WebUI and LangGraph exact versions/source pins remain **UNVERIFIED**. Do not claim IF-02 version compatibility without evidence.
- The isolated missing Rev0.16 source-identity JSON is **CLOSED / DOCUMENTED MISSING ORIGINAL / NONBLOCKING** under the owner-authorized bounded search and risk disposition in `REV016_SOURCE_EXCEPTION_CLOSED_20261116.md`. Do not repeatedly list it as an open blocker; reopen only for specifically contradictory/source-critical evidence or owner direction.
- **G-R exact requirements/acceptance baseline: NOT APPROVED. G-A concrete interface baseline: NOT APPROVED. G1 gateway data-collection and runtime-verification: OWNER HOLD. FAT: NOT RUN. No billable external APIs, runtime mutations, requirements-baseline promotion or PR merge authorized.**

## Next engineering increments (in order)

1. **RP-02/G-R:** Turn the source-checked 136-item candidate disposition into a controlled owner-review acceptance-criteria matrix, separated by product requirement vs deployment/FAT verification/compliance obligation vs deferred R2/R3. Keep 136 immutable historical IDs and exact source hashes. Review 28 replacement candidates and individual retirement/reclassification items; do not approve on behalf of owner. Avoid invented numbers or new module complexity.
2. **RP-03/G-A:** Source-pin the actual intended Open WebUI and LangGraph versions, and confirm a single thin Pipe can expose task submit/status/cancel/results with separate durable LangGraph service. Compare authoritative producer/consumer semantics for IF-01, IF-02, IF-03, IF-06 first; extend to all 19. Prepare source/fixture-only negative, cancel race, restart, stream-failure and checkpoint tests while G1 is held. Bifrost docs at tagged version are partial evidence; no live G1 API test.
3. **RP-04:** Source-link positive/negative/recovery predicates to approved requirements and candidate interfaces, clearly separate NOT RUN, NOT APPLICABLE, and genuine future PASS. Build genuine **installed first article** FAT plan, not a claim of test execution.
4. After independent reviews, present **only materially necessary owner decisions** for actual G-R/G-A baselines or G1 hold release. No additional routine permission requests. Assess conversation continuity after each substantial increment; commit verification receipts to GitHub, keeping PR draft and unmerged.

**Governance guardrails:** Preserve accepted decisions and historical IDs, never rewrite original evidence, verify every material checkpoint and exact GitHub HEAD, separate approved directions from candidate technical baselines, and challenge unjustified complexity. The GitHub checkpoint is sufficient to transfer approved decisions and the engineering worklist; to conduct **source-sensitive final authority adjudication**, recover original source bytes first.

# Local AI Development — RP-02 through RP-04 verified engineering continuation checkpoint
**Date label:** 2026-11-16 engineering series; authoritative current status is GitHub commit, not a date-based claim.  
**Scope:** bounded requirements/acceptance, pinned-source interfaces, oracle falsification. **No product baseline approved.**  
**Pre-checkpoint exact PR HEAD:** `cf933d6d194e342d22345405a88013f9f224b9a5`; **base main:** `46ec8e99eeb65627daa1b4296b1be32350282a67`; draft PR [#1](https://github.com/joeblow42/Local-Linux-AI-Orchestration/pull/1) open/unmerged. Verify the actual PR HEAD upon recovery; this checkpoint file and README linkage create later commits.

## 1. Recovery and authority
The prior [next-conversation handoff](./NEXT_CONVERSATION_HANDOFF_20261116.md) and three latest [owner approvals](./OWNER_DECISIONS_RP02_RP03_APPROVED_20261116.md) were read at original verified head `b4f245d4fb71c430dc7de8d5c0bbf7abe071f09a`. Verified original branch was 45 commits ahead / 0 behind base; latest pre-checkpoint branch was 50 ahead / 0 behind, PR draft and unmerged.

Approved directions unchanged:
- **104 R1 / 17 R2 / 15 R3** allocation for all original 136 IDs, preserve history and source bytes; **not** G-R wording/acceptance approval.
- Avoid unnecessary R1 resource-planner/monitor/edition-detector/duplicate policy subsystems; preserve required outcomes and FAT evidence.
- Provisional single trusted Open WebUI Pipe → independent local LangGraph HTTP supervisor, direct chat bypasses supervisor; **not** G-A approval.
- R1 local Ollama through Bifrost OSS, Open WebUI and two-specialist LangGraph delegation, task status/cancel/recovery, Bodhi 7 AMD64 .deb and full offline transport, access-controlled unencrypted-at-rest-permitted offline backup and verified three-owner restoration. R2 authorized OpenAI/Anthropic APIs; R3 persistent autonomous work; FAT Alternative B actual installed operational demonstration and owner acceptance.

## 2. New RP-02 acceptance draft and verified evidence
- [136-row acceptance/applicability/source-hash candidate](./RP02_136_ACCEPTANCE_AND_APPLICABILITY_REVIEW_CANDIDATE_20261116.csv), commit `43728a079a4d32b2eee6ec2eb07c08cad93ec211`; all **136/136** historical IDs, 27 need groups, approved release assignments, 28 replacement-candidate SHA refs, proposed positive and negative/recovery witnesses, per-item G-R gate, **NOT_RUN**, **CANDIDATE_NOT_G_R_APPROVED**.
- [Independent matrix verification receipt](./RP02_136_ACCEPTANCE_REVIEW_VERIFICATION_CHECKPOINT_20261116.md), commit `9ae1761c281dcb8115998b1c829a378d79bcc014`. Read an earlier Library-held 136-row source-anchored quality audit and independently recomputed all **136 SHA-256 of its extracted statement text**. All matched that historical audit; cross-referenced **124** public register entries covering **122** distinct ID hashes, all match. The other **14** are supported by the historical audit only, **not the original absent ZIP**. Original statement text was **not** published to GitHub. No hash mismatch found.
- Original recovery ZIP (3,451,941 bytes, SHA256 `9a48de5fa49420e470f003b7f3417277bd3aa2a6832a7b2c968d093004c2e37e`) remains outside public GitHub. Final source-sensitive G-R authority requires the exact original bytes or an owner-authorized explicit alternative with preserved provenance; do not silently substitute a derived audit. **Rev0.16 missing-JSON exception remains CLOSED/NONBLOCKING**.
- Pending owner-controlled G-R dispositions include N022-05 retirement; N023-05 verification/FAT classification; N021-03 packaging/compliance split; N018-02 R1 consequential tool-action restriction; N016-03/04 native tool-call applicability; N012-05 vendor permission revision; N023-02 measured storage threshold. Do not invent numbers.

## 3. New RP-03 pinned-source work (NOT G-A)
- [Exact source compatibility review IF-01/02/03/06](./RP03_PINNED_IF01_IF02_IF03_IF06_STATIC_COMPATIBILITY_CANDIDATE_20261116.md), commit `aca4a5171fae276c5ba1b9e72e4f570977ea07dd`. Historical repo `.in` candidate pins `open-webui==0.12.5` and `langgraph==1.2.19`; immutable upstream commits `f7ac7ee10962ddec0017f5c29b6740d9b9c5faca` and `5bd231cbfd913e05ebc662f519eb9a655bc766df` verified. These are source targets, **not installed versions or an approved lock**. Historical LiteLLM `.in` is superseded as gateway architecture by Bifrost OSS.
- Open WebUI exact source supports single model-selectable `Pipe` and signature-filtered keyword arguments. Event callback availability depends on metadata. UI `Stop` can cancel UI streaming without proving durable supervisor `cancel(task_id)`; **this is material IF-02 design/acceptance ambiguity**, not a proven failure of the Pipe.
- [LangGraph SQLite saver pinned-source bounded review](./RP03_LANGGRAPH_SQLITE_CHECKPOINTER_SOURCE_REVIEW_CANDIDATE_20261116.md), commit `cf933d6d194e342d22345405a88013f9f224b9a5`. The same tagged source presents `langgraph-checkpoint==4.3.1` and `langgraph-checkpoint-sqlite==3.1.3`, satisfying declared constraints for LangGraph 1.2.19. Upstream cautions against SQLite for high write-performance production workloads; single-operator R1 may still justify it **after** independent concurrency, restart, corruption and clean restore FAT. No mandatory PostgreSQL service adopted.
- The exact source packages and Open WebUI licensing notices must undergo package archive/redistribution due diligence. Python ABI/version closure, all transitive wheels, gateway image digest parity, actual SSE, Bifrost permissions, checkpoint locking/atomicity and installed-version source parity still **UNVERIFIED**.

## 4. New RP-04 falsification scope (NOT RUN)
- [Pinned-source cancellation and FAT falsification review](./RP04_PINNED_IF02_CANCEL_AND_FAT_FALSIFICATION_CANDIDATE_20261116.md), commit `8fae045b4e24af4275f8bd94a663481e12026dcf`. Preserved original **26/26** oracle IDs: 18 unconditional R1, 1 conditional R1 native tool-call case, 6 R2, 1 R3; all NOT RUN/NOT APPROVED.
- Developed **13** source/fixture-first negative, recovery and integrated FAT candidate cases. These are *draft fixture labels*, not new controlled original IDs. G1-dependent endpoint tests and actual first-article restore remain unauthorized/not run. Seven derived GAP-R1 witnesses remain candidates.

## 5. Concrete next owner-level UX decision — NOT YET APPROVED
For **operator-visible status and cancellation** on the owner-approved provisional IF-02 Pipe:
- **Alternative A (recommended for R1 first article):** one trusted Pipe, accept explicit deterministic user control commands (e.g. `/task status <task-id>`, `/task cancel <task-id>`) within delegated mode, pass them to independent supervisor HTTP status/cancel endpoints with authenticated operator identity and stable task ID. Supervisor owns durable acknowledgement/terminal status. WebUI Stop cancels view/generation only unless separate proven mapping exists. One Pipe, no second adapter or custom status dashboard.
- **Alternative B:** mandate dedicated graphical status/cancel affordance integrated with Open WebUI, requiring additional version-specific code/hook verification, packaging and UI acceptance. Independently justify complexity before implementation.
- Reject treating UI Stop as proof of supervisor cancellation without source and falsification tests.
- **This is only a narrowly scoped interaction-direction question; G-A field/schema selection, concrete exact-version stack and baseline remain unapproved.**

## 6. Continued restrictions and conversation assessment
- **G-R:** unapproved wording/applicability/criteria; **G-A:** unapproved concrete interface baseline.
- **G1 runtime/data collection:** OWNER HOLD; **26 original oracles / 13 fixtures / FAT:** NOT RUN.
- No production code changed; no installed service touched; no OpenAI/Anthropic billable API calls, no R2/R3 implementation, no source-public ZIP transfer, no PR merge.
- GitHub PR remains draft/unmerged. On pre-checkpoint exact head `cf933d6d194e342d22345405a88013f9f224b9a5`, GitHub returned **zero PR workflow runs**; this is **NO CI EVIDENCE**, not a CI PASS.
- After each substantial RP-02, RP-03 and RP-04 increment, no conversation-integrity failure was identified; new review records are recoverable from GitHub. Continuing in this conversation is technically safe. **Stop for the specific IF-02 UX owner decision** before freezing or implementing its operator-facing control path; the absence of original ZIP still prevents final G-R source-adjudication, but does not invalidate candidate source-design work.

**Next after UX decision:** refine minimum task submit/status/cancel/result wire schema, source/fixture-only review against exact pinned package candidates and selected durable saver; reconcile original source before actual G-R approval; seek G-A authority, separately release G1 hold only with owner approval; then conduct integrated installed FAT later.

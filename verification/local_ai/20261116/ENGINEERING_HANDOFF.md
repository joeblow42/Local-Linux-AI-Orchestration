# Local AI Development — Engineering Knowledge Transfer and Continuation

**Handoff:** Rev0.1, 2026-11-16. **Status:** working recovery record, not baseline approval.  
**Source artifact:** `LocalAI_Engineering_Knowledge_Transfer_Handoff_Rev0_1_20261116.odt` (SHA-256 `b5aa06df480aa172ccc532277cbf2d101ea64d145e942bff3acd1855d63ea57e`).  
**Authority:** owner-approved decisions and *AI-Assisted Software Engineering Development, Verification, Validation, and Governance Standard v1.0* (2026-11-04).  
**Important:** This Markdown is an accessible working transcription/reorganization of the ODT for recovery in GitHub; it is **not** a byte-identical replacement for the controlled ODT. The original ODT and recovery ZIP remain outside this public repository until separately transferred.

## 1. Reading order and authority

Read this lead first, then [verification and source recovery](./RECOVERED_EVIDENCE.md), the [source identity register](./RECOVERED_SOURCE_IDENTITIES.csv), and the [future-upgrades register](./POTENTIAL_UPGRADES.csv). Read original exact files before making source-sensitive decisions. The preceding 2026-11-15 checkpoint remains historical evidence; this lead supersedes it **for current status only**.

Distinguish **PROPOSED**, **APPROVED**, **IMPLEMENTED**, **TESTED**, **INDEPENDENTLY VERIFIED**, and **OWNER ACCEPTED**. Do not promote review recommendations to requirements, interfaces, oracle baselines, or gate decisions.

## 2. Approved product strategy

**Release 1 — Local AI.** Open WebUI provides the operator UI and owns user-facing conversation history. Direct chat follows `Open WebUI → Bifrost OSS → Ollama`. User-initiated delegated tasks follow `Open WebUI → independent LangGraph supervisor → Bifrost OSS → Ollama`. LangGraph Option A must support at least one useful multi-step local workflow with specialist roles, observable task status, durable checkpoints, cancellation, and recovery; tasks/checkpoints remain separate from chat history. Single-operator, local-only administration. Target Bodhi Linux 7 AMD64 (Ubuntu 22.04 package compatibility). Primary installation artifact is a Debian `.deb`, transported with complete required files/dependencies in ZIP or equivalent archive for personal/family use. Locally stored, access-controlled offline backup and independently verified restoration. **Encryption is indefinitely deferred** while permitting later optional encryption. No external API integration, external-provider mocks, real external calls, persistent autonomous scheduler, or enterprise infrastructure is required in R1.

**Release 2 — External AI.** Two independently usable external AI model integrations using OpenAI and Anthropic APIs, including owner-authorized paid calls, external context authorization, protected credentials and usage/spending controls. **No paid API call currently authorized.**

**Release 3 — Autonomous AI.** Persistent unattended operation, background agents, schedules, and autonomous tasks.

**Gateway:** Bifrost OSS is the **owner-approved LiteLLM substitution**. Historical repository text still referencing LiteLLM must not override this later owner decision.

**Runtime restriction:** G1 gateway data collection and runtime verification are on explicit **OWNER HOLD** until the release strategy and engineering issues are resolved. Do not modify deployed services.

**FAT endpoint:** Owner approved **Alternative B** on 2026-11-16: RP-14 retains readiness criteria **and** culminates in demonstrated operational first-article testing on the target, with recorded acceptance. FAT-entry authorization alone is insufficient.

## 3. Four accepted Release 2 extensibility criteria for Release 1

These are approved architectural directions; exact candidate requirements and interface wording are not automatically baselined.

- **AC-01 Gateway independence:** Both direct chat and supervised inference use the Bifrost gateway boundary. Avoid Ollama-specific calls scattered through core UI/supervisor integration.
- **AC-02 Model identity/selection:** Model routing can represent provider/model selection and retain selected/dispatched/resolved IDs without requiring redesign of history or supervisor architecture.
- **AC-03 Credential separation:** Define secret ownership boundaries that will isolate future external-provider credentials from local gateway/Ollama credentials and UI history.
- **AC-04 Policy insertion:** Provide defined architectural insertion points for future request-scoped consent, field projection, usage controls, and spending authorization, without redesigning history/checkpoint ownership.

**R1 evidence:** independent design and interface-impact review only. Do not build R2 adapters, mock external providers, or make hosted requests in R1. The criteria prevent *core architectural redesign*, not every future code change.

## 4. Engineering status and gate boundaries

- Candidate FAT Readiness Roadmap **Rev0.2**, Owner Decision Reconciliation **Rev0.7**, RP-02 adjudication, RP-03/RP-04 review, and 42-increment plan are **NOT APPROVED**.
- Preserve **14 RP identifiers**, **42 increment identifiers**, **136 original requirement IDs/statements/hashes**, **19 candidate interfaces**, **159 original allocation links**, and **26 candidate verification fixtures**.
- The provisional original-requirements allocation is **104 R1 / 17 R2 / 15 R3**. Derived requirements are additional and not yet approved.
- Phase I reviewed 136/136 statements; the latest engineering assessment distinguished **40 requirements with at least one reported quality FAIL** versus **96 QUESTIONED-only**. The reviewer recommending edits to all 136 does not prove all 136 have material defects. Evaluate every proposed correction source-first.
- **G-R blocked:** revised exact requirements, allocations, and acceptance criteria need independent adjudication and owner authorization.
- **G-A blocked:** 19 producer/consumer and interface contracts need independently supported semantics and owner authorization.
- **RP-04:** 26 source-linked oracle drafts are **NOT RUN** and not independently accepted. Mock evidence is not installed-system evidence.
- Execution optimization: consolidate overlapping work in RP-05/RP-07/RP-08/RP-12 safely, but retain individual package identities, unique verification goals and gates. Component tests do not replace integrated testing.
- Networking: necessary loopback/LAN services and authorized operator-initiated downloads are allowed. Unauthorized hosted inference and external application telemetry are disallowed in R1. No unapproved general air-gap/outbound-deny design.
- Personal/family packaging: one `.deb` and complete transport archive; no public release, public package index or enterprise license required. Check third-party redistribution rights before distributing included binaries/models.

## 5. Historical source recovery and limitations

Four previously missing source identities were recovered and **SHA-256 matched** on 2026-11-16:

1. Original Phase I results ZIP: `9f1b7cd2ea5ce838dd96e80caf5f0dc053a649cda1391896be027fa7874f0457`.
2. Phase I v3 input ZIP: `c39d43b81323fcf37f03136da407be9c6ce6d73dbfc28a2971c2803c53e788ae`.
3. Phase I v3 results ZIP: `14f4dc632c01c3baf16bfe33faaf79e532de6c17998953e01f68fe5260dcbfe9`.
4. Historical `LocalAI_Roadmap(2).odt`: `15df1165de6687bd452b52c3775954d1725ebe9c10e0abe0b0c50b13db4babf4`.

Phase II source-comparison ZIP was recovered (SHA-256 `17250360b8f1384d026bdcf09ab9f08a70cb1aa612f66d5123ac8502e2cc71bd`). ZIP CRC and outer manifest 54/54 PASS. **Exception:** nested Rev0.16 manifest lists `04_Rev0_16_Source_Identity_and_Authority.json` which is absent (7/8 other referenced Rev0.16 files match). Do not describe that nested source set as complete.

**What is not recovered or verified:** original conceptual `SRC-ROAD` Version 1.0 bytes (v3 used owner-authorized Rev1.2 descendant), raw G1 HTTP/SSE/reboot observations, current installed runtime state, or actual FAT execution. Historical Phase I judgments requiring two external providers in R1 or mandatory encrypted backup are **superseded by later owner decisions**; preserve the original review records without adopting obsolete interpretations.

Original transfer ZIP SHA-256: `9a48de5fa49420e470f003b7f3417277bd3aa2a6832a7b2c968d093004c2e37e`. It contains 14 entries, CRC PASS; 13 SHA-256 listed entries. **The original binary ZIP is NOT in this public GitHub repository**; see [recovery status](./RECOVERED_EVIDENCE.md).

## 6. Potential upgrades and additional functionality

A persistent idea backlog, **not** approved release requirements. No implementation, RP work or test obligation is created until an owner decision assigns scope.

**FUT-001 — Multi-computer, multi-Ollama local inference.** Owner-suggested exploratory option to host independent Ollama instances on several LAN-connected computers and potentially route selected requests via Bifrost/supervisor to those inference nodes. Potential benefits: use spare CPU/GPU compute, different model libraries, aggregate throughput and/or resilience. Future feasibility: Bifrost version and routing support, model identities, node discovery, permissions, encryption/confidentiality of LAN prompts, failure behavior, checkpoint ownership, health and load distribution. **Status: FUTURE OPTION; RELEASE UNASSIGNED; NOT DESIGNED/IMPLEMENTED/TESTED.** Do not enlarge the agreed single-host R1 scope because of this idea.

See the [potential upgrades register](./POTENTIAL_UPGRADES.csv).

## 7. Knowledge-transfer operating procedure

At the start of each new conversation:
1. Fetch GitHub branch/PR state and this lead. Confirm exact branch/head/commit, source authority, approved owner decisions, explicit supersessions and outstanding restrictions.
2. Read verification provenance and original source materials as needed. Do not assume text summaries replace exact 136-row or interface sources.
3. Maintain RP/increment statuses, artifact filenames/digests, original requirements/interfaces/oracles and trace IDs, tested-vs-paper evidence, open risks/defects, approvals and next action.
4. Update the lead at substantive owner decisions, source recovery, meaningful verification checkpoints or handoffs; preserve older source files without rewriting them.
5. Recheck conversation continuity at each substantial increment. Do not rely on chat memory as the only technical authority.

## 8. Next authorized work

- **RP-01:** reconcile recovered source identities and Rev0.16 missing-manifest item in the source authority ledger. Avoid duplicating completed integrity verification unnecessarily.
- **RP-02:** independently adjudicate all 136 original statements, 104/17/15 *candidate* release allocation, R1 task-status/cancellation/recovery gaps and discrepancies between reviewer and original author's verification criteria. Exact edits and G-R acceptance require appropriate authority.
- **RP-03:** reconcile all 19 interfaces against the two R1 paths, approved Bifrost substitution and the four R2-extensibility criteria. No G-A freeze without approval.
- **RP-04:** derive independently justified positive/negative/recovery oracles from approved requirements/interfaces. Keep NOT RUN until actually executed.

**Stop:** for material decisions, genuine evidence/verification conflicts, or continuity concerns. No billed API calls, service mutation, G1 runtime verification, silent scope change or baseline promotion.

## 9. Continuity snapshot

This handoff represents 2026-11-16 source and decision status; not a live runtime inspection. The owner confirmed that the stray standalone item “4.” in the last message was accidental; no fourth instruction exists.

## 10. Engineering continuation checkpoint — controlled source-first disposition (2026-11-16)

This section updates **current engineering status only**; it does not supersede original controlled source statements, earlier owner decisions, gate restrictions, or the historical 2026-11-16 handoff contents. The owner-provided exact original 3,451,941-byte recovery ZIP is available to the **current conversation**, but **not** published in this public GitHub repository. Source digests match. The isolated missing Rev0.16 authority JSON is now **CLOSED as a documented, nonblocking provenance exception**, with the original file still unrecovered; see [controlled exception disposition](./REV016_SOURCE_EXCEPTION_CLOSED_20261116.md).

**RP-02 progress:** all 136 original requirement IDs were assigned an individually documented bounded disposition, reviewed against original exact statements and the Phase I v3 / 2026-11-15 independent source reviews; all 40 reported quality failures were classified separately. **28 new exact-wording candidates** were drafted, with two focused quality corrections before checkpoint closure; 108 originals have no new proposed text. Proposed allocation remains **104 R1 / 17 R2 / 15 R3**. No requirement amendment, deletion, release allocation, retirement, acceptance criterion, or G-R approval is implied. Read [136-line disposition register](./RP02_136_INDEPENDENT_LINE_ITEM_DISPOSITIONS_CANDIDATE_20261116.csv) and [28 replacement wording proposals](./RP02_28_EXACT_WORDING_PROPOSALS_CANDIDATE_20261116.md). The full source-sensitive local CSV, including 136 exact original statement hashes, original text and 28 candidates, is retained in the current conversation's separately produced audit package, **not in public GitHub**.

**RP-03 progress:** Bifrost `transports/v2.4.0` tagged source docs at immutable commit `e869c3f9adc96ea53c38694a21bb04a8e1085487` were read. They support documented virtual-key headers/enforcement and OpenAI-compatible endpoint concepts, not exact deployed gateway behavior. Exact Open WebUI/LangGraph versions and IF-02 adapter behavior remain unverified. [Pinned-source/IF-02 candidate assessment](./RP03_PINNED_SOURCE_AND_IF02_ADAPTER_PREPARATION_CANDIDATE_20261116.md) compares a thin Pipe-to-independent-supervisor HTTP boundary versus an OpenAI-compatible supervisor endpoint, **without selecting or implementing either**.

**RP-04 progress:** [R1 operational FAT oracle candidate specification](./RP04_R1_OPERATIONAL_FIRST_ARTICLE_ORACLES_CANDIDATE_20261116.md) defines positive, negative and fault/recovery witnesses for all **19** provisionally R1 original oracle identities, including one native-tool-call conditional, and the seven **unapproved** derived R1 gap ideas. Original six R2 and one R3 oracle remain deferred. **ALL NOT RUN; NO FIRST ARTICLE TEST.** Neither a test mock nor paper-spec review is a substitute for operational owner FAT Alternative B.

**Unresolved before G-R/G-A:** independently challenge exact new wording and acceptance criteria; adjudicate duplicate/process-classified requirements and retirement recommendation with owner authority; decide exact supported Open WebUI/LangGraph versions and IF-02 route based on pinned evidence; verify Bifrost OCI code/config compatibility when owner permits; freeze wire schemas and failure semantics only after substantiation. No paid API requests or G1 runtime data collection until separate owner authorization.

**Next permissible technical increment:** offline requirements/trace QA, static producer-consumer/API contract refinement, review-ready G-R/G-A decision docket, and version/source reconciliation that does not inspect live G1. Keep this PR draft/unmerged; never silently promote these candidate records.

**Exception reporting:** The closed Rev0.16 original-source-loss record should not recur in routine blocker reports. Consult the controlled exception only when its missing historical authority assertions are relevant. The general G-R/G-A and G1 hold boundaries remain unchanged.

## 11. Latest continuation checkpoint — RP-02 quality and RP-03 interface control (2026-11-16)

**Current engineering status only; candidate not approved.** Subsequent to the [closed historical source exception](./REV016_SOURCE_EXCEPTION_CLOSED_20261116.md), engineering resumed using original exact 136 statements and 19 interfaces from the recovered ZIP. The **original 136 statement hashes, need links and source IDs all independently verified 136/136**.

- [RP-02 28-row independent second pass](./RP02_28_SECOND_PASS_QUALITY_DISPOSITIONS_CANDIDATE_20261116.md): of 28 previous candidate replacement texts, **21 sustained as candidates, five require refinement, two should retain original text**. The complete source-sensitive local review remains outside this public repo.
- [RP-02 other 12 reported FAILs](./RP02_12_QUALITY_FAIL_NONREWORD_DISPOSITIONS_CANDIDATE_20261116.md): controlled dispositions for duplicates, R2/R3 deferrals, evidence classification, licensed-edition detection and packaging rights. Together these cover all **40 reported quality FAILs**, not owner acceptance of all 136.
- [Targeted QUESTIONED-only challenges](./RP02_TARGETED_QUESTIONED_ONLY_SCOPE_CHALLENGES_20261116.md): **96 QUESTIONED-only does not imply PASS**. Resource monitoring/planning can likely be handled through FAT and installer/preflight, not additional runtime systems; `LAI-R1-N024-02` requires honest UNKNOWN counts when upstream omits token usage. Further 96-row review remains.
- [RP-03 minimum interface/task lifecycle](./RP03_R1_MINIMUM_INTERFACE_AND_TASK_LIFECYCLE_CANDIDATE_20261116.md): bounded IF-01/02/03/06 contract, task identity, durable status/cancel/restart invariants and 10 negative/recovery design challenges; the thin Open WebUI Pipe → independent local LangGraph service is a **provisional** design recommendation, **not** G-A selection or source-version certification.
- [Owner decision docket](./RP02_RP03_OWNER_DECISION_DOCKET_CANDIDATE_20261116.md): three specific owner choices concerning original release assignments, nonessential module obligations, and the provisional IF-02 entry. No choices have been approved by the act of drafting this docket.
- [Machine-readable second-pass checkpoint](./RP02_RP03_SECOND_PASS_VERIFICATION_CHECKPOINT_20261116.json) gives exact counts, identified source hashes, preserved statuses and next authority requirements.

**Approved product direction unchanged:** R1 local-only Open WebUI/Bifrost OSS/Ollama with independent LangGraph and .deb/offline closure/verified restoration; R2 operational authorized OpenAI/Anthropic; R3 autonomous; AC-01–04 design seams and FAT Alternative B. No R2 hosted mocks/adapters or R3 scheduler introduced in R1.

**Hard gates unchanged:** G-R and G-A are blocked pending genuine owner decisions and independently warranted acceptance/interface semantics. Exact Open WebUI/LangGraph runtime pins not established. G1 runtime verification still on OWNER HOLD. The 26 original oracles are NOT RUN. No deployed-service change, paid API call, baseline promotion, source rewrite or PR merge was performed.

**Next authorized task:** obtain owner disposition of the three bounded decisions, then complete residual 96 QUESTIONED-only screening, reconcile final exact 136-row wording/applicability/verification for G-R; conduct version-pinned interface/source review before G-A. Keep this candidate PR draft and unmerged.

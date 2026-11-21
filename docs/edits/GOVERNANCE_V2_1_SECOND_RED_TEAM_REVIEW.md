# Governance Standard and Roadmap Guide v2.1 second red-team review

**Disposition.** Ready for owner review. This is an implementing-agent red-team pass against the independent v2.0 review. Approval and independent confirmation of the v2.1 corrections remain separate decisions.

## Reviewed inputs

- The two v2.0 drafts and their [change register](GOVERNANCE_V2_0_CHANGE_REGISTER.md), preserved in local commit `97cb4d3`. Both match their recorded SHA-256 values.
- The [v1.1 red-team review](GOVERNANCE_V1_1_RED_TEAM_REVIEW.md).
- Owner-supplied `GOVERNANCE_V2_0_INDEPENDENT_REVIEW_R1.md`, SHA-256 `ad1bd489bd15abbae3571a8b36606e4f9c024454eeb0b3ebd7ee54775b035617`. The independent review found seven blockers and recommended local corrections while retaining the document structure.

## Blocker disposition

| Blocker | Finding | v2.1 correction and adversarial result |
| --- | --- | --- |
| B1 | RT-02 and newly exposed closure loss | Standard §15.2 restores applicable positive, negative, boundary, regression, interface and failure checks, privacy/security/safety evaluation and integration dependencies for behavioral claims. D.1/D.2 preserve the verified scope and open failures. A required FAIL, NOT_RUN or BLOCKED prevents COMPLETE in the claimed scope. An authority can approve a narrower deliverable through controlled change, with the original result retained. Guide §6.4 gives the same answer. Merely deferring a failed test leaves the original scope open. |
| B2 | RT-01 | Standard §5.2 and D.1 include a separate verification and validation vocabulary. Guide §3.3 and Template A use separate fields for authority, work state, case execution and result, scoped verification, validation and acceptance. Given an executed failed case, record FAIL and UNVERIFIED for the affected claim in both documents. |
| B3 | RT-06 | Standard §9.2 makes exception authority independent of implementation. §16.1 and D.5 reserve unconditional acceptance for full material-oracle review and allow only conditional acceptance on a bounded exception. §15.2 makes clear that the exception does not satisfy a still-applicable package criterion. Guide §5.4 and §7.1 use the approved plan’s material cases and apply extra challenge to high-consequence cases. |
| B4 | RT-08 | Standard §16.1 and Guide §10.3 both retain exceptions in the required-evidence denominator. Nine available out of ten is 9/10 with one exception. An approved scope change is a baseline change with a retained comparison. |
| B5 | RT-03 | Guide §4.1 now has an installation-first outcome form, §13 requests the selected entry path, and §9.2 qualifies recovery evidence by that path. A planner can authorize the witnessed installation as the first FAT step without reporting that the new target is already installed. |
| B6 | RT-05 and ORG-03 | Standard §14.2 accepts truthful partial evidence and pending approvals in a continuity handoff. Guide §12.3–12.4 and Template G carry the D.6 fields, including gate status, missing prerequisites, unexecuted cases, dependencies, privacy, artifact recovery and safe restart. A formal acceptance handoff invokes D.5 and §19. |
| B7 | RT-04 | Guide §13 now uses release authorized, published and deployed. An authorization by itself supports only the first label. |

RT-07 was resolved in the independent review. Its remaining editorial concern was addressed in Guide §13 by naming the precedence hierarchy and distinguishing reversible independent work from explicitly authorized irreversible steps.

## Six scenario re-walk

| Scenario | Result under both v2.1 drafts |
| --- | --- |
| Installation-first FAT | Record entry readiness for the identified package and dependency set, target prerequisites, install procedure and evidence plan. Prior integration evidence supports only its witnessed scope. Record the actual installation and operation as FAT results. Confirm entry authorization separately. |
| Preinstalled FAT | Verify the identified installed article against the approved readiness criteria before entry. Record its starting state and any reused dependencies or data. Earlier upgrade, restore or rehearsal evidence retains its original scope. |
| Failed required check | Record the executed case as FAIL and its scoped requirement claim as UNVERIFIED. Keep the original package open. Only a controlled approved change can close a narrower deliverable, with the original failed result remaining visible. |
| Design-only package | The designated authority can record COMPLETE for the approved design deliverable after scoped checks. Dependent implementation and operational verification remain pending. |
| Missing evidence with exception | Present 9/10, the missing item and the exception separately. If the exception concerns material oracle review, at most conditional acceptance is possible under the named independent authority. The exception does not satisfy a package exit criterion that still requires that evidence. |
| Continuity handoff while a gate is blocked | Record the named blocked gate, the missing prerequisites and the unexecuted or blocked cases. Verify recoverability and give the next safe operation. Transfer may proceed without a formal acceptance decision. |

The additional release-status challenge also agreed. An approved release with no published artifact or deployed target is release authorized only.

## Structural and editorial disposition

- **ORG-01 and ORG-02.** The proposed transfers remain explicitly deferred. Guide §6.3 points to Standard §16.2 and Appendix E. Guide §12.1 now points to Standard §14 and §18.3.
- **ORG-03.** Guide §15 maps Templates C/D to D.2 and D.3, Template F to readiness with D.5 for acceptance, and Template G to D.6. Template C records owner/reviewer, classification and rollback. Template D references case-level evidence. Template G carries the recoverability fields.
- **ORG-04.** Guide §11 names Standard §1.3, §12 distinguishes §14/D.6 continuity from D.5/§19 acceptance, and §9 retains both FAT paths and its Standard references.
- **E1–E7.** Matched clean-target terminology, used case outcome tokens consistently, repaired the §15.1 sentence, restored the bold labels, distinguished closure and acceptance authority, qualified recovery evidence by FAT path, and bounded reversible work and irreversible authorization.
- The second pass found and corrected two residual issues during drafting. An oracle exception could have been read as satisfying a still-required package criterion. It now has an explicit boundary. The expanded Template G split across pages and left a sparse spill page. Its heading and fields now render together and the following checklist flows on the same page as space permits.
- Both documents identify themselves as v2.1 drafts in their cover and footers and contain a revision note. The Guide refers to the project-adopted Standard and proposes the v2.1 pairing upon approval. The historical v1.0 source reference is retained as provenance.

## Verification and limits

Verified all seven blocker clauses against the final ODT content, re-walked the six scenarios, and checked the additional release-status case. Both ODTs parsed and rendered in LibreOffice, all original heading text was preserved, the v2.0 draft hashes were unchanged, and both rendered documents show the current draft footer on every page. The Standard rendered as 28 Letter pages and the Guide as 15 on this machine. Template G fits on one page. Word round-trip and independent v2.1 assessment were not performed.

| Review draft | SHA-256 |
| --- | --- |
| [Governance Standard v2.1 draft](../governance/AI_Assisted_Software_Engineering_Governance_Standard_v2_1_DRAFT.odt) | `fdc84873f2f0483a07699abf8a868e3b08ce1a3bea3da3425aa3bb9c4c952168` |
| [Roadmap Guide v2.1 draft](../governance/Software_Development_Roadmap_Planning_and_Execution_Guide_v2_1_DRAFT.odt) | `f6c41e13e84b54dfab18f9a7307ed49e71067074360bb530bdbb8552bb77eacd` |

# Governance v2.2 structural move review

The owner directed the structural moves from the approved v2.1 documents on `main`. The input commit is `1f5f7d688789db9eae3be750b2d51856dff455ed`. Version 2.1 remains the active governance pair while the v2.2 drafts are reviewed. This change applies ORG-01 and ORG-02 from the [red-team review](GOVERNANCE_V1_1_RED_TEAM_REVIEW.md). It preserves the dispositions of ORG-03 and ORG-04.

## Source-to-destination map

| Finding and source | Guide destination | Governing material kept in the Standard |
| --- | --- | --- |
| ORG-01, Standard §16.2 | §5.5 includes the small-increment, large-assignment and controlled-consolidation discussion and its qualitative caveat. | §16.2 still requires all eight failure classes to be evaluated, a recorded risk rationale for group size, and adjustment after observed failures. §7 remains the control for execution groups and verification boundaries. |
| ORG-01, Standard Appendix E | §5.5 contains the full eight-row comparison, its header, introduction and conclusion. The Guide adds a worksheet prompt for rationale, verification boundary and stop conditions. | Appendix E retains its original heading and bookmark and points to Guide §5.5. Appendix F now attributes the comparison at the Guide destination. |
| ORG-02, Standard §18.1 | §3.5 steps 1–2 cover charter assembly, early verification and validation roles, minimum artifacts and risk-scaled rigor. | §18.1 retains each charter field, approval boundary, minimum artifact obligation and timing of role identification. |
| ORG-02, Standard §18.2 | §3.5 steps 3–5 sequence needs and design-input baselines, traceability and glossary, architecture and interface approvals, review of test expectations, grouping, checkpoints, gates and durable state. | §18.2 keeps the before-first-implementation requirements and the existing narrow exploratory-prototype exception with its isolation and evidence limits. |
| ORG-02, Standard §18.3 | §12.5 contains the original practical continuation paragraph’s first sentence, including inventory, reconciliation, test-expectation review and corrective sequencing. | §18.3 retains the control to reconcile current authority and deployed state, review traceability and evidence, address material gaps, and preserve legitimate prior evidence. §14 and Appendix D.6 continue to govern handoffs. |

## Checks and counterexamples

- **Transfer completeness.** Compared all 36 table cells, including headers, across the v2.1 source and v2.2 destination. Verified that the comparison prose and existing-project walkthrough transferred into the Guide. Checked the entry checklist against every control in the original §18.1–18.2.
- **Change scope.** The approved v2.1 files retain their original hashes. No Standard heading or bookmark was removed. The three Guide subsections are additive, with no renumbering of other sections and no new dangling internal anchors. Changes outside the moved material are limited to publication status, cross-references and provenance. Appendix D and the Guide templates retain their responsibilities.
- **Grouping challenge.** A team proposing a large execution group still has to document evaluation of all eight risks and identify early independent verification boundaries. The relocated comparison informs the choice without superseding §§7 and 16.2.
- **First implementation challenge.** A team cannot use the practical checklist to bypass required baselines and approvals. An exploratory prototype is allowed only under the existing controlled exception, and its result cannot be claimed as verified fulfillment.
- **Recovery challenge.** If a resumed checkout or deployed state disagrees with the handoff, the Guide directs reconciliation before mutation. The Standard still requires trustworthy historical evidence to be retained and overclaims reclassified. A blocked gate can transfer in a continuity handoff without being marked accepted.
- **Acceptance regression check.** Verified unchanged text in Standard §§9.2, 15.1–15.2, 18.4 and 19 and D.1, D.5–D.6. Guide §§9.1–9.2 and Template G are unchanged, so both FAT entry paths and the handoff field set remain intact.
- **Rendering.** LibreOffice rendered the Standard as 27 Letter pages and the Guide as 17. Checked draft labels, visual readability of the complete comparison on Guide page 7, and pagination of the Standard’s Appendix E note and Appendix F. This editing and review pass is not independent. Microsoft Word round-trip formatting was not exercised.

## Exact review files

| Draft | SHA-256 |
| --- | --- |
| [Governance Standard v2.2 draft](https://github.com/joeblow42/Local-Linux-AI-Orchestration/blob/4d3307bbfb5566f1c14f6fef40f487597459ccf8/docs/governance/AI_Assisted_Software_Engineering_Governance_Standard_v2_2_DRAFT.odt) | `667b97a6d801046dfd77a2b4d6e56dfdddb04e4687285bdf3864d7316f2c5a3c` |
| [Roadmap Guide v2.2 draft](https://github.com/joeblow42/Local-Linux-AI-Orchestration/blob/4d3307bbfb5566f1c14f6fef40f487597459ccf8/docs/governance/Software_Development_Roadmap_Planning_and_Execution_Guide_v2_2_DRAFT.odt) | `a4649d392dbc7b7282640c1180a2d494e7dc3876bf603f93d751a52d747aa121` |

## Independent-review correction

The v2.2 check above verified raw bookmark starts and internal link targets. The subsequent independent save-and-reopen test exposed six unpaired bookmark ranges that LibreOffice discarded. The statement about bookmark preservation applies only to the raw start names. The [v2.3 correction record](GOVERNANCE_V2_3_REVIEW_CORRECTIONS.md) documents the range repair and the successful save-and-reopen check. It also records the privacy and prototype wording fixes.

# Governance and Roadmap Guide v2.0 change register

The two documents serve separate purposes. The Standard defines governing controls and the Guide explains how to apply them when planning and executing a project. This register tracks [all eight findings](GOVERNANCE_V1_1_RED_TEAM_REVIEW.md) across both drafts. A verified draft correction is eligible for owner review. Approval of either v2.0 document remains pending.

## Frozen inputs

| Artifact | SHA-256 |
| --- | --- |
| `AI_Assisted_Software_Engineering_Governance_Standard_v1_1_DRAFT.odt` | `c4e426c646b87867409d51395eea0ce2fd88027ff2ed029a8b3914fd8885fc6f` |
| `Software_Development_Roadmap_Planning_and_Execution_Guide_v1_1_DRAFT.odt` | `4c7dc1c5c2f630199c4c658d76deb8bba8fdac8531939cf5ba99cec00c3cea4d` |

## Findings and proposed dispositions

| ID | Affected clauses | Draft disposition and verification scenario | Status |
| --- | --- | --- | --- |
| RT-01 | Standard §8.3, §15, D.1. Guide §2.1, §7.1, §8.4, §9.3, Template D | Track execution, verification, validation and acceptance separately. A failed test is executed with outcome FAIL. Its requirement remains unverified. | Open |
| RT-02 | Standard §8.3, §15.2, §16.1, D.1–D.2. Guide §6.4, §7.1, Templates C and D | Scope package completion to the approved deliverable and applicable controls in §15.2. Close a design-only package without implying verified operation. | Open |
| RT-03 | Guide §2.1, §4.4, §5.1, §9.1–9.2, Template F | Distinguish readiness for an installation-first FAT from readiness of a preinstalled article. Record installation and operation during the applicable FAT. | Open |
| RT-04 | Standard §12.3 and D.1. Guide §2.1, §9.3 | Track repository integration, release authorization, publication, deployment and sustainment separately. An authorized release can remain unpublished and undeployed. | Open |
| RT-05 | Standard §14.2, §19, D.5–D.6. Guide §7.3, §12 | Distinguish continuity handoff from acceptance handoff. An incomplete project can transfer with missing evidence and blocked gates clearly recorded. | Open |
| RT-06 | Standard §9.2, §15.2, §16.1, §18.4. Guide §2, §6.2, §7.1, §8.3 | Define material test expectations and scope of review in the approved plan. Record authority and risk of exceptions. Routine smoke evidence cannot stand in for independent acceptance evidence. | Open |
| RT-07 | Standard §1.1 and §1.3. Guide §1.3, §3.4, §11 and §13 | Apply the hierarchy and distinguish authority from access. A blocked host mutation does not stop authorized independent work. | Open |
| RT-08 | Standard §16.1. Guide §10.3 and Template E | Use the approved required-evidence inventory as denominator. Nine available items out of ten remain 9/10 even when the tenth has an authorized exception. | Open |

## Structural decisions

| ID | Proposed transfer | Draft disposition |
| --- | --- | --- |
| ORG-01 | Detailed grouping comparison from Standard §16.2 and Appendix E to Guide §5–6 | Retain in place for this revision and add a Guide cross-reference. Consider moving it after owner review. |
| ORG-02 | Practical initiation and recovery walkthroughs from Standard §18.1–18.3 to Guide §3 and §12 | Retain in place and cross-reference the workflow. This preserves the Standard's standalone applicability. |
| ORG-03 | Standard Appendix D and Guide fillable templates | Keep the normative minimum records in the Standard and explicitly map the Guide templates to them. |
| ORG-04 | Repeated authority, handoff and FAT material | Keep the controlling clauses in the Standard and the practical steps in the Guide. Use cross-references for interpretation. |

The proposed Guide v2.0 is intended to accompany Standard v2.0 if both are approved. Until then, an adopting project continues to use its approved baseline.

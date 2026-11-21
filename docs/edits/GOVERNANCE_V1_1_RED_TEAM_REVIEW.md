# Governance Standard and Roadmap Guide v1.1 red-team review

**Keep the documents separate.** The Governance Standard defines what a project must control, who can decide, and what evidence supports a claim. The Roadmap Guide turns those controls into a sequence of work. Combining them would make practical defaults such as increment size, review cadence, and FAT sequencing harder to distinguish from mandatory controls.

The most important red-team finding is **status language**. An agent following the Guide’s summary states could report an executed test as verified, a completed FAT as accepted, or an authorized release as deployed. The detailed sections generally distinguish those outcomes. The short definitions and templates need to make that distinction consistently, because they are the parts most likely to be copied into a roadmap or agent prompt.

I reviewed the two local v1.1 drafts. The Guide still names **Governance Standard v1.0** as its governing reference. I treated Standard v1.1 as a candidate for compatibility review, with no change to which version governs the project. [Standard v1.1 draft](../governance/AI_Assisted_Software_Engineering_Governance_Standard_v1_1_DRAFT.odt) · Guide v1.1 draft reviewed from the local working copy at `docs/governance/Software_Development_Roadmap_Planning_and_Execution_Guide_v1_1_DRAFT.odt`.

## Red-team findings

| Priority | Sections | Finding and proposed correction |
|---|---|---|
| **High** | Guide **§2.1, §8.4, §9.3** and Standard **§8.3, §15, D.1** | The Guide labels an item **Verified** once checks have been executed, while allowing failures in that definition. It also combines **FAT executed/accepted** and **released/sustained**, although §9.3 separates these decisions. Use separate fields for execution outcome, verification status, owner acceptance, release authorization, deployment, and sustainment. A failed test can be executed and recorded without the requirement being verified. |
| **High** | Standard **§8.3, §15.2, §16.1, D.1** and Guide **§6.4, §7.1** | Standard §8.3 points **COMPLETE** to §16, which defines metrics. §15.2 contains package completion criteria, and D.1 does not define `COMPLETE` as a work state. Meanwhile, the Guide allows a design-only package to close when its design deliverable is met. Point §8.3 to §15.2 and define scoped package closure. Record the deliverable and evidence level so a design package can close without implying implementation or system verification. |
| **High** | Guide **§2.1, §4.4, §5.1, §9.1–9.2, Template F** | The new installation-first FAT path is clear in §9.1. Elsewhere, the ordered states put target integration qualification before FAT readiness, and §5.1 warns against a non-operational final article. An agent could read those as requiring the clean-host install before the witnessed install begins. Make both paths explicit throughout. For installation-first FAT, readiness means the approved article, media, target prerequisites, procedure, and evidence plan are ready. Successful installation and operation are test results. Prior integrated evidence can support entry within its demonstrated scope. |
| **Medium** | Standard **§12.3** and Guide **§2.1, §9.3** | The Standard says **Released** records an authorized release decision. The Guide’s combined **released/sustained** state also requires deployment, support, and maintenance to be in place. Use distinct labels such as **release authorized**, **release published**, **deployed**, and **sustained** where applicable. Keep **merged** as a repository event. |
| **Medium** | Standard **§14.2, §19, D.5–D.6** and Guide **§7.3, §12** | The Standard calls for a reproducible audit at each release **or handoff gate**, and the audit list includes executed tests and acceptance. The Guide permits an ordinary handoff while work is blocked or incomplete. Clarify the audit scope. A continuity handoff must faithfully expose unfinished work and verify recoverability. A formal release or acceptance handoff must also meet its designated gate criteria. |
| **Medium** | Standard **§9.2, §15.2, §16.1, §18.4** and Guide **§2, §7.1, §8.3** | The Standard requires independent review of material test expectations. The Guide sometimes says independence is needed *where required*, without identifying who determines applicability. Point to the Standard and the approved test plan. Define what makes an oracle material and who can approve an exception. Keep routine engineering checks available without giving them the weight of independent acceptance evidence. |
| **Medium** | Standard **§1.1, §1.3** and Guide **§1.3, §3.4, §11, §13** | The new access language is consistent in the main sections. The Guide’s reusable agent directive still says to continue permitted *read-only or isolated* work when a decision is pending, while §3.4 and the Standard allow any independent authorized work. Align the portable directive with the main text. Also make the Guide’s authority clause refer to the Standard’s precedence order, so a copied prompt cannot imply that project approval overrides binding controls. |
| **Low** | Standard **§16.1** and Guide **§10.3** | The Standard’s evidence-integrity calculation uses **required evidence links** as its denominator, but its acceptance wording refers to **committed acceptance evidence**. That wording could omit required evidence that was never committed. Use the approved required-evidence inventory as the denominator and show unavailable items and authorized exceptions explicitly. |

## What each section is for

The table maps the top-level sections. Rows share numbers for compactness. The two documents use independent numbering.

| Section | Governance Standard | Roadmap Guide |
|---|---|---|
| Front matter | Governing doctrine, mandatory language, applicability, and tailoring limits. | Document status, operating rule, and how to use the companion. |
| **1** | Authority hierarchy, roles, delegated autonomy, and stop rules. | Purpose, applicable projects, precedence, and exclusions. |
| **2** | Lifecycle transformations, verification versus validation, and required lifecycle outputs. | Roadmap vocabulary and engineering outcome states. |
| **3** | Elicitation, review, and validation of stakeholder needs. | Entry assessment, evidence ledger, unknowns, and blockers. |
| **4** | Controlled requirements and INCOSE-aligned quality. | Definition of the operational endpoint, scope, and FAT boundary. |
| **5** | Baseline control, traceability, and change authority. | Dependency sequencing, work grouping, and roadmap controls. |
| **6** | Architecture, interfaces, state semantics, and data responsibilities. | Work-package and increment fields, granularity, and exit evidence. |
| **7** | Controlled consolidation and required verification checkpoints. | Increment execution, alignment reviews, and when to hand off. |
| **8** | Agent entry, implementation, reporting, and AI-specific failure controls. | Evidence levels, integration paths, retest decisions, and fault witnesses. |
| **9** | Verification and validation, oracle independence, test layers, and evidence sufficiency. | FAT entry criteria, readiness assessment, and post-entry outcomes. |
| **10** | Adversarial review, semantic error analysis, and assurance claims. | Progress reporting, replanning, measurement, and estimation. |
| **11** | Security, privacy, privilege, cost, and supply-chain controls. | Escalation criteria, decision packets, and limits of approvals. |
| **12** | Configuration, CI, commit review, merge, and release discipline. | Durable state, handoff triggers, packet contents, and receiver checks. |
| **13** | Risks, unknowns, defects, and corrective action. | Reusable agent instructions and expected planning outputs. |
| **14** | Persistent records and cross-agent continuity. | Historical LBT and Local AI examples and their applicability limits. |
| **15** | Gate decisions, evidence, and package completion criteria. | Copyable planning, execution, FAT, and handoff templates. |
| **16** | Conformance measures and risk factors for work grouping. | Roadmap quality checklist before approval or starting the next package. |
| **17** | Operational sustainment, deployment, recovery, change, and retirement. | — |
| **18** | Applying the Standard to new and existing projects, including tailoring. | — |
| **19** | Mandatory conformance audit and gate disposition. | — |
| **Appendices and references** | **A–C** provide INCOSE crosswalks. **D** defines minimum records and checks. **E** compares execution approaches. **F** preserves provenance and attribution. | Reference and provenance identify the governing Standard and the source of the worked examples. |

## What I’d move or cross-reference

- **Move the detailed grouping comparison** from Standard **§16.2 and Appendix E** to Guide **§5–6**, where someone choosing package size can use it. Retain the Standard’s requirement to justify grouping and verification boundaries by risk.
- **Move the practical initiation and recovery walkthroughs** from Standard **§18.1–18.3** to Guide **§3 and §12**. Keep the mandatory entry controls and tailoring limits in the Standard, particularly **§18.4**.
- **Keep the minimum records and gate rules** in Standard **Appendix D and §15–19**. Keep the Guide’s templates in **§15** and map their fields to the Standard. That lets the templates improve without quietly changing a mandatory record or gate.
- **Keep short cross-references at the overlap points.** Guide **§11** can show how to prepare an owner decision using Standard **§1.3**. Guide **§12** can show how to execute a handoff using Standard **§14 and D.6**. Guide **§9** should retain the two FAT entry paths and refer to Standard **§15 and §19** for independent review and acceptance.

I’d fix the **status definitions, package completion reference, and installation-first FAT wording** before approving either draft. Those are the points most likely to change what an agent reports or when it asks the owner to proceed. No documents were edited during this review.

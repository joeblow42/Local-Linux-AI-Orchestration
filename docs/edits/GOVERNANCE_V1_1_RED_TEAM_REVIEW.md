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

## Controlled update plan

Use **one change register for both documents**. Give every red-team finding a stable ID, then edit both drafts in small batches. The committed review stays as the source record. The register tracks what we decided, what changed, and how we checked it.

### Start with eight tracked findings

| ID | Finding | Where to make the correction |
|---|---|---|
| RT-01 | Execution, verification, and acceptance states are blurred | Define the states in the Standard. Align the Guide’s glossary, sequence, and templates. |
| RT-02 | `COMPLETE` points to the wrong section and lacks a scoped definition | Fix the Standard’s cross-reference and record vocabulary. Align the Guide’s design-only package example. |
| RT-03 | Installation-first FAT is clear in §9.1 and ambiguous elsewhere | Align the Guide’s outcome states, readiness sequence, and FAT template. Check both installation-first and preinstalled FAT paths. |
| RT-04 | Release authorization, publication, deployment, and sustainment are conflated | Define the distinctions in the Standard and apply them in the Guide. |
| RT-05 | An ordinary handoff could be read as requiring acceptance-gate evidence | Clarify the Standard’s audit scope. Keep the Guide’s continuity checklist usable for blocked or incomplete work. |
| RT-06 | The Guide leaves material oracle review applicability unclear | Put the rule and exception authority in the Standard. Point to it from the Guide. |
| RT-07 | The reusable agent directive is narrower than the main instructions | Align the Guide’s directive with the authority hierarchy and permission to continue independent authorized work. |
| RT-08 | The evidence denominator could omit required evidence that was never committed | Correct the Standard’s metric and align the Guide’s reporting template. |

Each register entry should include the **source finding, affected clauses, approved disposition, exact revisions changed, verification example, and status**. If one issue affects multiple clauses, track those as subtasks under the same ID. Keep the proposed transfers of material between documents as **separate decisions**. A finding can be fixed even if we decide to retain the current section structure.

### Edit and verify in three batches

1. **Status and completion — RT-01, RT-02, RT-04.** Settle the vocabulary first. Check examples where a test ran and failed, a design-only package closed, and a release was authorized but deployment was still pending.
2. **FAT and evidence — RT-03, RT-06, RT-08.** Walk both FAT entry paths. Check that prior G1 evidence can support readiness within its scope, that clean-host installation remains a result to witness, and that missing evidence remains visible in the denominator.
3. **Authority and handoff — RT-05, RT-07.** Walk an interrupted project with a blocked gate and a newer published branch. Verify that an agent can hand off incomplete work and continue independent authorized work without treating either action as acceptance.

Before editing, record the **exact draft files and checksums**. The Standard v1.1 draft is already versioned. The Guide v1.1 draft and its index change are still uncommitted, so the first action would be to preserve that draft as a separate baseline commit. Then commit each reviewed batch with its finding IDs and update the register in the same commit.

A finding closes when its affected clauses and templates agree and the example produces the same decision under either document. At the end, reconcile **all eight IDs** against the original review. Anything deferred stays visible with its reason. The revised drafts can then go to you for approval as a pair.

## Path to the two v2.0 documents

The goal is **two separate v2.0 documents**: one Governance Standard and one Roadmap Planning and Execution Guide. A single change register will keep the edits coordinated.

| Step | Action | What shows it’s done |
|---|---|---|
| **1. Freeze the inputs** | Record the exact v1.1 ODT filenames and checksums. Commit the pending Roadmap Guide v1.1 draft and index as a baseline. Preserve the red-team review and its update plan. | Both starting drafts and the full review can be recovered from Git. |
| **2. Open one change register** | Create entries **RT-01 through RT-08**. For each, list every affected clause, glossary entry, template, and example in both documents. Give each proposed move between documents its own decision entry. | Every finding has an ID, scope, proposed correction, and verification example. |
| **3. Create two v2.0 drafts** | Copy each frozen v1.1 ODT into a separate v2.0 draft. Label both as drafts and retain the original files. | There are exactly two editable v2.0 candidates with clear provenance. |
| **4. Fix status and completion** | Resolve **RT-01, RT-02, and RT-04**. Define the states and scoped package completion in the Standard first, then align the Guide’s glossary, sequences, and templates. | Both drafts give the same answer for a failed test, a completed design-only package, and an authorized release with deployment pending. |
| **5. Fix FAT and evidence rules** | Resolve **RT-03, RT-06, and RT-08**. Align the two FAT entry paths, independent review of material test expectations, and the denominator for required evidence. | Both drafts agree on installation-first and preinstalled FAT. A required piece of evidence stays visible even when it is missing. |
| **6. Fix authority and handoff rules** | Resolve **RT-05 and RT-07**. Clarify ordinary continuity handoffs, formal acceptance handoffs, and what authorized work can continue when another step is blocked. | Both drafts let an agent hand off incomplete work without claiming acceptance or losing the blocker. |
| **7. Decide what material to move** | Review the proposed transfers separately from the eight fixes. Decide whether to move detailed grouping comparisons and practical walkthroughs into the Guide or keep them in place with cross-references. | Every proposed move has a recorded disposition. Mandatory controls remain easy to find in the Standard. |
| **8. Verify the drafts together** | Re-run the red-team scenarios across both full documents. Check the glossary, numbered clauses, templates, agent directive, and cross-references. Open and render both ODTs. | All eight findings have evidence of closure or an explicit deferral. Both files open and render correctly. |
| **9. Present the pair for approval** | Provide both drafts, the change register, and a short summary of any deferred decisions. Decide which Standard version the Guide will cite when approved. | The approval identifies the exact versions of both documents and any conditions. |
| **10. Publish the approved v2.0 pair** | Commit and publish both final ODTs, the governance index, and the completed change register. Update the project handoff to point to the approved versions. | GitHub has a versioned release record, local and remote are in sync, and the previous versions remain available. |

**Working rule:** At the end of each editing batch, verify the associated scenarios before marking the findings closed. Commit the document changes and register update together so a future session can see exactly what changed and why.

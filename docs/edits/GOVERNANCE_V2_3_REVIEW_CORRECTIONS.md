# Governance v2.3 independent-review corrections

The two v2.3 drafts form a matched pair. The approved v2.1 pair remains active. The v2.2 drafts are retained byte for byte as the inputs assessed in `GOVERNANCE_V2_2_INDEPENDENT_REVIEW_R1.md`. The independent reviewer’s baseline hashes matched the approved files in `main` at `1f5f7d6`.

| Finding | Correction and verification |
| --- | --- |
| Blocker 1 — privacy dropped in Standard §18.3 | Restored privacy and the unqualified design and requirements ambiguity check. Guide §12.5 now uses the same security, privacy, privilege and operations list. A reader resuming a stale handoff should check those gaps before changing the project. |
| Blocker 2 — prototype exception in Guide §3.5 | The Guide now permits an exploratory prototype before steps 3–4, requires the exploratory label and production isolation from the start, and states that its use in planning cannot establish verified fulfillment. Standard §18.2's controlling exception is unchanged. |
| Blocker 3 — six missing bookmark ends | Restored the ranges for Standard §16, §16.2, §§18.1–18.3 and Appendix E. Checked the paired markers in the editable draft and confirmed all six survived an actual LibreOffice ODT save and reopen. |
| Related consistency and editorial changes | Guide §3.5 applies the Standard’s minimum artifact set. §5.5 requires evaluation of all eight risks and points to the execution-group definition. Template C records group identity, scope, rationale, verification boundary and stop conditions. The Standard restores initiation terminology and the v2.1 revision note. The Guide credits Source 1 for the comparison. Companion references and draft labels use v2.3. |

The grouping scenario still requires all eight failure modes to be evaluated, with targeted evidence for material risks. The new-project scenario permits only a labelled and isolated early prototype. The continuation scenario checks privacy and ambiguities and preserves the existing blocked-gate handoff. Verified that the 36 comparison cells, the Standard’s independent-oracle and scoped closure clauses, both Guide FAT entry paths, and the recoverability template remain intact.

Both files opened, saved and reopened in LibreOffice and rendered with v2.3 draft footers. The Standard rendered as 27 Letter pages and the Guide as 17 on this machine. The 25 unresolved contents links in the Standard predate the v2.2 moves and are unchanged. Word round-trip verification and independent review of these new revisions remain open.

| Review draft | SHA-256 |
| --- | --- |
| [Governance Standard v2.3 draft](../governance/AI_Assisted_Software_Engineering_Governance_Standard_v2_3_DRAFT.odt) | `68ca72a5a28e17c01532fad5c04a13e4aa3cd8d00380f793e1303cfea1fa17cb` |
| [Roadmap Guide v2.3 draft](../governance/Software_Development_Roadmap_Planning_and_Execution_Guide_v2_3_DRAFT.odt) | `00108730bc601da3b67a81f831562a597d07ea8597adc1c5aa7fb4d559dff751` |

# Source recovery evidence and repository storage state — 2026-11-16

**Scope:** archival integrity and provenance only; no application/runtime verification.

## Published in this GitHub branch

- [Engineering handoff](./ENGINEERING_HANDOFF.md) — readable knowledge transfer based on the original 2026-11-16 ODT.
- [Recovered source identities](./RECOVERED_SOURCE_IDENTITIES.csv) — source roles, exact filenames, recorded SHA-256, sizes, and integrity dispositions.
- [Machine-readable evidence](./SOURCE_INTEGRITY_RECORD.json) — archive CRC, nested-manifest checks, and limitations.
- [Potential upgrades](./POTENTIAL_UPGRADES.csv) — FUT-001, multi-host Ollama concept, unapproved.
- [Original package manifest](./ORIGINAL_PACKAGE_SHA256SUMS.txt) — **hashes of source artifacts not stored in this Git branch**. This is not proof that those files were published.

## Complete binary recovery package — **NOT uploaded to GitHub**

Original name: `LocalAI_Engineering_Knowledge_Transfer_Recovery_20261116.zip`  
Original size: **3,451,941 bytes**  
SHA-256: `9a48de5fa49420e470f003b7f3417277bd3aa2a6832a7b2c968d093004c2e37e`  
Archive check: **ZIP CRC PASS**, 14 entries, 13 entries listed by `SHA256SUMS.txt` (13 of 13 matched during previous package generation).

The binary package includes the original lead ODT, source integrity records, preserved 2026-11-15 checkpoint, 2026-11-14 review inputs/results, Phase II source comparison, and **candidate unapproved** RP-02/RP-03/RP-04 and roadmap packages.

**Important publication limitation:** `joeblow42/Local-Linux-AI-Orchestration` is a **public repository**. The local ZIP nests historical source material, owner messages and system observations. Full original binary archives were **not** published here: these materials should be separately reviewed for disclosure/credential risk and transferred through a binary-capable authorized channel. The GitHub connector currently supports text-file commits but not direct local binary file transfer. A review branch in a public repository is **not private**. Do not mistake the GitHub source-index files for the full original recovery package.

To complete full-source GitHub continuity after disclosure review, choose either a **private** versioned source repository or an explicitly approved public bundle, upload the exact binary bytes, and independently verify SHA-256 against the values above. Record the upload path and artifact hash in this index. Do not overwrite the historical files to fit a changed decision.

## Verified recovery

- Four historical source identity gaps closed: original Phase I results, v3 review input, v3 review results, and the named original roadmap file matched expected recorded digests.
- Phase II comparison ZIP: CRC PASS; outer manifest **54/54** matched; embedded Rev0.16 manifest **7/8** matched, missing `04_Rev0_16_Source_Identity_and_Authority.json`. Other named nested manifests matched.
- This supports **file identity and integrity** only; it does not establish historical conceptual roadmap v1.0 bytes, current running G1 evidence or installed Release 1 operation.
- Historical reviews recommending R1 hosted providers and encryption predate owner decisions superseding those assumptions. Do not change the historical evidence itself.

## Gate and work-state protection

G1 verification remains **OWNER HOLD**. No external API calls, service changes, or baselining of requirements/interfaces/oracles. Candidate 104/17/15 requirement allocation and 19 interfaces remain unapproved. Preserve original RP and increment IDs.

## Next technical continuation

Verify this branch, documents, file provenance and exact current approval state; conduct bounded RP-01 recovery reconciliation, then continue RP-02 source-first adjudication. For exact original requirement/interface/oracle source claims, obtain the original binary source package from an authorized location or request the upload; **do not invent missing exact source text from this summary**.

# RP-02 — second-pass disposition of 12 reported quality FAILs without new wording

**Date:** 2026-11-16. **Status:** independent candidate source-first review, **not G-R approved**. The complete 136 original statements/hash identities were checked against the original controlled Phase I v3 input. The initial 40 reported FAILs comprise **28 previously proposed rewrites** (second pass separately assessed) and these **12 unchanged records**. A reported FAIL is a quality-review signal, not an instruction to rewrite regardless of derivation.

| Historical requirement | Proposed non-reword disposition | Why not add a separate subsystem / what must be independently verified |
| --- | --- | --- |
| `LAI-R1-N002-05` | **RETAIN / SHARED OWNERSHIP WITNESS** | Overlaps N017-01; one authoritative Open WebUI chat-history store satisfies both. Preserve both source IDs or seek controlled consolidation; do not create a second store |
| `LAI-R1-N009-01` | **DEFER TO R2** | External field projection and per-request provider/model authorization belong to R2, not R1. Proposed allocation change does not approve an external context controller in R1 |
| `LAI-R1-N010-04` | **RETAIN / ADAPT BACKUP CRITERIA** | Classify sensitive backup members for access control, confidentiality limits and restoration; owner has indefinitely deferred mandatory backup encryption. No encryption implementation required |
| `LAI-R1-N011-06` | **RETAIN / SHARED TOOL-GRANT WITNESS** | Shares the active task capability gate with N018-01; one tool-admission implementation and test can cover both distinct trace IDs |
| `LAI-R1-N013-05` | **DEFER TO R2 / CLARIFY CONCURRENCY** | Paid call concurrency/budget controls are not implemented in R1; R2 must distinguish simultaneous-call ceiling from authorization/spend limit. No paid calls currently approved |
| `LAI-R1-N015-04` | **RETAIN / DEFINE READINESS CRITERION** | Gate model requests on real local inference readiness. Observe/configure the actual Ollama-supported health signal or wrapper; do not modify third-party Ollama merely to expose a new proprietary readiness API |
| `LAI-R1-N017-01` | **RETAIN / SHARED OWNERSHIP WITNESS** | One Open WebUI conversation-history owner; LangGraph owns only tasks/checkpoints. N002-05 is a related data-contract expression, not a second implementation |
| `LAI-R1-N018-01` | **RETAIN / SHARED TOOL-GRANT WITNESS** | One active task-specific tool authorization gate can verify N011-06 and N018-01; no enterprise policy broker required |
| `LAI-R1-N021-03` | **HOLD FOR CONTROLLED SPLIT OR TRACE TREATMENT** | Original combines interface declaration and legal asset redistribution permission. Candidate split: keep package interface/version declaration as product/deployment artifact; verify actual inclusion permissions and notices in package-release compliance gate. Preserve original ID and source; any replacement/new normative ID requires owner G-R approval |
| `LAI-R1-N022-05` | **OWNER DECISION: RETIRE CANDIDATE** | Detection of optional licensed editions is not needed for the approved OSS-only local R1. Licensing due diligence for redistributed binaries/models still applies; do not create a runtime edition detector |
| `LAI-R1-N023-05` | **OWNER DECISION: RECLASSIFY TO FAT VERIFICATION PLAN** | Acceptance thresholds must be defined for actual operational FAT and kept traceable, but a test-specification obligation is not a separate application runtime subsystem. Missing numeric thresholds remain unapproved, not invented |
| `LAI-R2-N027-04` | **DEFER TO R3** | External agent capability-grant isolation belongs with the autonomous/external-agent adapter; internal LangGraph R1 specialist roles do not require an agent registry |

## Combined 40-FAIL quality accounting

- **28 original FAILs** have former replacement candidates, subjected to independent second pass: **21 sustain candidate**, **5 refine**, **2 return to original**.
- **12 original FAILs** have these bounded no-reword quality dispositions (six retain with shared/clarified witnesses, three deferred by release, three classification/retirement matters). This is **40/40 independently dispositioned**, not **40/40 owner-approved**.
- **96 QUESTIONED-only** original items remain subject to individual applicability/acceptance review; a question does not establish a defect or authorize a new requirement.
- **136/136 source identities, parents and original hashes** remain verified. Historical source records and original requirement IDs remain unchanged.

## Decisions that need explicit owner authority before product G-R closure

1. Accept the controlled release distribution (**104 R1 / 17 R2 / 15 R3**, candidate), retaining historical original ID prefixes.
2. Authorize the pending requirement-text change set only after the **26 viable** rewrites and their exact verification criteria are reconciled. Do not treat this as a request to approve all 136 by simple count.
3. Decide disposition of `N022-05` optional licensed-edition detection (**retire recommended**); `N023-05` FAT-threshold specification (**classify as test-plan obligation recommended**); `N021-03` package interface declaration versus licensing gate (**split responsibility recommended**).
4. Resolve unbounded R1 state transition and retention semantics as interface/verification criteria (not new service inventions) before G-R/G-A freeze.

**No changes to production code, owner-approved standards, original evidence, installed G1 configuration or held runtime tests.**

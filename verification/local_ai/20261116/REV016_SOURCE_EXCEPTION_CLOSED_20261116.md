# Rev0.16 original source-identity JSON — closed provenance exception

**Disposition ID:** `LAI-SRC-EXC-REV016-001`  
**Disposition date:** 2026-11-16  
**Status:** **CLOSED — DOCUMENTED SOURCE LOSS; RESIDUAL RISK ACCEPTED FOR CONTINUATION**  
**Owner authorization:** Owner selected **Alternative A**: one final targeted recovery search, then apply mitigation if unsuccessful. Owner reported no match in local ZIP tree. This record implements that direction; it does **not** claim restoration or approval of any dependent historical assertion.

## Exact evidence gap

- **Missing original:** `04_Rev0_16_Source_Identity_and_Authority.json`.
- **Manifest-recorded SHA-256:** `a9a2ce478cc5cc0647e20418787f948ac8faaaf7fd491cb6e880d10d9a1eebaa`.
- **Manifest context:** `03_REV0_16_CANDIDATE_QUALITY_AND_ORACLE_SCREENS/SHA256SUMS_rev0_16.txt`, within the original `LocalAI_Independent_Review_PhaseII_Source_Comparison_20261114(1).zip`.
- The missing file is an **authority/source-identity metadata JSON by its recorded name**; its exact keys, entries, and statements are **UNKNOWN**, and must not be inferred from its name or recreated from a later summary.
- This is **one absent manifest-listed member**, not evidence of altered bytes or corruption of the seven present members.

## Bounded final recovery search

| Search scope / witness | Observed result |
| --- | --- |
| Owner's laptop `./` ZIP tree, including recursive/nested ZIP search script | Owner reported **NO MATCH**; complete archive count/output unavailable to this record |
| Conversation original `LocalAI_Engineering_Knowledge_Transfer_Recovery_20261116(1).zip` | 3,451,941 bytes; SHA-256 `9a48de5fa49420e470f003b7f3417277bd3aa2a6832a7b2c968d093004c2e37e`, exact known original identity; ZIP CRC PASS; original outer 13/13 manifest PASS |
| Conversation recovery and candidate audit ZIPs | 3 on-disk ZIP files recursively inspected; **15 unique ZIP instances, 247 non-directory members, 32 JSON files SHA-256-hashed**. No exact filename match, no match to expected SHA-256 under any JSON filename, no decompression errors |
| Phase II source-comparison ZIP within original recovery | Independently rechecked **54/54 outer manifest members MATCH**; Rev0.16 nested manifest **7/8 MATCH**, **1 MISSING**, **0 MISMATCH** |
| Public project GitHub default-branch file search | No search result for exact missing filename; this is **not** evidence it is absent from all Git branches or non-indexed assets |
| Project Library historical `Local_AI_GR_GA_Comprehensive_Recovery_Through_Rev0_17_2026-11-09.zip` (5,702,383 bytes) | Metadata found, **raw bytes inaccessible** through available Library materialization/read access; **NOT INSPECTED**. Do not claim this or all historical archives were exhaustively checked |

**Search conclusion:** exact original **not recovered from byte-accessible sources**. The named Library archive was identified but cannot currently be opened; this is a bounded search limit, not proof that it lacks the missing member. Further hunting is not warranted absent new access, a specific contrary finding or a new owner direction.

## Surviving independent evidence and control boundaries

1. Rev0.16 `01_136_Source_Anchored_Quality_Gate_Audit_rev0_16.csv`, `02_26_Source_Specific_Oracle_Falsification_Gates_rev0_16.csv`, `03_26_Candidate_Oracle_Predicates_rev0_16.json`, `05_Offline_Oracle_Predicate_Falsification_Harness_rev0_16.py`, `06_104_Synthetic_Predicate_Results_rev0_16.csv`, `07_Rev0_16_Gate_and_Session_Continuity_Status.json`, and original Rev0.16 ODT remain present and individually hash-verified.
2. The EX-01 `ORIGINAL_AUTHORITY_REGISTER_CROSSWALK.csv` separately records many original source identifiers, authority categories, and limitations. It **overlaps provenance**; it is **not** a byte-identical substitute for the missing JSON or proof of every claim originally present.
3. The original 136 requirement statements and hashes, 159 allocation links, and 26 oracle identities were separately recovered and cross-checked in the 2026-11-16 RP-01–RP-04 working audit. **Their independently observed identity evidence does not depend on this missing JSON**.
4. Release decisions after Rev0.16 are recorded separately. The owner-approved R1 local-only / R2 two hosted providers / R3 autonomous strategy, FAT Alternative B and four R2 architecture seams are **not adjudicated by the missing Rev0.16 file**.

## Risk acceptance and mitigation

| Risk domain | Residual classification | Mitigation / limit |
| --- | --- | --- |
| Exact reconstruction of historical Rev0.16 source-identity/authority assertions | **MODERATE localized provenance gap** | Preserve original manifest/hash and explicit missing status; do not cite the missing file as an authority or fill its unknown content by inference |
| Current R1 requirements allocation and independent review | **LOW additional risk from this missing file** | Revalidate every controlling requirement statement, owner decision, hash, trace link and acceptance predicate against accessible original independent sources; cite those sources, not the missing JSON |
| RP-03 / RP-04 source-based interface and oracle decisions | **LOW additional risk from this missing file** | Keep G-A/interface schema/oracle acceptance independently gated; never use a Rev0.16 simulation to prove installed-system behavior |
| Application runtime, deployment and FAT | **No demonstrated direct impact** | Runtime checks and first-article demonstrations remain separate future obligations under existing holds and owner authorization |

**Accepted residual limitation:** historical Rev0.16 completeness cannot be certified and any unique authority assertion that existed *only* in the missing JSON remains unverified. This is an archival/provenance exception, **not** a waiver for G-R, G-A, engineering evidence, software functionality or FAT.

**Closure rules:** maintain the original manifest and surviving records unchanged; record **`MISSING_ORIGINAL / RISK_ACCEPTED / NON_BLOCKING`** in any future inventory. Do not place the issue into routine blocker lists or repeat warnings in every engineering increment. Link this decision when source provenance specifically matters. Reopen **only** upon a recovered matching-byte original, contradictory controlling source/authority evidence, a source-sensitive adjudication that cannot be supported by surviving originals, or an explicit owner request.

## Outcome

**CLOSED FOR ENGINEERING CONTINUATION** under the owner's Alternative A fallback. No source bytes reconstructed. No changed approved baseline, production service, G1 runtime hold, release scope, billable API authorization, gate approval or FAT acceptance is implied.

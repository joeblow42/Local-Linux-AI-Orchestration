# Owner-approved 42-increment FAT planning dispositions and installation sequence

**Decision label:** `LAI-OD-20261119-08` — new administrative owner-approval reference (NOT a historical requirement/oracle/interface ID).  
**Date:** 2026-11-19. **Authority:** owner approved all 42 recommended dispositions in [full 42-increment audit](./R1_42_INCREMENT_RISK_PROPORTIONALITY_AUDIT_CANDIDATE_20261118.md) by stating “approved, answer question and then continue if safe, which increment will OpenWebUI or LangGraph be installed?” The earlier prompt explicitly sought approval to **adopt the 42 proposed dispositions as the basis for a revised FAT roadmap**. This is **planning-direction approval only**, not permission to remove essential outcomes, authorize a runtime installation, approve G-R/G-A contract baselines, release G1 hold or merge PR #1.

**Verified uploaded original:** `LocalAI_Release_Strategy_Rev0_2_Candidate_Engineering_Package_20261115(2).zip` (SHA-256 `0e3c45e6d5fd5b0180264a542030c10cca8ca48c6b0ba196ab378276c214ffc1`); ZIP CRC PASS; 12/12 embedded SHA-256 manifest members PASS. Original Rev0.2 ODT and actual 42-row trace CSV both inspected. Source archive remains external to this public repo.

## Accepted planning decisions — 42 IDs preserved

- `RETAIN 15`, `SIMPLIFY 12`, `COMBINE 12`, `DEFER 2`, `REMOVE 1` **as standalone work activities only**. All historical RP-01 through RP-14 and 42 individual INC IDs stay traceable. The canonical per-increment disposition is the linked [full audit](./R1_42_INCREMENT_RISK_PROPORTIONALITY_AUDIT_CANDIDATE_20261118.md); do not silently rewrite historical Rev0.2 source content.
- `RP-06.INC-02 REMOVE` means remove a **blanket network-denial interceptor as a standalone R1 implementation**. Keep Ollama-only inference, no hosted fallback and external application telemetry disabled; necessary loopback/LAN and authorized downloads remain allowed.
- `RP-14.INC-03 RETAIN` means **actual operational installed FAT, independent evidence and owner FAT acceptance**; not FAT-entry authorization alone.
- Eliminate unjustified parallel monitor/resource planner, licensing detection, second Pipe/UI, external-provider mocks, autonomous schedules and repeated synthetic hardening. Preserve checkpointing/restart recovery, cancellation, original chat automatic result delivery, real three-owner backup/restore, storage-mount guard and offline installation/redistribution compliance.
- Original 136 requirement identities with approved release assignments 104 R1/17 R2/15 R3, original 19 interface identities and 26 original oracle identities remain intact. Their G-R/G-A exact baseline and test execution remain **NOT APPROVED/NOT RUN**.

## Clarification: Where the real application is installed

This wording is grounded in the **original Rev0.2 roadmap source**, reconciled with the owner's approved 42-disposition reductions:

| Increment | Correct installation/development role | Approved 42-disposition effect |
| --- | --- | --- |
| `RP-05.INC-01` | Select/pin candidate Open WebUI, LangGraph, Bifrost OSS, Ollama versions, Bodhi 7 AMD64/Python ABI, storage and resource prerequisites | RETAIN. This is **pre-installation** preparation; no claim of installed versions |
| **`RP-05.INC-02`** | **First provision/install** of actual local service foundation: UI (Open WebUI), independently managed LangGraph supervisor service, gateway and Ollama, plus correct data-store ownership | RETAIN. Install each component **once** on an expressly selected non-G1 test host; avoid inventing admin/monitor daemon |
| `RP-07.INC-01` | Original Rev0.2 says **“Install/pin UI”**, but revised approved audit **combines** the installation into RP-05.INC-02, and preserves Open WebUI conversation DB/persistence verification here and RP-12 | COMBINE; not a second UI installation |
| `RP-09.INC-01` | Develop and activate real independent LangGraph HTTP task supervisor, single Open WebUI Pipe, stable task IDs and two configured local specialist roles | SIMPLIFY; initial service provision at RP-05.INC-02 is **not** proof that the task supervisor already functions |
| `RP-09.INC-03` | Execute actual end-to-end user-triggered two-specialist workflow; later owner-approved **automatic result delivery to the originating Open WebUI conversation** must be included | RETAIN |
| `RP-13.INC-02` | Package tested services and dependency closure as project Debian `.deb` and complete offline transport archive | RETAIN; separate from initial engineering installation |
| `RP-14.INC-02/03` | Rehearse and execute real installed system FAT and owner acceptance on supported target | SIMPLIFY / RETAIN respectively |

**Important ordering distinction:** `RP-05.INC-02` installs/provisions the foundational service processes; `RP-09.INC-01` builds the functioning application-specific LangGraph delegation implementation. A Python environment or service unit named LangGraph is not evidence of a functioning supervisor.

## First bounded, safe RP-05.INC-01 preparation (no installation authorized)

Current GitHub source inventories show:
- `dependencies/inputs/open-webui.in` proposes `open-webui==0.12.5`, source tag commit `f7ac7ee10962ddec0017f5c29b6740d9b9c5faca` (not deployed version proof).
- `dependencies/inputs/langgraph.in` proposes `langgraph==1.2.19`, source commit `5bd231cbfd913e05ebc662f519eb9a655bc766df` (not installed or fully transitively locked).
- Existing LangGraph source review identifies `langgraph-checkpoint==4.3.1` and `langgraph-checkpoint-sqlite==3.1.3` as version-constraint-compatible **candidates**, not installed packages.
- Bifrost OSS is the approved gateway instead of historic LiteLLM, with v2.4.0 tagged source-review candidate `e869c3f9adc96ea53c38694a21bb04a8e1085487`. Its exact OCI/image digest and current configuration still require bounded verification.
- `dependencies/inputs/litellm-proxy.in` and `dependencies/scripts/generate_locks.sh` still reference **obsolete LiteLLM**; do not package LiteLLM or silently run obsolete lock generator as the current product. Align build tooling before actual dependency acquisition.
- Historical local Ollama version reported in project observations is **0.40.13**; independently identify chosen test-host version rather than assert deployed state.
- Pinned Open WebUI source review reports Python >=3.11 and <3.13; selected runtime/interpreter on **Bodhi 7 AMD64** not yet verified. Historical lock script expects a bundled Python 3.12.14 executable; presence not established on target.
- **Data unavailable:** nominated isolated non-G1 installation target, actual target Python/Docker ABI, free storage, installed component versions, candidate complete offline wheel/dependency locks and full real UI/supervisor readiness. Do not invent resource thresholds.

**Immediate next engineering step:** finish RP-05.INC-01 using **read-only evidence from an explicitly selected isolated non-G1 host** and the approved candidate source pins; check service installation/port/storage conflicts before any RP-05.INC-02 changes. Build one real installation and connected direct/delegated test rather than a new round of mocks. The operator has approved a *planning direction*, **not** a specific host mutation or release of held G1.

**Status and boundaries:** no G1 inspection/mutation, no user-owned key creation/rotation, no hosted API calls, no broad network interception, no R2/R3 code, no unapproved G-R/G-A baseline promotion, no PR merge; original 26 FAT oracle executions NOT_RUN. PR #1 remains draft/unmerged.

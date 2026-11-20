# Local AI — RP-05.INC-01 host and dependency pre-install checkpoint

**Date:** 2026-11-19. **Status:** safe source/tool preparation completed; target-host observations pending. **RP-05.INC-02 service installation NOT STARTED.**  
**Governance:** AI-Assisted Software Engineering Governance Standard v1.0; owner-approved simplified 42-increment FAT planning disposition `LAI-OD-20261119-08`. This document is a checkpoint, **not** a G-R/G-A owner approval or permission to mutate G1.

## 1. Original roadmap boundary and approved plan

Read the original uploaded `LocalAI_FAT_Roadmap_42_Increment_Change_Trace_Candidate_20261115.csv` and the original Rev 0.2 candidate roadmap ODT (ZIP SHA-256 `0e3c45e6d5fd5b0180264a542030c10cca8ca48c6b0ba196ab378276c214ffc1`, 12/12 member hashes previously validated). Original `RP-05.INC-01` is **“Select target host and lock dependency inputs”**, with source work **“Inventory host OS/ABI/CPU/network, exact Open WebUI/LangGraph/gateway/Ollama versions, storage and dependency licenses”** and an expected **reproducible pin/lock, service bill of materials, verified prerequisites, no guessed installed version**. Rev 0.2 clarifies exact version pins, Bodhi Linux 7 AMD64 / Ubuntu 22.04 ABI, and resource budget.

Original `RP-05.INC-02`: **“Deploy separate durable service boundaries”** and provision isolated operator UI, independent supervisor, gateway, local conversation/checkpoint data and service identities. Later owner-approved consolidation folds duplicate WebUI setup from RP-07.INC-01 into RP-05.INC-02. The target installation is NOT yet approved/executed.

## 2. Completed source/engineering corrections

- Added [read-only host readiness inspection](../../../dependencies/scripts/host_readiness_readonly.sh), git blob `ceb78669c6d6d39ccda6a0071036cd7d247052f7`. Requires an explicit `--confirm-non-g1` argument, reads **only** OS/kernel/architecture, PATH and candidate bundled Python 3.12 presence, memory/CPU and nominated storage capacity/mount state; emits no usernames, IPs, service credentials, model output or configuration file contents. No sudo, package install, gateway/API calls, or host mutation. Inspected with `bash -n`; refusal without opt-in test PASS; execution on temporary **Debian container** succeeded as a functional syntax/smoke check, **not Bodhi/G1 evidence**.
- Updated active `dependencies/scripts/generate_locks.sh` (git blob `63c2b3bfacac7c321c48c76ff0db4dcdd755ca2a`). Only `open-webui` and `langgraph` Python lock inputs are now active; `litellm-proxy` removed from generation. Writes explicit `RELEASE1_PYTHON_LOCK_ALLOWLIST.txt` and warns if a stale LiteLLM lock already exists without deleting historical files. Uses candidate Python 3.12.14 path unless `LOCALAI_PYTHON_BIN` is set. **Modified but NOT executed; no lock/resolution/downloading completed.** Bifrost OSS OCI/image and Ollama binaries require distinct component provenance and offline closure.
- Prepended a **superseded-for-R1 warning** to the historical 2026-10-31 `dependencies/LICENSE_AUDIT_WORKFLOW.md`. Original evidence remains in Git history; old three-lock and LiteLLM license wording is now unmistakably labeled historical rather than active R1 procedure.
- Rechecked upstream **source-pinned candidate** Python constraints: `open-webui/open-webui@f7ac7ee10962ddec0017f5c29b6740d9b9c5faca` `pyproject.toml` blob `737226fb10971e5fd875c8a02f62730324760aa2`, `requires-python = ">= 3.11, < 3.13.0a1"`; `langchain-ai/langgraph@5bd231cbfd913e05ebc662f519eb9a655bc766df` `libs/langgraph/pyproject.toml` blob `0f50773525faf770592eff417a89752031964e83`, `requires-python >=3.10`, `langgraph==1.2.19`; same LangGraph source `libs/checkpoint-sqlite/pyproject.toml` blob `7eff2a5969547be703fc22964584339cc4cf0e9a`, `langgraph-checkpoint-sqlite==3.1.3`, `requires-python >=3.10`. Python 3.12 is within this **declared** overlap; full lock/install/ABI behavior remains UNVERIFIED.
- Repository's `dependencies/inputs/open-webui.in` and `langgraph.in` retain **candidate** pins `0.12.5` and `1.2.19` respectively. Bifrost OSS `v2.4.0` is the approved gateway architecture but image digest and full offline artifact closure are not verified. Never reintroduce the superseded LiteLLM package as Release 1 dependency.

## 3. Host readiness information needed before installation

**Data unavailable for selected real non-G1 R1 test environment**: actual OS and kernel, Python 3.12 interpreter path, Python/uv installed versions, AMD64 check, available application-storage bytes and exact mount, host RAM/CPU, service manager, actual installed version/ports for any preexisting test services, and potential conflicts. Existing historical Bodhi laptop observations are not a new source for today's state. The isolated build container used to syntax-test the preflight is **Debian 13** and is NOT the target computer; do not mistake its results for Bodhi evidence.

**Smallest next safe request to owner:** on the chosen Bodhi/non-G1 test environment, run the [read-only preflight script](../../../dependencies/scripts/host_readiness_readonly.sh) with explicit `--confirm-non-g1`; operator may provide a different absolute `LOCALAI_STORAGE_PATH` for its isolated application test mount. Capture only reported non-sensitive OS/runtime/resource facts. Do not infer G1 service state or alter it. A **non-G1 test environment can share a physical laptop with held G1 if storage/services/ports are separate**; do not assume a second physical machine is mandated.

After facts: confirm compatible supported Python, host storage and lack of test-service conflicts, decide specific isolated directories/service identities; prepare the minimal 2-input Python lock plus separate Bifrost/Ollama provenance. **Before executing lock generation/downloads or RP-05.INC-02 installation**, verify dependency and G-A/host authorization gates. Do not arbitrarily require an unrelated extra daemon or exhaustive threat testing.

## 4. Gating and no-go boundaries

- G-R complete exact requirement baseline **NOT APPROVED**. G-A source-specific runtime/auth/HTTP schemas **NOT APPROVED**. Owner approval of 42 planning dispositions does not implicitly freeze technical baseline.
- G1 target runtime/data collection **OWNER HOLD**; no current installed configuration verified. Do NOT obtain G1 API credentials or inspect/mutate G1.
- No server, package, virtualenv, image or key was installed/configured/generated here; no external paid inference. Python lock generator **NOT RUN**. No original FAT oracles executed (**26/26 NOT_RUN**).
- PR #1 must remain draft/open/unmerged; no CI passing without workflow evidence.
- This is sufficient progress for **RP-05.INC-01 in progress**. The only blocker to further target-specific work is **read-only host evidence** and applicable deployment/technical approvals, not another mock-only source review or the closed Rev0.16 historical exception.

**Recommended follow-on:** operator provides read-only preflight output; finish RP-05.INC-01 candidate version/ABI/storage prerequisites and authorize isolated RP-05.INC-02 provisioning on a specifically identified non-G1 environment.

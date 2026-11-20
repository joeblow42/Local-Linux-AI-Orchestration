# Local AI RP-05 — Existing-G1 prerequisite and checkpoint tooling

**Date:** 2026-11-19 (America/Denver). **Status:** source-only engineering checkpoint, not completed installation. Applicable owner decisions: LAI-OD-20261119-08/-09. Governance: AI-Assisted Software Engineering Governance Standard v1.0.

## Confirmed scope

Existing Bodhi Linux 7.0 / Ubuntu 22.04 x86_64 host is the selected Release 1 development target. No separate host or cloned G1. Reuse running healthy Bifrost Docker container (root-only Docker administration) and active local Ollama. The old G1 hold and non-G1 test-host instructions have been superseded. PR #1 remains draft/unmerged. No paid APIs or LiteLLM. Original 136 requirement, 19 interface and 26 oracle identities and 42 roadmap identities remain traceable; original oracles NOT_RUN.

## Operator-run sequence

Run from a checked-out current PR #1 head; first inspect the scripts before execution. All scripts have explicit modes and should stop on material mismatches.

1. Existing-G1 read-only inspection: `bash dependencies/scripts/rp05_g1_readonly_gate.sh --existing-g1`. This invokes `sudo -v` once and uses `sudo -n` for root-only Docker/socket inspections. It verifies pinned Python availability, exact storage mount, healthy G1 identity, current Ollama API, G1 listener on 8080, and candidate port availability (Open WebUI 3000; LangGraph supervisor 8010). The proposed ports are *not* an approved G-A freeze. The routine prints no container env or user credentials.
2. Single real current gateway inference: `python3 dependencies/scripts/rp05_g1_local_inference.py --model 'EXACT_LOCAL_OLLAMA_TAG'`. Use an actual local model tag reported by step 1. Enter the *existing* virtual key at the hidden prompt; do **not** provide it in shell command arguments, GitHub, ChatGPT, logs, or screenshots. This sends one small request to Bifrost at localhost and returns a redacted PASS/FAIL; a failed request stops the gate, without key rotation or G1 replacement. Confirm local-only dispatch with actual runtime evidence.
3. Root-only recoverable checkpoint **before any existing-service modification or new package provisioning**: `sudo -v && sudo -n python3 dependencies/scripts/rp05_g1_checkpoint.py --create`. It verifies current G1 bind mount and running state, copies existing data with SQLite online backup, stores the Docker inspect (which may contain secrets) in a root-only local directory under `/mnt/local-ai-storage/development/checkpoints/`, and re-reads SHA-256 hashes. Do not upload any `.private.json` content. A failed checkpoint stops installation. The checkpoint stays on the same mount; **not** an offline RP-11 backup, full transactional multi-file snapshot, or verified independent restore.
4. After preceding checks pass: `bash dependencies/scripts/generate_locks.sh` generates hash-locked *candidate* dependency resolutions (no package install) under `/mnt/local-ai-storage/development/dependencies/locks/` for Open WebUI 0.12.5 and LangGraph 1.2.19 plus SQLite checkpointer 3.1.3. Inspect package ABI, space, license and transitive closure and confirm actual service bind paths before provisioning. Maintain separate persistent Open WebUI conversation and LangGraph checkpoint data on the same application mount. Never prune or replace existing G1 data/container/image to create room.

## Source-level verification and status

Initial code review and focused syntax/SQLite snapshot-function checks passed on authoring environment only. The actual Bodhi host has *not* executed these new tools; current gateway inference and recoverable checkpoint have not been observed; candidate Python locks and complete offline artifacts have not been produced. **RP-05.INC-01 remains in progress and RP-05.INC-02 is not installed.** The independent service provisioning follows only after successful host gates and must be independently verified. LangGraph *process provisioning* in RP-05 is not the functioning two-specialist supervisor/Pipe acceptance in RP-09.

Any mismatch in G1 ownership, live inference, data bind, save/restore practicality or unanticipated service impact is a material engineering stop, not permission to rewrite prior approvals. Do not claim a FAT or production baseline from the scripts.

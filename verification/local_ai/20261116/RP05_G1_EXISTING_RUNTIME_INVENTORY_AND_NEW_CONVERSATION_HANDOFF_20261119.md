# Local AI — RP-05 existing-G1 inventory verified by operator; next-conversation handoff

**Date:** 2026-11-19. **Status:** read-only operating environment and existing-G1 inventory collected from operator terminal output, source-reconciled; candidate RP-05.INC-01 progress checkpoint. **No application installation or G1 modification performed.**  
**Governance:** AI-Assisted Software Engineering Governance Standard v1.0.  
**Authority:** Latest explicit owner decision [LAI-OD-20261119-09](./OWNER_APPROVAL_BODHI7_AND_G1_IN_PLACE_RP05_20261119.md) supersedes the previous G1 hold **for bounded in-place engineering**. The owner's approved 42-increment planning classifications are recorded in [LAI-OD-20261119-08](./OWNER_APPROVAL_R1_42_INCREMENT_DISPOSITIONS_AND_EARLY_INSTALL_SEQUENCE_20261119.md) and the [42-increment audit](./R1_42_INCREMENT_RISK_PROPORTIONALITY_AUDIT_CANDIDATE_20261118.md). Original requirements, interface and oracle IDs must remain traceable.

## Decided and verified platform

- **Bodhi Linux 7.0** laptop on **Ubuntu 22.04 Jammy** base. `/etc/lsb-release` reads `DISTRIB_DESCRIPTION="Bodhi 7.0"`; Moksha `0.4.2-4`. **Do not re-question the distribution or seek a separate non-G1 test host.**
- Architecture x86_64; kernel `6.2.0-26-generic`; root `/dev/nvme0n1p7` ext4; application mount `/mnt/local-ai-storage` on `/dev/loop2` ext4; `/mnt/local-ai-storage/development` exists; `/mnt/local-ai-storage/r1-test` absent and **not needed**. Preflight reports mount exact YES and **32,536,731,648 bytes** available (observed at preflight, not a guaranteed installation threshold).
- Bundled candidate Python **3.12.14 executable present**; `python3.12` not on PATH, not a blocker. Tools `uv`, `docker`, `dpkg`, `dpkg-deb`, `systemctl` and `findmnt` present. 12 logical CPUs, 32,563,648 KiB RAM, 33,400,828 KiB swap.
- **Docker administrative access is deliberately root-restricted**; previous non-sudo `docker ps` permission failures are expected. Never infer “container not found” from permission-denied inspection. For bounded diagnostics use `sudo -v` once then `sudo -n docker ...`; **do not add user to the docker group**.

## Fresh G1 inventory (operator read-only root-authorized observations)

| Subject | Observed | Engineering consequence |
| --- | --- | --- |
| Docker container | `bifrost-g1`; `Up 9 days (healthy)` | Preserve and reuse operational G1. Docker health is a check, **not proof of latest inference success** |
| Docker image | `maximhq/bifrost@sha256:a1c90607dcfd13c1fb2f9476ceb3bb24407a50ade7fdf3e61a59fb42b09e5c57` | Pinned runtime identity observed. No need to replace it without evidence |
| Network | `host` | Port ownership and collision matter for new local services |
| Data bind mount | `/mnt/local-ai-storage/bifrost/g1/data:/app/data` | Existing G1 persistent storage; do not overwrite |
| Restart policy | `unless-stopped` | Existing G1 service policy |
| Docker root | `/mnt/local-ai-storage/infrastructure/docker` | Already relocated, within application storage |
| Docker images | 1 active image, 411.8 MB Docker-reported usage | `100% reclaimable` field must **not** justify pruning an image that is currently in use |
| Containers | 1, running G1; 16.38 kB writable size | No other Docker containers shown in this inventory |
| Docker volumes/build cache | 0/0 reported | Bifrost uses bind mount, not named Docker volume |
| Ollama | `systemctl is-active ollama` → `active`; `127.0.0.1:11434` listening | Reuse existing local backend; current version/model readiness not independently verified here |
| Loopback port 8080 | `127.0.0.1:8080`, process label `main`, PID 1979 | **Port occupied**; likely gateway but **process ownership not proven**. Verify without exposing command-line secrets before choosing WebUI port |
| Other observed listening ports | 22, 8096, 53, 34343, 631, 6463 (plus 11434 and 8080) | Do not assume 8080 or other occupied port available for new WebUI. No need for exhaustive network threat tests |

Operator first ran Docker without privileges; resulting “bifrost-g1 container not found” conclusion was **invalid**. Correct `sudo` inspection demonstrates the running and healthy container.

## Engineering scope and readiness

**RP-05.INC-01:** Supported platform identity, Python availability, existing-G1 identity, Docker root, data mounts and baseline capacity now established. Actual candidate Python lock generation and complete license/ABI/offline closure, current installed model request verification, and final service bind choices still pending; do **not** mark RP-05.INC-01 fully accepted.

**RP-05.INC-02:** The **first in-place installation/provisioning of Open WebUI and independently managed LangGraph supervisor**, alongside the existing G1 Bifrost/Ollama. RP-07.INC-01's duplicate Open WebUI installation is absorbed by approved roadmap simplification. RP-09 later implements one functional trusted Pipe, two local specialist roles, durable task/checkpoint status/cancel, and automatic synthesized result in originating conversation. Do not confuse package provisioning with a completed supervisor.

**Current source candidate pins:** `open-webui==0.12.5`, `langgraph==1.2.19`, `langgraph-checkpoint-sqlite==3.1.3`, Bifrost OSS 2.4.0 tagged source candidate; exact **deployed** Docker image digest now observed as above; Ollama currently active but version not checked in this last command. Python 3.12.14 executable verified. [Active R1 Python lock generator](../../../dependencies/scripts/generate_locks.sh) excludes historical LiteLLM and outputs only Open WebUI and LangGraph candidate Python locks. **Generator has not been executed, no dependency wheelhouse produced or verified**.

### Narrow next-session action

1. Read this handoff and the controlling two owner-decision docs **directly from the latest GitHub commit**, verify exact-head PR #1 is draft/open/unmerged. Do not reopen Bodhi release or assume a second test environment.
2. Finish **only remaining** RP-05.INC-01 readiness: ensure existing G1 data/config are recoverable before any mutation, choose non-conflicting WebUI/supervisor bind ports and distinct persistent directories on the **same** application mount, verify the gateway's existing port ownership, and verify the minimal package/runtime/ABI dependencies with no unapproved paid API use.
3. Move directly into the first bounded RP-05.INC-02 **in-place** provision when technical and authority gates permit. Keep root-only Docker privilege, reuse already-running G1 Bifrost/Ollama, and stop on unexpected destructive/irreversible change. No duplicate installation and no speculative security test expansion.
4. Verify each actual installation action promptly. Original 26 FAT oracles remain `NOT_RUN` until actual installed tests; retain requirements 136 (R1 104, R2 17, R3 15), interfaces 19, 42 planning identities and the distinction between candidate G-R/G-A vs owner approvals.

**Authority boundaries:** Current owner **does authorize in-place G1 inspection and staged development**. It does **not** authorize rotating secrets, merging PR #1, running hosted paid APIs, building R2/R3 features or silently promoting exact G-R/G-A baselines. Preserve source-only vs observed results. No new mock permutations solely to simulate improbable hostile-operator races.

## Why new conversation now

Long conversation already contains many superseded historical restrictions and preliminary assumptions. Handoff is appropriate before the **mutating installation phase** while the current increment's observational G1 inventory is complete. This checkpoint consolidates current facts without implying RPM/DEB/application deployment is done.

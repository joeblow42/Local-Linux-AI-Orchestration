# Local AI Codex handoff at RP-13

For the current continuation point, use the [packaged G1 and clean-target FAT handoff](LOCALAI_CODEX_HANDOFF_AFTER_PACKAGED_G1_20261121.md). This file retains startup instructions and the earlier RP-13 history.

## Instructions for the next Codex session

**Run this block only when the owner's message ends with the standalone word `wait`.**

1. Wait. Do not proceed with the requested work or use tools to carry it out.
2. Summarize the request back to the owner.
3. Ask clarifying questions only if needed. Keep any required question and its options available while waiting for the owner's answer.

Resume when the owner explicitly directs you to proceed. A mention of `wait` anywhere else in a message does not trigger this block.

### Normal working instructions

- Follow the AI-Assisted Software Engineering Governance Standard v1.0. Put reliability and verification before speed. Consult the approved roadmap when changing increments, and use actual evidence to determine status. Proceed in order through the authorized work. After a verification passes, move directly to the next step. If the owner asks for status, answer briefly and keep working. Stop for an explicit pause, a material blocker you cannot resolve, or an owner decision or action you genuinely need.
- Use the root `AGENTS.md` as startup orientation only. For ongoing decisions, use the current owner approval records, roadmap, and verification evidence. Preserve historical records and cite the later controlling decision when earlier instructions differ.
- Treat routine non-destructive Local AI work as authorized when the owner directs continuation. Avoid asking the owner to reconfirm it. Workspace sandbox approvals and OS authentication are separate from project authorization. Explain any mandatory tool approval in terms of the specific operation. Keep privileged work narrow, use the operator's current authorization, and avoid repeatedly retrying a known authentication failure. Never print, stage, commit, or transfer secrets or private machine configuration. Confirm before destructive actions and before committing or pushing this session's work.
- Develop in place on the established Bodhi Linux 7 / Ubuntu 22.04 AMD64 G1 system. Preserve Bifrost and Ollama. Keep Docker administration root-restricted. Take recoverable checkpoints before changing existing services or data. Reuse installed runtimes and prior evidence. Avoid duplicate installs, unnecessary hardening, and repeated mock suites.
- Keep Release 1 inference local through Bifrost and Ollama, with external application telemetry disabled and paid providers outside scope. Keep PR #1 draft and unmerged. Preserve all 42 increment identities, 136 requirement identities and their 104/17/15 release allocation, 19 interfaces, and 26 original FAT oracle identities. Exact G-R and G-A baselines and formal installed FAT acceptance remain pending.
- For operator commands, specify the host, working directory when it matters, and the expected output to share. Keep credentials in their local prompts or protected stores. Do not include private backup paths or credential values in GitHub evidence.

## Checkout and source of authority

Continue in the `Local-Linux-AI-Orchestration` checkout on `handoff/localai-20261116-recovery`. The handoff's base commit and last verified fetched upstream were `2f40cf0468848af18c17de73c8e7a73dc5a06485`. The owner directed that the handoff, related implementation, verification records, and release evidence be versioned locally. Review `git status --short --branch` and `git log` before making changes. PR #1 was verified open, draft, and unmerged at the base commit during the original setup. [Draft PR #1](https://github.com/joeblow42/Local-Linux-AI-Orchestration/pull/1)

Read the [owner-approved dispositions](./OWNER_APPROVAL_R1_42_INCREMENT_DISPOSITIONS_AND_EARLY_INSTALL_SEQUENCE_20261119.md) together with the [42-increment roadmap audit](./R1_42_INCREMENT_RISK_PROPORTIONALITY_AUDIT_CANDIDATE_20261118.md) for the current sequence. The later [Bodhi 7 and in-place G1 decision](./OWNER_APPROVAL_BODHI7_AND_G1_IN_PLACE_RP05_20261119.md) controls host selection. The [original inventory](./RP05_G1_EXISTING_RUNTIME_INVENTORY_AND_NEW_CONVERSATION_HANDOFF_20261119.md) and [provisioning proposal](./RP05_EXISTING_G1_PROVISIONING_TOOLS_CANDIDATE_20261119.md) supply historical and candidate context. [Automatic delivery decision](./OWNER_APPROVAL_IF02_AUTOMATIC_FINAL_DELIVERY_A_20261117.md) · [Operator-owned WebUI key decision](./OWNER_APPROVAL_IF02_DELIVERY_OPERATOR_WEBUI_KEY_A_20261117.md)

## Verified work and lessons

- **RP-05 through RP-08.** The preflight, recoverable checkpoints, hash-verified offline wheel sets, separate installed Open WebUI and LangGraph runtimes, and loopback listeners were verified. Existing Bifrost and Ollama were reused. Open WebUI's offline embedding-model warning affects document retrieval. Its readiness check passed. Direct chat succeeded at a 4,096-token context after disabling the model's **Built-in Tools**. Reuse the existing Bifrost virtual key through the `x-bf-vk` header. Earlier HTTP 401 responses cleared after the operator copied the correct existing key. An operator restart of Ollama was followed by successful Bifrost inference. The timeout witness measured a client deadline and recovery. [Provisioning evidence](./RP05_INC02_G1_PROVISIONING_EVIDENCE_20261120.md) · [Authentication evidence](./RP06_INC01_EXISTING_AUTH_WITNESS_20261120.md) · [Live direct-route evidence](./RP06_RP08_EXISTING_G1_LIVE_WITNESS_20261120.md)
- **RP-09.** The registered Open WebUI Pipe submits work to the independent LangGraph supervisor. Live evidence covers stable task IDs, duplicate submission, owner isolation, running cancellation, mid-workflow restart, two sequential specialists, synthesis, and automatic final delivery. The Open WebUI API key is endpoint-restricted to chat routes. The browser renders structured `output`, so delivery must update both `content` and `output`, independently read them back, and emit the structured completion event. The operator saw the repaired reply appear in the original conversation without refreshing. The existing API retains a narrow concurrent edit/deletion race. The owner deferred an atomic patch as **FUT-002**. [Supervisor evidence](./RP09_G1_SUPERVISOR_CHECKPOINT_20261120.md) · [Upgrade backlog](./POTENTIAL_UPGRADES.csv)
- **RP-10.** The supervisor records sanitized stage metadata and observed token counts, with missing values stored as unknown. A live task yielded all six observed counts. The 30-day purge checks passed and preserved task history. This does not establish container-log retention or a comprehensive egress audit. [Metadata and retention evidence](./RP10_G1_METADATA_RETENTION_EVIDENCE_20261120.md)
- **RP-11.** The owner selected their home filesystem for the private backup. The fresh-directory restore verified 14 manifest entries and five SQLite snapshots. An isolated startup against a disposable copy passed Bifrost health, authenticated WebUI chat readback, and matching LangGraph task readback with the already installed runtimes. Live services stayed in place. Treat the copy as separate from the application mount and still on the same laptop. [Backup and restore evidence](./RP11_G1_BACKUP_RESTORE_EVIDENCE_20261120.md)
- **RP-12.** Reuse the installed direct and delegated browser journeys and the isolated restore. A missing local model returned HTTP 403. One measured request took 4.53 seconds directly through Bifrost. The measured delegated task acknowledged in 0.01 seconds and delivered in 36.29 seconds, with peak sampled memory and stage counts recorded. These are measurements from one workload. Formal FAT and independent release acceptance remain open. [Integrated workload evidence](./RP12_G1_INTEGRATED_WORKLOAD_EVIDENCE_20261120.md)

## Resume at RP-13

The local wheel BOM includes 253 unique artifacts and 414 embedded notices. Three of ten embedded-notice gaps received same-version notices from hash-checked source distributions. The local Bifrost image export passed SHA-256 readback. Its exact OCI digest and export checksum identify the artifact. The owner expects the exact source revision to be unrecoverable. Keep that revision unknown and avoid repeatedly searching for it. Use verified artifact identity in local work and record the remaining provenance and notice limits for redistribution.

Continue RP-13.INC-01 with the remaining wheel notices and the distribution-level provenance and licensing review for the Bifrost image, Python runtime, Ollama runtime, and model. Then follow the approved sequence for the project-owned home-use Debian package, separate offline dependency transport, and compatible upgrade and rollback check. Record any distinction between local-only rehearsal and a transport approved for public redistribution. The package, complete offline transport, and RP-14 acceptance have not been completed. [Current RP-13 checkpoint](./RP13_G1_ARTIFACT_PROVENANCE_CHECKPOINT_20261120.md)

Local work to preserve includes the [supervisor](../../../localai/supervisor.py), [trusted Pipe](../../../localai/webui_pipe.py), [delivery client](../../../localai/delivery.py), [backup and file-restore tool](../../../dependencies/scripts/rp11_backup.py), [isolated startup rehearsal](../../../dependencies/scripts/rp11_restore_startup.py), and [wheel BOM generator](../../../dependencies/scripts/rp13_wheel_bom.py), plus the verification records above. Keep runtime state, private backups and credentials local. Review the working tree before any Git publication.

The [G1 service configuration](../../../localai/README.md) records the installed service arrangement using generic credential paths. The [versioned artifact inventory](../../../dependencies/manifests/r1-g1-20261120/artifact-inventory.json) preserves the precise wheel and archive hashes and points to the two portable candidate locks beside it.

## Recurring alignment review

After every three to five completed roadmap increments, rate your work against the guiding documents. Default to four increments. Use a natural checkpoint after three if available, and run the review by the fifth. Count only completed engineering increments since the last recorded review. Record each review and the last completed increment in the project evidence so the cadence depends on the roadmap record. Start this cadence from the current RP-13 checkpoint. Run the review during normal sequential work and continue afterward unless a material issue requires a decision. The trailing `wait` instruction takes precedence.

Read the applicable owner decisions, roadmap entries, and current verification records. Give an overall past and current rating out of 10 as engineering judgments. Use the table below and distinguish process alignment from release readiness. Cite evidence for material claims and say when a controlling document or independent verification is unavailable. Identify material deviations and any corrective action. Exclude the owner-managed local sudo password file from this project's rating.

| Area | Rating or status | What to assess |
| --- | --- | --- |
| Owner direction and scope | Out of 10 | Compliance with current owner decisions, release scope, roadmap dispositions, and change authority. |
| Verification and evidence | Out of 10 | What was exercised on the installed system, what the evidence proves, and what remains unverified. |
| Working discipline | Out of 10 | Sequential progress, useful diagnosis, proportional checks, checkpoints, and handling of real blockers. |
| Release gates | Open or met | Remaining or completed acceptance gates, including packaging, offline rehearsal, traceability, and owner acceptance where applicable. |

### RP-13 review baseline

The latest review rated overall alignment **8.5/10 over the project so far** and **9/10 at the RP-13 checkpoint**. Owner direction and scope scored 9/10, verification and evidence 8.5/10, and working discipline 8/10. The owner confirmed the intended use is private and directed that the local sudo password file be excluded from scoring. Working-discipline deductions reflected pauses after routine status checks, repeated tests without a changed condition, and retries after the privilege blocker was known. The review used the owner decisions, roadmap, and verification records in the checkout. The full Governance Standard v1.0 was unavailable for a clause-by-clause audit.

Release gates remain open. The same-laptop restore provides operational recovery evidence. The clean-host restore, comprehensive egress and backend-outage witness, full packaging and offline rehearsal, upgrade and rollback, requirement-to-evidence traceability, and formal FAT acceptance still need their applicable verification or recorded disposition.

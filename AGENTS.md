# Local AI Development startup handoff

Use this file once to orient Codex at the start of the Local AI Development recovery. The sections below summarize the context at the handoff commit `2f40cf0468848af18c17de73c8e7a73dc5a06485`. After orientation, use the governance standard, current owner decisions, and repository verification records directly for ongoing engineering direction and status. This file is a startup snapshot and should not be maintained as a project instruction file or progress log.

For the current continuation point, read the [RP-13 Codex handoff](verification/local_ai/20261116/LOCALAI_CODEX_HANDOFF_AFTER_G1_RP13_20261120.md).

## Engineering governance

- Follow the [Governance Standard v2.3](docs/governance/AI_Assisted_Software_Engineering_Governance_Standard_v2_3.odt) and use the [Roadmap Planning and Execution Guide v2.3](docs/governance/Software_Development_Roadmap_Planning_and_Execution_Guide_v2_3.odt) as its companion. Confirm active documents in the [current governance index](docs/governance/README.md). Treat earlier versions as historical. Put reliability and verification before speed. Verify each increment with evidence appropriate to the change and continue in the approved sequence unless a material engineering problem or owner decision requires a stop.
- Follow the owner-approved [42-increment FAT planning dispositions](verification/local_ai/20261116/OWNER_APPROVAL_R1_42_INCREMENT_DISPOSITIONS_AND_EARLY_INSTALL_SEQUENCE_20261119.md). Preserve traceability for all 42 increment identities, 136 requirement identities (104 R1, 17 R2, 15 R3), 19 interfaces, and 26 FAT oracles. Record installed FAT results only after actual execution.
- Apply the later [Bodhi 7 and in-place G1 owner decision](verification/local_ai/20261116/OWNER_APPROVAL_BODHI7_AND_G1_IN_PLACE_RP05_20261119.md) for host selection and authority. Keep candidate pins, tooling, bind choices, and exact G-R/G-A baselines at their documented approval and verification status.
- Keep GitHub PRs draft and unmerged unless the owner explicitly authorizes a status change or merge.

## Release 1 operating constraints

- Develop in place on the existing G1 environment on Bodhi Linux 7.0 (Ubuntu 22.04 Jammy, x86_64). Preserve and reuse the existing Bifrost OSS and Ollama services, configuration, and persistent data.
- Keep Docker administration root-restricted. Use `sudo` for scoped administrative inspection or operations and leave Docker group membership unchanged.
- Before modifying services or data or provisioning new packages, inspect the relevant current state and verify a recoverable local checkpoint of affected configuration and persistent data. Stop on material mismatches or unexpected destructive changes.
- Use local Ollama inference through Bifrost for Release 1, with hosted fallback and external application telemetry disabled. Paid external APIs are outside Release 1 scope.
- Keep secrets and private machine configuration out of tracked files and shared output. Keep credentials and sensitive checkpoint contents local and access-restricted.
- Avoid redundant installations, unnecessary hardening, and repeated mock testing. Retain prior successful Bifrost–Ollama integration tests as historical evidence. Repeat the full suite only when a specific change or observed regression justifies it. Use focused live verification for current readiness.

## RP-05 handoff

- Use the [verified inventory and handoff](verification/local_ai/20261116/RP05_G1_EXISTING_RUNTIME_INVENTORY_AND_NEW_CONVERSATION_HANDOFF_20261119.md) as historical host evidence and the [existing-G1 provisioning tool proposal](verification/local_ai/20261116/RP05_EXISTING_G1_PROVISIONING_TOOLS_CANDIDATE_20261119.md) as a candidate procedure. Review the scripts before use and record actual host results.
- Complete RP-05.INC-01 readiness before provisioning. Verify current gateway ownership, non-conflicting service bindings and distinct persistent directories, one current local inference request, a recoverable checkpoint, and candidate dependency locks with ABI, license, and offline closure.
- RP-05.INC-02 first provisions Open WebUI and the independently managed LangGraph supervisor alongside the existing Bifrost and Ollama services. RP-07 retains UI persistence verification, and RP-09 implements and verifies the functional delegated workflow.

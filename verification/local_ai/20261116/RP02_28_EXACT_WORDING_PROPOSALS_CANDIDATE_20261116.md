# RP-02 — 28 bounded exact-wording proposals (candidate)

**2026-11-16; G-R NOT APPROVED.** These are newly authored replacement **proposals**, not the original controlled statements, not an owner acceptance, and not an amendment to any historical artifact. They arose from independent consideration of the owner-provided ZIP (SHA-256 `9a48de5fa49420e470f003b7f3417277bd3aa2a6832a7b2c968d093004c2e37e`), original 136 exact SHA-verified statements, v3 quality review, and later approved three-release strategy. The local restricted `RP02_136_Exact_Wording_Decision_Local_Candidate_20261116.csv` contains original exact text, both statement hashes and review details; original bytes remain **outside** this public repository.

**Governance:** Preserve all 136 historical requirement IDs. The R1/R2 label in a historical ID is **not** a live release assignment; proposed allocations stay 104/17/15 until owner G-R authorization. Of the 136 exact originals, this increment proposes replacement wording for just 28. Every other row stays unrewritten, though some require release reclassification, shared verification witnesses, a FAT process record instead of a product requirement, or an explicit owner retirement decision. All 28 are NOT IMPLEMENTED/NOT RUN; exact acceptance tests are proposed, not accepted.

| Historical ID | Newly proposed replacement statement |
| --- | --- |
| LAI-R1-N001-01 | The application shall install and operate on a supported Bodhi Linux 7 AMD64 system without replacing the installed host operating system. |
| LAI-R1-N005-01 | For a user-initiated delegated workflow, the supervisor shall invoke at least two configured local specialist roles under the same task identifier. |
| LAI-R1-N005-03 | The supervisor shall produce a consolidated result using the successful specialist responses associated with an accepted delegated task. |
| LAI-R1-N006-03 | The supervisor shall mark the result of each failed specialist invocation as failed or unavailable and shall not present its output as a successful contribution. |
| LAI-R1-N008-02 | After a supported supervisor restart, the supervisor shall retrieve the last durably checkpointed task state and report a recoverable, completed, failed, or recovery-error disposition consistent with that state. |
| LAI-R1-N009-02 | For an explicitly authorized external inference request, the outbound-context controller shall transmit only fields in the authorized projection for that one request and selected provider/model. **(Proposed R2.)** |
| LAI-R1-N009-05 | Before transmitting content to an external inference provider, the outbound-context controller shall verify authorization for that request, provider/model, and field projection; absent authorization, it shall block transmission. **(Proposed R2.)** |
| LAI-R1-N010-01 | Retained operational request logs shall omit raw prompts, responses, secret values, and message content. |
| LAI-R1-N010-02 | The Release 1 application shall not transmit application telemetry to an external collection service. |
| LAI-R1-N010-03 | The application shall remove sanitized operational request and diagnostic metadata older than the approved 30-day retention interval, without treating conversation history and backups as operational metadata. |
| LAI-R1-N010-06 | The diagnostic export function shall exclude raw prompts, responses, and secret values from sanitized Release 1 diagnostic exports. |
| LAI-R1-N011-04 | The local gateway management API shall deny unauthenticated and unauthorized requests to read or modify protected configuration. |
| LAI-R1-N011-05 | Sanitized diagnostic records and exports shall not contain local virtual keys, passwords, or other credential secret values. |
| LAI-R1-N012-04 | For a Release 1 local-inference request, the gateway shall deny unauthorized model/provider routing rather than dispatch to an unrequested backend or any hosted provider. |
| LAI-R1-N014-01 | In Release 2, the gateway shall support independently usable operator-authorized OpenAI and Anthropic inference integrations. **(Proposed R2.)** |
| LAI-R1-N017-04 | The direct-chat and supervised inference clients shall use a documented Bifrost gateway interface so that neither client relies on Ollama-specific request handling. |
| LAI-R1-N017-05 | The deployed Release 1 configuration record shall identify the tested version of each required component and the configured interface endpoint used by that component. |
| LAI-R1-N018-05 | The tool executor shall reject a tool invocation derived from retrieved or model-generated text unless it satisfies the active task capability grant and input validation. |
| LAI-R1-N019-03 | The local health view shall distinguish a required service that is ready, unavailable, or providing degraded capability according to the documented service-specific checks. |
| LAI-R1-N020-05 | The restore procedure shall restore Bifrost gateway configuration and required gateway secret material from a compatible approved backup so the previously authorized local model route is usable. |
| LAI-R1-N021-04 | After a failed application upgrade, the rollback procedure shall restore the last validated service configuration and maintain access to previously accepted user-facing history and durable supervisor task state. |
| LAI-R1-N024-04 | Operational error records shall distinguish gateway authentication rejection, authorization rejection, local-backend connection failure, and local-backend timeout without reporting any as a successful completion. |
| LAI-R1-N024-05 | Sanitized diagnostic exports shall exclude local gateway credentials, application passwords, encryption secrets when present, and other configured authentication tokens. |
| LAI-R2-N025-02 | In Release 3, an explicitly authorized scheduled job shall be executable by the autonomous worker without a concurrent user-interface session. **(Proposed R3.)** |
| LAI-R2-N025-04 | After a supported Release 3 worker restart, each interrupted scheduled job shall enter the documented recovery, retry, failed, or completed state without silently reporting unperformed work as complete. **(Proposed R3.)** |
| LAI-R2-N026-04 | In Release 3, an accepted consequential-action approval shall remain associated with its exact job and action identifier through a supported worker restart. **(Proposed R3.)** |
| LAI-R2-N027-03 | In Release 3, the external-agent workflow adapter shall associate each delegated external agent invocation with its originating task identifier. **(Proposed R3.)** |
| LAI-R2-N027-05 | In Release 3, the external-agent adapter shall reject an incompatible protocol version, report the incompatibility, and preserve the prior committed workflow state. **(Proposed R3.)** |

## Required independent-review dispositions before G-R

1. **Product vs. verification evidence:** `LAI-R1-N001-04` and `LAI-R1-N023-05` are principally host-fact/FAT-gate records, not software capabilities. Preserve IDs and traceability; owner must authorize any move out of the product requirement baseline.
2. **Duplicate enforcement:** `LAI-R1-N011-06` and `LAI-R1-N018-01` express the same active tool-grant enforcement; one implementation/test is sufficient if both retained IDs trace to it. `LAI-R1-N002-05` and `LAI-R1-N017-01` identify one Open WebUI history owner; do not implement a second owner.
3. **Bifrost OSS licensing:** `LAI-R1-N022-05` optional proprietary-edition capability detection is not justified by the owner-approved OSS scope; candidate recommendation is **retire**, subject to explicit G-R owner authority, not silent deletion.
4. **Conditional scope:** `LAI-R1-N016-03` native tool-call transport is required only if a selected R1 workflow actually depends on that model protocol. R1 supervisor tools themselves remain required where the real workflow needs them.
5. **Backup:** `LAI-R1-N010-04` classification can remain useful; `LAI-R1-N020-03` Bifrost configuration/secret restoration remains relevant. Both must be evaluated under the owner’s **locally stored, access-controlled offline backup** direction; mandatory backup encryption was explicitly deferred. No speculative vault or key-management subsystem.
6. **Resource and packaging:** `LAI-R1-N023-04` measurement may share `N023-01` witness; `N023-02` should check the actual storage threshold, not require an elaborate planner; `.deb` plus complete offline dependency transport is already an accepted packaging method.
7. **Unchanged reviewed statements:** 108/136 exact originals were not given new words. Absence of rewriting is **not** a claim their acceptance criteria or implementation are validated. Each remains in the 136-ID disposition index.

**Outstanding:** independent wording-level second review, G-R authority, interface schema freeze G-A, source identity exception for missing Rev0.16 JSON, and actual first-article execution. Do not let any candidate wording silently supersede the preserved original.

## Focused candidate wording QA (same increment)

- **N005-03:** narrowed the proposed requirement to one obligation: synthesizing successful contributions. Missing/failed specialist coverage is separately covered by `LAI-R1-N006-02` and the distinct operational failure oracle; do not duplicate those outcomes here.
- **N010-06:** removed a loophole implying message-content diagnostic exports could be allowed by a general exception. For R1 **sanitized diagnostics**, prompts, responses and secrets are suppressed; the owner did not approve raw diagnostic export.
- These are refinements to unapproved candidate wording only; no original source text, owner decision or baseline has been changed.

# RP-14 G1 rehearsal and FAT gate

## RP-14.INC-01

The [candidate evidence trace](RP14_R1_ENGINEERING_EVIDENCE_TRACE_CANDIDATE_20261121.csv) contains one row per owner-assigned R1 requirement, in original release-assignment order. It identifies 18 engineering witnesses, 59 partial witnesses, nine pending applicability or retirement dispositions and 18 open rows. Every row remains pending FAT acceptance. The approved 104/17/15 allocation, 19 interface identities and 26 original oracle identities are preserved. The [release allocation decision](OWNER_DECISIONS_RP02_RP03_APPROVED_20261116.md) grants scope authority. Exact G-R wording, G-A interfaces and acceptance criteria remain pending controlled review.

## RP-14.INC-02

A disposable application-mount rehearsal used Python and wheel inputs from the [private offline transport](RP13_G1_PRIVATE_PACKAGE_TRANSPORT_AND_ROLLBACK_20261121.md). The existing RP-11 private backup and restore were reverified before startup. Open WebUI and LangGraph used offline-installed dependencies and the supervisor ran from the project Debian installation. Bifrost used the existing pinned local image with Docker pull disabled. The test network namespace had no external interfaces. Bifrost health, authenticated Open WebUI chat readback and matching LangGraph task readback passed. The rehearsal also checked that the live Bifrost container identity and running state stayed constant.

The startup rehearsal reused an installed Docker base and existing Bifrost image. It did not launch Ollama in the test namespace or repeat inference. The [RP-12 installed direct and delegated witnesses](RP12_G1_INTEGRATED_WORKLOAD_EVIDENCE_20261120.md) cover live local inference on G1. An end-to-end install and inference rehearsal from transport alone, independent clean-host restoration, comprehensive egress for live inference and a backend-outage witness remain open.

## RP-14.INC-03

Formal first-article testing and acceptance remain open. The [operational oracle candidates](RP04_R1_OPERATIONAL_FIRST_ARTICLE_ORACLES_CANDIDATE_20261116.md) require the approved requirements and interfaces as well as independent installed evidence. Engineering results are available for reuse. All original oracle execution statuses remain at `NOT_RUN`. The owner still needs a controlled G-R/G-A review and must resolve how to witness requirements calling for a clean supported target under the in-place G1 decision. Installed FAT requires independent review and recorded owner acceptance.

## FAT package entry point candidate

The owner requested that FAT start with their Debian package installation. Candidate `localai-home_0.1.0~g1.5_all.deb` has SHA-256 `6e47c4bd10dfdfa497abde104c8e1ff3debdc0f510f6b9e1e91389fa97f72c0a`. It installs `localai-stage-offline` alongside the project code. The staging command pins the companion transport by SHA-256, rejects mismatched input and requires application-mount staging. It builds both Python environments from hash-locked local wheels and performs dependency and supervisor CLI checks.

The exact candidate installed in a disposable dpkg database. The empty database required a dependency override. The host's Python 3 and tar packages were checked separately. The installed staging command rejected a mismatched archive, successfully staged both environments from the verified transport, and reported no broken requirements. The packaged restore tool then started both staged runtimes and the pinned preexisting Bifrost image in an isolated network namespace. Bifrost health, authenticated WebUI chat readback and matching LangGraph task readback passed. Approximately 13 GiB remained available on the application mount after staging, and root usage remained 74%.

The owner's live install is still pending. Existing G1 unit activation, checkpoint and live rollback must be verified at the FAT boundary. The package install and archive staging are explicit operations so service activation can be witnessed separately. [Installation entry point](../../../localai/README.md#fat-installation-on-existing-g1)

## Operator installation witness

The owner reported completing the first FAT step. The live G1 package database independently returned `install ok installed 0.1.0~g1.5` and `dpkg -V localai-home` produced no discrepancies. The installed command staged the paired offline archive on the application mount and reported no broken requirements in either environment. Root usage remained 74% and the application mount had 8.5 GiB free after staging.

Before activation, both existing user services reported active and both readiness endpoints returned HTTP 200. The running Bifrost reference and installed Ollama model digest matched the verified inventory. A fresh private G1 checkpoint passed backup-manifest verification for 14 entries. Live activation and restart were not performed during this step.

## Live packaged activation witness

After owner authorization, the activation preflight confirmed the expected package, staged transport receipt, active units, and no queued, running or cancelling delegated tasks or pending deliveries. The switch added one operator-only `90-localai-fat-package.conf` override per user unit. It changed the Open WebUI executable and the LangGraph interpreter and supervisor paths while preserving their existing launch arguments, data and ports. The prior units and runtimes were retained for rollback. The activation command was prepared to remove the new overrides and restart the prior commands if activation failed before readiness. Both restarted services returned HTTP 200, so the fallback was not used.

A fresh local request through Bifrost returned a completion from the pinned Ollama model. Separate authenticated live API reads verified that an existing saved WebUI conversation retained its delegated reply and the installed supervisor returned the matching completed task and result. The owner browser witness for a fresh direct chat and a fresh delegated reply on this installation remains pending. This record does not close formal FAT or update the original oracle statuses.

The owner reported completing the requested direct and delegated browser checks. Independent readback confirmed the latest delegated task was completed and marked delivered, and its result matched the reply saved in the originating WebUI conversation. The timing of the visible reply is covered by the owner browser report. This records the browser witness for the packaged G1 activation. Formal FAT acceptance remains open.

## Packaged G1 authorization and recovery checks

The active packaged installation returned HTTP 401 for a missing Bifrost virtual key and for an invalid key, HTTP 403 for a request for an absent model using the valid key, and HTTP 401 for an unauthenticated supervisor task lookup. These are service-response witnesses. Upstream dispatch counters were not collected.

Runtime environment readback verified the intended Open WebUI offline and telemetry settings and disabled LangSmith tracing in the supervisor. Both active units exposed an application-mount guard and operated with umask 0077. This was a configuration check with the mount available. It did not exercise a missing mount or capture egress. Point-in-time resident memory was 818,264 KiB for Open WebUI and 72,024 KiB for LangGraph. These samples do not establish workload peaks or supported thresholds.

The fresh preactivation checkpoint again passed 14-entry verification. The backup verifier rejected a disposable manifest that named a missing payload. The real checkpoint passed readback again afterward. This witness exercised manifest verification, while the earlier isolated restore provided positive recovered-data startup evidence.

Open decisions include controlled G-R/G-A and oracle review, disposition of the clean-target requirement under the in-place G1 policy, and independent FAT acceptance. Backend-outage and egress witnesses remain incomplete. The original oracle statuses have not been promoted.

## Owner direction for clean-target FAT

The owner selected a separate computer with a fresh Bodhi Linux 7 installation for the clean-target FAT and will prepare that computer. The existing G1 results remain engineering evidence. Run the clean installation and offline restore as distinct witnesses on the new target. Start with fresh application state for the installation and functional journeys, then use an access-controlled restore copy for the recovery witness. Preserve the existing G1 installation and private backup as the source of recovery evidence.

| Work for the fresh host | Candidate ingredients and remaining verification |
| --- | --- |
| Confirm target and storage | Bodhi 7 / Ubuntu 22.04 AMD64, an application filesystem at `/mnt/local-ai-storage` with write access for the staging operator, and measured available storage. The installed staging command requires at least 5 GiB free for Python staging alone. Additional space is needed for the transport, container data, Ollama runtime and model, and separate restore data. |
| Close host dependency transport | Capture the fresh host package inventory. Determine the exact missing offline Debian closure for Docker, containerd, runc and other prerequisites. G1's versions are reference observations and need compatibility verification on the fresh host. |
| Provision the four services | Reuse the verified Python, wheel, Bifrost image, Ollama runtime and model artifacts. Verify offline engine/image import, Ollama installation and model startup, new loopback service units, newly initialized local configuration and protected credentials, Pipe registration and launch order. The existing `localai-home` package automates Python staging and provides the glue code. Its G1 activation procedure relies on already configured services. |
| Run the witnessed fresh install | The owner starts with the project `.deb`. Use the verified offline inputs and record health, a fresh direct chat, a fresh delegated task with automatic delivery, saved-state readback and controlled failure/recovery. |
| Restore and review | Verify a protected checkpoint copy against its manifest on transfer. Restore and independently read WebUI and LangGraph data and verify the Bifrost route on the clean host. Review release evidence and the remaining G-R/G-A and oracle dispositions before formal acceptance. |

The next host-dependent inputs are the fresh machine's AMD64 and Bodhi release confirmation, root and application filesystem free space, and installed base package inventory. The fresh host has not yet been nominated or inspected. The original 26 oracle statuses remain `NOT_RUN`.

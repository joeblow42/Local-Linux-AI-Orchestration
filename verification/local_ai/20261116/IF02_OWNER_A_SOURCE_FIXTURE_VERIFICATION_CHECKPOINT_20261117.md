# IF-02 owner Alternative A — bounded source/fixture verification checkpoint
**Date:** 2026-11-17. **Status:** COMPLETED SOURCE + CANDIDATE DESIGN SELF-CONSISTENCY REVIEW; NOT A DEPLOYMENT TEST.  
**Parent checkpoint:** [RP-02 through RP-04 2026-11-16](./RP02_RP04_CONTINUATION_CHECKPOINT_20261116.md).  
**Starting verified PR HEAD:** `f9b8ac0adb99ae6b8f89c9905c06ae6bb420ca45`; subsequent commits record this work. GitHub is authoritative for final branch head. PR #1 remains **open/draft/unmerged**, base `main` at `46ec8e99eeb65627daa1b4296b1be32350282a67`.

## Owner approval and safeguards
- Owner explicitly approved **Alternative A**: one trusted delegated Open WebUI Pipe exposing operator-initiated text commands for task status and cancellation, backed by independently managed local LangGraph supervisor. Decision [LAI-OD-20261117-04](./OWNER_DECISION_IF02_TASK_CONTROL_A_APPROVED_20261117.md) committed `bf7e051b2338cf4f580dd2b549f6cccb10f495b8`.
- Approval was **interaction direction only**, not G-A HTTP/schema/status approval, G-R wording/acceptance approval or implementation permission. G1 data collection and runtime owner hold remains active.
- No source/production code or installed service modified. No mock external provider or paid API call. No Release 2/3 implementation. No merge.

## New engineering artifacts and inspection
| New source/evidence record | GitHub commit | Status |
| --- | --- | --- |
| [Owner decision IF-02 Alternative A](./OWNER_DECISION_IF02_TASK_CONTROL_A_APPROVED_20261117.md) | `bf7e051b2338cf4f580dd2b549f6cccb10f495b8` | OWNER DIRECTION APPROVED |
| [Candidate command/lifecycle fixture catalog](./IF02_TASK_COMMAND_AND_LIFECYCLE_FIXTURES_CANDIDATE_20261117.json) | `dca95dc9defb14a3a0142767c29c8a398e34c73a`, corrected in `4ab2ee528d37d193610e986a56f2b5f83090ebf5` | CANDIDATE NOT RUN |
| [Pure-stdlib Python fixture consistency checker](./verify_if02_candidate_fixtures.py) | `fecffc700d959d8c4be83ce0447b4a7181203469` | SOURCE STORED; PYTHON RUN NOT EXECUTED IN THIS SESSION |
| [Minimal IF-02 command and HTTP supervisor control contract](./RP03_IF02_TASK_COMMAND_HTTP_MINIMUM_CONTRACT_CANDIDATE_20261117.md) | `27ad62f5c1f6d9fcee061c0a31684d06cb981b80` | SOURCE-REVIEWED CANDIDATE; NOT G-A |

### Exact pinned-source finding
Read upstream Open WebUI `v0.12.5` at `f7ac7ee10962ddec0017f5c29b6740d9b9c5faca`, including [MessageInput.svelte](https://github.com/open-webui/open-webui/blob/f7ac7ee10962ddec0017f5c29b6740d9b9c5faca/src/lib/components/chat/MessageInput.svelte) and [SlashCommands.svelte](https://github.com/open-webui/open-webui/blob/f7ac7ee10962ddec0017f5c29b6740d9b9c5faca/src/lib/components/chat/MessageInput/Commands/SlashCommands.svelte). Frontend contains a slash command suggestion menu including builtin `/status`. Therefore *no assertion is made* that illustrative `/task status` reaches the Pipe unchanged. **Provisional more conservative input grammar** is `task status <id>` and `task cancel <id>` (no slash), with strict full-message matching and malformed reserved command rejection. Owner approved **text-command interaction**, not these exact bytes.

Existing pinned [Open WebUI functions.py](https://github.com/open-webui/open-webui/blob/f7ac7ee10962ddec0017f5c29b6740d9b9c5faca/backend/open_webui/functions.py) supports one selectable Pipe and optional injected metadata. LangGraph `1.2.19` source/checkpointer remains candidate, no deployed provider installed-version proof. UI `Stop` does **not** prove cancellation of supervisor task.

## Fixture self-consistency evidence — independently calculated
A separate JavaScript in-memory checker (not the Python reference checker, not the project Pipe) fetched the **exact committed JSON source** at commit `fecffc700d959d8c4be83ce0447b4a7181203469` and independently evaluated each case against the strict candidate grammar and cancellation transition model:
- **23/23** command classification cases matched proposed expected intent and task ID.
- **11/11** cancellation/status lifecycle cases matched proposed state, accepted-cancel flag and no-new-step result.
- **14/14** negative/recovery scenario **records validated for structure/provenance and NOT_RUN state**. No faults were injected or executed.
- All fixture IDs unique; owner/G-R/G-A/G1 status fields consistent. **No candidate-self-consistency errors.**
- Exact GitHub fixture blob: `8e312dfb9f7fe0d2c8220cd0e86e733ccd5836a0`; Python reference runner blob: `6f332e4b25f19543c33124f940d7e770431ec7ca`.

**Result naming:** `DESIGN_SELF_CONSISTENCY_PASS` for the checked candidate model **only**. The standalone Python runner was **not executed** because the container could not retrieve the GitHub file in this session; do not claim Python PASS. No Open WebUI frontend interaction, Pipe execution, LangGraph HTTP call, gateway request, cancellation race, checkpoint saver fault injection or installed-system FAT ran. Actual product oracle result remains **NOT RUN**.

## Materially unresolved before G-A or implementation
1. Verify non-slash command delivery through the **pinned actual WebUI frontend and selected Pipe** in an isolated fixture. The source finding establishes a slash-suggestion concern, **not a proven compatibility failure**.
2. Finalize syntax, operator/identity forwarding, HTTP status/cancel/result fields, durable task ID and state-version/ack semantics; confirm no model-generated text can initiate task controls.
3. Demonstrate cancel-before-terminal/after-terminal ordering, in-flight inference acceptance, idempotent submit retry, restart recovery, checkpoint saver corruption and UI reconnect behavior on a **separate isolated local fixture**, respecting G1 hold.
4. Resolve exact dependency lock and Bifrost OCI source/effective configuration identity through approved source material; target G1 test **only** after owner releases the hold.
5. Complete source-sensitive original 136 requirement G-R review and 19 interfaces G-A approval before baselines/implementation. Original recovery ZIP remains outside public GitHub; isolated Rev0.16 missing-JSON exception **remains CLOSED/NONBLOCKING**.
6. All **26 original oracle IDs** retain NOT RUN (18 unconditional R1, one conditional R1, six R2, one R3); 13 prior RP-04 new draft fixtures remain candidate. This increment's 23+11+14 are **supplemental oracle-model cases**, not additional original controlled IDs.

## Conversation safety and immediate next increment
Current conversation is safe for a further **source-only or separate fixture-only** increment. This checkpoint plus owner record and specs are persistent in GitHub; no new owner decision required for the next narrow verification step. Do not progress to G-A or target runtime without actual evidence and authority. Verify the actual exact PR HEAD before continuing; retain draft/unmerged.

# RP-12 existing G1 integrated workload evidence

The [live direct route](./RP06_RP08_EXISTING_G1_LIVE_WITNESS_20261120.md), [delegated browser journey](./RP09_G1_SUPERVISOR_CHECKPOINT_20261120.md), and [isolated restore](./RP11_G1_BACKUP_RESTORE_EVIDENCE_20261120.md) provide the three installed journey witnesses. The delegated reply appeared in the original browser conversation without refresh. Reuse the recorded absent-credential denials, running-task cancellation and mid-workflow recovery.

The authenticated gateway model list contained only provider-qualified Ollama entries. A request for an absent local model returned HTTP 403 without a model reply. A real direct gateway inference immediately afterward completed in 4.53 seconds. The separate representative delegated task acknowledged in 0.01 seconds and delivered in 36.29 seconds. The test read both saved message representations and saw the selected model resident in Ollama. The test chat was archived.

| Stage | Elapsed | Observed input/output tokens |
| --- | ---: | ---: |
| Analysis | 5.12 s | 37 / 28 |
| Review | 17.48 s | 69 / 125 |
| Synthesis | 11.41 s | 199 / 20 |

Thirteen samples during this task on the 12-thread Bodhi host recorded peak service memory of 673 MiB for Open WebUI, 52 MiB for LangGraph, and 3,446 MiB for Ollama. Minimum sampled host available memory was 7,788 MiB. The application mount had 27,502 MiB available. These measurements describe one workload and do not establish supported performance limits.

The missing-model test exercised gateway rejection and subsequent recovery. It did not stop Ollama or capture network egress. Bifrost memory was not independently sampled. This engineering evidence does not change original FAT oracle statuses or replace installed release acceptance.

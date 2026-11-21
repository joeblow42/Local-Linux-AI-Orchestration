# Local AI G1 service configuration

This records the installed service arrangement for the Bodhi 7 engineering environment. Use actual local paths when creating user units. Store credentials and persistent data outside the checkout. [G1 provisioning evidence](../verification/local_ai/20261116/RP05_INC02_G1_PROVISIONING_EVIDENCE_20261120.md)

The `localai-home` Debian package places the project Python files in `/usr/share/localai`. When using the package, launch the supervisor with the dedicated LangGraph interpreter and `/usr/share/localai/supervisor.py`. Register the Pipe from `/usr/share/localai/webui_pipe.py`. Run the backup and restore tools from the same directory. The package supplies code and documentation. The existing user units, credentials, runtime dependencies and data remain managed by the operator.

| Service | Launch and binding | Persistent data |
| --- | --- | --- |
| Open WebUI | User systemd unit `localai-open-webui.service`. Run the installed `open-webui serve --host 127.0.0.1 --port 3000`. | Private working directory for the signing-key file and a separate `DATA_DIR` for the application database and files. |
| LangGraph | User systemd unit `localai-langgraph.service`. Run `localai/supervisor.py` with the dedicated Python 3.12.14 environment. Listen on `127.0.0.1:8010`. | Private SQLite task, checkpoint, delivery and diagnostic store. Keep credential files private and outside Git. |
| Bifrost and Ollama | Reuse the existing G1 services on `127.0.0.1:8080` and `127.0.0.1:11434`, respectively. | Existing data and configuration remain with their original service owners. |

The WebUI unit uses `OFFLINE_MODE=true`, `DO_NOT_TRACK=true`, and `ANONYMIZED_TELEMETRY=false`. Configure only the local OpenAI-compatible connection at `http://127.0.0.1:8080/v1` with the existing Bifrost virtual key in `x-bf-vk`. Leave the direct Ollama connector disabled. Keep the default browser chat model's Built-in Tools disabled for the tested 4,096-token runtime configuration. Enable API keys for the approved operator credential and restrict them to `/api/v1/chats`.

Launch the supervisor with `LANGSMITH_TRACING=false` and `UMask=0077`. Set `--checkpoint-db`, `--gateway-key-file`, `--pipe-key-file`, and `--webui-key-file` to the private local files. Set `--model` to `ollama/qwen3:4b-instruct-2507-q4_K_M` for the recorded setup. Register [webui_pipe.py](./webui_pipe.py) in the Open WebUI Admin Panel as an enabled Function with ID `localai_delegated` and set its `PIPE_KEY_FILE` valve to the supervisor's pipe credential file. The valve contains a path. Confirm each key file is owner-readable only.

Check Open WebUI and LangGraph at their respective `/ready` endpoints. Use the recorded installed browser journey for acceptance evidence. Automatic delivery updates both the plain content and structured output, then publishes a live completion event. FUT-002 tracks the deferred atomic-update improvement. [RP-09 evidence](../verification/local_ai/20261116/RP09_G1_SUPERVISOR_CHECKPOINT_20261120.md)

Root-owned backup and restore bundles contain credentials and stay outside Git. See the [backup and restore evidence](../verification/local_ai/20261116/RP11_G1_BACKUP_RESTORE_EVIDENCE_20261120.md) and the versioned [backup tool](../dependencies/scripts/rp11_backup.py) and [isolated startup tool](../dependencies/scripts/rp11_restore_startup.py).

## FAT installation on existing G1

Start the witnessed installation with `sudo dpkg -i ./localai-home_<version>_all.deb`. This registers the package and installs its code, documentation and staging command.

As the operator, run `localai-stage-offline /path/to/localai-g1-private-dependencies.tar --stage-in /mnt/local-ai-storage/development`. Use the archive paired with the package. Staging checks its SHA-256, creates fresh Python environments from local wheels, checks their dependency closure and verifies that the packaged supervisor loads. Keep the reported staging directory in place so the virtual environments retain valid paths. The staging command does not start services or write to the operator's existing configuration, model store or databases.

The remaining FAT activation step must validate the existing G1 service and artifact identities, verify a recoverable checkpoint, and deliberately point the Open WebUI and supervisor user units at the staged runtimes. Keep the existing service launch arguments and environment settings. Use the packaged supervisor and check the two readiness endpoints. Retain the prior unit configuration and runtimes until the witnessed installed journeys and rollback checks are complete. Existing Bifrost and Ollama are reused under the owner-approved G1 scope.

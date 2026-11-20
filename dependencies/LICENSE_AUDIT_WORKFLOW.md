> **HISTORICAL WORKFLOW — SUPERSEDED FOR RELEASE 1 (2026-11-19).**
> The 2026-10-31 three-component lock instructions below are retained as historical candidate evidence only. They are **not** the active Release 1 preparation procedure. Later owner decisions select **Bifrost OSS instead of LiteLLM** and exclude paid external providers from R1. The active `dependencies/scripts/generate_locks.sh` now proposes **two Python lock inputs only** (`open-webui` and `langgraph`); Bifrost OCI and Ollama binary/artifact provenance are tracked separately. **Do not execute any acquisition, installation, service mutation, G1 inspection, or key/configuration change** on the authority of this historical document. Verify target host and approve the current dependency closure before acting. No baseline or license clearance is implied.

# License gate execution procedure — candidate, 2026-10-31

## Scope
Approved concept: one project-owned GPL-3.0 Debian package plus a distinct complete offline external-dependency ZIP. The ZIP is NOT yet licensed for redistribution.

## Step 1 — Lock
On the Bodhi host, from the repository checkout, run:
```bash
bash dependencies/scripts/generate_locks.sh
```
Each of the 3 lockfiles is written to `/mnt/local-ai-storage/development/dependencies/locks/`, outside the Git working tree. These are provisional until the offline artifact test. Re-resolving later may differ; lockfile SHA-256 is recorded.

## Step 2 — Acquire artifacts (subsequent approved increment)
Download distributions for each lock into an offline wheelhouse, including the selected Python 3.12.14 runtime and OS-level dependency closure. Preserve exact source, filename, SHA-256, license text and notices. Do NOT omit a selected required distribution to force license compatibility.

## Step 3 — Audit wheel metadata
After wheels have been acquired:
```bash
python3 dependencies/scripts/license_inventory.py /path/to/wheelhouse --output /path/to/license-inventory.csv
```
This inventory is an initial triage, not a license compatibility certification. Manually inspect embedded `LICENSE`, `NOTICE`, bundled native libraries, vendor assets, source distribution licenses, and upstream terms. Every missing/unusual license must be dispositioned.

## Specific gate holds
- Open WebUI 0.12.5: modified BSD branding terms; preserve native branding and assess combination vs separate-service licensing.
- LiteLLM 1.106.6 [proxy]: `litellm-enterprise` appears in full proxy resolution; investigate necessity and redistribution permission. Proxy extras metadata is insufficient to permit enterprise redistribution.
- All transitive dependencies: license clearance incomplete.

## Exit criteria
Immutable locked artifacts, complete provenance/SBOM, verified redistribution permissions and notices, successful fully offline clean installation and smoke tests, owner acceptance. Public redistribution blocked pending all items.

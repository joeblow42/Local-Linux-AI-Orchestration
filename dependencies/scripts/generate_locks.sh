#!/usr/bin/env bash
set -euo pipefail
# R1 candidate lock preparation only: no package install and no live service calls.
# Bifrost OSS and Ollama require separate image/binary provenance, not pip locks.
ROOT="${1:-/mnt/local-ai-storage/development}"
PY="${LOCALAI_PYTHON_BIN:-$ROOT/venvs/python/cpython-3.12.14-linux-x86_64-gnu/bin/python3.12}"
CACHE="$ROOT/build/uv-cache"
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
OUT="$ROOT/dependencies/locks"
test -x "$PY" || { echo "Candidate Python interpreter unavailable: $PY" >&2; exit 1; }
command -v uv >/dev/null 2>&1 || { echo 'uv not found' >&2; exit 1; }
mkdir -p "$OUT" "$CACHE"
for component in open-webui langgraph; do
  echo "Resolving R1 Python dependency: $component"
  opts=(--python "$PY" --python-platform x86_64-unknown-linux-gnu --generate-hashes --no-python-downloads --cache-dir "$CACHE")
  if [[ "$component" == "open-webui" ]]; then opts+=(--torch-backend cpu); fi
  uv pip compile "$REPO/dependencies/inputs/$component.in" "${opts[@]}" --output-file "$OUT/$component.lock.txt"
  sha256sum "$OUT/$component.lock.txt" > "$OUT/$component.lock.txt.sha256"
done
printf '%s\n' open-webui.lock.txt langgraph.lock.txt > "$OUT/RELEASE1_PYTHON_LOCK_ALLOWLIST.txt"
if [[ -f "$OUT/litellm-proxy.lock.txt" ]]; then
  echo 'Historical LiteLLM lock detected; excluded from R1 allowlist (not deleted).' >&2
fi
echo 'Candidate R1 Python locks generated. Bifrost/Ollama need separate provenance and offline closure.'

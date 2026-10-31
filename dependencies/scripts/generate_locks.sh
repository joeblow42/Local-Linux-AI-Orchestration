#!/usr/bin/env bash
set -euo pipefail
# Phase 0 Sprint A: lock per-service dependency graphs without installing distributions.
ROOT="${1:-/mnt/local-ai-storage/development}"
PY="$ROOT/venvs/python/cpython-3.12.14-linux-x86_64-gnu/bin/python3.12"
CACHE="$ROOT/build/uv-cache"
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
OUT="$ROOT/dependencies/locks"
mkdir -p "$OUT" "$CACHE"
test -x "$PY" || { echo "Python not found: $PY" >&2; exit 1; }
for component in open-webui langgraph litellm-proxy; do
  echo "Resolving $component"
  opts=(--python "$PY" --python-platform x86_64-unknown-linux-gnu --generate-hashes --no-python-downloads --cache-dir "$CACHE")
  if [[ "$component" == "open-webui" ]]; then opts+=(--torch-backend cpu); fi
  uv pip compile "$REPO/dependencies/inputs/$component.in" "${opts[@]}" --output-file "$OUT/$component.lock.txt"
  sha256sum "$OUT/$component.lock.txt" > "$OUT/$component.lock.txt.sha256"
done
echo "Lockfiles in $OUT; these are resolution evidence, NOT artifact-level clearance."

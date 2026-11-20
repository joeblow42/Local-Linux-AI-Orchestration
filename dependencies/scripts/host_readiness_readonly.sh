#!/usr/bin/env bash
# RP-05.INC-01: non-invasive host and storage readiness; no passwords required.
set -euo pipefail
if [[ "${1:-}" != "--confirm-non-g1" || $# -ne 1 ]]; then
  printf '%s\n' 'USAGE: bash host_readiness_readonly.sh --confirm-non-g1' \
    'Run ONLY on the selected non-G1 test host; do not run against held G1.' >&2
  exit 2
fi
store="${LOCALAI_STORAGE_PATH:-/mnt/local-ai-storage}"
if [[ "$store" != /* ]]; then
  echo 'INVALID_STORAGE_PATH: absolute path required' >&2; exit 2
fi
printf 'RP05_INC01_MODE=READ_ONLY_NON_G1\n'
printf 'HOST_ARCH=%s\n' "$(uname -m)"
printf 'KERNEL=%s\n' "$(uname -r)"
if [[ -r /etc/os-release ]]; then
  # /etc/os-release is the OS-provided metadata source.
  ( . /etc/os-release; printf 'OS_ID=%s\nOS_VERSION=%s\n' "${ID:-UNKNOWN}" "${VERSION_ID:-UNKNOWN}" )
else
  echo 'OS_ID=UNKNOWN'; echo 'OS_VERSION=UNKNOWN'
fi
for name in python3.12 python3 uv docker podman dpkg dpkg-deb systemctl findmnt; do
  if command -v "$name" >/dev/null 2>&1; then
    printf 'TOOL_%s=FOUND\n' "$name"
  else
    printf 'TOOL_%s=MISSING\n' "$name"
  fi
done
if command -v python3.12 >/dev/null 2>&1; then
  python3.12 --version 2>&1 | sed 's/^/PYTHON312_VERSION=/'
fi
bundled_python="${LOCALAI_PYTHON_BIN:-/mnt/local-ai-storage/development/venvs/python/cpython-3.12.14-linux-x86_64-gnu/bin/python3.12}"
if [[ -x "$bundled_python" ]]; then
  printf 'CANDIDATE_BUNDLED_PYTHON=FOUND\n'
  "$bundled_python" --version 2>&1 | sed 's/^/CANDIDATE_BUNDLED_PYTHON_VERSION=/'
else
  echo 'CANDIDATE_BUNDLED_PYTHON=NOT_FOUND'
fi
if [[ -r /proc/meminfo ]]; then
  awk '/^MemTotal:/{printf "RAM_TOTAL_KIB=%s\n",$2} /^SwapTotal:/{printf "SWAP_TOTAL_KIB=%s\n",$2}' /proc/meminfo
fi
printf 'LOGICAL_CPUS=%s\n' "$(getconf _NPROCESSORS_ONLN 2>/dev/null || echo UNKNOWN)"
if [[ -d "$store" ]]; then
  if command -v mountpoint >/dev/null 2>&1 && mountpoint -q -- "$store"; then
    echo 'STORAGE_EXACT_MOUNT=YES'
  else
    echo 'STORAGE_EXACT_MOUNT=NO_OR_UNKNOWN'
  fi
  if command -v df >/dev/null 2>&1; then
    df -B1 --output=avail -- "$store" | awk 'NR==2{printf "STORAGE_AVAILABLE_BYTES=%s\n",$1}'
  fi
else
  echo 'STORAGE_DIRECTORY=ABSENT'
fi
printf 'STATUS=COLLECTION_ONLY_NO_INSTALL_NO_CONFIGURATION\n'

#!/usr/bin/env bash
# RP-05.INC-01: existing G1 operator-run read-only inspection. No secrets printed.
set -euo pipefail
[[ $# -eq 1 && "$1" == '--existing-g1' ]] || { echo 'Usage: bash rp05_g1_readonly_gate.sh --existing-g1' >&2; exit 2; }
STORAGE=/mnt/local-ai-storage
DATA=/mnt/local-ai-storage/bifrost/g1/data
PY="$STORAGE/development/venvs/python/cpython-3.12.14-linux-x86_64-gnu/bin/python3.12"
sudo -v
rootcmd() { sudo -n "$@"; }
printf 'RP05_MODE=EXISTING_G1_READ_ONLY\n'
[[ $(uname -m) == x86_64 ]] || { echo 'STOP: architecture mismatch'; exit 1; }
mountpoint -q -- "$STORAGE" || { echo 'STOP: application mount absent'; exit 1; }
[[ -d "$DATA" && -x "$PY" ]] || { echo 'STOP: existing data or bundled interpreter absent'; exit 1; }
printf 'PYTHON_VERSION=%s\n' "$("$PY" --version 2>&1)"
printf 'UV_VERSION=%s\n' "$(uv --version 2>&1)"
printf 'STORAGE_AVAILABLE_BYTES=%s\n' "$(df -B1 --output=avail "$STORAGE" | awk 'NR==2{print $1}')"
printf 'G1_DATA_BYTES=%s\n' "$(rootcmd du -sb -- "$DATA" | awk '{print $1}')"
printf 'DOCKER_ROOT=%s\n' "$(rootcmd docker info --format '{{.DockerRootDir}}')"
info="$(rootcmd docker inspect --type container --format '{{.Name}}|{{.State.Running}}|{{if .State.Health}}{{.State.Health.Status}}{{else}}NONE{{end}}|{{.HostConfig.NetworkMode}}|{{.HostConfig.RestartPolicy.Name}}|{{.Image}}' bifrost-g1)" || { echo 'STOP: G1 inspect failed'; exit 1; }
IFS='|' read -r cname running health network restart imageid <<< "$info"
printf 'G1_CONTAINER=%s\nG1_RUNNING=%s\nG1_HEALTH=%s\nG1_NETWORK=%s\nG1_RESTART=%s\nG1_IMAGE_ID=%s\n' "$cname" "$running" "$health" "$network" "$restart" "$imageid"
[[ "$cname" == /bifrost-g1 && "$running" == true && "$health" == healthy && "$network" == host ]] || { echo 'STOP: G1 state differs'; exit 1; }
printf 'G1_IMAGE_REF=%s\n' "$(rootcmd docker inspect --type container --format '{{.Config.Image}}' bifrost-g1)"
mounts="$(rootcmd docker inspect --type container --format '{{range .Mounts}}{{println .Source "->" .Destination}}{{end}}' bifrost-g1)"
grep -Fxq "$DATA -> /app/data" <<< "$mounts" || { echo 'STOP: G1 bind mount differs'; exit 1; }
echo 'G1_MOUNT_MATCH=YES'
systemctl is-active --quiet ollama || { echo 'STOP: Ollama is not active'; exit 1; }
echo 'OLLAMA_SERVICE=active'
python3 - <<'PY'
import json, urllib.request
for endpoint, label in [('http://127.0.0.1:11434/api/version','OLLAMA_API_VERSION'),('http://127.0.0.1:11434/api/tags','OLLAMA_MODELS')]:
    try:
        with urllib.request.urlopen(endpoint,timeout=4) as response: data=json.load(response)
        if label=='OLLAMA_API_VERSION': print(f'{label}={data.get("version","UNKNOWN")}')
        else: print(f'{label}='+','.join(sorted(m.get('name','?') for m in data.get('models',[]))))
    except Exception as exc:
        print(f'{label}=NOT_AVAILABLE:{type(exc).__name__}')
        raise SystemExit(1)
PY
listeners="$(rootcmd ss -H -ltnp)"
echo 'PORT_OWNERS_BEGIN'
for port in 8080 11434 3000 8010; do
  found="$(awk -v p=":$port" '$4 ~ (p "$") {print}' <<< "$listeners")"
  if [[ -z "$found" ]]; then printf 'PORT_%s=FREE\n' "$port"; else
    printf 'PORT_%s=IN_USE\n' "$port"
    printf '%s\n' "$found"
  fi
done
echo 'PORT_OWNERS_END'
port8080="$(awk '$4 ~ /:8080$/ {print}' <<< "$listeners")"
pids="$(grep -oE 'pid=[0-9]+' <<< "$port8080" | cut -d= -f2 | sort -u || :)"
container_pids="$(rootcmd docker top bifrost-g1 -eo pid | sed '1d' | tr -d ' ' || :)"
match=NO
while IFS= read -r pid; do
  [[ -n "$pid" ]] || continue
  if grep -Fxq "$pid" <<< "$container_pids"; then match=YES; break; fi
done <<< "$pids"
printf 'GATEWAY_8080_PROCESS_IN_G1=%s\n' "$match"
[[ "$match" == YES ]] || { echo 'STOP: 8080 listener not demonstrated inside G1'; exit 1; }
[[ -z $(awk '$4 ~ /:3000$/ || $4 ~ /:8010$/ {print}' <<< "$listeners") ]] || { echo 'STOP: proposed service ports occupied'; exit 1; }
echo 'RP05_GATE=HOST_READINESS_PASS_INFERENCE_NOT_YET_ATTESTED'

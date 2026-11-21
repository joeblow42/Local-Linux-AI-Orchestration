# RP-05.INC-01 — Operator-provided read-only host preflight reconciliation

**Date:** 2026-11-19. **Status:** host baseline observation from operator's explicitly invoked non-G1 preflight; **not independently collected live**, not installation approval or G-R/G-A freeze. PR #1 retains draft/unmerged status; G1 owner hold remains.

## Evidence source

Operator executed the checked-in script `dependencies/scripts/host_readiness_readonly.sh --confirm-non-g1` from the verified `4ae5931a3222f262ce46d5158a6f73e1fa675e9b` source, with `sha256sum -c` reporting `/tmp/localai-rp05-preflight.sh: OK`. Results were directly supplied in conversation.

| Probe | Operator report | Interpretation |
| --- | --- | --- |
| Mode | `READ_ONLY_NON_G1`; status `COLLECTION_ONLY_NO_INSTALL_NO_CONFIGURATION` | No reported installation; operator opted into non-G1 read-only inspection |
| Architecture/kernel | `x86_64`; `6.2.0-26-generic` | AMD64 CPU architecture confirmed; kernel observed, not certified Bodhi-specific |
| OS ID/version | `ubuntu` `22.04` | Consistent with Ubuntu 22.04 base used by Bodhi 7 but **does not independently establish Bodhi 7 installation or live-USB state** |
| Interpreter | `python3.12` not on PATH; bundled `Python 3.12.14` executable present and runnable | Python candidate is available; PATH omission is not an installation blocker |
| Tools | `python3`, `uv`, `docker`, `dpkg`, `dpkg-deb`, `systemctl`, `findmnt` FOUND; `podman` MISSING | Basic preparation tools present; Podman not a requirement |
| Memory/swap/CPU | `32563648` KiB RAM, `33400828` KiB swap, 12 logical CPU | Capacity data observed; required resource acceptance/overhead still unmeasured |
| Storage | `STORAGE_EXACT_MOUNT=YES`; `32536731648` bytes available at nominated mount | Exact mount check passed. This **does not** establish sufficient complete package closure or isolation from held G1 data/services |

## Disposition

**RP-05.INC-01 advanced: operator's preflight source verified and host facts captured.** No package installation, lock generation, G1 access, key inspection, or target mutation was reported or done here.

The next lowest-risk required checks are (a) establish Bodhi 7 product identity and whether this is a live/persistent USB root environment, and (b) choose isolated app-data paths and nonconflicting test ports **without inspecting or changing G1 services**. Verify root/mount semantics before changes on a live USB overlay. Also establish an approved storage acceptance threshold from actual dependency closure rather than treating 32.5 GB as a guaranteed pass.

Use **one read-only terminal block**, avoiding further duplicate mock testing:
```bash
printf '%s\n' '=== Bodhi identity ==='
dpkg-query -W -f='${binary:Package} ${Version}\n' moksha 2>/dev/null || true
for f in /etc/bodhi-version /etc/bodhi-release /etc/lsb-release; do
  if [ -r "$f" ]; then
    printf 'FILE=%s\n' "$f"
    sed -n '1,12p' "$f"
  fi
done
printf '%s\n' '=== Root and app storage mounts (read-only) ==='
findmnt -no TARGET,SOURCE,FSTYPE /
findmnt -no TARGET,SOURCE,FSTYPE /mnt/local-ai-storage
printf '%s\n' '=== Relevant persistent storage directories (no content inspection) ==='
for d in /mnt/local-ai-storage/development /mnt/local-ai-storage/r1-test; do
  if [ -d "$d" ]; then
    printf 'PRESENT %s\n' "$d"
  else
    printf 'ABSENT %s\n' "$d"
  fi
done
```

Note: the `/etc/lsb-release` contents may say Ubuntu (which is not definitive); Moksha installation alone does not prove Bodhi release. A root mount reported as overlay warrants explicit persistence/storage assessment before any `.deb` changes. The proposed `r1-test` path is a **placeholder for isolation design**, not a committed deployment target.

**Owner approvals preserved:** 42 simplified planning dispositions approved; Open WebUI and LangGraph initial service provision at RP-05.INC-02; original 136/19/26 identifiers remain unchanged and FAT original oracles NOT_RUN; G-R/G-A approval pending; no G1 hold release or merge inferred.

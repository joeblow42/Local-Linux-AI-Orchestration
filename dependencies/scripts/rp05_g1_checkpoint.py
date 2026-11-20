#!/usr/bin/env python3
"""Create root-only, same-mount rollback checkpoint for existing G1.
No service stop/restart. This is not an offline RP-11 backup or restore test.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import shutil
import sqlite3
import stat
import subprocess
import sys
from urllib.parse import quote

ROOT = Path('/mnt/local-ai-storage')
DATA = ROOT / 'bifrost/g1/data'
CHECKPOINTS = ROOT / 'development/checkpoints'

def docker(args):
    return subprocess.run(['docker', *args], text=True, check=True, capture_output=True).stdout

def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

def sqlite_format(path):
    with open(path, 'rb') as f:
        return f.read(16) == b'SQLite format 3\x00'

def online_sqlite_copy(src, dst):
    uri = 'file:' + quote(str(src), safe='/') + '?mode=ro'
    with sqlite3.connect(uri, uri=True, timeout=15) as source:
        with sqlite3.connect(dst, timeout=15) as target:
            source.backup(target, pages=256, sleep=0.05)
            integrity = target.execute('PRAGMA quick_check').fetchone()[0]
            if integrity != 'ok':
                raise RuntimeError(f'SQLite quick_check failed: {src.name}')
    shutil.copystat(src, dst, follow_symlinks=False)
    os.chown(dst, src.stat().st_uid, src.stat().st_gid)

def safe_copy_data(source, dest):
    dbs = set()
    for parent, _, files in os.walk(source, followlinks=False):
        for name in files:
            path = Path(parent) / name
            if path.is_file() and not path.is_symlink() and sqlite_format(path):
                dbs.add(path)
    copied, sqlite_count = 0, 0
    for parent, dirs, files in os.walk(source, followlinks=False):
        p = Path(parent)
        out = dest / p.relative_to(source)
        out.mkdir(parents=True, exist_ok=True, mode=0o700)
        shutil.copystat(p, out, follow_symlinks=False)
        os.chown(out, p.stat().st_uid, p.stat().st_gid)
        for name in dirs[:]:
            f = p / name
            if f.is_symlink():
                (out / name).symlink_to(os.readlink(f))
                dirs.remove(name)
        for name in files:
            src = p / name
            dst = out / name
            if src.is_symlink():
                dst.symlink_to(os.readlink(src))
                continue
            if not stat.S_ISREG(src.stat().st_mode):
                raise RuntimeError(f'Unsupported special file: {src.relative_to(source)}')
            if name.endswith(('-wal', '-shm')) and (src.with_name(name.rsplit('-', 1)[0]) in dbs):
                continue  # Online SQLite backup includes committed WAL transactions.
            if src in dbs:
                online_sqlite_copy(src, dst)
                sqlite_count += 1
            else:
                if name.endswith(('.sqlite', '.sqlite3', '.db', '.db3')):
                    raise RuntimeError(f'Unrecognized database-like file: {src.relative_to(source)}')
                shutil.copy2(src, dst, follow_symlinks=False)
                os.chown(dst, src.stat().st_uid, src.stat().st_gid)
            copied += 1
    return copied, sqlite_count

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--create', action='store_true', required=True)
    p.parse_args()
    os.umask(0o077)
    if os.geteuid() != 0:
        raise RuntimeError('Run with sudo; checkpoint contains credentials')
    if not ROOT.is_mount() or not DATA.is_dir():
        raise RuntimeError('Expected G1 application mount or data directory absent')
    inspect = json.loads(docker(['inspect', '--type', 'container', 'bifrost-g1']))[0]
    if not inspect.get('State', {}).get('Running'):
        raise RuntimeError('G1 is not running; reconcile before checkpoint')
    if not any(m.get('Source') == str(DATA) and m.get('Destination') == '/app/data'
               for m in inspect.get('Mounts', [])):
        raise RuntimeError('G1 data mount does not match the handoff')
    total = sum((Path(parent) / name).stat().st_size
                for parent, _, names in os.walk(DATA)
                for name in names if not (Path(parent) / name).is_symlink())
    CHECKPOINTS.mkdir(parents=True, exist_ok=True, mode=0o700)
    os.chmod(CHECKPOINTS, 0o700)
    free = shutil.disk_usage(CHECKPOINTS).free
    if total >= free:
        raise RuntimeError(f'Insufficient free space for checkpoint: source={total}, free={free}')
    label = 'rp05-g1-' + dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    dest = CHECKPOINTS / label
    dest.mkdir(mode=0o700)
    try:
        info_file = dest / 'bifrost-g1-inspect.private.json'
        info_file.write_text(json.dumps(inspect, indent=2) + '\n', encoding='utf-8')
        os.chmod(info_file, 0o600)
        snap = dest / 'data'
        copied, db_count = safe_copy_data(DATA, snap)
        entries = []
        for parent, _, names in os.walk(snap):
            for name in sorted(names):
                path = Path(parent) / name
                if path.is_symlink():
                    entries.append({'path': str(path.relative_to(dest)), 'symlink': os.readlink(path)})
                else:
                    entries.append({
                        'path': str(path.relative_to(dest)),
                        'sha256': sha256(path), 'size': path.stat().st_size,
                        'uid': path.stat().st_uid, 'gid': path.stat().st_gid,
                        'mode': oct(stat.S_IMODE(path.stat().st_mode))
                    })
        entries.append({'path': info_file.name, 'sha256': sha256(info_file), 'size': info_file.stat().st_size})
        manifest = {
            'kind': 'RP05_EXISTING_G1_ONLINE_ROLLBACK_COPY',
            'note': 'Root-only on same mount; not RP11 offline backup or independent restore.',
            'created_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
            'source': str(DATA), 'component': 'bifrost-g1',
            'files_copied': copied, 'sqlite_databases_online_backed_up': db_count,
            'files': entries
        }
        manifest_file = dest / 'manifest.private.json'
        manifest_file.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
        os.chmod(manifest_file, 0o600)
        for row in entries:
            if 'sha256' in row and sha256(dest / row['path']) != row['sha256']:
                raise RuntimeError('Checkpoint readback hash mismatch')
        print('CHECKPOINT_RESULT=CREATED_AND_READBACK_VERIFIED')
        print('CHECKPOINT_LOCATION=' + str(dest))
        print('CHECKPOINT_SQLITE_DATABASES=' + str(db_count))
        print('CHECKPOINT_FILES=' + str(copied))
        print('CHECKPOINT_LIMIT=LOCAL_SAME_MOUNT_NO_RESTORE_TEST')
    except Exception:
        print('CHECKPOINT_RESULT=FAILED_PARTIAL_DIRECTORY_REQUIRES_REVIEW', file=sys.stderr)
        print('PARTIAL_CHECKPOINT_LOCATION=' + str(dest), file=sys.stderr)
        raise

if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, subprocess.CalledProcessError, OSError, sqlite3.Error) as exc:
        print('STOP: ' + str(exc), file=sys.stderr)
        sys.exit(1)

#!/usr/bin/env bash
# Build the project-owned package without provisioning services or dependencies.
set -euo pipefail

if [[ $# != 2 || ! -d "$2" ]]; then
    echo "Usage: $0 DEBIAN_VERSION EXISTING_OUTPUT_DIRECTORY" >&2
    exit 2
fi

version=$1
if ! dpkg --validate-version "$version" || [[ ! $version =~ ^[0-9][0-9A-Za-z.+~-]*$ ]]; then
    echo "Expected a Debian package version without an epoch" >&2
    exit 2
fi

repo=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)
output=$(cd -- "$2" && pwd)
stage=$(mktemp -d "$output/.localai-deb.XXXXXXXX")
trap 'rm -rf -- "$stage"' EXIT
tree="$stage/package"
artifact="localai-home_${version}_all.deb"

install -d -m 0755 "$tree/DEBIAN" "$tree/usr/bin" "$tree/usr/share/localai" "$tree/usr/share/doc/localai-home"
install -m 0644 "$repo/localai/"{supervisor,delivery,webui_pipe}.py "$tree/usr/share/localai/"
install -m 0755 "$repo/localai/stage_offline.py" "$tree/usr/share/localai/"
ln -s ../share/localai/stage_offline.py "$tree/usr/bin/localai-stage-offline"
install -m 0644 "$repo/dependencies/scripts/"{rp05_g1_checkpoint,rp11_backup,rp11_restore_startup}.py \
    "$tree/usr/share/localai/"
install -m 0644 "$repo/localai/README.md" "$tree/usr/share/doc/localai-home/README.md"
install -m 0644 "$repo/LICENSE" "$tree/usr/share/doc/localai-home/copyright"
cat > "$tree/DEBIAN/control" <<CONTROL
Package: localai-home
Version: $version
Architecture: all
Maintainer: Local AI Development
Section: utils
Priority: optional
Depends: python3 (>= 3.10), tar
Description: Local AI supervisor and trusted Open WebUI Pipe for home use
 Includes the independent supervisor, delivery client, trusted Pipe source,
 and G1 backup and restore tools. Requires the separately provisioned
 Bodhi 7 AMD64 local runtime documented in README.md.
CONTROL
chmod 0644 "$tree/DEBIAN/control"
dpkg-deb --root-owner-group --build "$tree" "$stage/$artifact"
# Publish the finished package atomically without replacing an existing build.
ln -T -- "$stage/$artifact" "$output/$artifact"

# RP-13 private G1 package, transport and rollback

This record follows the [private-use provenance review](RP13_G1_PROVENANCE_FOLLOWUP_20261120.md) and the [owner's in-place G1 decision](OWNER_APPROVAL_BODHI7_AND_G1_IN_PLACE_RP05_20261119.md). The rehearsal used disposable directories on the Bodhi 7 AMD64 G1 host. The live application services and their data were not changed.

## RP-13.INC-02

The [Debian builder](../../../dependencies/scripts/rp13_build_deb.sh) produced `localai-home_0.1.0~g1.1_all.deb`. The package owns project code and documentation only. The dependencies travel in a separate private archive. `dpkg` installed the package in a disposable package database and the installed supervisor source matched the build input.

The private dependency tar includes the pinned Python, Ollama and Bifrost distributions, verified Ollama model closure, all 283 wheels, both locks, the artifact inventory and notice material. All 304 payloads matched the embedded checksum manifest on readback. The model tar independently matched the wrapper manifest, registry manifest, config and four content layer digests.

- Transport SHA-256 `db384cde5a107740d3f8dc0cdfb7e87f1e6e0f84cd3480b20e09d87b37c9d413`.
- The two Python environments were created with the Python distribution extracted from the transport. Offline sync with the archived wheels and locks used `--offline --no-index --no-build --require-hashes`. Dependency checks passed for 41 LangGraph packages and 242 Open WebUI packages. The installed supervisor CLI loaded with the rebuilt LangGraph environment.
- The private transport assumes the approved existing G1 base, including the host Docker engine, containerd and system service tooling. The base system package closure, full offline service bring-up, and public redistribution remain open. This witness did not load a new image into live Docker or change the model store.
- The initial rehearsal used root-backed temporary space. The verified transport and rehearsal data were moved to the application mount after root filesystem pressure surfaced. Future large staging uses that mount. Moved virtual environments retain original absolute paths and should be recreated from the wheelhouse when needed.

## RP-13.INC-03

On the application mount, a new offline LangGraph environment exercised the packaged supervisor against a disposable SQLite database. The first package created and cancelled a task. The same task ID remained readable with the cancelled state after installing `0.1.0~g1.2` over `0.1.0~g1.1` and downgrading to `0.1.0~g1.1`. The wrong actor was denied readback at all three stages. The documentation update did not migrate the database. This is evidence for the tested compatible version pair and the project-owned package boundary. Storage migration, interrupted upgrade recovery and live service rollback were outside this rehearsal.

| Package | SHA-256 |
| --- | --- |
| `localai-home_0.1.0~g1.1_all.deb` | `2bd63447bf859ba43ff4ccf0f9d6ecfc82cb49d69cb47926cd8472de1776e84d` |
| `localai-home_0.1.0~g1.2_all.deb` | `a290548ff93a8c10492de2ddbd922e5a8e925b73e04299038f5dcbd2e86307fc` |

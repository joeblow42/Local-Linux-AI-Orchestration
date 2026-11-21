# RP-13 G1 provenance follow-up

The [committed checkpoint](RP13_G1_ARTIFACT_PROVENANCE_CHECKPOINT_20261120.md) remains the baseline. All four saved artifacts identified by hash in the [versioned inventory](../../../dependencies/manifests/r1-g1-20261120/artifact-inventory.json) passed SHA-256 readback. This review uses the owner's private home-use scope. The public redistribution review remains open.

## Wheel notices

Six additional same-version upstream source notices were retrieved and hashed. These supplement the embedded and source-distribution notices already recorded. The hashes identify the retrieved texts. Native and vendored components still require their own coverage before redistribution.

| Source notice | SHA-256 |
| --- | --- |
| [CTranslate2 4.8.4](https://github.com/OpenNMT/CTranslate2/blob/v4.8.4/LICENSE) | `54aa79d9fe3c09e67a16dcd95b9e88676405a6ec174efda31036983cf7672ecb` |
| [FlatBuffers 25.12.19](https://github.com/google/flatbuffers/blob/v25.12.19/LICENSE) | `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30` |
| [LangChain Core 1.4.8](https://github.com/langchain-ai/langchain/blob/langchain-core==1.4.8/LICENSE) | `4ec67e4ca6e6721dba849b2ca82261597c86a61ee214bbf21416006b7b2d0478` |
| [LangChain Text Splitters 1.1.2](https://github.com/langchain-ai/langchain/blob/langchain-text-splitters==1.1.2/LICENSE) | `4ec67e4ca6e6721dba849b2ca82261597c86a61ee214bbf21416006b7b2d0478` |
| [Loguru 0.7.3](https://github.com/Delgan/loguru/blob/0.7.3/LICENSE) | `b35d026cc7aca9d5859a02eb87ddf7a386a24c986838651bd1f283f94e003327` |
| [sqlite-vec 0.1.9 MIT](https://github.com/asg017/sqlite-vec/blob/v0.1.9/LICENSE-MIT) | `6ce72bbe12d975bd5286e5ab0a064c069693300c47bccbc57bec18485f1621ea` |
| [sqlite-vec 0.1.9 Apache](https://github.com/asg017/sqlite-vec/blob/v0.1.9/LICENSE-APACHE) | `a38070a94d4afd9cd710e3ce67bd1de78097cfe1784c1f0109ac95d3c196bfdc` |

Starlette Compress 1.7.1 declares 0BSD. The local wheel hash matches the subject of PyPI's publishing attestation. The wheel, same-version sdist and the published source tree at commit `2f77508c7dd5ca538e21bc673123f81bcc281a8a` supplied no separately named license file. The release metadata and attestation are the available evidence. [Published release and attestation](https://pypi.org/project/starlette-compress/1.7.1/)

## Distribution artifacts

- **Bifrost.** The checked image has Alpine 3.23.7 as its later package database. The database enumerates 18 packages and records GPL, LGPL, MPL, MIT, BSD, Apache and zlib declarations. Representative copyleft components include BusyBox 1.37.0-r30, apk-tools 3.0.8-r0 and libgcc 15.2.0-r2. The layer scan found package records and no conventional license or copyright paths. The Go application revision remains unknown. Public distribution requires a complete image notice and corresponding-source review, including the Go dependencies and Alpine components.
- **Ollama.** The saved Linux AMD64 archive hashes to `c9490e0f520be21271d969e6703f012268b1d39f8b70dd58854e5bfef7a75bb6`. Its `bin/ollama` hash matches the previously hashed installed executable. The archive lists 11 notices under `lib/ollama`, covering cpp-httplib, DLPack, fmt, Go, llama.cpp, its vendored components, MLX, MLX-C, PicoJSON and XGrammar. The retrieved version-tagged application license hashes to `5934ed2ce0d15154bcdb9c85203210abac0da4314af34081e36df4599f90b226`. The installed library tree and full distribution notice coverage remain unverified. [Ollama v0.40.13 application license](https://github.com/ollama/ollama/blob/v0.40.13/LICENSE)
- **Model.** G1 Ollama returned `0edcdef34593eac1aa2be9c7d06c432dcf81945adca5eca2f27662c18f168ba0` for `qwen3:4b-instruct-2507-q4_K_M`. The downloaded registry manifest matches that digest. The manifest records the 2,497,280,480-byte weights layer as `sha256:85e4a5b7b8ef0e48af0e8658f5aaab9c2324c76c1641493f4d1e25fce54b18b9`. The Apache 2.0 license returned by the local API hashes to the manifest's license-layer digest `d18a5cc71b84bc4af394a31116bd3932b42241de70c77d2b76d69a314ec8aa12`. The offline copy still needs local readback of the model blobs. [Ollama registry entry](https://ollama.com/library/qwen3:4b-instruct-2507-q4_K_M) · [Qwen upstream license](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/cdbee75f17c01a7cc42f958dc650907174af0554/LICENSE)
- **Python.** The checked-in inventory's executable hash and the installed `libpython3.12.so.1.0` hash both match the standard x86-64 stripped install-only CPython 3.12.14 archive from build 20260929. The archive passed the published SHA-256 check (`ef605200f8174e87ecfc308e52a88127543f85dd5c940dc5e92cab244b98a003`). The unstripped archive and x86-64-v2 stripped archive have different executable and library hashes. The installation includes the CPython license and the matching distribution carries pip vendor notices. A complete review of native dependency notices and any corresponding-source obligations remains open for redistribution. [Build release](https://github.com/astral-sh/python-build-standalone/releases/tag/20260929) · [Distribution licensing documentation](https://github.com/astral-sh/python-build-standalone/blob/main/docs/running.rst#licensing)

A scoped read of the model store verified all five config and content blobs against the upstream manifest. The on-disk Ollama wrapper manifest has hash `6214d088d3846e16c9fe00adcbabdbfddc61ce4a70daacc46cb2310c38603054`. It additionally references the original registry manifest as a sixth layer. Preserve both manifest identities when transporting the model.

RP-13.INC-01 private-use provenance review is recorded. The open notice and source items apply to redistribution. The project has not approved a public dependency transport.

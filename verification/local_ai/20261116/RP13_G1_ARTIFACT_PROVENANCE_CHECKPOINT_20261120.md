# RP-13 Release 1 artifact provenance checkpoint

The exact installed wheel sets contain 283 files across both environments, deduplicated to 253 artifacts by SHA-256. The local BOM records component, filename, hash, package license metadata, project links and vendored metadata. Its notice archive contains 414 embedded files, and both artifacts passed checksum readback. Ten wheels had no recognized embedded notice. Hash-checked same-version source distributions supplied notices for primp, SentencePiece and tokenizers. The remaining gaps include sources whose distributions or precise tagged license paths were unavailable during this check.

The installed Bifrost OCI image was exported locally by its digest and the archive passed SHA-256 readback. The OCI index retains the Docker Hub source and digest, and the image is AMD64. The exported Docker manifest has no repo tag. The image has no OCI version or revision label. The embedded Go build information identifies the Bifrost HTTP transport, marks its own module `(devel)`, and provides no recorded source revision. That identifies the deployed artifact and its source family. It does not tie it to the earlier source candidate or provide a complete image-level license inventory.

The owner expects the exact revision to be unrecoverable. Use the verified OCI digest and export checksum to identify the deployed image. Retain the source revision as unknown and leave any source provenance required for redistribution open.

The installed Ollama executable and bundled Python executable were hashed independently. That evidence does not cover their full binary distributions, bundled native components or the installed model provenance. Open WebUI keeps upstream branding and is packaged separately from project-owned code.

Public redistribution review and the complete offline transport build remain open. This checkpoint did not install or change any running service.

The [versioned artifact inventory](../../../dependencies/manifests/r1-g1-20261120/artifact-inventory.json) preserves the unique wheel identities, license metadata, source-notice results, and SHA-256 receipts for local artifacts. The two candidate locks beside it omit only the generated comments that contained host paths. The inventory records both original and tracked lock hashes.

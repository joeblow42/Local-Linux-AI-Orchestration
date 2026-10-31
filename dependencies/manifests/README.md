# Frozen external dependency baseline

The project will acquire one complete offline dependency ZIP per approved baseline, containing pinned external primary components and their transitive installation artifacts for the explicitly supported operating environment.

The ZIP must remain outside ordinary Git history. Git tracks the manifest, SHA-256 file hashes, source/version/license records, supported environment, dependency-resolution procedure, and explicit baseline revision.

Baseline artifact fields: component, artifact filename, version, source URL, license identifier, SHA-256, artifact type, runtime ABI/platform, dependency parent, acquisition date UTC, baseline ID, verification status.

No external dependency baseline is approved until an offline clean-install dependency-closure test has passed. An archive update requires a reason, a new revision and regression verification. Until host facts are collected, do not declare Ubuntu/Python/ABI compatibility or offline closure.

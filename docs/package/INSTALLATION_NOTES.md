**A complete, automated setup is a reasonable expectation for Release 1.** The operator should be able to run one documented install command on a supported fresh Bodhi 7 laptop, make a few choices only they can make, and end up with a working direct chat and delegated workflow. That’s an installer design choice for the existing Release 1 scope. It doesn’t add a separate FAT requirement.

### What a `.deb` and APT can do

A **`.deb`** can install files, declare dependencies, and run configuration scripts. It could technically do most of the setup you listed. The tradeoff is recovery. Debian can rerun those scripts after an interrupted install, during upgrades, or without an interactive terminal. Configuring storage, importing multi-gigabyte artifacts, and creating an Open WebUI account inside those scripts makes failures harder to diagnose and resume. [Debian maintainer script guidance](https://www.debian.org/doc/debian-policy/ch-maintainerscripts.html)

**`apt install ./localai-home.deb`** installs the same `.deb` format. APT can resolve dependencies such as Docker, containerd, and runc when the required packages are available to it. For an offline install, we would supply those packages and their dependency metadata on the install media and configure the install to use that local source. APT handles the Debian package dependencies. Local AI still needs setup logic to load the model, configure the services, and register the Pipe. [Ubuntu offline APT documentation](https://manpages.ubuntu.com/manpages/jammy/man8/apt-offline.8.html)

### What I’d aim for on the new laptop

**One offline bundle and one operator-facing install command.** That command would coordinate APT, the Local AI `.deb`, and the application setup. It would:

1. Verify the OS, architecture, application mount, free space, and artifact checksums before making changes.
2. Install Docker and its dependencies offline while keeping Docker administration root-restricted.
3. Load and configure Bifrost, install Ollama, and load the verified model.
4. Set up Open WebUI and LangGraph, configure loopback services and persistent storage, and register the delegated Pipe.
5. Verify service readiness and tell you exactly where to open WebUI and issue your first direct and delegated requests.

You’d still choose the target storage and establish the initial Open WebUI administrator account or credentials. The installer should guide you through those choices without asking you to edit service files or copy secrets between applications. If setup fails partway, it should say which step failed and let you retry safely.

**Where we are today:** the existing `.deb` installs the glue code and provides verified offline Python staging. The G1 installation reused Docker, Bifrost, Ollama, and existing application configuration. The fresh-host dependency bundle and provisioning steps are the remaining work. A self-contained, multi-gigabyte `.deb` is possible, but a small `.deb` shipped with an offline bundle gives you the same one-command experience and lets us replace or retry individual pieces more easily.

## Subsequent decisions and draft notes

- The owner selected a small `.deb` and companion offline bundle. Installation automation and documentation serve the existing Release 1 scope and FAT. The editable final guide is ODT. This running Markdown file tracks decisions and verification gaps.
- Evaluate rootless Docker on the fresh host for an unprivileged runtime account. The opening response describes the tested G1 arrangement. The existing G1 rootful Docker daemon and its socket access remain under the prior owner decision. Verify user namespaces, `uidmap`, subordinate IDs, user systemd startup, container storage and bind ownership, loopback networking and backup/restore with the exact offline Docker packages. OS package installation and provisioning system-wide settings may still require limited administrator access. [Docker rootless prerequisites](https://docs.docker.com/engine/security/rootless/)
- Add read-only preflight coverage for package and bundle readability by the installer account, expected checksums and version pairing, offline Debian dependency closure, package-manager availability, supported host architecture and OS, writable and executable application storage as the runtime account, free bytes and inodes for peak staging on both filesystems, local port conflicts, existing installations and upgrade-vs-fresh intent, and service-account readiness. Measure requirements on the clean target before declaring supported thresholds.
- [Draft fresh install guide](README_freshinstall.odt). Use screenshots only when they clarify a verified WebUI action. Keep commands editable in monospace text and leave credentials out of examples and screenshots. Word for Microsoft 365 desktop on Windows can open and save ODT. Check layout after round-tripping because formatting can change. [Microsoft ODT support](https://support.microsoft.com/en-us/word/use-word-to-open-or-save-a-document-in-the-opendocument-text-odt-format)
- [Clean-target plan and current FAT evidence](../../verification/local_ai/20261116/RP14_G1_REHEARSAL_AND_FAT_GATE_20261121.md). The current package and archive support staged G1 deployment. The fresh-host offline Docker closure, automated service initialization and operator-facing install entry point still need implementation and verification.

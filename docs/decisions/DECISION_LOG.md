# Architecture and delivery decision register

| ID | Decision | Status | Source |
|---|---|---|---|
| ARCH-001 | Open WebUI, LangGraph and LiteLLM are the initial modular foundation | Accepted conceptual baseline | Owner architecture discussions |
| ARCH-002 | Open WebUI has direct LiteLLM model route **and** independent LangGraph supervisor route | Accepted | Owner decision, 2026-10-31 |
| ARCH-003 | LangGraph supervisor is an independently executable service with stable task IDs and persistent state design | Accepted architecture direction | Owner-approved roadmap |
| DIST-001 | One primary project-owned Debian package; external primary components remain outside it | Accepted | Owner decision, 2026-10-31 |
| DIST-002 | Maintain an offline dependency ZIP including complete transitive installation closure for the supported environment | Accepted A/A baseline | Owner decision, 2026-10-31 |
| DIST-003 | Distribution uses the primary Debian package plus offline dependency archive / documented provisioning mechanism | Accepted A/A baseline | Owner decision, 2026-10-31 |
| REQ-STYLE-001 | Apply requirements-writing guidance without repeated attribution in everyday project text | Accepted | Owner clarification, 2026-10-31 |

Evidence-dependent items remain open: host OS/ABI inventory, Python/runtime compatibility, offline artifact closure, licenses, archive size and provisioner choice.

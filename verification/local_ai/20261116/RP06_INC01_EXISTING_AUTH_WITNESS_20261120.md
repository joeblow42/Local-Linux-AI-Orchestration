# RP-06.INC-01 existing authentication witness

**Date:** 2026-11-20. **Scope:** simplified Release 1 authentication on existing G1.

- A loopback request for the Open WebUI session identity without a session returned HTTP 401. A read-only account count found one administrator. The operator previously verified a working signed-in chat session.
- A loopback Bifrost chat-completion request for the installed Ollama model without a virtual key returned HTTP 401. The earlier authenticated gateway request and the operator's Open WebUI chat both returned a model response. The credential-free probes recorded only HTTP status codes and did not alter authentication settings.
- This establishes route-level authentication enforcement for the two sampled endpoints. Upstream dispatch telemetry, expired-key cases, management authorization, and credential logging were outside these probes. No FAT oracle status changes follow from this witness.
- The current implementation uses no delegated task tools. Verify one task-tool admission boundary when delegated tools enter the workflow.

RP-06.INC-02 has no standalone implementation under LAI-OD-20261119-08. Carry its local-only inference and telemetry checks into the retained work. RP-06.INC-03 covers local secret, bind, and log protections.

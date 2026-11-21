# RP-05.INC-02 existing G1 provisioning evidence

**Date:** 2026-11-20. **Scope:** foundational service provisioning on Bodhi 7 under owner decisions LAI-OD-20261119-08 and LAI-OD-20261119-09.

- The operator verified that Bifrost owned the local gateway listener, Ollama was active, and the selected ports were free. One gateway inference request succeeded using the existing virtual key. The operator created a same-mount checkpoint and verified its readback. Independent restore remains untested.
- Open WebUI 0.12.5 and LangGraph 1.2.19 with SQLite checkpointer 3.1.3 were installed from hash-verified local wheels in separate existing Python 3.12.14 environments. Both dependency checks and focused native imports passed. Redistribution and full release transport verification remain open.
- Open WebUI user service returned HTTP 200 from its readiness endpoint. The operator received `Ready` in a direct chat via Bifrost and Ollama after disabling the model's Built-in Tools. Offline document retrieval still lacks the default embedding model.
- The independent LangGraph user service returned HTTP 200 from its loopback readiness endpoint before and after a service restart. A real LangGraph invocation wrote state to the service's SQLite database, a fresh connection read it after the restart, and the smoke-test thread was removed. The database had owner-only permissions. The readiness endpoint verifies the checkpoint store, while delivery, specialists, cancellation, and workflow recovery belong to RP-09 and subsequent installed verification.
- Both user services were active at the end of verification. The existing Bifrost and Ollama services were reused. No FAT oracle was marked executed by this checkpoint.

Under the approved roadmap, the RP-05.INC-03 lifetime and local-only witness is combined into RP-12/RP-14. The next standalone increment is RP-06.INC-01, which reuses existing WebUI and Bifrost authentication.

# Three-way gateway functional gap analysis — 2026-10-31

Comparison: full LiteLLM Proxy reference; Bifrost OSS; Bifrost Enterprise **licensed and supplied directly by each end user**. No Enterprise binaries, license keys or proprietary assets will be redistributed in the public offline archive.

**Status:** candidate assessment; gateway substitution not approved, end-to-end tests not executed.

51 evaluated capabilities; provisional classifications: 16 need contract verification, 9 optional Enterprise, 8 project-owned development, 7 OSS configuration, 4 custom configuration adapters, 3 unresolved functional gaps, 3 packaging/license matters, 1 orchestration-platform responsibility. Values are engineering planning categories and not statements of confirmed deficiencies. Proposed R1/R2/R3 priority allocation needs owner acceptance.

**OSS candidate coverage (documented):** OpenAI-compatible API; multi-provider routing; fallbacks; model credentials; virtual keys, budgets, rate limits; MCP; caching; built-in monitoring; OpenTelemetry; OSS extensibility. **Enterprise-only additions:** vendor guardrails; SSO/OIDC; RBAC; native vault support; audit logging/export; adaptive balancing; clustering; federated MCP authentication. Edition boundary from https://www.getmaxim.ai/pricing.

**Likely project work packages:**
1. Open WebUI direct and LangGraph gateway compatibility contracts; JSON/SSE/tool/model discovery/error semantics.
2. Configuration/credential adapter, model aliases and policy reconciliation.
3. Per-agent/task IDs, execution limits and gateway usage correlation.
4. Secure service startup, secrets, log minimization, recovery and offline rollback.
5. Versioned AMD64 OSS gateway binary provenance, hashes, notices, SBOM, systemd, offline archive tests.
6. Optional edition detection, end-user-provided Enterprise integration, failure fallback to OSS without entitlement.
7. Comprehensive offline / API / provider failure / security fixtures.

**Unverified:** exact endpoint/provider coverage; tool schema and streaming fidelity; health and retry behavior; data persistence, management API security, budget enforcement boundaries and actual release artifact licensing. A2A interoperability not established; enterprise entitlement/installation contract not verified.

**Owner decisions:** approve provisional feature priority categories; whether guardrails, SSO, and immutable audit are first-release essential; ownership of gateway vs orchestrator system of record; enterprise supply integration policy; pinned binary acceptance.

**Sources:** https://docs.litellm.ai/docs/ ; https://docs.litellm.ai/docs/proxy/architecture ; https://docs.litellm.ai/docs/enterprise ; https://www.getmaxim.ai/pricing ; https://github.com/maximhq/bifrost/blob/dev/docs/overview.mdx ; https://github.com/maximhq/bifrost/blob/dev/docs/quickstart/cli/getting-started.mdx .

The detailed 51-row versioned CSV and ODT accompany this analysis in the conversation. Public redistribution remains blocked until artifact-level legal and technical verification.

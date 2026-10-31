# External Dependency License Gate — Sprint A (candidate)

Date: 2026-10-31. Decision: **BLOCKED for public redistribution**, not blocked for local resolution/testing.

Scope: project GPL-3.0 Debian package plus separate offline archive of Open WebUI 0.12.5, LangGraph 1.2.19 and LiteLLM 1.106.6 [proxy], Python 3.12.14, and all transitive dependencies.

## Preliminary findings
- Project source: GPL-3.0, repository LICENSE.
- LangGraph 1.2.19: MIT, https://pypi.org/project/langgraph/1.2.19/
- LiteLLM core: MIT outside enterprise portions, https://github.com/BerriAI/litellm/blob/main/LICENSE
- LiteLLM proxy extras 0.4.108: MIT metadata, https://pypi.org/project/litellm-proxy-extras/0.4.108/
- LiteLLM proxy resolution pulls `litellm-enterprise==0.1.76.post1`: commercial/proprietary license; redistribution permission and technical necessity unresolved. https://pypi.org/project/litellm-enterprise/
- Open WebUI 0.12.5: Open WebUI License (modified BSD branding restriction), not standard BSD-3-Clause and not OSI approved. Keep upstream branding/attribution; no assumed GPL relicensing. https://docs.openwebui.com/license/
- Transitive package license audit NOT COMPLETE. Resolved 242 Open WebUI CPU-only, 38 LangGraph, 117 LiteLLM proxy package entries before cross-environment deduplication.

## Gate prerequisites
1. Hash-bearing, platform-specific dependency lockfiles for all three environments.
2. Artifact-level SBOM with exact filename, source, hash, version, licenses and bundled assets.
3. Legal/technical disposition of LiteLLM enterprise requirement and Open WebUI redistribution/branding conditions.
4. Notices, corresponding source provisions (where required), and verification of independent service boundaries.
5. Fully offline clean installation, smoke tests and approval of frozen archive revision.

These findings are a preliminary engineering review and not a legal opinion. Do not publish the dependency ZIP as approved/redistributable until the gate closes.

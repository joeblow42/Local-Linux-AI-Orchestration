# Gateway licensing and security alternatives — Review 2026-10-31

Status: technical evaluation only; no architecture replacement approved.

## Evidence and findings
- LiteLLM v1.106.6 [proxy] includes `litellm-enterprise==0.1.76.post1`, confirmed by lockfile annotations and owner-inspected published PyPI extras. Core package omits it but does not provide a verified standalone OpenAI-compatible gateway.
- LiteLLM 1.107.0 was a compromised PyPI/Docker release on 2026-10-21. Maintainer: https://docs.litellm.ai/blog/security-incident-oct-21-2026 ; canonical attack chain: https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain ; Microsoft: https://www.microsoft.com/en-us/security/blog/2026/10/23/inside-the-litellm-1-107-0-supply-chain-compromise-credential-theft-through-python-startup-hooks/
- Historical LiteLLM v1.60.0 lacked enterprise extra; this is not a production recommendation.
- Bifrost (maximhq/bifrost) Apache-2.0 open-source core; GPLv3 compatible according to Apache Software Foundation. Standalone Linux binary available. Enterprise-only capabilities must be excluded and the exact release/artifact audited. Sources: https://github.com/maximhq/bifrost ; https://www.getmaxim.ai/bifrost/releases ; https://www.apache.org/licenses/GPL-compatibility
- Portkey-AI/gateway uses MIT, OpenAI compatible; Node runtime packaging and project maintenance cadence require examination. Sources: https://github.com/Portkey-AI/gateway and https://geekflare.com/open-source/portkey-gateway/
- LiteLLM core SDK plus custom FastAPI proxy is technically conceivable, but creates custom gateway maintenance/security and must be compared against existing gateway products.

## Proposed decision
Make **Bifrost OSS standalone binary** the leading alternative for an isolated proof-of-concept against LiteLLM, not an immediate baseline substitution. Maintain Open WebUI direct gateway and LangGraph gateway routes regardless of provider gateway selection.

## Required tests
1. Exact-version license/notice and bundled assets inventory; verify no enterprise module in selected artifact.
2. SHA-256, release provenance and artifact signature when available.
3. Native AMD64 Ubuntu 22.04 start/stop under systemd.
4. OpenAI-compatible completion and streaming calls from both Open WebUI and LangGraph (or contract-test clients).
5. Provider routing, fallback, cost/budget protection, logging privacy and credential isolation.
6. Offline install/reinstall from archived artifact, no network resolution.
7. Explicit owner architectural choice before updating the gateway baseline.

Public redistribution gate stays BLOCKED pending full artifact license audit and offline testing.

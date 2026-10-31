# LiteLLM proxy historical licensing review — 2026-10-31

## Result
Historical source tags demonstrate that an earlier LiteLLM proxy extra omitted `litellm-enterprise`, but more recent verified tags include it. This does not provide an acceptable current redistribution baseline by itself.

## Reviewed source-tag evidence
| Upstream git tag | `proxy` extra includes `litellm-enterprise`? |
|---|---|
| v1.60.0 | No |
| v1.84.0 | Yes: 0.1.40 |
| v1.85.0 | Yes: 0.1.40 |
| v1.90.0 | Yes: 0.1.43 |
| v1.95.0 | Yes: 0.1.52 |
| v1.100.0 | Yes: 0.1.62 |
| 1.106.6 PyPI (owner tested) | Yes: 0.1.76.post1 |

Source paths: `https://github.com/BerriAI/litellm/blob/<tag>/pyproject.toml` and owner-provided PyPI metadata / lockfile. Tag examination does not establish exact first introduction; interval bounded only by sampled tags.

## Disposition
Do not select v1.60.0 for a new public-facing gateway just to avoid proprietary packages: older version security/support and Python 3.12 compatibility have not been validated, and current upstream supports only a rolling set of recent minor versions.

Next review actions:
1. Determine exact GPLv3 + independent gateway packaging compatibility and redistribution conditions of packaged enterprise distribution in writing.
2. Evaluate whether current LiteLLM supports a documented proxy install that omits the enterprise package without deleting mandatory dependencies or bypassing licensing.
3. If not, evaluate a separate OpenAI-compatible gateway with auditable licenses, or a custom API adapter using core LiteLLM SDK.
4. Audit transitive artifact licenses before external ZIP approval.

Status: **Redistribution gate remains BLOCKED**. This is an engineering assessment, not a legal opinion.

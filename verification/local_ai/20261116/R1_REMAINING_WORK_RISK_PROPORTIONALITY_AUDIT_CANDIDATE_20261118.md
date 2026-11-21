# Local AI Development — Remaining-work risk-proportionality audit

**2026-11-18. REVIEW CANDIDATE, NOT APPROVED CHANGE TO G-R/G-A OR RELEASE SCOPE.**  
**Project:** Local AI Development, AI-Assisted Software Engineering Governance Standard v1.0.  
**Source state read:** GitHub `joeblow42/Local-Linux-AI-Orchestration` draft PR #1, initial HEAD `1a26ec161b9038c822214c00c691a7cdf8db2fe3`, base `46ec8e99eeb65627daa1b4296b1be32350282a67`.  
**Critical interpretation:** This is a domain-by-domain screen of **all 27 validated-need groups represented by the 136-row matrix** (104 assigned R1, 17 R2, 15 R3), **all 19 interfaces** and **all 26 historical FAT-oracle identities**, plus recorded RP-01–RP-14 work-package boundaries. It is **not** a verified line-by-line audit of all 42 roadmap increments because the complete standalone `LocalAI_FAT_Readiness_Roadmap_Rev0_2_Candidate_20261115.odt` / 42-increment source artifact is not included in the current GitHub tree. Preserve identifiers and revisit the complete roadmap only if bytes become available; do not invent its exact tasks.

## Executive finding

The project has **multiple remaining candidates for disproportionate low-risk engineering**, especially hypothetical state races, duplicate test fixtures, complex tracing, status/error proliferation and unnecessary infrastructure. The principal process risk is that source review/mock/approval artifacts could continue expanding without a working installed Release 1 article. The repository currently contains extensive verification/docs and candidate tests, **not a verified integrated Release 1 system**. G1 remains on owner hold. Risk screening must **not** reduce approved first-article outcomes: direct local conversation, independent two-specialist supervisor, persistent task status/cancel/automatic final result, verified offline install, and independently restored three application data owners.

Risk rule: **necessity = approved need/outcome + plausible failure/operational impact + least complex sufficient control + one representative falsifiable test.** A low-probability fault with catastrophic data-loss consequence can justify a cheap guard. A low-probability failure requiring a new service, custom fork, broad testing permutations or artificial adversarial model usually does not.

## Full domain scan of remaining R1 requirements

| Parent validated need / original IDs | Required result | Disproportionate design risk | Recommended action | Assessment |
| --- | --- | --- | --- | --- |
| NEED-001 (N001-01..04) | Install and use on supported Bodhi 7 AMD64, observable health | New product health dashboard or per-subsystem monitoring service | Use existing systemd/container health and installation checks, one real host FAT | **SIMPLIFY** |
| NEED-002 (N002-01..05) | WebUI is single conversation-history owner; persistence, ordering, restart | Duplicate history replication into supervisor for redundancy | Retain one WebUI store and readback; do not build second archive | **KEEP OUTCOME, NO DUPLICATE STORE** |
| NEED-003 (N003-01..04) | Direct WebUI→Bifrost→Ollama, model selection and truthful route failure | Generic cross-vendor model alias engine and endless client schema variants | One approved model route, explicit IDs/UNKNOWN and representative negative test | **SIMPLIFY** |
| NEED-004 (N004-01..04) | Delegation, two separate modes, automatic final result and service-unavailable result | Additional Stop button/dashboard, multiple adapters, hypothetical callbacks/cross-store exactly-once transaction | One Pipe, native WebUI interface, one supervisor; use simple repeatable update and readback | **HIGH OVERBUILD RISK** |
| NEED-005 (N005-01..05) | Two genuine specialist roles with contribution evaluation/synthesis | Separate evaluator agent, provenance service or workflow registry just to judge two roles | Sequential two-role LangGraph with clear attribution and basic substantive validation | **SIMPLIFY** |
| NEED-006 (N006-01..04) | Truthful failed/missing specialist contribution | Large fault-state vocabulary or exhaustive race/agent-betrayal models | Preserve failed/incomplete cause and one real negative specialist test | **SIMPLIFY** |
| NEED-007 (N007-01..04) | Stable task ID and correct chat/role correlation | Duplicate identity service, arbitrary UUID/format permutations | Supervisor-owned ID, one fixed mapping; basic restart/second-task test | **SIMPLIFY** |
| NEED-008 (N008-01..05) | Durable checkpoints and restart recovery | General distributed transaction layer, formal concurrent linearizability, adversarial corruption matrix | SQLite checkpoint + minimal durable task state, one crash/restart/missing-state test. Keep durability | **KEEP CORE; LIMIT EXTRA HARDENING** |
| NEED-009 (all five N009) | External context authorization | Hosted R1 mocks/policy enforcement | **Defer to R2**; R1 AC-04 seam design only | **EXCLUDED R1** |
| NEED-010 (N010-01..06) | Sanitized logs, no telemetry, 30-day metadata expiry, safe diagnostics | Logging framework, telemetry egress daemon, standalone diagnosis/export engine, many seeded marker permutations | Existing logging/rotation; one privacy/export sample plus expiry readback; enforce approved 30-day scope | **SIMPLIFY IMPLEMENTATION; KEEP PRIVACY** |
| NEED-011 (N011-01..06) | Gateway auth/secret protection, operator management and one task-tool admission boundary | Hostile-party threat infrastructure, second identity service, multiple tool-policy engines | Reuse Bifrost/WebUI controls and single tool gate; keep secret handling essential | **SIMPLIFY, NOT BYPASS** |
| NEED-012 (N012-01/03/04/05; N012-02 R2) | Local model/provider admission and denial | Vendor-specific permission revision registry or unrequested fallback simulations | Verify approved Bifrost controls; if revision unavailable, record UNKNOWN rather than build registry | **SIMPLIFY** |
| NEED-013 (all six N013) | Hosted billing/usage | R1 paid-call budgeting | **Defer R2** | **EXCLUDED R1** |
| NEED-014 (all five N014) | Hosted provider integrations | Two fake hosted models in R1 | **Defer R2** | **EXCLUDED R1** |
| NEED-015 (N015-01..05) | Ollama-only routing and truthful outage | Global air-gap/egress firewall infrastructure solely to detect fallback to nonconfigured hosted provider | Verify direct and delegated route/config, one Ollama-down behavior, no hosted path | **SIMPLIFY; KEEP LOCAL-ONLY** |
| NEED-016 (N016-01..07) | Compatible response/model list/SSE/errors; tool calls if actually used | Full streaming format fuzzing or native tool-call compatibility adapter when unused | One normal response, one stream/terminal and one error test. N016-03/04 conditional on R1 native tool-call use, subject G-R | **CONDITIONAL** |
| NEED-017 (N017-01..05) | Separate UI vs task store, common gateway, versions | Generic plugin framework/provider-neutral abstraction layer or live inventory daemon | Architecture diagram, narrow interfaces, deployment manifest; R2 seams design review only | **SIMPLIFY** |
| NEED-018 (N018-01..05) | Bounded, nondestructive tool capabilities/input validation | Enterprise agent authorization broker, prompt-injection security lab, redundant approval gates | One shared task-level capability admission/input validation before executor. Clarify whether R1 needs a tool at all before implementing a generic adapter | **MATERIAL G-R APPLICABILITY QUESTION** |
| NEED-019 (N019-01..05) | Predictable startup/health and safe data mount | New orchestration/monitor daemon, all possible interruption sequences | Existing service manager and single mandatory mount check; test reboot and mount absence | **KEEP MOUNT GUARD; SIMPLIFY MONITORING** |
| NEED-020 (N020-01..05) | Back up and independently restore WebUI, LangGraph, Bifrost | Cryptographically signed/encrypted backups, malicious tamper defenses and every conceivable corruption matrix | One complete access-controlled offline backup, checksum/structure check, clean-host restore and readback; encryption deferred as approved | **KEEP HIGH-IMPACT RESTORE** |
| NEED-021 (N021-01..06) | Reproducible Debian .deb/offline closure, ABI/licensing, bounded rollback | Arbitrary historical version compatibility/rollback matrix, custom updater, redundant install tests | One supported installation, one last-compatible rollback, manifest and legal notices. Reuse FAT evidence | **SIMPLIFY EXTRAS; KEEP PACKAGE** |
| NEED-022 (N022-01..05) | Free personal use and legal redistribution | Runtime proprietary-edition detector, extra entitlement subsystem | Static license/redistribution review; N022-05 retirement at G-R, not silent deletion | **RETIRE CANDIDATE** |
| NEED-023 (N023-01..05) | Measured CPU/RAM/storage and bounded concurrency | Runtime resource planner/monitor, standalone scheduling/queue service, arbitrary synthetic thresholds | Installer capacity preflight, existing gateway/Ollama concurrency controls and one representative FAT host measurement; original G-R reclassification pending | **HIGH OVERBUILD RISK, ALREADY OWNER-DIRECTED** |
| NEED-024 (N024-01..05) | Sanitized request identity, actual-or-UNKNOWN usage, latency and error classifications | Full telemetry collector, forced token counts, exhaustive error matrix | Existing Bifrost/source metadata, simple sanitized record, UNKNOWN where absent, few true negative cases | **SIMPLIFY** |
| NEED-025/026/027 (15 original R3) | Unattended persistence, agent protocol and consequences | R1 autonomous daemon, scheduler, autonomous policy simulator | **Defer to R3**, retain R1 tasks initiated by operator | **EXCLUDED R1** |

## Cross-cutting interface and test-screen dispositions

The existing 19-interface inventory has **15 R1 interface IDs, 2 R2, 2 R3**. Retain original IDs, do not split interfaces into 19 microservices. Highest scrutiny: `IF-02`/ `IF-05`/ `IF-06` completion delivery vs checkpoint ownership; `IF-TOOL` single gate; `IF-LOG` privacy; `IF-OPS` mount start; `IF-BACKUP` three-owner restore; `IF-PACK` offline closure. `IF-04`/ `IF-BUDGET` R2 and `IF-SCHED`/ `IF-AGENT` R3: no R1 implementations.

The **26 original oracle IDs** remain NOT_RUN (18 unconditional R1, one conditional R1, six R2, one R3). The seven supplemental gap proposals and later many `IF02-N` / `IF02-DEL` / `IF02-AUTH` scenarios should be **evidence references to a small number of connected FAT journeys**, not separately implemented mocks or 40+ owner gates. Retain traceability but execute only representative, independently observable failure conditions plus true installed integrated behavior.

## Ranked opportunities for subtraction before implementation

| Priority | Proposal | Specific evidence/constraint | Disposition |
| --- | --- | --- | --- |
| **P1** | Stop iterating paper/static/mocked IF-02 cancellation and automatic-delivery permutations | Source guards, in-memory fake supervisor and synthetic 12-case HTTP/SQLite suite now exist, but real Open WebUI + LangGraph not tested. Speculative deleted-message race has no demonstrated routine autonomous trigger | **STOP FURTHER MOCK EXPANSION**; retain one negative case for real fixture |
| **P1** | Do not implement general-purpose logging/health/tracing/permissions infrastructure | N010/N011/N019/N024 outcomes can use current component controls with simple configuration and bounded evidence | **DESIGN TO ONE IMPLEMENTATION OWNER** |
| **P1** | Consolidate RP-05, RP-07, RP-08, RP-12 overlapping installation/gateway/integration evidence and tests | Prior roadmap guidance; exact 42 increment artifact unavailable for line-by-line applicability | **REUSE EVIDENCE**, preserve stage identifiers/hold gates |
| **P1** | Do not implement native model tool-call adapter if two-specialist R1 workflow does not use it | N016-03/04 and original F17 conditional; applicability requires G-R review | **CONDITIONAL, NOT AUTOMATIC BUILD** |
| **P2** | Do not create a separate service for self-termination, cancellation, status or result delivery | Single selected Pipe, native END and independent supervisor already approved | **REUSE/ONE SUPERVISOR** |
| **P2** | Simplify cancellation/late result semantics | Genuine cancel request and no-next-step fence essential; elaborate general distributed linearizability framework is not | **ONE SERVER-SIDE TASK-STATE COMMIT** with real race check |
| **P2** | Avoid exact-once cross-store perfection as an up-front R1 gate | Open WebUI message edit is upsert; deleted-message race is operator/integration-action dependent, not demonstrated spontaneous occurrence | **IDEMPOTENT REPLACE + READBACK**, one deletion-race test; no fork unless real failure requires |
| **P2** | Avoid enterprise identity/hostile prompt assumptions | Approved single-operator local-only admin; operator key is broader than one task and must be protected, but a second auth server is not justified | **KEEP MINIMAL AUTH/SECRET PROTECTION** |
| **P2** | Avoid arbitrary backup encryption/tamper adversaries and unlimited rollback compatibility | Owner deferred backup encryption, authorized access-controlled offline backups; only last-compatible rollback | **KEEP ONE RESTORE + ONE ROLLBACK TEST** |
| **P2** | Avoid arbitrary host budgets or a complex capacity planner | N023-02/05 limits are not yet measured | **MEASURE FIRST**, then basic installer gating |
| **P3** | Fold repeated source/negative witnesses into a single integrated evidence plan | Original test IDs and approved requirement IDs must remain unchanged, but test activities need not be one-to-one with IDs | **ONE CONNECTED R1 FAT SCENARIO** and a few targeted negative/recovery cases |

## Explicit non-candidates for elimination (failure impact justifies effort)

1. **Verified independent restore of three stores**: loss of conversation history, checkpoints or gateway access is high-impact regardless of probability.
2. **Durable checkpoint/readback and restart recovery**: required for independent supervisor function, not hostile-actor hardening.
3. **Service mount-before-write guard**: cheap and directly protects the owner's storage layout from writes into unmounted underlying directories.
4. **Gateway/model-key and basic tool-input authorization**: avoid uncontrolled operations and accidental credential exposure; one existing mechanism suffices.
5. **No external telemetry and sanitized/30-day metadata policy**: affirmative approved privacy requirement, not speculative.
6. **True Debian offline closure, licensing, and installed FAT**: necessary definition of a functional home-use deliverable.
7. **Automatic final result in originating WebUI conversation**: owner-approved usability outcome, not optional because delivery is tricky.

## Project sequencing recommendation

The **highest remaining risk is process overengineering**: many candidate paperwork artifacts and mock suites can give an appearance of progress without producing an operable first article.

Recommended compressed execution: (1) one controlled G-R/G-A review focusing on material disagreements, thresholds and actual selected client versions; (2) verify real non-G1 direct route and delegated two-specialist task including status/cancel/automatic delivery/restart; (3) wire simplest complete backup/restore and offline Debian install; (4) execute representative connected FAT and actual host evidence; (5) retain final original oracle/requirement trace matrix, avoid invented per-increment owner gates.

**Outstanding material questions, not approvals:** whether N018 requires a real R1 local tool adapter, exact storage/concurrency thresholds based on measured host and package, what G-R/G-A state vocabulary is essential; and when the owner will release G1 hold for approved target checks. The full historical 42-increment roadmap is needed for exhaustive **task-by-task** decisions; this review does **not** silently retire or reassign any task/requirement.

**Change authority:** this candidate document is a recommendation for owner review only, NOT new owner approvals, formal G-R/G-A changes, merge, service change, or release. G1 hold, draft/unmerged PR, R2/R3 exclusions, original evidence/identities and no paid external calls remain intact.

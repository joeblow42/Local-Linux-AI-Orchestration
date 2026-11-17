# RP-02/RP-04 bounded Release 1 candidate requirements and verification predicates

**2026-11-16 — CANDIDATE; source-first design review only; no G-R or oracle baseline approval.** Source: exact 136 original requirement statements and 26 original oracle records recovered from the owner-provided, SHA-verified 3,451,941-byte recovery ZIP; later owner-approved R1/R2/R3 strategy, LangGraph Option A, AC-01–AC-04, FAT Alternative B, local-only policy, and no mandatory backup encryption. Do not read this file as historical original evidence or as execution proof.

## Seven outstanding derived R1 needs — candidate disposition

**Preserve the existing `GAP-R1-01` … `GAP-R1-07` identifiers**. These are candidate refinements, not automatically seven new product requirements; avoid double-counting existing originals.

| Gap | Bounded candidate obligation | Source-first resolution and acceptance criterion |
| --- | --- | --- |
| GAP-R1-01 | Each accepted user-delegated task has a stable ID and observable state, retrievable after supervisor restart | Original N007/N008 cover identity/checkpoint but not user-visible lifecycle. Demonstrate accepted → running → one truthful terminal outcome; test observed status against durable record, not fabricated timestamps. Exact state vocabulary requires interface review |
| GAP-R1-02 | Operator can request cancellation of an active delegated workflow; accepted cancellation blocks starting subsequent specialist steps and never reports false success | Original R3 autonomous cancel N026-01 is not an R1 replacement. A downstream inference already running may be uncancellable; distinguish cancellation accepted, in-flight call termination, and final task disposition |
| GAP-R1-03 | Both R1 direct and delegated inference are Bifrost → local Ollama only; no hosted inference or external application telemetry | Supplements N003/N015 and approved R1 scope. Allow necessary loopback/LAN traffic and operator-authorized OS/model/dependency downloads; do not implement general host outbound-deny infrastructure |
| GAP-R1-04 | Independently verified, access-controlled offline restore recovers readable Open WebUI history, LangGraph task/checkpoint state and usable Bifrost configuration | Refines N020-01..05. Use a clean isolated target, verify component-level readback and full local request after restore. Encryption is not mandatory |
| GAP-R1-05 | Backup archive has a versioned format/metadata seam capable of indicating a future optional encryption mode | Architecture/schema acceptance criterion, **not** an obligation to build encryption/decryption or recovery-key management in R1 |
| GAP-R1-06 | Architecture demonstrates AC-01 Bifrost common gateway, AC-02 selected/dispatched/resolved model identities, AC-03 secret ownership separation, AC-04 future policy insertion without changing history/checkpoint ownership | A **design verification criterion** for four approved architecture directions, **not** an implemented R2 adapter/mocked external provider |
| GAP-R1-07 | Every R1 delegated workflow is initiated by a current operator action; R1 has no project-owned unattended recurring task entrypoint | Negative R1 scope acceptance criterion. Do not prohibit unrelated host scheduled jobs or require an R3 scheduler just to test its absence |

**Overlaps and traceability:** GAP-R1-01/02 tie to N004/N007/N008; GAP-R1-03 to N003/N012/N015; GAP-R1-04/05 to N020/N021; GAP-R1-06 to N003/N017 plus AC-01..04; GAP-R1-07 to the deferred N025/N026/N027 group. Prefer exact amendments or a small number of newly justified requirements over wholesale proliferation.

## RP-04 independent observability: 19 prospective R1 oracles

All below are **NOT RUN / NOT ACCEPTED**; they depend on G-R/G-A owner authorization and later safe test execution. They are grounded in original source requirements and late owner decisions, not successful historical tests.

| Oracle | Falsifiable FAT witness (positive AND negative/fault condition) | Observation channel and guard |
| --- | --- | --- |
| F01 | Direct model request reaches Bifrost/Ollama; LangGraph invocation counter stays unchanged | Gateway/local request and independent supervisor invocation records |
| F02 | One authorized alias resolves to expected Ollama model; ambiguous/unauthorized alias does not silently route | UI selection plus gateway dispatch/resolved-model IDs |
| F06 | Distinctive safe test-marker prompt is absent from all retained operational metadata; any retained prompt content fails | Local application/journal/container diagnostic sinks, not just one logger |
| F07 | No external *application telemetry* emitted during workflow; observed telemetry is failure | Targeted egress capture; authorized dependency downloads do not cause failure |
| F08 | Older-than-policy sanitized request metadata is purged according to **30-day** rule; outside-window retention beyond approved tolerance fails | Seeded or isolated record store age/purge test; not message archive or backups |
| F09 | Valid local virtual key succeeds; inactive/expired/revoked key fails with **no upstream Ollama dispatch** | Gateway admission evidence + independent upstream counter |
| F10 | Unauthenticated or unauthorized management read/write is denied; authorized local operator succeeds | API outcomes, config-state comparison, network locality |
| F11 | Request for unpermitted local model/provider fails; no alternate or hosted fallback dispatch | Gateway routing record and upstream/egress witness |
| F15 | Direct and delegated requests both reach only allowed local inference; any hosted inference dispatch fails | Request correlation across WebUI, LangGraph, Bifrost, Ollama and egress |
| F16 | SSE emits well-formed deltas and a genuine terminal state; malformed or cancelled stream never falsely completes | Raw event framing + client-visible status at pinned versions; G1 hold prevents current execution |
| F17 | **Conditional** if R1 workflow actually uses native tool calls: accepted tool-call ID/arguments remain intact; mutation or wrong call fails | Gateway request/response vs supervisor invocation; otherwise record NOT APPLICABLE, not fictitious test PASS |
| F18 | WebUI model selector lists a routable gateway model and completes matching request; wrong alias/listing fails | Client UI enumeration and gateway request target |
| F19 | Unauthorized tool operation is denied *before* execution; authorized nondestructive operation is permitted | Independent adapter call counter, task grant, tool result; no speculative hostile-actor engine |
| F20 | Acknowledged supervisor checkpoint is durable; restart returns truthful state; missing/corrupt state yields error | Filesystem/database readback independent of supervisor's success claim |
| F21 | Offline backup preserves needed Bifrost config and local credentials; restored gateway serves the previously authorized route | Isolated restore and valid request; **do not require encrypted backup** |
| F22 | Invalid/incomplete backup is rejected before replacing active stores; valid isolated restore is usable | Before/after data hashes and actual readback; operational corruption, not malicious tampering |
| F23 | Unmounted application-data filesystem blocks writer startup or writes; no service writes into underlying mount directory | Independent mount check, service state and underlying path inspection |
| F24 | Fresh supported Bodhi 7 AMD64 host can install via primary `.deb` and complete transport archive with dependency downloads disabled | Isolated installer logs, dependency list, service health and live local task |
| F25 | Known usage counts are retained as observed; missing Ollama tokens are marked **UNKNOWN**, never invented | Raw gateway/producer response compared to sanitized usage record |

**Deferred oracles:** F03/F04/F05 (R2 external field-projection/consent), F12/F13/F14 (R2 paid-call budget), F26 (R3 consequential autonomous action recovery). Preserve their exact `GRGA07-` prefixed IDs and original source requirement links. Do not run R2/R3 tests in R1.

## Contract and gate notes

- **IF-01, IF-03, IF-LOCAL** jointly protect both R1 routes through Bifrost without conflating WebUI history and LangGraph checkpoints.
- **IF-02** still needs the actual supported Open WebUI delegated integration mechanism verified; the prior recommendation requiring *both* Pipe adapter and a local API is not established by source. Independently executable LangGraph remains required.
- **IF-BACKUP**'s original encrypted-backup wording and **IF-PACK**'s prior review “unapproved .deb” assertion must be superseded **only in new candidate wording**, never by rewriting historical evidence.
- **AC-01–AC-04**: perform R1 design-impact walkthrough; no hosted provider mocks, paid calls, R2 credential deployment, R3 schedulers, or other architecture overbuild.
- Each candidate predicate needs fixed setup, actual positive witness, independent negative/fault witness, pass/fail/unknown logic, and executable trace to the approved requirement/interface before becoming a verification oracle. No CI, gateway, host or acceptance execution is asserted here.

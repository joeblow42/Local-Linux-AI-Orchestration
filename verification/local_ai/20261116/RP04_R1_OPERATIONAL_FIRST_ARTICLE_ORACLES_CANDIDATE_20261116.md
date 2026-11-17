# RP-04 — independently falsifiable R1 first-article oracle specifications (candidate)

**2026-11-16.** Specification only, **NOT RUN**, **NOT independently accepted**, **G-R / G-A NOT APPROVED**, **G1 runtime hold ACTIVE**. This increment refines the 19 current R1 (including one conditional) of the original 26 source-linked `GRGA07-F01` through `GRGA07-F26` oracle identities. Original source identities and their requirement links remain unchanged in `RP04_26_ORACLE_SCOPE_INDEX_CANDIDATE_20261116.csv`. All positive, negative and recovery witnesses below are new candidate test predicates, **not historical test results**.

## Oracle principles

- Every witness observes an external product behavior, durable record or independent source/target counter; do not treat a mock's own reported success as proof of installed-system behavior.
- A **negative** test is a controlled ordinary failure (unavailable dependency, invalid credential, incomplete archive, cancelled task), **not** an unapproved hostile actor or threat model on the single-operator host.
- **PASS** requires actual target execution against the owner-authorized version/configuration with evidence and a clearly defined pass threshold. **NOT RUN** is distinct from **NOT APPLICABLE** and **UNKNOWN**.
- Preserve 30-day sanitized operational metadata; user chat history and backups have independent retention/restore controls. No external application telemetry or hosted inference in R1. Necessary loopback/LAN and operator-authorized downloads are allowed.
- First-article execution requires a full installed system: Open WebUI, independent LangGraph supervisor, Bifrost OSS, local Ollama, supported Bodhi Linux 7 AMD64, primary `.deb` and offline dependency archive.

## Source-linked existing oracle identities

| Original ID | Positive witness | Independent negative or fault witness | Independent observation / authority caveat |
| --- | --- | --- | --- |
| GRGA07-F01 | Direct UI selection reaches **Bifrost → Ollama**, and LangGraph receives no request | Supervisor invoked or gateway bypassed on a direct chat | Gateway/upstream request correlation and supervisor counter; **IF-01/IF-LOCAL pending G-A** |
| GRGA07-F02 | Selected local model routes with consistently observed selected/dispatched/resolved identity | An ambiguous/unapproved alias is denied, not silently redirected | UI request, gateway decision and local Ollama backend observation; **AC-02 design accepted**, not implementation |
| GRGA07-F06 | A test prompt marker is absent from retained operational records | The marker appears in a log, journal or sanitized export | Independently inspect actual app/container/journal sinks; do not require new surveillance |
| GRGA07-F07 | R1 operations produce no external application-telemetry events | Deliberately enabled application telemetry would violate R1 configuration and must be rejected in design review | Targeted egress and config inspection; do not label authorized dependency/model download as telemetry |
| GRGA07-F08 | Sanitary operational metadata older than 30 days is purged | An out-of-policy record remains while in-window records are intact | Isolated seed of age-controlled metadata plus datastore readback; do not purge chat history |
| GRGA07-F09 | Active permitted virtual key reaches authorized local model | Missing/inactive/expired key receives denial and no Ollama dispatch | Gateway response plus independent upstream counter, not only a UI error |
| GRGA07-F10 | Local authenticated operator can read/update allowed gateway settings | Unauthenticated/unauthorized protected read or write denied with no state change | Separate management API status/config readback |
| GRGA07-F11 | Allowed local model routes; model/provider denied by active policy does not | Unapproved model/provider request yields no fallback dispatch | Gateway route record and upstream/egress witness |
| GRGA07-F15 | Both direct and delegated task paths resolve to Ollama only | Unselected hosted inference route or missing local backend cannot silently trigger hosted fallback | Correlate Open WebUI, supervisor, Bifrost and Ollama; no paid calls to test this |
| GRGA07-F16 | Pinned gateway SSE data and termination are decoded and displayed accurately | Invalid/truncated/cancelled stream is not reported as a successful complete answer | Raw gateway event capture **later**, once hold lifted, and UI state; current schema NOT FROZEN |
| GRGA07-F17 | **Conditional**: if the selected R1 task actually uses native model tool calls, tool ID/args survive through gateway | Changed or unsupported tool schema fails without unintended tool execution | Source/fixture then target gateway/supervisor adapter; otherwise **NOT APPLICABLE with reason**, never synthetic PASS |
| GRGA07-F18 | UI model selector lists and completes request through authorized Bifrost route | Stale/disallowed model alias fails visibly without false success | UI selector ID vs gateway model list/dispatch and local response |
| GRGA07-F19 | Task capability grant permits approved nondestructive tool and result is traceable | Denied capability/tool input results in zero adapter calls | Independent adapter call counter and grant decision |
| GRGA07-F20 | Completed checkpoint acknowledged only after durable state; restart recovers recorded state | Missing/corrupt checkpoint yields recovery error, not a fabricated successful task | Checkpointer source-of-truth readback and supervisor service outcome |
| GRGA07-F21 | Clean-target offline restore recovers usable Bifrost local route, secret/config material | Absent key/config produces explicit restore or route failure | Bifrost config and successful authenticated local request; **backup encryption NOT required** |
| GRGA07-F22 | A complete validated archive restores data on isolated target | Truncated/incompatible archive rejected **before** replacing active stores | Before/after independently read persistent-store integrity and application readback |
| GRGA07-F23 | When required data mount absent, writer startup blocked or redirected safely | Unavailable mount causes write into underlying empty mount directory | External mount identity and writer-state inspection; controlled target failure |
| GRGA07-F24 | Install `.deb` plus complete archive on supported Bodhi 7 AMD64 **without fetching dependencies**, then direct/delegated task | Missing/incompatible dependency yields installation failure rather than misleading success | Package manager, manifest, filesystem, service/functional readback; verify licenses |
| GRGA07-F25 | Usage records distinguish actual upstream counts from unavailable counts | Missing Ollama token data is not fabricated as zero or estimated actual | Compare raw producer payload with sanitized gateway/usage record; **UNKNOWN** is an allowed observation |

**Deferred original cases:** `GRGA07-F03`, `F04`, `F05` and `F12`, `F13`, `F14` target authorized R2 external consent and paid-call budgets; `F26` targets R3 autonomous consequential action. All remain **NOT RUN** and not R1 prerequisites.

## Additional candidate gap witnesses — no new controlled oracle IDs assigned

These follow the **seven R1 derived gap candidates** and must not be counted among the 26 approved/original oracle identities. No implementation or G-R obligation follows from this review until authorized.

| Gap | Positive operational FAT witness | Counterexample / recovery witness |
| --- | --- | --- |
| GAP-R1-01 task status | A user-submitted delegated task gets stable task ID and independently readable queued/running/terminal states | UI disconnect/reconnect cannot invent task success or lose durable ID |
| GAP-R1-02 cancellation | Operator cancellation acknowledged; no new specialist step starts after cancellation acceptance; terminal disposition truthful | Cancel during in-flight inference distinguishes request to cancel from completed cancellation; no silently synthesized success |
| GAP-R1-03 local-only routing | Both modes use gateway and Ollama; local-only and no external application telemetry | Ollama unavailable => explicit failure, never external fallback; LAN/local download allowances preserved |
| GAP-R1-04 three-owner restore | On clean host, Open WebUI history, LangGraph task/checkpoint and Bifrost local route all independently readable/usable | Missing one of the three stores => restore cannot be marked fully complete |
| GAP-R1-05 optional encryption seam | Versioned backup format contains a documented optional encryption-mode discriminator | Unrecognized encryption mode rejected cleanly; no R1 encryption implementation required |
| GAP-R1-06 AC-01..04 | Source/design walkthrough identifies common Bifrost gateway, model IDs, distinct external secret future boundary and request-consent insertion point | Design introduces future provider dependence directly into WebUI history or LangGraph checkpoint ownership => fail **design review**, not a live hosted test |
| GAP-R1-07 no unattended execution | All R1 delegated task-creation events correlate to active operator requests | Restart alone or cron-like unattended trigger creates application task => violation; normal host maintenance jobs exempt |

## Integration witness and owner acceptance

The R1 operational FAT should exercise one **connected end-to-end user scenario**: install offline, start services and inspect health; select and complete a direct local chat; initiate a delegated two-specialist task; observe status, checkpoint and synthesized answer; cancel another delegated task; restart LangGraph and recover accepted task state; back up application data, restore on an independent clean target, and retrieve history/checkpoints/Bifrost route. This joins the components and catches failures that isolated gateway fixtures cannot.

**Acceptance states:** candidate design → independent verification-spec review → G-R/G-A authority → tests authorized and executed → evidence independently reviewed → owner FAT acceptance. An owner’s approval of the roadmap is **not** approval of these predicates. A synthetic simulation cannot become the FAT demonstration.

**Next source needs:** pinned Open WebUI and LangGraph versions; verified exact Bifrost image digest/source-code contract (tagged docs reviewed but runtime held); final IF-02 adapter selection; source-sensitive acceptance criteria; independently justified resource thresholds. Do not invent these data to close G-R/G-A.

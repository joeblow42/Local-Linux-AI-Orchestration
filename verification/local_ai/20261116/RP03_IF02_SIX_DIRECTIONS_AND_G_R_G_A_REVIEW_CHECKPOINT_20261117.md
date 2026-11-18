# Local AI — IF-02 owner-guidance reconciliation and minimum G-R/G-A review checkpoint

**Date label:** 2026-11-17. **State:** source-first bounded engineering increment complete; owner-level outcome decision identified and open. No G-R/G-A baseline or product test.
**Starting PR HEAD:** `06653192d914ec32e4c99c36a9001d09d151fc1d`. **Pre-checkpoint HEAD:** `ee4df4b059149714efa73ab59fa3891385dfb1d2`; checkpoint/README commits occur after this. Verify latest exact head on continuation.

## 1. Recorded authority and completed source reconciliation

- Owner response **"approved, continue"** to provisional six-direction IF-02 engineering guidance has been recorded in [LAI-OD-20261117-05](./OWNER_APPROVAL_IF02_SIX_ENGINEERING_DIRECTIONS_20261117.md), commit `1de913f97ce57c54e2f19ef069c82368377fcba2`. Approval limited to **engineering directions**, not G-R/G-A source wording, field schemas, product implementation or R1 acceptance.
- [Machine trace crosswalk](./RP03_IF02_SIX_APPROVED_DIRECTIONS_GR_GA_CROSSWALK_CANDIDATE_20261117.json), commit `80841c73fb401a46ca4f96482e520f7add1ab7e4`: derived from *exact* original source-linked GitHub matrices, verified 136 requirements, 19 interfaces, 26 original oracle IDs and 136 release allocations. Every direction's original requirement/interface/oracle anchor exists; **0 orphan references; no new controlled IDs**. Six directions cover 14 unique original R1 requirements, no historical source/hash mutation.
- [Minimum G-R/G-A candidate review packet](./RP03_IF02_GR_GA_MINIMUM_REVIEW_PACKET_AND_FINAL_DELIVERY_DECISION_CANDIDATE_20261117.md), commit `ee4df4b059149714efa73ab59fa3891385dfb1d2`, reconciles stop, self-end, durable task acceptance, native WebUI Stop, operator task commands, and truthful terminal statuses.
- All owner decisions on Alternative A single Pipe and six technical directions preserved. LangGraph native conditional END terminates an already authorized workflow; `interrupt()` is a resumable pause. No independent stop button, R1 unattended scheduler, separate status daemon or duplicated supervisor service added.

## 2. New precise source finding

An additional pinned-source read of Open WebUI `v0.12.5` upstream commit `f7ac7ee10962ddec0017f5c29b6740d9b9c5faca` found a conditional WebUI event emitter/persistent message update implementation in `backend/open_webui/socket/main.py`, blob `1338308fb6d77f96532229b5d3444bcb3c5605d7`, which handles `message` / `replace` content changes in a **saved** chat when `update_db` is enabled and required context is present.

Cross-check: `backend/open_webui/functions.py`, blob `20601fee7e42e69f7d21bb452c740ec4c3df96f9`, only injects the Pipe event emitter when eligible metadata and declared signature are present. `src/lib/components/chat/Chat.svelte`, blob `438c173eb91833192d822d15d6ecaa76f3b99e15`, may queue later task commands while assistant generation is active. **13 of 13 source-fragment guards matched.** No actual event/callback after Pipe closure, delayed supervisor final delivery, crash recovery, UI rendering, HTTP integration or installed system behavior was tested. Do not overstate this as validated autonomous push or completion notification capability.

## 3. Material G-R ambiguity requiring owner decision

The source-linked candidate acceptance witness for `LAI-R1-N004-03` requires a delegated result to reach its initiating Open WebUI conversation. A prompt task-ID acknowledgement alone does not guarantee that the final synthesized answer appears automatically.

**Decision A (recommended for usability, subject to feasibility):** asynchronously deliver final result in the same conversation without manual retrieval, with existing task-ID status command as fallback. Requires proven durable and restart-safe update or appropriately explicit failure limitations; cannot assume source emitter provides it.

**Decision B (lowest complexity):** on-demand terminal result appears in the originating conversation when the operator enters a task-ID status/retrieval command; no promise of automatic completion update.

This is **one material acceptance choice**, not part of the six directions approved. Do not infer owner selection or advance the exact G-R witness or G-A presentation contract until owner responds. Other open schema details require later formal G-A review but no new duplicative owner approval of the six directions.

## 4. Evidence and state of work

- Source-based matrix counts PASS 136/19/26/136, 14 distinct reviewed R1 requirement anchors, 0 orphan anchor; six source-trace entries. All original sources/hashes untouched.
- Prior independent LangGraph 7/7 source checks, WebUI 15/15 source guards and 20/20 isolated fake suite retained with their earlier limitations; not rerun or recharacterized as product tests.
- New Open WebUI message/update 13/13 static source guards PASS only; no runtime validation, original 26 oracles **ALL NOT_RUN**, owner-controlled G-R and G-A **NOT APPROVED**.
- Release 1 remains local-only Open WebUI, Bifrost OSS, Ollama and a separately managed LangGraph supervisor with two operator-initiated specialist roles. Release 2 paid OpenAI/Anthropic, Release 3 autonomous scheduler untouched.
- **G1 runtime/data collection OWNER HOLD**, PR #1 open, draft, unmerged. Do not merge, change services or claim CI PASS absent evidence.

## 5. Next action and conversation safety

Present owner with only the concrete **A-versus-B completion delivery decision**, including known tradeoff; stop before interpreting candidate `LAI-R1-N004-03` acceptance. Once decided, update the accepted engineering direction and refine minimal IF-02 presentation/terminal-result contract; only seek controlled G-R/G-A baseline approval with source and independently falsifiable evidence. **Context integrity remains good** because all new authority, source-hash-linked reconciliation, verification limits and decision are persisted in GitHub. Safe to resume in this conversation or from this checkpoint.

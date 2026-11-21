# RP-03 bounded checkpointer source and complexity review
**2026-11-16 continuity date — NOT FROZEN / NOT IMPLEMENTED / NOT TESTED.**  
**Base engineering branch HEAD:** `8fae045b4e24af4275f8bd94a663481e12026dcf`; G-A not approved; G1 owner hold in force.

## Tagged version compatibility, not dependency closure
The repository's `dependencies/inputs/langgraph.in` already specifies `langgraph==1.2.19`. The exact upstream [`langchain-ai/langgraph` tag `1.2.19`](https://github.com/langchain-ai/langgraph/tree/5bd231cbfd913e05ebc662f519eb9a655bc766df) resolves to commit `5bd231cbfd913e05ebc662f519eb9a655bc766df`.

At that exact source commit:
- [`libs/langgraph/pyproject.toml`](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/pyproject.toml) specifies LangGraph 1.2.19 and `langgraph-checkpoint>=4.3.0,<5.0.0`.
- [`libs/checkpoint/pyproject.toml`](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/checkpoint/pyproject.toml) specifies `langgraph-checkpoint==4.3.1`, MIT license (blob `1ab07b711f4bcfc07941f0a6a25bb8614df94b72`).
- [`libs/checkpoint-sqlite/pyproject.toml`](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/checkpoint-sqlite/pyproject.toml) specifies `langgraph-checkpoint-sqlite==3.1.3`, MIT, and dependency `langgraph-checkpoint>=4.3.1,<5.0.0` (blob `7eff2a5969547be703fc22964584339cc4cf0e9a`).
- [`libs/checkpoint-sqlite/langgraph/checkpoint/sqlite/aio.py`](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/checkpoint-sqlite/langgraph/checkpoint/sqlite/aio.py) contains `AsyncSqliteSaver`, `from_conn_string`, an `aiosqlite` backing database, and asynchronous checkpoint APIs (blob `a62a35473c05c4cf93b77e5fc787c890521d2bd0`).

**Conclusion of static dependency check:** The three exact version numbers 1.2.19 / 4.3.1 / 3.1.3 are compatible with the *declared version constraints*. This does **not** prove pip/uv resolution, signed artifact provenance, transitive dependency closure, successful offline installation, stable migrations or runtime safety.

## Design choice and deliberately bounded counterargument
Source comments in `AsyncSqliteSaver` warn that SQLite may be unsuitable for production workloads due to **write performance**, and suggest a stronger database (e.g. PostgreSQL). This is a real caution, not a categorical disqualification for an independently tested **single-operator local first article**.

**Provisional minimal option:** Use a local SQLite-backed checkpoint saver and task metadata under one LangGraph supervisor service. Prefer one durable storage/backup responsibility boundary, not a separately administered database server. Require an explicit connection/shutdown lifecycle and successful clean backup/restore of the checkpoint data. The candidate can use identical stable opaque `task_id`/`thread_id` where safe, or a minimal durable mapping if needed; do not infer that LangGraph automatically provides task IDs.

**Fail-closed upgrade condition:** Do not promote SQLite to G-A or first-article acceptance until independent workload tests verify:
1. Acknowledged checkpoint is actually durable after restart and across a fault-injection interruption.
2. Checkpoint/metadata updates remain truthful under *measured* intended single-operator direct/delegated load and controlled concurrent requests.
3. Cancel/complete race cannot fabricate a successful final state, start new specialist actions after cancellation acceptance or lose an acknowledged checkpoint.
4. Consistent offline snapshot and independently verified clean-target restore of SQLite checkpoint data work together with Open WebUI chat history and Bifrost config.
5. Busy/locked/unavailable/corrupt SQLite conditions return classified failures rather than success; SQLite locking or latency measured at FAT is not falsely suppressed.
6. Saver/database revision migration and rollback are documented and exercised before claiming upgrade/restore compatibility.

No throughput, latency, disk or concurrency numbers are presently authorized. If actual results cannot satisfy justified criteria, reconsider a stronger storage backend with evidence; **do not introduce PostgreSQL solely because a general upstream doc warns about large production workloads.**

## G-A gate
Selected source version candidates are now inspectable, but **not approved pins**. Need owner-authorized exact dependency set; a complete `uv` lock with hash identity; offline wheels; independent fixture behavior; testable supervisor HTTP task protocol; and evidence of actual target-host behavior after G1 hold release. No installation or test executed.

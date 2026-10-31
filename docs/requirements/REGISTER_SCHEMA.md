# Requirements register schema — Phase 0 Sprint A candidate

Status: **candidate**; approved register schema requires owner review. Requirement statements must express one verifiable obligation. Do not duplicate requirements as user stories.

| Field | Meaning |
|---|---|
| requirement_id | Immutable identifier, never reused |
| type | Need, functional, interface, quality, security, packaging, or process |
| responsible_entity | Component or system obligated |
| statement | Singular unambiguous requirement |
| rationale | Why the obligation is needed |
| source | Source identifier and location |
| parent | Higher-level trace |
| verification_method | Inspection, analysis, demonstration, test |
| verification_success_criteria | Objective pass/fail condition |
| priority | Approved priority |
| owner | Responsible decision owner |
| status | Proposed, approved, changed, deferred, retired |
| revision | Document/register revision |
| evidence | Test artifact or evidence reference |

Example candidate:
IF-REQ-001 | interface | Open WebUI | The local conversation interface shall provide a configurable connection to the model gateway for direct model requests.

Controlled terminology is defined in a project glossary as it is developed.

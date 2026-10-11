# Wave 16 — A001 Contract Alignment and Trigger Validation — 2026-10-11

## Scope

Continue the canonical roadmap's F.1.2 gate by reconciling the A001 agent contract, SK001 skill, skill registry, tool registry, canonical event envelope, event draft, and n8n trigger. This is a bounded implementation checkpoint; it does not replace cross-functional business-plan system work.

## Verified repository findings

1. `agents/market-research/agent.yaml` requires `research_question` and `target_market`, lists `research.completed`, and declares three allowed tools.
2. SK001 is now `specified`, but not approved/active. SK002 remains `planned`.
3. All three A001 research tools remain `planned`; the mapping policy requires active/approved skills, authorized tools, compatible contracts, and integration-test evidence.
4. `06-data/event-schemas/README.md` requires a canonical event envelope including event ID/type/version, occurrence time, source, company/entity identifiers, correlation/causation identifiers, payload and metadata.
5. `EVENT_REGISTRATION.yaml` does not register `market.research.requested` or `research.completed`; its policy requires test evidence before production registration.
6. The previous n8n code accepted flat input and synthesized an event ID, while the event envelope contract requires stable event identity and envelope metadata. The old behavior did not match the canonical event contract.
7. The n8n workflow is inactive and its runtime-boundary node is a placeholder, not an A001 executor.

## Changes committed

- Added `Chats/ChatGPT/Multi Agent AIOS/02-agents/agent-skill-mappings.yaml` with an explicit A001 → SK001 required / SK002 optional traceability record. Its status is `blocked`, not authorized; it enumerates all unfulfilled gates and uses fail-closed resolution.
- Updated `08-infrastructure/n8n/workflows/A001-market-research-trigger.json` to validate the canonical event type/version, event identity, source, company/entity IDs, correlation ID, timestamp, payload, required request fields, and basic types for source policy/competitor set. It no longer invents an event ID for malformed requests and emits `runtime_invoked: false` / `validated_pending_runtime` at the placeholder boundary.
- Updated the trigger README to document the canonical envelope, negative-validation behavior, inactive status, and live-runtime evidence required before F.1.3 completion.

## Commit evidence

- Mapping record: `929a98340cad1e3fe3f1acaf5a1204298eeef0b2`
- Trigger JSON alignment: `672ff5ea24c5ff3ee330d36ad0a685c14bdd385d`
- Trigger README alignment: `effe456805d33a2188c6827ee388d12d1053fffb`

## Static read-back checks

After committing, the mapping, trigger JSON and README were fetched from GitHub again. The mapping is explicitly blocked; the workflow JSON remains valid JSON for parsing and retains `active: false`; the code contains the canonical event checks and explicit pending-runtime state; the README describes the same envelope and non-production status.

These are repository/static checks only. No n8n instance, A001 runtime, YAML validator, JSON Schema validator, research tool adapter, database event store, or automated contract-test runner was executed in this step. Do not interpret this report as passing runtime tests.

## Remaining blockers / next actions

1. Validate YAML syntax for the skill registry, mapping record, fixture file and event draft with the actual project validator; record validator/version and output.
2. Validate event payload schemas with the project's actual schema validator; tighten the request schema to enforce all envelope metadata requirements consistently (including `metadata`) and explicitly define nullable `causation_id`.
3. Add and run negative/positive automated tests against the actual n8n Code node logic, including malformed envelope, missing required fields, wrong event version, wrong event type, invalid timestamp, and invalid optional fields.
4. Decide canonical request idempotency behavior and ensure retries cannot create duplicate research runs.
5. Approve/activate SK001 only after its evaluation fixtures pass and independent review is recorded; do not treat a draft mapping as authorization.
6. Resolve and health-check each research tool adapter; all remain planned.
7. Connect the actual A001 runtime and event persistence path, then capture execution ID, logs, output schema validation and persisted `research.completed` evidence.
8. Keep A001 `runtime_verified: false` until these conditions are met.

## Route guard

This A001 checkpoint supports source-attributed market research within the main business-plan system. Continue the canonical plan's cross-functional gap reconciliation and implementation across Sales, Marketing, Operations/Delivery, HR, Customer Success, Legal/Compliance, Technology/Data, Finance, QA, execution and monitoring. Do not narrow the project to finance or to agent documentation alone.

## Status

**Contract alignment implemented and statically read back; executable validation and runtime tests pending.**

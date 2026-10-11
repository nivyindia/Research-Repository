# Wave 15 — Market Research Contract Fixtures and Event Contract Draft — 2026-10-11

## Objective

Continue the canonical implementation roadmap after Wave 14 by specifying the next A001 Market Research Agent contract prerequisites without claiming runtime readiness.

## Work completed and committed

1. Added 12 SK001 contract fixtures at `Chats/ChatGPT/Multi Agent AIOS/03-skills/SK001-market-research/fixtures/contract-fixtures.yaml`.
   - Covers valid request; each required input missing; conflicting sources; stale time-sensitive source; unsupported material claim; unauthorized domain; timeout; empty evidence; broken evidence reference; incompatible currency/geography/market definitions; and AI-generated content incorrectly treated as independent corroboration.
   - Fixtures state expected outcomes and critical acceptance constraints.
2. Added draft event contracts at `Chats/ChatGPT/Multi Agent AIOS/06-data/event-schemas/research-events-v1.yaml`.
   - Defines proposed `market.research.requested` and `research.completed` event payload contracts and the canonical envelope fields.
   - Explicitly marked `draft`; not added to production `EVENT_REGISTRATION.yaml`, because the registration policy requires test evidence and review first.
3. Updated `Chats/ChatGPT/Multi Agent AIOS/03-skills/registry.yaml` so SK001 is `specified`, matching the existing canonical SKILL.md and newly authored fixtures. Added a note that it is untested, not approved/active, and still blocked by tool/runtime prerequisites.
4. Read back the new fixture and event-contract files from GitHub after commit to confirm that the expected paths and content are present.

## Commit evidence

- Fixtures commit: `15e399eb8aaa35bd5d0785fe5ee69ab8defc75df`
- Draft event contract commit: `90eaba4d4950b1aa3479d2a803f972b5d8af373a`
- SK001 registry status update commit: `4d1a732db697ef76c8fb4189cb9f6c9e9c0e363a`

## Important limits

- These are authored specifications and fixtures, **not executed tests**.
- No YAML/schema validator or agent runtime was executed in this step.
- The three A001 research tools remain `planned`; adapters, credentials, health checks, allowed-domain policy enforcement, and runtime wiring have not been demonstrated.
- `research.completed` is still a proposed event contract and is not production-registered or confirmed persisted by the event store.
- A001 `runtime_verified` must remain `false`; no agent status percentage may be advanced on the strength of documentation alone.

## Next gate (F.1.2)

1. Validate YAML syntax and the event payload schema using the project's actual validator; record tool/version and output.
2. Reconcile request/output payloads with `agents/market-research/agent.yaml`, the n8n workflow JSON, the event envelope and the data catalog. Resolve the required `causation_id` nullable semantics and confirm whether `request_id`/idempotency key is canonical.
3. Validate each agent → skill → tool mapping against the mapping contract. Planned tools do not satisfy activation requirements.
4. Run the 12 fixtures in an automated harness, including negative tests that prove no tool call occurs for invalid inputs and unauthorized domains.
5. Only after the contract and authorization tests pass, run one harmless public-source smoke test in an available runtime and capture execution ID, logs, source URLs, output validation and resulting event persistence.
6. Update A001 status only when the exact gate evidence exists. Keep the main business-plan roadmap as the canonical route; this work is a supporting research/provenance component, not a replacement for the cross-functional plan-system work.

## Status

**Specified / authored; validation and execution pending.** This checkpoint does not certify the agent as tested, integrated or production-ready.

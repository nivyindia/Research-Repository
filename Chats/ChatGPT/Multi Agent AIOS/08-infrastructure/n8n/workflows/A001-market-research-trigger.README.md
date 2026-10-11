# A001 n8n Trigger Integration

## Purpose

Connect the registered A001 Market Research Agent to an n8n event boundary for F.1.3. This workflow remains inactive until imported, reviewed, connected to an actual executor, and tested in the target n8n instance.

## Trigger contract

- Method: `POST`
- Path: `/webhook/aios/a001/market-research`
- Event type: `market.research.requested`
- Event version: `1.0`
- Required envelope fields: `event_id`, `event_type`, `event_version`, `occurred_at`, `source`, `company_id`, `entity_type`, `entity_id`, `correlation_id`, `payload`, `metadata`
- `causation_id` may be null when no causative event is known.
- Required payload fields: `research_question`, `target_market`
- Optional payload fields: `geography`, `industry`, `customer_segment`, `time_horizon`, `competitor_set`, `source_policy`, `output_format`
- Agent: `A001`

The workflow code fails closed on a wrong event type/version, missing envelope identifiers, invalid timestamp, missing required payload fields, and malformed `source_policy` or `competitor_set`. It does not generate a replacement event ID for malformed requests.

## Execution boundary

The current JSON validates and normalizes the incoming envelope, then reaches a placeholder runtime-boundary node. The boundary explicitly marks `runtime_invoked: false` and `status: validated_pending_runtime`. It does **not** execute A001 or claim that research completed.

A real F.1.3 completion requires:

1. Import and review this workflow in the AIOS n8n instance.
2. Connect the runtime-boundary node to the actual registered A001 executor (LangGraph/AIOS runtime or the approved equivalent).
3. Verify tool registration, authorization, allowed-domain enforcement and health checks before allowing research tool calls.
4. Send a valid `market.research.requested` event and negative test envelopes.
5. Capture the n8n execution ID, agent logs, validated report, and persisted `research.completed` event.
6. Record test results and event-store evidence in the A001 status/test log.

Until steps 1–6 have been performed against a live runtime, F.1.3 must not be marked complete and A001 `runtime_verified` must remain `false`.

## Contract alignment note

The trigger uses the canonical event envelope described in `06-data/event-schemas/README.md` and the proposed A001 payload draft in `06-data/event-schemas/research-events-v1.yaml`. That event file remains a draft and is not production-registered; the integration is therefore not approved for production use.

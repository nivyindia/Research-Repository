---
skill_id: SK001
name: Market Research
version: "1.0"
status: specified
owner_role: research_operations
classification: internal_reusable_capability
portable: true
---

# SK001 — Market Research Skill

## 1. Purpose

Produce a source-attributed, decision-grade market research evidence pack that downstream agents and business-plan workflows can reuse. This is a reusable capability, not a standalone autonomous agent and not a substitute for legal, tax, investment, or other qualified professional review.

## 2. Lifecycle status

**Specified, not approved for runtime use.** This file defines intended behavior and contracts. It does not prove that tools, credentials, adapters, policies, or runtime integrations exist. Activation requires registry review, security/permission review, contract tests and recorded evaluation evidence.

## 3. Inputs

Required:
- `research_question`: non-empty string stating the decision or question to investigate.
- `target_market`: non-empty string identifying the market, industry, audience, or business context.

Optional:
- `geography`: geography/jurisdiction.
- `industry`: industry definition.
- `customer_segment`: target segment.
- `time_horizon`: period relevant to the decision.
- `competitor_set`: named competitors, if known.
- `source_policy`: allowed source classes/domains and exclusions.
- `output_format`: requested output shape.

Reject missing required inputs. Do not silently fill missing market scope or decision context with assumptions; ask for clarification or return a structured input error.

## 4. Output contract

Return a `market_research_report` with:
- `schema_version`
- `research_question`
- `scope` (market, geography, segment, time horizon, exclusions)
- `findings[]` (finding ID, claim, claim type, evidence grade, confidence, as-of date)
- `evidence[]` (evidence ID, source title, canonical URL, publisher, publication date if known, access/research date, source type, relevant excerpt/summary, support relationship)
- `implications[]` (decision implication, linked finding IDs, caveats)
- `assumptions[]` (assumption ID, statement, reason, owner/reviewer if known, confidence, validation action)
- `contradictions[]` (claims that conflict, sources, resolution or unresolved state)
- `gaps[]` (unknown, why material, next research action)
- `confidence` (high/medium/low plus rationale; not a success probability)
- `researched_at` (timestamp with timezone)
- `limitations` and `review_required`

Each material finding must link to one or more evidence IDs. An unsupported material claim must be removed, clearly labeled as a hypothesis, or recorded as unresolved.

## 5. Procedure

1. Validate required inputs and policy scope.
2. Translate the request into research objectives and explicit definitions.
3. Build a source plan prioritizing primary/official sources and method-transparent secondary sources.
4. Collect only through registered, authorized, read-scoped tools and approved public sources.
5. Preserve source URL, publisher, dates, evidence excerpt/summary and retrieval time.
6. Normalize currency, units, dates, geography and market definitions; do not combine incompatible definitions silently.
7. Cross-check material claims using independent sources where practical.
8. Record contradictions and stale/weak evidence rather than hiding them.
9. Separate observed facts, estimates, interpretations, hypotheses and recommendations.
10. Assign evidence grade A–D and confidence with a short rationale.
11. Validate output schema and claim-to-evidence links.
12. Return a report with limitations and next research actions; do not execute downstream business actions.

## 6. Evidence grading

- **A:** authoritative primary source, official statistics, regulator, audited disclosure or original dataset.
- **B:** reputable secondary source with transparent method and clear provenance.
- **C:** credible public signal with partial independent verification.
- **D:** weak, stale, promotional or uncorroborated signal; never use alone to support a material conclusion.

Evidence grade describes the source/evidence, while confidence describes the strength of the conclusion given quality, recency, consistency and coverage.

## 7. Tool and security boundary

Only use tools explicitly approved for this skill and mapped through the chain Agent → Skill → Tool → Action. Intended candidates for A001 are:
- `TOOL-FIRECRAWL-EXTRACT` — structured extraction from approved public URLs.
- `TOOL-BROWSER-USE-RESEARCH` — bounded public-source research.
- `TOOL-POSTGRES-QUERY-READONLY` — read-only retrieval of explicitly authorized internal research records.

All three are currently recorded as planned in the tool registry. Therefore this skill must not invoke them until registry status, adapters, health checks, permissions, allowed-domain restrictions, and tests are approved. Do not bypass the skill/tool authorization layer.

Prohibited:
- Unauthorized credentialed access or bypass of access controls.
- Collecting private personal data outside an explicitly authorized lawful purpose.
- Fabricating sources, statistics, market sizes, quotes or findings.
- Treating AI-generated content as independent corroboration.
- Writing to CRM/database or changing system state.
- Sending messages, purchasing data, or publishing externally.
- Presenting unsupported forecasts as observed facts.

## 8. Failure behavior

Fail closed with a structured error when required inputs are absent, authorization fails, an approved tool is unavailable, source access is prohibited, evidence is inadequate for the requested claim, or the output schema fails validation. Preserve partial findings only if clearly marked incomplete and every retained claim remains traceable.

Retry transient failures only within the agent's bounded retry policy. Do not retry authorization or policy failures as if they were transient.

## 9. Evaluation requirements before activation

Required fixture categories:
1. Valid scoped research request.
2. Missing `research_question`.
3. Missing `target_market`.
4. Conflicting source claims.
5. Stale source on a time-sensitive claim.
6. Material claim without supporting evidence.
7. Unauthorized domain/tool request.
8. Tool timeout/transient error.
9. Empty or insufficient evidence.
10. Invalid output schema or broken claim-to-evidence reference.

Acceptance checks:
- Required inputs validated.
- Every material finding has valid evidence references.
- Dates and source URLs are preserved.
- Conflicting claims remain visible until resolved.
- Facts, estimates, assumptions and recommendations are distinguishable.
- Unauthorized actions fail closed.
- Output conforms to the versioned contract.
- Run logs and test evidence are recorded.
- Independent review approves activation.

## 10. Dependencies and lifecycle

Dependencies: A001 agent contract, skill registry, agent-skill mapping, tool registry/adapters, allowed-source policy, data/evidence schema, event contract if emitted, audit/logging and evaluation fixtures.

Lifecycle: `draft → specified → reviewed → approved → tested → active → deprecated`. A file's existence or a registry row does not imply activation. Never set `active` without test evidence and approval.

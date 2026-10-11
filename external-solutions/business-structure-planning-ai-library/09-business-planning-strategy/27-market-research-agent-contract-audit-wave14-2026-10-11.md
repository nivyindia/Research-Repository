# Market Research Agent Contract Audit — Wave 14
**Updated:** 2026-10-11  
**Roadmap phase:** Phase 1 — exact-file qualification; supports Phase 2 common evidence/data contracts  
**Agent:** A001 — Market Research Agent  
**Scope:** Static inspection of exact repository files only. No agent runtime was executed; no external tool was called through the agent; no production behavior is verified.

## 1. Exact files inspected

| Artifact | Exact path | Static result |
|---|---|---|
| Agent definition | `Chats/ChatGPT/Multi Agent AIOS/agents/market-research/agent.yaml` | Defined required inputs, report output fields, workflow, tools, policies, observability, retries and success criteria |
| Agent prompt | `Chats/ChatGPT/Multi Agent AIOS/agents/market-research/prompt.md` | Detailed scope/source/collect/normalize/cross-check/synthesize/confidence/report procedure; evidence grades A–D; explicit stop conditions |
| Tool allow-list | `Chats/ChatGPT/Multi Agent AIOS/agents/market-research/tools.yaml` | Default-deny allow-list for Firecrawl extraction, bounded browser research and read-only PostgreSQL |
| Agent status | `Chats/ChatGPT/Multi Agent AIOS/02-agents/F1-A001-status.yaml` | Stage F / micro-step F.1.1; status 25 means definition and prompt finalized; `runtime_verified: false`; next step F.1.2 |
| Skill registry | `Chats/ChatGPT/Multi Agent AIOS/03-skills/registry.yaml` | Explicitly a registry skeleton; SK001 Market Research and SK002 ICP Definition are both `planned` |
| Agent-skill contract | `Chats/ChatGPT/Multi Agent AIOS/02-agents/AGENT_SKILL_MAPPING.md` | Requires registered, active/approved, compatible skills and passing integration tests; missing/ambiguous mappings must fail closed |
| Tool registry | `Chats/ChatGPT/Multi Agent AIOS/04-tools/TOOL_REGISTRY.yaml` | A001's three tool IDs have registry entries with schemas, owner/version, healthcheck requirements and safety constraints; entries are `planned`, not operationally verified |

## 2. What is already strong

- The agent has explicit required inputs (`research_question`, `target_market`) and a structured output contract.
- The prompt separates observed facts, estimates, interpretations, hypotheses and recommendations.
- Material claims require provenance and cross-checking; confidence and uncertainty must be explicit.
- Tool access follows the default-deny Agent → Skill → Tool → Action chain.
- Research is limited to approved/public sources; unauthorized credentialed access, private personal-data collection, fabricated claims and bypassing source controls are prohibited.
- External publication and policy exceptions require human approval.
- Observability metrics and bounded retry/failure behavior are specified.

These are specification strengths only; they are not proof of runtime compliance.

## 3. Blocking findings

| Finding | Severity | Evidence | Required resolution |
|---|---|---|---|
| A001 requires SK001, while SK001 is still marked `planned` | P0 | Agent YAML + skill registry | Create/verify the canonical skill definition, register its version/status and pass skill-contract validation; otherwise fail closed |
| A001 optionally resolves SK002, which is also `planned` | P1 | Agent YAML + skill registry | Keep SK002 disabled/unavailable until its definition, input/output contract and compatibility are approved; optional must not silently imply executable |
| All three A001 tool registry entries are `planned` | P0 | Tool registry | Verify actual adapters, credentials/secrets handling, allowed-domain enforcement, read-only database guard, healthchecks, logs and error handling in a safe environment |
| Tool schemas are abstract YAML contracts, not executable proof | P0 | Tool registry | Add schema-validation fixtures and adapter contract tests, including malformed input, unauthorized domain, empty result, timeout and tool failure |
| The agent status is not runtime verified | P0 | Status YAML | Do not advance to tested/accepted; run only after SK/tool prerequisites are resolved and a harmless public-data test is approved |
| Event output is named `research.completed`, but the event schema/registration and persistence path were not inspected in this pass | P1 | Agent YAML; data catalog lists event schemas as canonical | Resolve the exact registered event schema and validate emitted payload, required fields, provenance references and idempotency/correlation metadata |
| Cross-agent handoff compatibility is not yet proven | P1 | A001 outputs + downstream SK002/ICP and plan research needs | Define a shared evidence record and demonstrate that downstream consumers can reference claims/sources without losing source dates or confidence |

## 4. Required next micro-step: F.1.2

Keep the existing status record at its current verified level until these checks have evidence. The next safe work package is:

1. Inspect the full tool registry entries for Firecrawl, Browser Research and PostgreSQL Readonly; confirm the tool IDs match A001's allow-list exactly.
2. Locate or create a canonical SK001 definition only after checking for an existing equivalent; do not duplicate the skill or reuse its ID for another purpose.
3. Validate agent → skill → tool mappings against the registry contract; `planned` must not satisfy the active/approved prerequisite.
4. Inspect the registered `research.completed` event schema and relevant data contracts.
5. Write input/output JSON/YAML fixtures covering valid request, missing required input, conflicting sources, stale source, unsupported material claim, unauthorized domain, tool timeout and empty evidence.
6. Only after contract validation, execute a harmless public-source smoke test in the authorized runtime. Capture run ID, timestamp, inputs, source URLs, output schema validation, claim/source coverage, tool logs and failure behavior.
7. If smoke test passes, expand to the planned 10-case golden set; report every failure and keep the agent non-production until the acceptance gate passes.

## 5. Roadmap mapping

| Stable gap / register item | Impact of this audit | Status change |
|---|---|---|
| G04 Market research | Source-attribution design inspected; runtime unverified | No upgrade |
| G33 Research provenance | Agent requirements are explicit; end-to-end trace not tested | No upgrade |
| G34 Assumption management | Research output contract mentions assumptions/gaps, but shared assumption schema is not verified | No upgrade |
| G36 Independent plan QA | Agent's self-checks are not an independent evaluator | No upgrade |
| G38 Citation/source QA | Provenance requirements specified; source freshness/broken-link checks not tested | No upgrade |
| G55 International localization | Geography is an input; country-specific research behavior and legal/tax overlays are not validated | No upgrade |
| Initial register RES-01 | Research plan/evidence design specified; conflicting/stale-source fixture not run | No upgrade |
| Initial register INTG-01 | Shared orchestration contract still unproven | No upgrade |

## 6. Acceptance gate

A001 may be marked **tested** only after skill and tool prerequisites are active/approved, schemas validate, the smoke test passes with traceable sources, failure cases fail closed, and logs are preserved. It may be marked **accepted** only after the golden test set and independent review pass. Production readiness additionally requires permission/security review, monitored failure handling and a human-approved release record.

## 7. Route and continuity

No roadmap route change. This is Phase 1 exact-file qualification for the highest-value research/evidence layer. Return point is F.1.2 contract resolution, then a controlled smoke test; afterward resume the broader requirement matrix and other P0 modules. Finance validation remains a parallel P0 blocker, and this agent audit does not close it.

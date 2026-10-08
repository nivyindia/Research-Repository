# 8D Universal Definition Framework

## Why 8 blocks (not 20+)

Research across RACE, SOSTAC, OKR, RACI, BPMN, ITIL, playbook standards, and agent schemas shows that human-usable definitions collapse into eight stable concerns. Extra fields belong in machine metadata, not in the definition document.

## The 8 Blocks

### 1. WHY
- Purpose (why this exists in the system)
- Objective (what success looks like)
- Expected outcome (business / marketing result)

### 2. WHAT
- Scope (in / out)
- Inputs (data, decisions, upstream artifacts)
- Outputs (deliverables, artifacts, signals)

### 3. HOW
- Process (high-level steps)
- SOP (detailed, repeatable procedure) — may link to Component Library
- Workflow (system + human sequence)

### 4. WHO
- Owner (role)
- Human responsibilities
- AI Agent responsibilities
- RACI where multi-party

### 5. WITH WHAT
- Tools / software (prefer library IDs)
- Resources (docs, training, official sources)
- APIs / data sources

### 6. AUTOMATE
- What can be automated today
- AI skills required
- AI agents that can own or assist
- Integrations / triggers / webhooks / MCP

### 7. MEASURE
- Primary KPIs
- Quality criteria
- Cost / effort
- ROI or contribution model

### 8. IMPROVE
- Feedback loops
- Optimization levers
- Reuse opportunities
- Scale path (geo, channel, volume)

## Document template (Markdown)

```markdown
# [Topic Name]

**ID:** DM-L1-XX-L2-YY-...
**Status:** stub | researched | defined | automated | agent-ready
**Canonical path:** ...

## 1. WHY
...

## 2. WHAT
...

## 3. HOW
...

## 4. WHO
...

## 5. WITH WHAT
...

## 6. AUTOMATE
...

## 7. MEASURE
...

## 8. IMPROVE
...

## References
- Component Library links
- Official sources
- Related topics (references only)
```

## Frontmatter (machine-readable)

See `../06-METADATA/00-METADATA-SCHEMA.md` for YAML fields (id, depends_on, inputs, outputs, tools, agents, kpis, geo_tags, business_models, etc.).

# Integration Contracts & AIOS — Company OS V7

**Code:** ALL-STRAT-006  
**Title:** Integration Contracts, AI Agent Registry, and Research→Operational Knowledge Flow  
**Department:** ALL / TECH / DATA  
**Type:** STRAT  
**PARA Bucket:** Resource  
**Version:** v1.0  
**Lifecycle Status:** Draft  
**Confidentiality:** Internal  
**Owner (Accountable):** CTO / Workspace Admin  
**Responsible:** TECH / DATA  
**Created Date:** 2026-10-03  
**Last Updated:** 2026-10-03  
**Next Review:** 2027-01-03  
**Tags:** integration, AIOS, agents, research, automation  
**Related Documents:** Canonical-Object-Model.md, Operational-Workflows-Model.md, GOVERNANCE/10-GitHub-Actions-Automation-Map.md, GOVERNANCE/05-Repository-Branch-Workflow.md  
**Related Diagrams:** NIVY-AIOS-ARCHITECTURE, NIVY-AUTOMATION-INTEGRATION-MAP, NIVY-RESEARCH-KNOWLEDGE-LIFECYCLE, NIVY-DATA-KNOWLEDGE-ARCHITECTURE

> **Purpose:** Centralize integration contracts, AI agent definitions, and the Research → Canonical → Operational promotion path.  
> **Rule:** REUSE existing diagrams, Doc 10 workflows, Research-Inbox, Classifier-Skill. Do not invent a second automation stack.

---

## P17 — Integration contracts

### Contract schema (every integration)

```
ID: INT-[nnn]
Name:
Source system:
Destination system:
Objects exchanged: (canonical object IDs / types — Customer, Task, Document, …)
Trigger: (event / schedule / manual)
Direction: Push | Pull | Bidirectional
Action: (create / update / classify / notify / …)
Owner (Accountable):
Department:
Auth method: (OAuth / API key / GitHub App / …) — store secrets outside repo
Evidence: (log location / audit trail)
Failure / retry / escalation:
Status: Planned | Active | Deprecated
Version:
```

### Contract register (seed)

| ID | Name | Source → Destination | Objects | Trigger | Owner | Status |
|---|---|---|---|---|---|---|
| INT-001 | Research-Inbox classify → Company-OS PR | Research-Inbox → Company-OS | Document | New dump item | Workspace Admin | Active (classify-and-pr.yml) |
| INT-002 | Metadata validation on PR | GitHub PR → CI | Document metadata | PR open/sync | Workspace Admin | Active |
| INT-003 | Naming / folder validation | GitHub PR → CI | Document path/name | PR | Workspace Admin | Active |
| INT-004 | Link check | Repo → CI report | Internal links | PR / schedule | Workspace Admin | Active |
| INT-005 | Orphan detection | Repo → Issue/report | Document graph | Schedule | Workspace Admin | Active |
| INT-006 | Health report | Repo metadata → Issue + metrics | Next Review, Owner, Draft age | Weekly | Workspace Admin | Active |
| INT-007 | Dashboard generate | Repo → dashboard.md | Health metrics | Weekly / manual | Workspace Admin | Active |
| INT-008 | Ownership matrix generate | Repo → Ownership-Matrix.md | Owner fields | Push main | Workspace Admin | Active |
| INT-009 | Publish sync | Company-OS → Wiki/Notion | Published docs with publish:true | Merge main | Workspace Admin | Scaffold (needs target API) |
| INT-010 | Stale PR/Issue reminders | GitHub → comments | PR/Issue | Schedule | Workspace Admin | Active |
| INT-011 | CRM ↔ Customer master | CRM ↔ Company OS IDs | Customer, Opportunity | Event | Head of Sales / CTO | Planned |
| INT-012 | HR ↔ Person/Role | HR/ATS ↔ Company OS | Person, Role | Event | CHRO / CTO | Planned |
| INT-013 | Finance ↔ billing records | Accounting ↔ FIN Records | Invoice, Payment, Customer | Event | CFO / CTO | Planned |
| INT-014 | Email / Calendar intake | Email/Cal → Tasks/Meetings | Task, Meeting | Message / event | Ops | Planned |
| INT-015 | WhatsApp / comms intake | WhatsApp → triage | Lead, Issue, Task | Message | Sales/CS / CTO | Planned |
| INT-016 | TickTick / PM task sync | Task tool ↔ Task objects | Task, Work | Sync | PMO | Planned |
| INT-017 | AI agent actions | Agent → systems (via INT-*) | Varies | Agent trigger | Agent Owner | Planned per agent |

**Rule:** New systems get an INT row before production write access. Canonical object IDs (CUST-, PERS-, PROJ-, document codes) are the cross-system keys.

---

## P18 — AI agent registry

Aligned to **NIVY-AIOS-ARCHITECTURE** (Goals → Knowledge → Applications → Integration → Agents → Models → Execution → Observability → Control).

### Agent record schema

```
ID: AGENT-[nnn]
Name:
Purpose:
Owner (Accountable):
Department:
Trigger: (schedule / event / user request / webhook)
Inputs: (systems, document types, data fields)
Tools: (APIs, MCP, search, write targets)
Permissions: (read / draft / comment only / …)
Outputs: (PR, comment, draft doc, classification, …)
Human approval required: Always | On write | On high-risk | Never (discouraged)
Logging / audit: (where actions are recorded)
Failure / escalation: (retry, alert Owner, open Issue)
Version:
Status: Draft | Active | Retired
Linked Integration IDs:
```

### Agent register (seed)

| ID | Name | Purpose | Owner | Trigger | Outputs | Human approval | Status |
|---|---|---|---|---|---|---|---|
| AGENT-001 | Research Classifier | Classify Research-Inbox dump → dept/type/code/metadata | Workspace Admin | New dump file | PR into Company-OS | Always (merge) | Active (classify-and-pr + Classifier-Skill) |
| AGENT-002 | Doc Health Assistant | Summarize health metrics / suggest fixes | Workspace Admin | Weekly report / on demand | Issue comment / draft notes | On write | Planned |
| AGENT-003 | SOP Explainer | Explain published SOPs in plain language | Dept Owner | User query | Answer + source citation | Read-only preferred | Planned |
| AGENT-004 | Sales Research Enrichment | Enrich prospect data from allowed sources | Head of Sales | New lead / batch | Draft CRM fields | On write to CRM | Planned |
| AGENT-005 | Meeting Notes Structurer | Turn raw notes into MEET doc + action Tasks | Ops / Admin | Meeting end | Draft MEET + Task list | Always | Planned |

**Golden rule (Doc 05 / Doc 07):** AI proposes and classifies; authorized humans approve governance and production writes. Agents never merge to `main` or change Published policy without human approval.

---

## P19 — Research → Canonical → Operational knowledge

Aligned to **NIVY-RESEARCH-KNOWLEDGE-LIFECYCLE**:

```
Research question
  → Source discovery
    → Raw capture (provenance)
      → Ingest / normalize
        → Classify / deduplicate
          → Evaluate (quality, license, confidence)
            → Transfer-ready
              → Canonical repository (Company-OS)
                → Operational publication (SOP, Notion, diagram, AIOS)
                  → Feedback / refresh → archive
```

### Promotion path (implemented pieces)

| Stage | Where | Automation |
|---|---|---|
| Raw capture | `Research-Inbox/dump/` | Human or agent drop |
| Classify | Classifier-Skill + classify-and-pr.yml | AGENT-001 |
| Transfer-ready → Canonical | PR into Company-OS correct folder | Human merge |
| Canonical | Company-OS with Doc 04 metadata | validate-metadata / naming |
| Operational publication | publish-sync.yml when `publish: true` + Approved/Published | INT-009 (scaffold) |
| Feedback | Next Review, health-report, Issues | INT-006 |

### Promotion rules

1. Research material is **not** official until merged as Approved/Published in Company-OS.
2. Every promoted document keeps provenance (source link or Research-Inbox path in Related Documents / Evidence).
3. Operational copies outside GitHub (Notion/Wiki) are **publications** of the canonical file, not independent masters (Doc 07 Canonical-Source Rule).
4. Stale research branches / dump items >60 days without activity are flagged (Doc 07 / health checks).

---

## Observability & control (shared)

| Concern | Mechanism |
|---|---|
| Logs | GitHub Actions logs, PR bodies, agent audit fields |
| Evidence | REC documents, commit SHAs, workflow run IDs |
| KPI | Doc health metrics; future agent success/failure rates |
| Permissions | CODEOWNERS, Confidentiality, agent Permissions field |
| Escalation | Agent Failure path → Issue → Exception/Decision (P14/P27) |

---

## Phase 6 exit check

| Item | Evidence |
|---|---|
| Integration contract schema + seed register | §P17 |
| Active GitHub automations mapped to INT-001…010 | Doc 10 + §P17 |
| Planned CRM/HR/Finance/Email/WhatsApp/PM contracts | INT-011…016 |
| AI agent schema + seed agents | §P18 |
| Research→Canonical→Operational path | §P19 + Research-Inbox + Classifier |
| Human approval boundary | Explicit on every agent; Doc 05/07 |

---

## What was reused vs. created

| Reused | Created |
|---|---|
| AIOS, Automation Integration, Research Knowledge diagrams | Integration contract schema + register |
| Doc 10 + all listed workflows | AI agent schema + register |
| Research-Inbox, Classifier-Skill | Promotion rules tying research lifecycle to Company-OS |
| Doc 05 AI rules, Doc 07 Canonical-Source | — |

No second AI platform or integration hub was created inside the repo.

---

## Open items (not blockers for Phase 6 exit)

- Notion/Wiki API credentials for INT-009
- CRM/HR/Finance system selection and API wiring (INT-011…013)
- Activate planned agents (002–005) with explicit Owner approval
- Agent runtime hosting decision (n8n / MCP / other) under CTO

# Company OS Health & Automation Control — V7

**Code:** ALL-STRAT-007  
**Title:** Company OS Health Dashboard and Automation Control Surface  
**Department:** ALL  
**Type:** STRAT  
**PARA Bucket:** Resource  
**Version:** v1.0  
**Lifecycle Status:** Draft  
**Confidentiality:** Internal  
**Owner (Accountable):** Workspace Admin / CTO  
**Responsible:** Workspace Admin  
**Created Date:** 2026-10-03  
**Last Updated:** 2026-10-03  
**Next Review:** 2027-01-03  
**Tags:** health, automation, audit, dashboard, workflows  
**Related Documents:** GOVERNANCE/10-GitHub-Actions-Automation-Map.md, GOVERNANCE/07-Governance-Health-AI-Policy.md, dashboard.md, Integration-Contracts-and-AIOS.md  

> **Purpose:** Single control surface for Phase 8 — every health check and automation path mapped to an implemented workflow.  
> **Rule:** REUSE existing `.github/workflows`. Do not invent parallel CI.

---

## P29 — Health / audit dashboard

### Primary surfaces

| Surface | Path | Generator |
|---|---|---|
| Documentation health dashboard | `03_RESOURCES/Company_Master_Standards/dashboard.md` | `dashboard-generate.yml` |
| Weekly health Issue | GitHub Issues (from Action) | `health-report.yml` |
| Ownership matrix | `Ownership-Matrix.md` | `ownership-matrix-generate.yml` |
| This control map | This document | Manual / Phase gate |

### Dashboard metrics (Doc 07 §9)

| Metric | Detection |
|---|---|
| Total Documents | File scan |
| Outdated (past Next Review) | `Next Review` field vs date |
| Awaiting Review | Lifecycle Status = Under Review |
| Unowned | Missing Owner field |
| Draft stuck >30 days | Status Draft + age |
| Published | Status count |
| Broken Internal Links | `check-links.yml` |

---

## Automation checklist (Phase 8 requirements)

| Requirement | Workflow / mechanism | Status |
|---|---|---|
| Metadata validation | `validate-metadata.yml` | ✅ Active |
| Naming validation | `validate-naming.yml` | ✅ Active |
| Orphan detection | `orphan-detection.yml` | ✅ Active |
| Missing-owner detection | `health-report.yml` + ownership matrix | ✅ Active |
| Missing-link detection | `check-links.yml` | ✅ Active |
| Stale-content detection | `health-report.yml` (Draft age, Next Review) + `stale-check.yml` (PR/Issue) | ✅ Active |
| Research Inbox | `Research-Inbox/dump/` + classify-and-pr (Inbox repo) | ✅ Active |
| Classification | Classifier-Skill + classify-and-pr / AGENT-001 | ✅ Active |
| PR / merge workflow | Branch protection + CODEOWNERS + `auto-label.yml` + `inbox-merge-confirmation.yml` | ✅ Active (handles placeholders) |
| Supersession | Doc 04 `Superseded By` + health-report deprecation reminder (Doc 10) | ✅ Defined |
| Archive | `04_ARCHIVE/` + Doc 04 Retired move | ✅ Structure present |
| Health dashboard | `dashboard-generate.yml` + `dashboard.md` | ✅ Active |
| Publication workflow | `publish-sync.yml` | ⚠️ Scaffold — needs Notion/Wiki target |

### Deprecated

| Item | Note |
|---|---|
| `inbox-classify.yml` (Company-OS) | Deprecated stub; real engine is Research-Inbox `classify-and-pr.yml` |

---

## Operating rhythm

| Cadence | Action |
|---|---|
| On every PR | validate-metadata, validate-naming, check-links, auto-label |
| Weekly | health-report, dashboard-generate, stale-check |
| On push to main | ownership-matrix-generate; publish-sync if tagged |
| On Inbox dump | classify-and-pr → human merge |
| Quarterly | Full audit per Doc 04 Governance table |

---

## How to run health now

1. Open Company-OS GitHub Actions (when repo is split/deployed as its own GitHub repo per package design).
2. Run **Generate Documentation Health Dashboard** manually.
3. Read `dashboard.md` and any Issue opened by health-report.
4. Fix unowned / outdated / broken links; re-run.

*Note: While nested under Research-Repository, Actions paths assume Company-OS as workflow root — deploy Company-OS (and Research-Inbox) as intended separate repos for full CI effect, or adjust paths if running monorepo CI later.*

---

## Failure / escalation

| Signal | Response |
|---|---|
| CI validation fail | Block merge until fixed |
| Health Issue opened | Workspace Admin triages within weekly cycle |
| Orphan / unowned spike | Assign Owners; escalate to Ops Head if unresolved 2 cycles |
| Publish-sync fail | Log + Owner; do not treat external copy as master |
| Agent/classify error | PR not opened or marked failed; human re-run |

---

## Phase 8 exit check

| Item | Evidence |
|---|---|
| All listed health checks have an owner workflow | Table above |
| P29 dashboard surface identified | dashboard.md + generators |
| No parallel automation stack | Reused Doc 10 + existing yml only |
| Publication gap explicit | publish-sync scaffold / INT-009 |
| Archive path exists | 04_ARCHIVE (Phase 5) |

---

## Open items (not blockers)

- Configure Notion/Wiki credentials on publish-sync
- Real CODEOWNERS handles
- Confirm CI root when Company-OS is published as standalone repo
- Optional: monorepo workflow path adaptation if staying nested long-term

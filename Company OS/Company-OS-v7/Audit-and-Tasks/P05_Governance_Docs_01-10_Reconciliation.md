# P05 — Governance Docs 01–10 Reconciliation

**Date:** 2026-10-03  
**Phase:** 0 — Baseline and Authority  
**Status:** COMPLETE (verified against actual files)  
**Canonical location:** `Company OS/Company-OS-v7/Company-OS/03_RESOURCES/Company_Master_Standards/GOVERNANCE/`

---

## 1. Inventory — all 10 documents present

| Doc | Filename | Size (approx) | Status in file | Reconciliation result |
|---|---|---|---|---|
| 01 | 01-Department-Code-Registry.md | ~2.5 KB | Present | **CANONICAL** — Department + Brand codes. Section C brand list partially filled; 4 tentative codes remain open (human confirm). |
| 02 | 02-Document-Type-Code-Registry.md | ~2.2 KB | Present | **CANONICAL** — 12 document types. Matches Classifier-Skill JSON (verified in prior audit). |
| 03 | 03-Folder-Structure-Map.md | ~4.0 KB | Present | **CANONICAL** — PARA structure + per-department folders including Strategy/ and Forms/ (M2 applied). |
| 04 | 04-Classification-Naming-Rulebook.md | ~5.3 KB | Approved | **CANONICAL** — Metadata header includes Confidentiality + Next Review (Doc 09 plan applied). Lifecycle enum matches workflows. |
| 05 | 05-Repository-Branch-Workflow.md | ~14.8 KB | Present | **CANONICAL** — Multi-company / branch / Research-Inbox model. Unchanged by Doc 09. |
| 06 | 06-Navigation-Standard.md | ~20 KB | FINAL | **CANONICAL** — Explicitly built on Doc 03 folder names. Doc 09 rewrite applied. |
| 07 | 07-Governance-Health-AI-Policy.md | ~7.2 KB | Present | **CANONICAL** — Health dashboard metrics, ownership matrix claim, AI rules. Ownership-matrix workflow now exists (M4 applied). |
| 08 | 08-Audit-New-vs-Repeated.md | ~6.3 KB | Present | **CANONICAL** — Audit checklist. Cross-references Docs 04/07. |
| 09 | 09-Final-Change-Plan.md | ~7.4 KB | Plan (pre-edit) | **HISTORICAL / SUPERSEDED as instruction** — Was the change plan for Docs 04/06/07. Changes applied in live files. Keep as audit evidence; do not treat as active directive. |
| 10 | 10-GitHub-Actions-Automation-Map.md | ~7.5 KB | Present | **CANONICAL** — Maps workflows to claims. Updated in v6 for deprecated inbox-classify and dashboard entry. |

---

## 2. Doc 09 vs live state (key conflicts resolved)

| Planned change (Doc 09) | Actual live state | Verdict |
|---|---|---|
| Doc 04: add Confidentiality field | Present in Required Metadata Header | **Applied** |
| Doc 04: Next Review (via later H2) | Present in header + Recurring Maintenance table | **Applied** |
| Doc 06: rewrite to use Doc 03 names | Doc 06 marked FINAL; uses `01_AREAS`, `Policies/`, etc. | **Applied** |
| Doc 07: trim duplicates, keep health/AI | Live Doc 07 retains health metrics + AI policy; ownership matrix automation exists | **Applied / consistent** |
| Docs 01, 02, 03, 05: no structural change | Unchanged as planned | **Confirmed** |

**Authority rule:** Live Docs 01–08 + 10 are the active standards. Doc 09 is retained as historical planning evidence only.

---

## 3. Workflow vs governance claims (spot-check from prior v6 audit + current tree)

| Claim | Workflow | Status |
|---|---|---|
| Lifecycle status enum includes "Under Review" | dashboard-generate.yml | Fixed (H1) |
| Next Review field used for outdated metric | health-report.yml, dashboard-generate.yml | Field now in Doc 04; workflows use it |
| Confidentiality value validation | validate-metadata.yml | Value check added (M1) |
| Naming regex allows PROJ-DOC alphanumeric | validate-naming.yml | Fixed (H3) |
| Strategy/ + Forms/ folder placement | validate-naming.yml + Doc 03 | Fixed (M2) |
| Ownership matrix auto-update | ownership-matrix-generate.yml | Exists (M4) |
| inbox-classify.yml deprecated | Map + stub | Documented |

Remaining open from v6: **L3 CODEOWNERS real handles** (human input).

---

## 4. Cross-document consistency checks performed

- Doc 01 department codes ↔ Classifier-Skill `departments.json` (prior verification held).
- Doc 02 document types ↔ Classifier-Skill `document-types.json` (prior verification held).
- Doc 03 folder names ↔ Doc 06 navigation paths (aligned).
- Doc 04 metadata header ↔ validate-metadata.yml required fields + Confidentiality values (aligned).
- Doc 04 lifecycle enum ↔ dashboard / health workflows (aligned after H1).
- Doc 07 health metrics ↔ dashboard-generate.yml (aligned).
- Doc 10 automation map ↔ actual `.github/workflows/` files present under Company-OS.

---

## 5. Disposition of Doc 09

- **Classification:** Historical planning document / superseded as active instruction.
- **Action:** Leave in place. Add a short status banner is optional; not required for Phase 0 exit.
- **Reference:** Future changes to governance must update the live numbered docs, not re-open Doc 09 as a change plan.

---

## 6. Validation evidence

- Directory listing of GOVERNANCE/ confirms exactly 10 files (01–10).
- Content inspection of Doc 04, Doc 06, Doc 09, Doc 10.
- Cross-check against CHANGELOG_v6-consolidated.md (H1–M4, L1–L2 applied).
- Cross-check against Company_OS_v6_Audit_and_Implementation_Plan.md status note.

---

## 7. Residual gaps (not Phase 0 blockers)

1. Brands / Department Code Registry Section C — 4 tentative brand codes need human confirmation.
2. CODEOWNERS placeholder handles (L3).
3. No formal "Status: ACTIVE" banner on every governance doc (cosmetic; content is authoritative).
4. Doc 09 still reads as a forward plan; readers must consult this reconciliation for current status.

---

## 8. Files created/modified by this task

- Created: `Audit-and-Tasks/P05_Governance_Docs_01-10_Reconciliation.md`

**Phase 0 exit criteria met:** One authoritative baseline; version disposition recorded; governance docs reconciled to actual files.

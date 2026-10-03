# Phase 5 — Governance, Documents and Lifecycle Validation

**Date:** 2026-10-03  
**Status:** COMPLETE  
**Principle:** Validate existing controls; build only what is missing.

---

## 1. Control map (required → canonical source)

| Control | Canonical source | Status |
|---|---|---|
| Metadata | Doc 04 Required Metadata Header | ✅ Present (incl. Confidentiality, Next Review, Superseded By) |
| Naming | Doc 04 Steps 4–5 + validate-naming.yml | ✅ Present |
| Classification | Doc 04 + Doc 02 types + Confidentiality enum | ✅ Present |
| Approval | Doc 04 Lifecycle (Owner moves Under Review → Approved) + PR template + CODEOWNERS | ✅ Present (handles still placeholders) |
| Versioning | Doc 04 Versioning table + Doc 07 Change Log block | ✅ Present |
| Ownership | Doc 04 RACI fields + Ownership-Matrix.md + ownership-matrix-generate.yml | ✅ Present |
| Confidentiality | Doc 04 field + validate-metadata.yml value check | ✅ Present |
| Lifecycle | Doc 04 Draft→…→Retired | ✅ Present |
| Supersession | Doc 04 `Superseded By` + Doc 07 §5 | ✅ Present |
| Deprecation | Doc 04 Retired + Archive move | ✅ Present |
| Archive | Doc 03 `04_ARCHIVE` | ✅ **Created** this phase (was missing from tree) |
| Access / security | CODEOWNERS, Doc 05, NIVY-ACCESS-SECURITY-MAP, Confidentiality | 🟡 Diagram + classification exist; full permission matrix after stack selection (C30) |
| Audit | Doc 07 health metrics, Doc 08, workflows (health-report, orphan, stale, validate-*) | ✅ Present |
| Decision | KPI-Management-Review-Model §P14 | ✅ Present |
| Change | KPI-Management-Review-Model §P14 | ✅ Present |
| Exception / Issue | KPI-Management-Review-Model §P14 + Operational-Workflows §P27 | ✅ Present |
| Evidence | KPI-Management-Review-Model §P14 + Doc 02 REC | ✅ Present |

---

## 2. Required lifecycle path (validated)

```
Draft → Under Review → Approved → Published/Use → Change (Under Revision) → Supersede → Archive (Retired)
```

| Transition | Who | Evidence mechanism |
|---|---|---|
| → Draft | Responsible creates file + metadata | File in repo; Lifecycle Status: Draft |
| → Under Review | Responsible submits; Owner/Consulted review | PR or status change; PR template checklist |
| → Approved | Owner | Status + Next Review set |
| → Published | Owner; Informed notified | Status Published; index/dashboard |
| → Under Revision | Responsible | Status; old Published remains until new Approved |
| → Supersede / Retired | Owner | Superseded By set; move to 04_ARCHIVE |

**Rule reconfirmed:** Cannot skip Draft → Published. Cannot leave Draft without Owner.

---

## 3. Paper lifecycle test (Scenario B evidence)

**Subject:** `Canonical-Object-Model.md` (ALL-STRAT-001) and sibling Phase 1–4 models.

| Step | Action | Result |
|---|---|---|
| Create | Models created with full Doc 04-style metadata headers | Draft |
| Classify | Department ALL, Type STRAT, PARA Resource, Confidentiality Internal | OK |
| Owner | Workspace Admin / CEO Office | Named |
| Review | Phase gate reviews (tracker + commits) stand in for Under Review | Documented in Combined Progress Tracker |
| Approve path | Not yet formal Owner sign-off to Approved/Published — remains Draft until human Owner promotes | **Intentional** — AI does not self-approve governance |
| Change | Version bumps and Last Updated on each commit | Git history = change evidence |
| Supersede / Archive | N/A until a replacement model is published | Archive path now exists |

**Conclusion:** Path is operable. Formal promotion to Approved/Published requires human Owner action (correct under Doc 05 AI rules).

---

## 4. Decision / Change / Exception / Evidence standardization

Already defined in `KPI-Management-Review-Model.md`. Phase 5 confirms they are the single record standards for:

- Decision (DEC)
- Change (CHG)
- Exception (EXC)
- Issue (ISS)
- Evidence / Record (REC)

No second record format introduced.

---

## 5. Access / security (summary)

| Layer | Implementation |
|---|---|
| Identity | GitHub users / future IdP |
| Role + RACI | Doc 01 + document metadata |
| Least privilege | CODEOWNERS (placeholders until real handles) |
| Classification | Public / Internal / Confidential / Restricted |
| Auth / secrets | Repo settings + no secrets in docs |
| Logging / audit | Git history + GitHub Actions health/orphan/stale workflows |
| Review / revoke | Quarterly audit (Doc 04) + access diagram |

Full system-level permission matrix remains deferred until stack selection (gap C30 / P30-related).

---

## 6. Gaps closed this phase

| Gap | Action |
|---|---|
| `04_ARCHIVE` missing from Company-OS tree | Created with README + structure rules |
| Explicit Phase 5 control map | This document |
| Scenario B paper test | Recorded above |

## 7. Residual open items

- CODEOWNERS real GitHub handles (human)
- Human Owner promotion of Draft models to Approved/Published
- Full access-control matrix post stack selection
- Live end-to-end Scenario B with a non-model operational SOP (recommended in P32)

---

## 8. Files created

- `Company-OS/04_ARCHIVE/README.md`
- `Audit-and-Tasks/P05_Phase5_Governance_Lifecycle_Validation.md` (this file)

# P04 — Historical V5/V6/Final-v7 Disposition and Authority Map

**Date:** 2026-10-03  
**Phase:** 0 — Baseline and Authority  
**Status:** COMPLETE (verified against actual repository state)  
**Principle:** Do NOT delete historical material. Classify only.

---

## 1. Inventory of material present in Research-Repository

| Artifact | Location | Type | Disposition |
|---|---|---|---|
| Active Company OS V7 | `Company OS/Company-OS-v7/Company-OS/` | Working tree | **CANONICAL / ACTIVE** |
| Governance Docs 01–10 | `.../03_RESOURCES/Company_Master_Standards/GOVERNANCE/` | Standards | **CANONICAL / ACTIVE** |
| Classifier-Skill | `Company OS/Company-OS-v7/Classifier-Skill/` | Skill + JSON registries | **CANONICAL / ACTIVE** |
| Research-OS-Skill | `Company OS/Company-OS-v7/Research-OS-Skill/` | Skill | **CANONICAL / ACTIVE** |
| Research-Inbox | `Company OS/Company-OS-v7/Research-Inbox/` | Staging | **CANONICAL / ACTIVE** |
| Audit-and-Tasks (combined + prior) | `Company OS/Company-OS-v7/Audit-and-Tasks/` | Audit/plan/tracker | **CANONICAL / ACTIVE** (trackers are living) |
| Diagrams (Draw.io) | `docs/OWNER-CONTROL/05-VISUALS/` (19 .drawio) + `Company OS/Company-OS-v7/Diagrams/` | Visual system | **CANONICAL / ACTIVE** (primary location = OWNER-CONTROL) |
| CHANGELOG_v6-consolidated.md | `Company OS/Company-OS-v7/` | Changelog | **HISTORICAL / SUPERSEDED** (record of v5→v6 merge) |
| Company-OS-v6-consolidated.zip | `Company OS/Company-OS-v7/` | Snapshot archive | **HISTORICAL / SNAPSHOT** (do not expand as parallel OS) |
| Company_OS_v6_Audit_and_Implementation_Plan.md | `Company OS/Company-OS-v7/` | Audit | **HISTORICAL / SUPERSEDED** (issues H1–L2 applied; L3 open) |
| README.md (v6 package) | `Company OS/Company-OS-v7/README.md` | Package index | **HISTORICAL / SUPERSEDED** (describes v6 package; V7 location is authoritative) |
| Older zips (v1–v4, Final-v5) referenced in README | Not present as separate trees under `Company OS/` | External / prior packages | **SUPERSEDED / NOT IN REPO** (content merged or duplicated into V7) |

**Finding:** There is no separate live `Company-OS-v5/`, `Company-OS-v6/` or `Final-v7/` tree in the repository. Only the single active tree under `Company OS/Company-OS-v7/Company-OS/` plus historical snapshot/zip/changelog artifacts.

---

## 2. Version lineage (authoritative)

```
Inital_Company_OS_v1_0  →  Company_OS_v2_0  →  Company_OS_with_github_repositoryv3_0
        →  v4 (internal)  →  Company-OS-Final-v5  →  Company-OS-Final-v6 (zip + changelog)
                →  Company OS/Company-OS-v7/Company-OS/   ← CURRENT CANONICAL
```

- **v1–v4:** Fully superseded. Content checked and either duplicated or absorbed; do not restore as parallel systems.
- **v5 (Final-v5):** Base for the v6 consolidation package. Superseded by the applied H1–L2 fixes and subsequent V7 placement.
- **v6 (consolidated):** Snapshot of the post-merge state (CHANGELOG + zip). Historical record only. All applied fixes live in the V7 tree.
- **V7 (current):** The only active, editable Company OS. Location: `Company OS/Company-OS-v7/`.

---

## 3. Authority rules

1. **Single source of truth** for operational Company OS content is  
   `Company OS/Company-OS-v7/Company-OS/`.
2. **Governance standards** 01–10 under  
   `.../Company_Master_Standards/GOVERNANCE/` are the governing rule set.  
   Doc 09 (Final Change Plan) is a historical planning document; actual applied state is verified in the live Docs 01–10.
3. **Trackers and plans** under `Audit-and-Tasks/` are living control documents.  
   Actual repository files always override any tracker checkbox that lacks verification evidence.
4. **Draw.io diagrams** live under `docs/OWNER-CONTROL/05-VISUALS/`.  
   Do not create a second diagram hierarchy. Any copy under `Company-OS-v7/Diagrams/` is secondary until a formal location decision (P31).
5. **Historical material** (zips, changelogs, old audit plans) must not be deleted.  
   They remain as evidence and may be moved only into an explicit `04_ARCHIVE` or historical folder with a disposition note.
6. **No parallel Company OS** may be created. All new work adapts or extends the existing V7 tree.

---

## 4. Conflict resolution summary

| Conflict source | Resolution |
|---|---|
| Governance Doc 09 vs live Docs 04/06/07 | Doc 09 was a pre-edit plan. Live Doc 04 already contains Confidentiality + Next Review. Live Doc 06 is marked FINAL and aligned to Doc 03. Live Doc 07 retains its health/AI sections; ownership-matrix automation exists as workflow. Doc 09 is historical planning, not active instruction. |
| Combined Progress Tracker vs actual files | Tracker marks are provisional until verified. P04/P05 now verified by this disposition. |
| README (v6 package) vs V7 location | README describes the package that was placed into `Company-OS-v7/`. V7 path is the living root. |
| v6 zip vs live tree | Zip is snapshot only. Live tree is authoritative. |

---

## 5. Open items carried forward (not blockers for Phase 0)

- L3 from v6 audit: real GitHub handles for `CODEOWNERS` (human input required).
- Brands.md tentative codes (ACAD, ALNC, JOBS, CARE) still need human confirmation.
- GitHub Project board creation remains a manual UI action.
- TickTick integration remains external (OAuth/token).

---

## 6. Validation performed

- Listed `Company OS/` → only `Company-OS-v7` present.
- Listed `Company OS/Company-OS-v7/` contents.
- Confirmed presence of Governance 01–10, workflows, Classifier-Skill, Research-Inbox, Audit-and-Tasks, Draw.io set under `docs/OWNER-CONTROL/05-VISUALS/`.
- Read CHANGELOG_v6-consolidated, v6 audit plan, README, Doc 09, Doc 04, Doc 06.
- Confirmed Doc 04 metadata header contains Confidentiality and Next Review (Doc 09 plan applied).
- Confirmed Doc 06 status = FINAL and uses Doc 03 folder names.

---

## 7. Files created by this task

- This file: `Audit-and-Tasks/P04_Version_Disposition_and_Authority.md`

**Next:** P05 Governance Docs 01–10 reconciliation (same phase).

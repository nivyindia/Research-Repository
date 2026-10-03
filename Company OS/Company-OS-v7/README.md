# Company OS V7 — Active Package

**Status:** Structural implementation complete (Phases 0–10)  
**Canonical working tree:** `Company-OS/`  
**Handover index:** [Audit-and-Tasks/P33_Publication_and_Handover.md](Audit-and-Tasks/P33_Publication_and_Handover.md)  
**Progress:** [Audit-and-Tasks/Company_OS_Combined_Progress_Tracker.md](Audit-and-Tasks/Company_OS_Combined_Progress_Tracker.md)

> Historical note: Earlier package README described the v5→v6 consolidation (Aug 2026). That lineage remains valid background. **V7 is the active Company OS** after the 2026-10-03 standardization program (object model, strategy-execution, KPI/review, workflows, integrations, diagrams, health, E2E scenarios, handover).

---

## What's inside

| Folder | What it is |
|---|---|
| `Company-OS/` | Working OS — departments, governance Docs 01–10, V7 Master Standards models, GitHub Actions, templates, `04_ARCHIVE/` |
| `Research-Inbox/` | Staging — drop raw notes in `dump/`, classify, PR into Company-OS |
| `Classifier-Skill/` | Classification skill (departments + document types) |
| `Research-OS-Skill/` | Research workflow skill |
| `Audit-and-Tasks/` | Progress tracker, P04–P07/P32/P33 validation, historical audit notes |
| `Diagrams/` | V7 index only — **canonical Draw.io sources live at** `docs/OWNER-CONTROL/05-VISUALS/` |

---

## V7 Master Standards (new in this program)

Under `Company-OS/03_RESOURCES/Company_Master_Standards/`:

- Canonical-Object-Model.md  
- Strategy-Execution-Model.md  
- Goal-Registry.md  
- KPI-Management-Review-Model.md  
- Operational-Workflows-Model.md  
- Integration-Contracts-and-AIOS.md  
- Company-OS-Health-Automation-Control.md  

---

## How to operate

1. **Humans:** Start at `Company-OS/README.md` or P33 handover index.  
2. **New documents:** Classify per Doc 04; CI validates metadata/naming.  
3. **Research:** Drop into Research-Inbox → PR → human merge.  
4. **Health:** Run dashboard-generate / read `dashboard.md`.  
5. **Diagrams:** Edit only under `docs/OWNER-CONTROL/05-VISUALS/`.  
6. **External publish:** Optional via publish-sync after configuring target; GitHub remains source of truth.

---

## Still open (human / operational)

- Brand code confirmation (tentative entries in Brands.md)  
- CODEOWNERS real handles  
- Human Approve/Publish of Draft STRAT models  
- Real KPI targets  
- Notion/Wiki API for publish-sync  
- Optional split deploy of Company-OS + Research-Inbox as separate GitHub repos  

See P33 handover checklist for the full list.

---

## Authority

Version disposition: `Audit-and-Tasks/P04_Version_Disposition_and_Authority.md`  
Do not revive parallel V5/V6 trees as active OS.

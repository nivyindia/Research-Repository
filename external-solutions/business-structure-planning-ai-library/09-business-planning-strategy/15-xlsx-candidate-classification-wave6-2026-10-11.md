# XLSX Candidate Classification — Wave 6
**Updated:** 2026-10-11  
**Method:** Read-only GitHub recursive tree metadata (path, size, blob SHA) and connector attempts to fetch binary content. No binary workbook was edited or executed.

## Result
The repository tree contains 14 `.xlsx` paths. Two paths are identical copies of `agency_lead_tracker_template.xlsx` (same blob SHA), one evaluation workbook, one checklist, and ten BDE training/pilot/CRM assets. No path is clearly an integrated company financial model.

**Important technical warning:** Ten BDE workbook paths report a size of only **2 bytes** and share the same blob SHA. They are almost certainly empty/placeholder files or invalid workbook artifacts, not usable Excel workbooks. Treat them as **corrupt/placeholder until repaired from source**. Do not try to open or run them as financial models.

The binary content connector returned UTF-8 decode errors when fetching the evaluation and lead-tracker XLSX files. This is a connector limitation for binary XLSX, not proof that those two files are corrupt. Their contents remain uninspected. Do not infer formulas/sheets from the filenames alone.

## Candidate-by-candidate classification

| # | File | Size | SHA | Initial classification | Finance-model relevance |
|---:|---|---:|---|---|---|
| 1 | [Evaluation Sheet - Nivy.xlsx](https://github.com/nivyindia/Research-Repository/blob/main/Chats/Claude/Evaluation%20Sheet%20-%20Nivy.xlsx) | 10,645 B | `322e800f720e7ca87f227cde2e0a79629db831f5` | Candidate workbook; binary contents not inspected | Unknown; inspect locally read-only |
| 2 | [Quiz & Assignment Bank](https://github.com/nivyindia/Research-Repository/blob/main/Nivy%20Research%20Data/BDE%20Complete%20Training/BDE%20launchpad%20training%20system/06_LMS_Content/Quiz_&_Assignment_Bank.xlsx) | 2 B | `8d1c8b69c3fce7bea45c73efd06983e3c419a92f` | Placeholder/corrupt candidate | None apparent; restore from source if required |
| 3 | [Closure Status Sheet](https://github.com/nivyindia/Research-Repository/blob/main/Nivy%20Research%20Data/BDE%20Complete%20Training/BDE%20launchpad%20training%20system/07_CRM_Setup/Closure_Status_Sheet.xlsx) | 2 B | same | Placeholder/corrupt candidate | Sales operations only, not finance engine |
| 4 | [Follow-Up Tracker](https://github.com/nivyindia/Research-Repository/blob/main/Nivy%20Research%20Data/BDE%20Complete%20Training/BDE%20launchpad%20training%20system/07_CRM_Setup/Follow-Up_Tracker.xlsx) | 2 B | same | Placeholder/corrupt candidate | Sales operations only |
| 5 | [Zoho CRM Lead Template](https://github.com/nivyindia/Research-Repository/blob/main/Nivy%20Research%20Data/BDE%20Complete%20Training/BDE%20launchpad%20training%20system/07_CRM_Setup/Zoho_CRM_Lead_Template.xlsx) | 2 B | same | Placeholder/corrupt candidate | CRM only |
| 6 | [Content Index](https://github.com/nivyindia/Research-Repository/blob/main/Nivy%20Research%20Data/BDE%20Complete%20Training/BDE%20launchpad%20training%20system/09_BookStack_Wiki/Content_Index.xlsx) | 2 B | same | Placeholder/corrupt candidate | None apparent |
| 7 | [Mentor Assignment Sheet](https://github.com/nivyindia/Research-Repository/blob/main/Nivy%20Research%20Data/BDE%20Complete%20Training/BDE%20launchpad%20training%20system/10_Pilot_Launch_Assets/Mentor_Assignment_Sheet.xlsx) | 2 B | same | Placeholder/corrupt candidate | None apparent |
| 8 | [Pilot Batch Tracker](https://github.com/nivyindia/Research-Repository/blob/main/Nivy%20Research%20Data/BDE%20Complete%20Training/BDE%20launchpad%20training%20system/10_Pilot_Launch_Assets/Pilot_Batch_Tracker.xlsx) | 2 B | same | Placeholder/corrupt candidate | Training operations only |
| 9 | [Leaderboard Format](https://github.com/nivyindia/Research-Repository/blob/main/Nivy%20Research%20Data/BDE%20Complete%20Training/BDE%20launchpad%20training%20system/11_Orientation_&_Motivation/Leaderboard_Format.xlsx) | 2 B | same | Placeholder/corrupt candidate | None apparent |
| 10 | [Cohort Rollout Plan](https://github.com/nivyindia/Research-Repository/blob/main/Nivy%20Research%20Data/BDE%20Complete%20Training/BDE%20launchpad%20training%20system/12_Final_Deployment_Plan/Cohort_Rollout_Plan.xlsx) | 2 B | same | Placeholder/corrupt candidate | Training operations only |
| 11 | [Payout Tracker](https://github.com/nivyindia/Research-Repository/blob/main/Nivy%20Research%20Data/BDE%20Complete%20Training/BDE%20launchpad%20training%20system/12_Final_Deployment_Plan/Payout_Tracker.xlsx) | 2 B | same | Placeholder/corrupt candidate | Potential payout-tracking only; not an integrated finance model |
| 12 | [Checklist.xlsx](https://github.com/nivyindia/Research-Repository/blob/main/Nivy%20Research%20Data/BDE%20Complete%20Training/BDE%20launchpad%20training%20system/Checkllist.xlsx) | 17,707 B | `0f6a5b8c19ef9d03805c69fd65ad5e741aaf91cb` | Candidate workbook; binary contents not inspected | Unknown; likely operational checklist based on path |
| 13 | [Lead tracker — Global Systems Workspace](https://github.com/nivyindia/Research-Repository/blob/main/Notion%20-%20Global%20Systems%20Workpace/agency_lead_tracker_template.xlsx) | 7,411 B | `601984c9737197a4fdfea18ba71f4c22f447f299` | Lead-tracker candidate; binary contents not inspected | CRM/lead pipeline, not financial model |
| 14 | [Lead tracker — Nivy OS](https://github.com/nivyindia/Research-Repository/blob/main/Notion%20-%20Nivy%20OS/agency_lead_tracker_template.xlsx) | 7,411 B | same | Exact duplicate of #13 | CRM/lead pipeline; preserve both until canonical pointer decision |

## Decisions
1. No workbook has yet been confirmed as an executable integrated financial model.
2. The two lead tracker files are byte-identical at Git blob level. Recommend choosing one canonical location and replacing the other only with a pointer after review; no deletion performed.
3. The ten 2-byte BDE XLSX artifacts need recovery from their originating generator or known-good copy if those assets are required. Avoid silently replacing them with empty workbooks.
4. The Evaluation Sheet and Checklist need local read-only inspection of ZIP/XLSX package contents, sheets, formula counts and named ranges. The connector's binary decoding failure is not an integrity diagnosis.
5. Do not create a replacement financial workbook until the source financial narrative, monthly tracker, assumptions and ownership are reconciled.

## Next action
Proceed with the source-file inventory for all Nivy Next Financial Model linked sections and mirrored copies, then inspect the two viable unknown workbooks locally if binary access is available. Update the master coverage register only with evidenced findings.

# Nivy Financial Artifact Inventory — Wave 5
**Updated:** 2026-10-11  
**Scope:** Complete GitHub recursive tree listing plus read-only inspection of the finance tracker CSV, finance database CSV, 10.0 Financial Plan document and financial automation section. No files were modified and no workbook was executed.

## Repository inventory results

The recursive Git tree returned **10,466 blob files** and was not marked truncated. Extension counts across the repository:
- `.xlsx`: 14
- `.xlsm`: 0
- `.xls`: 0
- `.csv`: 123
- `.py`: 10
- `.json`: 118
- `.ipynb`: 0

A filename-focused scan did **not** identify an `.xlsx`/Excel workbook whose filename indicates a financial model or forecast. It did identify the following financial artifacts. This is stronger than text search alone, but the result does not prove no workbook elsewhere could be used for finance.

## Exact artifacts inspected

| Artifact | Path | SHA | Observed status |
|---|---|---|---|
| Monthly Financial Tracker | [Nivy Nexus CSV](https://github.com/nivyindia/Research-Repository/blob/main/Nivy%20Nexus/%F0%9F%93%8A%20Monthly%20Financial%20Tracker%20(Planned%20vs%20Actual)%2070ae230a7ee04dec9afd21898c51f019_all.csv) | `b6e1e2fe803a161ff0150ddf34dd61a9cb5e6445` | Planned/actual tracking schema exists; actual-value columns are blank in inspected rows |
| Mirrored Monthly Financial Tracker | [Notion - Nivy Nexus CSV](https://github.com/nivyindia/Research-Repository/blob/main/Notion%20-%20Nivy%20Nexus/%F0%9F%93%8A%20Monthly%20Financial%20Tracker%20(Planned%20vs%20Actual)%2070ae230a7ee04dec9afd21898c51f019_all.csv) | `b6e1e2fe803a161ff0150ddf34dd61a9cb5e6445` | Same blob SHA as Nivy Nexus version: exact duplicate in this repository revision |
| Finance database | [Nivy Research Data CSV](https://github.com/nivyindia/Research-Repository/blob/main/Nivy%20Research%20Data/finance_database%20ff3fee8dd15e4e508346ec2193bff6ff_all.csv) | `3b715d3cc9ce279bd9f09a7a06e1aa4776b931fc` | Only header and one placeholder row: `Sample,0,`; not a usable ledger/model |
| General financial plan | [10.0 Financial Plan](https://github.com/nivyindia/Research-Repository/blob/main/Notion%20-%20Nivy%20OS/10%200%20Financial%20Plan%2033eeb94b1a2a83478eaf81c19e2bf7f4.md) | `2dd35d06ad74586e822d42a2448240ebd39d7dc1` | Narrative model with financial assumptions and forecasts; not an executable spreadsheet |
| Financial automation stack | [Section 10](https://github.com/nivyindia/Research-Repository/blob/main/Notion%20-%20Nivy%20OS/%F0%9F%A7%AESECTION%2010%20%E2%80%94%20Financial%20Automation%20Stack%20f94eb94b1a2a8311a7510139dcac31a4.md) | `f415f43972b97c6cbd103834992fe0e2cbdc5e92` | Describes proposed tools and automation; named forecasting scripts were not found in this exact file as attached runnable source |

Other repository spreadsheets include an evaluation sheet, a lead-tracker template and training/CRM trackers. They are not identified as the integrated company financial model and must not be substituted for one without inspecting their contents and intended purpose.

## Data-quality and model-risk findings

### 1. Monthly tracker is not a verified actuals ledger
The CSV includes planned and actual fields for active clients, profit, commission, new clients, outsourcing cost and revenue. In the inspected rows, actual fields are blank and status is `Not Started`. The file is useful as a tracking template, but it cannot substantiate realized revenue, profit or financial performance.

### 2. Duplicate monthly rows can distort totals
The CSV contains alternate labels for the same periods, including both `M4: October 2026` and `M4 — October 2026`, and similarly for other months. Some rows have differing planned intern counts for the same month. Do not sum the rows as if they are independent periods. A canonical period key and duplicate-row reconciliation are required before calculating totals.

### 3. Forecast figures need arithmetic and evidence validation
The tracker includes planned monthly revenue and profit values, cumulative net-profit values and client-count assumptions. They are plans, not actuals. The model must document how monthly revenue, delivery costs, commissions, overhead and cumulative profit are derived. Inputs need an assumption ID, source/date, confidence and owner. No forecast number should be treated as validated simply because it appears in the CSV.

### 4. Financial plan uses a dated FX assumption and unsourced commercial benchmarks
The inspected narrative uses `1 USD = 83 INR`, gives client-retainer ranges, estimated startup costs, team-cost estimates and ambitious Year 1–3 revenue targets. These are assumptions in the document, not verified current benchmarks. The FX rate needs a dated source and explicit scenario range. The revenue ramp, costs, capacity and cash timing must be recalculated together; the forecast should not be accepted from narrative arithmetic alone.

### 5. The finance database is a placeholder
A 33-byte CSV with a single sample row does not establish a working financial database, transaction ledger, automated data pipeline or live dashboard.

## Updated coverage decision

| Requirement | Status after Wave 5 | Evidence / next gate |
|---|---|---|
| Executable integrated financial workbook | **Not located in filename scan; unresolved** | Inspect all 14 XLSX files read-only and classify purpose; do not call the gap closed until this is complete |
| Actuals and forecast tracker | **Template present; actuals unverified** | Fill actuals from source records, define reconciliation owner and close calendar |
| Duplicate-period controls | **Gap identified** | Normalize period IDs and reject duplicate month keys in totals |
| Finance database | **Placeholder / gap** | Define schema, source-of-truth and import/validation rules |
| Forecast assumptions and FX | **Documented but unvalidated** | Source each key input and run low/base/high sensitivity cases |
| Automation | **Proposed, not demonstrated** | Locate actual scripts/workflows and test on dummy data with logs |

## Next steps
1. Inspect all 14 `.xlsx` files read-only and record workbook sheets, formula counts, named ranges, data validation and intended use. Binary downloads through this connector are not supported; use metadata where possible and arrange local inspection for contents.
2. Compare all mirrored Nivy finance-section files by blob SHA and establish canonical references. Preserve originals.
3. Normalize the monthly tracker into one row per month; separate forecast version from actuals and keep actuals blank until supported by source records.
4. Build the independent numeric test fixture only after artifact classification.
5. Update the master capability coverage register and action backlog with these findings.

## Safety and limitation
No files were edited or deleted. No workbook was downloaded, recalculated or executed. This inventory proves the recursive tree was fully returned and identifies visible candidate files; it does not certify accounting accuracy, current market pricing, legal/tax compliance or release readiness.

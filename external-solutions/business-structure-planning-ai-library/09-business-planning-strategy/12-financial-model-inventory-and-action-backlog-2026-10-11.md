# Financial Model Inventory and Action Backlog
**Updated:** 2026-10-11  
**Purpose:** Convert the Wave 4 static findings into trackable actions. This is a work register, not a claim that financial validation is complete.

## Current inventory

| Asset / family | Location | Type | Initial assessment | Required follow-up |
|---|---|---|---|---|
| Financial Model Overview | [Notion - Nivy OS](https://github.com/nivyindia/Research-Repository/blob/main/Notion%20-%20Nivy%20OS/Financial%20Model%20Overview%20945eb94b1a2a83a396d501dfd927f831.md) and [Nivy Research Data](https://github.com/nivyindia/Research-Repository/blob/main/Nivy%20Research%20Data/Financial%20Model%20Overview%202b1b3416c76d80cd95cee09d46e68db2.md) | Markdown framework | Broad 16-section agency finance plan | Compare exact content hashes; designate canonical source and reference/archival copy if duplicates confirmed |
| Nivy Next Financial Model index | [Notion - Nivy OS](https://github.com/nivyindia/Research-Repository/blob/main/Notion%20-%20Nivy%20OS/Nivy%20Next%20Financial%20Model%20e4feb94b1a2a8214823701f5c30c9a4c.md) and [Nivy Research Data](https://github.com/nivyindia/Research-Repository/blob/main/Nivy%20Research%20Data/Nivy%20Next%20Financial%20Model%2029bb3416c76d818bbe6ae31cc86e3929.md) | Markdown index | Links finance sections across cash flow, budgeting, unit economics, compliance, FX, risk and dashboards | Resolve all links; inventory every child file; compare mirrored copies before any consolidation |
| Part 2: Cash Flow Clarity System | [Notion - Nivy OS](https://github.com/nivyindia/Research-Repository/blob/main/Notion%20-%20Nivy%20OS/%F0%9F%92%B9%20Financial%20Model%20%E2%80%94%20Part%202%20Cash%20Flow%20Clarity%20Syste%205d7eb94b1a2a83d1b02681d922e8b294.md) and mirrored Nivy Research Data version | Markdown specification | Descriptive cash-flow process and tracking | Extract actual formulas, timing rules, receivables, taxes, payout timing and forecast assumptions |
| Part 3: Growth Budgeting Framework | [Notion - Nivy OS](https://github.com/nivyindia/Research-Repository/blob/main/Notion%20-%20Nivy%20OS/%F0%9F%92%B9%20Financial%20Model%20%E2%80%94%20Part%203%20Growth%20Budgeting%20Framew%20cb1eb94b1a2a83d898fb815a5800c316.md) and mirrored Nivy Research Data version | Markdown specification | Growth allocation, budget and ROI topics | Separate suggested ratios from evidence-backed policies; connect budgets to forecast and decision gates |
| Financial Automation Stack | [Notion - Nivy OS](https://github.com/nivyindia/Research-Repository/blob/main/Notion%20-%20Nivy%20OS/%F0%9F%A7%AESECTION%2010%20%E2%80%94%20Financial%20Automation%20Stack%20f94eb94b1a2a8311a7510139dcac31a4.md) and mirrored Nivy Research Data version | Markdown / proposed tooling | Mentions spreadsheet dashboards and Python forecasting scripts | Locate actual scripts, tests, input schemas and outputs; treat named tools as proposed until found |
| Financial Plan Overview / section 10.0 | Nivy OS and Nivy Research Data copies | Markdown checklists | Mentions P&L, cash flow, balance sheet, break-even, ratios and funding ask | Determine whether these are duplicate general templates or add unique requirements |
| External Musengimana workbook engine | [Source repository](https://github.com/Musengimana/develop-a-business-plan-in-minutes) | XLSX template + Python scripts | Protected workbook write/recalculate/verify method specified | License/NOTICE/dependencies; do not run before obtaining a safe local copy and confirming runtime dependencies |
| External Peter release gate | [Release-gate contract](https://github.com/peterbamuhigire/business-plan-skills/blob/main/docs/quality-gates/business-plan-release-gate.md) | Markdown contract + validator | Blocker-first release policy specified | Inspect validator and fixture files only after finance inventory; keep runtime and human approval separate |

**Inventory limitation:** Repository code search is not a complete binary-file tree listing. No conclusion is made that Nivy has no XLSX/CSV files; a full repository tree/artifact inventory remains required.

## Action backlog

| ID | Priority | Task | Owner role | Acceptance / exit criteria | Status |
|---|---|---|---|---|---|
| FM-INV-01 | P0 | Enumerate repository tree for `.xlsx`, `.xlsm`, `.csv`, `.json`, `.py`, notebooks and financial outputs | Repository auditor | File path, size/type, last commit, source/owner and license recorded; binary search limitation resolved | Open |
| FM-INV-02 | P0 | Resolve all links from Nivy Next Financial Model index | Finance-model auditor | Each link marked valid/broken; each child categorized as narrative, assumptions, formula, output or automation | Open |
| FM-INV-03 | P1 | Compare Notion OS and Nivy Research Data mirrors | Content librarian | Hash-based duplicate list; no originals deleted; canonical and mirror/pointer recommendation recorded | Open |
| FM-INV-04 | P0 | Extract assumption and benchmark inventory | Finance analyst | Every numeric policy has ID, value/range, unit, currency, geography, date, source, confidence, owner and validation state | Open |
| FM-INV-05 | P0 | Build model driver map | Finance-model designer | Revenue, service mix, capacity, direct costs, commissions, overhead, collections, taxes, FX and hiring linked to model rows/formulas or marked missing | Open |
| FM-INV-06 | P0 | Confirm whether any executable Nivy workbook exists | Repository auditor | Exact artifact paths listed; workbook not edited; metadata and formula inventory read-only if present | Open |
| FM-TEST-01 | P0 | Define independent numeric fixture | Model QA | Known input/output values for revenue, cost, margin, ending cash and funding need; calculations independently reproducible | Blocked by FM-INV-06 |
| FM-TEST-02 | P0 | Plan isolated runtime tests | QA engineer | Disposable copy, pinned versions, dependencies, expected results, logs, rollback and no-original-write guarantee documented | Blocked by FM-INV-06 |
| FM-GOV-01 | P0 | Add license and dependency disposition | Compliance/repository owner | Main license and separately governed templates/assets checked; dependency manifest and permitted-use decision recorded | Open |
| FM-GOV-02 | P0 | Tie financial outputs to release gate | Finance reviewer + release owner | Plan narrative, model, ask/use-of-funds, milestones, downside case and evidence bundle reconcile; release remains blocked until authorized | Open |

## Required status vocabulary
- **Open:** work not started or evidence absent.
- **In review:** artifact is being inspected.
- **Specified:** documentation describes the method.
- **Static pass:** source/content checks pass; no runtime claim implied.
- **Runtime pass:** exact pinned environment and test fixture passed, with logs.
- **Independently reconciled:** critical outputs agree with separately computed expected values within stated tolerance.
- **Blocked:** prerequisite, evidence, license, or approval missing.
- **Released:** all mandatory gates pass and named authority approves.

## Immediate next action
Complete **FM-INV-01** first. Until the actual artifact inventory is known, do not build a replacement workbook or run external code. Then resolve the index links and update the master coverage register with exact artifact references.

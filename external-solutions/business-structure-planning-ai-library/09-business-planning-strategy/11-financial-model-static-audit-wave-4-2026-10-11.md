# Financial Model Static Audit — Wave 4
**Updated:** 2026-10-11  
**Scope:** Exact-file static inspection of the Musengimana workbook instructions/scripts, Peter's release gate, and Nivy's existing financial-model documents. No scripts or workbooks were executed.

## Executive result
The review has progressed from capability claims to inspecting exact instructions and code. The strongest external financial workbook candidate has a detailed safety pipeline and formula-integrity checks, but those checks do not independently prove business logic is correct. Nivy's inspected financial-model assets are planning documentation and linked section outlines; this review did not identify or execute an integrated Nivy XLSX model. Treat Nivy financial coverage as **documented / not executable evidence yet**, not as a tested financial engine.

## Exact files inspected

| Source | File | Blob SHA / status | What the file establishes | What it does not establish |
|---|---|---|---|---|
| Musengimana | [SKILL.md](https://github.com/Musengimana/develop-a-business-plan-in-minutes/blob/main/build-client-business-plans/SKILL.md) | `1f182e419314f98a4a9a2b2a94e10283a3b60439` | Specifies client intake, source logging, assumption IDs, Word/XLSX deliverables, downside/upside cases, formula-preservation workflow | Does not prove a model was run for Nivy or is localized for UAE |
| Musengimana | [financial-model-map.md](https://github.com/Musengimana/develop-a-business-plan-in-minutes/blob/main/build-client-business-plans/references/financial-model-map.md) | `0411bac22096af01d8a9d32a5672e1ee69ccbd9d` | Documents workbook architecture, protected write engine, disposable LibreOffice shadow recalculation, cached-value extraction, scenario path, formula checks | Documentation alone does not prove execution succeeded in this session |
| Musengimana | [financial-model-audit.md](https://github.com/Musengimana/develop-a-business-plan-in-minutes/blob/main/build-client-business-plans/references/financial-model-audit.md) | `cb3eead66bbf5e34a98dfe32407f32e87de3196b` | Requires an independently designed audit spec, rendering, scenario perturbation, independent arithmetic checks, reconciliation and final formula-integrity verification | The checks are prescribed; no controlled workbook was executed here |
| Musengimana | [verify_formula_integrity.py](https://github.com/Musengimana/develop-a-business-plan-in-minutes/blob/main/build-client-business-plans/scripts/verify_formula_integrity.py) | `1283a9fa5aad1aec5683ecf9c8912064d708454e` | Code compares formula inventory against pristine template, checks template package parts and cached formula errors, and fails on regressions | Formula preservation is not the same as validating model assumptions, accounting policy or independent expected outputs |
| Musengimana | [populate_financial_workbook.py](https://github.com/Musengimana/develop-a-business-plan-in-minutes/blob/main/build-client-business-plans/scripts/populate_financial_workbook.py) | `2efec65845d471fd96e2716dd21cd7256449f6a0` | Code describes guarded input injection, shadow recalculation, cached-result grafting and integrity checks | Runtime dependencies, workbook compatibility and actual output values remain untested here |
| Peter Bamuhigire | [business-plan-release-gate.md](https://github.com/peterbamuhigire/business-plan-skills/blob/main/docs/quality-gates/business-plan-release-gate.md) | `ec13d6660ad7be8cd6c5fb579c7cb4aea36e1616` | Defines release vs blocked, mandatory blockers, evidence bundle and explicit release authority; validator checks structural/path/state consistency | Validator cannot decide whether source evidence truly supports claims or financial judgement is correct |
| Nivy | [Financial Model Overview](https://github.com/nivyindia/Research-Repository/blob/main/Notion%20-%20Nivy%20OS/Financial%20Model%20Overview%20945eb94b1a2a83a396d501dfd927f831.md) | `151542ebeed002c9e2e105c2bb0e4b0eaa124f30` | Documents 16-section international digital-marketing-agency finance framework, including cash flow, unit economics, compliance, FX, bad debt, team, automation, milestones and dashboards | It is an outline, not a calculated P&L / balance sheet / cash-flow workbook |
| Nivy | [Nivy Next Financial Model index](https://github.com/nivyindia/Research-Repository/blob/main/Notion%20-%20Nivy%20OS/Nivy%20Next%20Financial%20Model%20e4feb94b1a2a8214823701f5c30c9a4c.md) | `0499d9a1cbf60af4ea2f96f70df8bea5f631808d` | Links separate parts for cash flow, growth budgeting, unit economics, tax/compliance, FX/pricing, payments, risk, automation, scaling, LTV, pricing tests and reporting | Index links do not establish all parts are complete, reconciled, or executable |

## Material findings

### A. Musengimana finance engine: strong controls specified, independent arithmetic still required
The model map reports a template with 1,064 formulas, 22 dropdown controls, 64 named ranges and a hidden support sheet. It warns that ordinary save/recalculation paths can damage the template and prescribes a protected writer. Follow that project's exact safety rules if testing its own workbook. Do not assume these constraints apply identically to a separately built Nivy workbook.

The audit design is appropriately layered:
1. Design the audit spec from approved assumptions/model design before looking at final workbook outputs.
2. Populate a disposable copy through the supported engine.
3. Check recalculation report and render the workbook for visual inspection.
4. Perturb revenue, operating cost and financing inputs in scenario copies.
5. Independently recompute key metrics outside the workbook.
6. Run numeric/tie-out checks and formula-integrity verification.

**Critical distinction:** formula-preservation gate = structural integrity; scenario perturbation + independent recomputation + reconciliations = stronger calculation evidence. Neither replaces accounting/tax review.

### B. Peter release gate: preserve blocker-first state semantics
The release gate requires decision, audience, jurisdiction, version, owner, evidence paths, finance/research/regulatory handoffs, rendering and explicit authority. A structurally valid release bundle can remain blocked. Adopt separate states for:
- specified
- statically inspected
- runtime test passed
- independently reconciled
- professional review complete
- authorized for external release

Never promote a state merely because a document exists or a structural validator passes.

### C. Nivy model inventory: breadth exists; execution evidence is missing
The inspected Nivy overview covers many appropriate agency-specific topics. The main gap is not another outline section; it is conversion of the documented logic into a source-traceable, formula-driven model with reconciled outputs. At minimum, a future model must connect:
- client count, average contract value, service mix, churn and collection timing → revenue;
- delivery hours, freelancer rates, commissions, tools and overhead → direct costs and operating expenses;
- gross/contribution margin, CAC, LTV and payback → unit economics;
- invoicing/payment delays, tax reserves, FX conversion and bad debt → cash timing and working capital;
- hiring and growth spend → monthly cash runway and financing need;
- base/upside/downside assumptions → scenario outputs and decision thresholds.

Existing guidance such as a 3–5% FX buffer, 2–5% bad-debt reserve, and three months of emergency expenses is recorded in the outline as proposed policies; it is **not validated for the actual company** and must not be treated as a confirmed benchmark without evidence and sensitivity analysis.

### D. Jurisdiction and license are hard gates
Musengimana defaults to Canada/CAD and requires localization when another jurisdiction is named. Peter's material has regional defaults elsewhere. UAE/India cross-border operations therefore need a deliberate jurisdiction and currency convention, dated FX inputs, and qualified review for tax/legal obligations. The third-party BDC workbook is separately governed according to the prior review; do not infer that the repository's MIT license covers it.

## Coverage-register delta

| Requirement | Revised status | Reason | Next proof required |
|---|---|---|---|
| FIN-01 integrated P&L / balance sheet / cash flow | **Gap in Nivy executable evidence** | Inspected Nivy assets are narrative/index documents | Locate actual workbook or create a new one only after inventory |
| FIN-02 revenue/cost driver model | **Partial — documented** | Framework sections exist; no formula/output reconciliation inspected | Map each driver to input cell/formula/source |
| FIN-04 scenarios and break-even | **Specified externally; Nivy runtime unverified** | External instructions require scenarios; Nivy outline mentions risk/scaling | Run controlled base/upside/downside fixture on a copy |
| FIN-05 formula integrity and independent audit | **Specified externally; not run** | Exact scripts inspected, not executed | Test safe copy and independent numeric checks |
| FIN-06 forecast-to-actual variance | **Partial — documentation** | Review/dashboard ideas exist, no standard variance action contract found in inspected files | Define metric, threshold, owner, cadence and action |
| LIC-01 third-party license/dependency | **Partial / blocker before reuse** | Separate workbook terms and dependencies require checking | Record license/NOTICE per asset and dependency manifest |
| REL-01 external release approval | **Specified externally; not assessed for Nivy** | Release gate defines blocked states; no Nivy release bundle assessed | Create Nivy evidence bundle and require named approval |

## Next work sequence
1. Search the Nivy repository for actual `.xlsx`, `.xlsm`, CSV model inputs, calculation scripts and outputs; do not assume a Markdown financial-model title means a workbook exists.
2. Inventory and compare all linked model parts; identify broken links, duplicate copies, missing parts and assumptions without dated sources.
3. If an actual workbook is found, inspect metadata and formulas read-only first. Never overwrite the original; establish a safe copy and tool-compatible recalculation path.
4. Create a small independent benchmark fixture (known revenue, costs, margin, cash, financing need) before attempting the full model.
5. Update the master coverage register and build a gap-to-action backlog with owner, evidence, priority and exit criteria.

## Limitations
This is static inspection only. No workbook was downloaded or executed, no financial figures were independently recalculated, no UAE legal/tax conclusion was made, and no external release is approved.

# Master Capability Coverage Register — Wave 7 Update
**Updated:** 2026-10-11  
**Use with:** [Initial register](09-master-capability-coverage-register-initial-2026-10-11.md), [Wave 5 register delta](14-master-capability-coverage-register-wave5-update-2026-10-11.md), [Wave 6 workbook inventory](15-xlsx-candidate-classification-wave6-2026-10-11.md), [Wave 7 source map and audit](16-canonical-finance-source-map-and-assumption-audit-wave7-2026-10-11.md), [Assumption ledger v1](17-financial-assumption-ledger-v1-2026-10-11.csv).

## Status changes this wave

| ID | Capability | Previous status | Current status | Evidence / next exit criterion |
|---|---|---|---|---|
| FIN-01 | Integrated P&L, balance sheet and cash flow | Blocked / workbook search unresolved | **Blocked** | Main plan contains a P&L table but not an integrated, validated model. Binary workbook review still blocked. Identify/recover actual workbook or formally approve build decision. |
| FIN-02 | Revenue and cost drivers | Partial; planned values only | **Static assumption inventory created; unverified** | Assumption ledger v1 has 17 stable IDs. Add dated sources, units, owners, formulas and confidence; reconcile all values before use. |
| FIN-03 | Unit economics | Specified, not tested | **Static inconsistencies identified; not tested** | Margin definitions conflict across sections; reconcile a single sample client with cost and commission detail. |
| FIN-04 | Base/upside/downside and break-even | Specified externally; Nivy unverified | **Blocked** | No validated monthly driver forecast. Build scenario-specific client starts, churn, ARPC, costs and cash collections after resolving Year-1 conflict. |
| FIN-05 | Formula integrity and calculation correctness | Control design inspected; runtime not tested | **Not tested** | FX pricing formula interpretation error found; no workbook formula checks or independent output reconciliation run. |
| FIN-06 | Forecast-to-actual and variance workflow | Template present; workflow unverified | **Template/data-quality risks remain** | Actuals blank in inspected tracker rows and duplicate period naming noted in Wave 5. Define unique period key and close process. |
| FIN-07 | Finance data source of truth | Gap / placeholder | **Gap confirmed in inspected finance CSV** | Finance database CSV contains only header and sample placeholder. Define ledger schema and import/reconciliation rules. |
| FIN-08 | Currency, jurisdiction and tax | Partial; stale/unverified inputs | **High-risk claims flagged for professional verification** | FX rate is undated; tax and GST statements lack dated official citations. Obtain qualified review before operational use. |
| LIC-01 | Third-party asset/dependency license | Blocked before reuse | **Unchanged / blocked** | Asset-level license review still required before external code or workbook reuse. |
| REL-01 | Release gate | Specified; Nivy release not assessed | **Not release-ready** | No workbook execution logs, independent reconciliation, professional review, or authorized release record. |

## New audit conclusions
1. The financial-model index is a navigation hub, not an executable model; it has unclear/missing links for sections 1, 9 and 11, plus an untitled child link.
2. The main agency Financial Plan has a material Year-1 revenue conflict: narrative forecast is about **$68,500**, while quarterly P&L rows sum to **$190,000**.
3. The FX pricing formula labels a 1.20 cost multiplier as a 20% profit margin. A 20% markup produces a 16.7% margin before any FX buffer.
4. Cost, commission, reserve, margin and scaling assumptions vary across sections and are not consistently defined.
5. Tax, refund, late-fee, FX-market and “industry benchmark” claims are not approved evidence. Obtain dated primary sources and professional review where applicable.
6. The assumption ledger is a normalized capture of documented values, not a validated set of model inputs.

## Current work queue
- **P0:** Resolve Year-1 revenue baseline before using any projection.
- **P0:** Add source, as-of date, confidence and owner to every material assumption.
- **P0:** Have a qualified Indian CA/tax professional review Section 5; obtain legal review for international payment/refund/late-fee terms.
- **P1:** Resolve index navigation gaps and classify the untitled linked document.
- **P1:** Compare mirror copies by exact blob SHA and preserve originals.
- **P1:** Inspect workbook bytes using a binary-capable/local route; the GitHub text connector cannot decode XLSX contents.
- **P1:** Only after evidence, decide whether to reuse a workbook or build a model, then run independent fixture/scenario tests.

## Release status
**Blocked — research and static audit only.** No model was built or recalculated, no workbook was altered, no external benchmark was freshly verified, and no legal/tax conclusion is approved.

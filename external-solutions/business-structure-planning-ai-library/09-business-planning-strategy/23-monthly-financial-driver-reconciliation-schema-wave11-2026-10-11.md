# Monthly Financial Driver Reconciliation Schema — Wave 11
**Created:** 2026-10-11  
**Purpose:** Define the minimum monthly bridge needed to reconcile the existing $68,500 narrative Year-1 revenue claim with the $190,000 sum of the quarterly P&L rows. This is a schema only: no disputed forecast has been selected, no missing values have been invented, and no workbook has been built or executed.

## 1. Decision gate

**Current baseline status: BLOCKED.** The narrative Year-1 revenue figure ($68,500) and quarterly P&L sum ($190,000) cannot both be treated as the approved base case. The arithmetic sum of the quarterly rows is correct, but source assumptions and revenue recognition are not reconciled. Neither figure should be copied into a new model as the approved baseline.

## 2. Source documents to reconcile
- Main agency financial plan: Notion - Nivy OS/10 0 Financial Plan 33eeb94b1a2a83478eaf81c19e2bf7f4.md
- Part 1 agency model: Notion - Nivy OS/💹 Financial Model — Part 1 Agency Overview 36beb94b1a2a837da5d50174154090ac.md
- Section 4 unit economics: Notion - Nivy OS/SECTION 4 — Cost Structure & Unit Economics 7c8eb94b1a2a828ca6ab81d82babc463.md
- Section 6 FX/pricing: Notion - Nivy OS/💹 Financial Model — Part 6 Currency Risk, Pricing  abbeb94b1a2a833f9fc381d7cf645d5d.md
- Section 11 operating costs: Notion - Nivy OS/🧾SECTION 11 — Operational Cost Structure 49beb94b1a2a83159e7e818f3c6f15ed.md
- Existing assumption ledger: 17-financial-assumption-ledger-v1-2026-10-11.csv

## 3. Monthly driver schema

Use one row per month and scenario. For Year 1, create months M01–M12; extend the same structure through at least 36 months only after the first-year bridge is reconciled.

| Field | Definition / required treatment | Evidence needed |
|---|---|---|
| scenario_id | Downside / Base / Upside, each independently driven | Approved scenario definitions |
| period | YYYY-MM | Forecast start date |
| opening_active_clients | Active paying clients at start of month | CRM/starting cohort or explicit opening assumption |
| new_clients_won | Newly signed clients that meet the defined revenue-start condition | Funnel conversion and start-date assumption |
| churned_clients | Clients ending recurring service in the month | Historical data or clearly labeled assumption |
| ending_active_clients | Opening + new − churn, adjusted for partial-month start/end rules | Formula and reconciliation |
| new_client_start_days | Start date / billable days by client where material | Contract/onboarding assumptions |
| recurring_arpc | Average recurring price per active client, by service mix | Signed price list / evidence-backed price assumption |
| recurring_revenue | Recognized recurring revenue for the period | Client-month calculation and revenue-recognition policy |
| project_revenue | One-off project revenue recognized in period | Project pipeline, milestones, acceptance/billing rules |
| discounts_credits_refunds | Discount, credit and refund reductions | Contract and payment-policy evidence |
| total_recognized_revenue | Recurring + project revenue − discounts/credits/refunds | Reconciled calculation |
| delivery_cost_by_service | Contractor cost, service mix, revisions, QA and project management | Scope-level cost and capacity evidence |
| sales_commission | Commission by eligible contract/payment and defined base | Approved policy, payout trigger and clawback rules |
| payment_processing_fx_fees | Processor, conversion and bank fees | Provider pricing and currency path |
| tools_and_software | Actual required seats and subscriptions by month | Named tool inventory and billing cycle |
| fixed_opex | Fixed recurring operating costs | Contracts/approved budget |
| step_fixed_and_hiring_cost | Cost increases when capacity/volume thresholds are crossed | Hiring plan and threshold assumptions |
| one_time_setup_cost | Non-recurring setup, legal, equipment and launch costs | Quoted or documented cost |
| taxes_and_statutory_costs | Entity/jurisdiction-specific tax assumptions, separated from operating cost | Dated official sources and qualified CA review |
| gross_profit | Recognized revenue less direct delivery cost | Defined accounting policy |
| contribution_profit | Gross profit less variable sales/payment/acquisition costs | Stable contribution-margin definition |
| operating_profit_or_ebitda | Contribution less applicable OPEX, per defined policy | Consistent cost classification |
| invoice_amount | Amount invoiced in period | Billing schedule |
| cash_collected | Cash actually expected/received in period, separated from recognized revenue | Payment terms, collection lag, bad debt assumptions |
| receivables_open_close | Opening + invoices − collections − write-offs/credits | AR roll-forward |
| contractor_payouts | Cash payment timing, distinct from expense recognition | Contract terms and payout schedule |
| sales_commission_cash_paid | Cash payout timing, distinct from commission expense | Approved payout policy |
| tax_cash_paid | Cash tax payment timing | Professional tax schedule |
| opening_cash | Cash available at start of period | Bank balance / explicit starting point |
| closing_cash | Opening cash + collections − cash outflows | Independent cash roll-forward |
| fx_rate_assumption | Currency conversion rate used for each relevant cash flow | Dated source and downside/base/upside values |
| source_ids | Assumption IDs and source document references | Link each material input to the ledger |
| confidence_and_owner | Confidence level and accountable reviewer | Named role/person and review date |

## 4. Core relationships to test

These are design relationships, not validated formulas in an existing workbook:

1. Ending clients = opening clients + new wins − churn, adjusted for contract start/end timing and any explicit client reactivation.
2. Recognized revenue is calculated from service delivery/contract rules; it must not automatically equal invoices or cash collected.
3. Total recognized revenue = recurring revenue + project revenue − applicable discounts/credits/refunds, with accounting treatment documented.
4. Direct delivery costs must be driven by service/client scope and capacity, not copied as an unexplained percentage of revenue.
5. Gross profit = recognized revenue − direct delivery cost under the chosen cost classification.
6. Contribution profit must deduct all costs classified as variable contribution costs; the policy must state treatment of sales commission, payment fees and variable acquisition spend.
7. Closing cash = opening cash + actual/forecast cash collections − contractor payouts − commission payouts − payroll/OPEX cash paid − taxes paid − capital/setup spending ± financing/FX cash effects.
8. Annual revenue must equal the sum of the 12 monthly recognized-revenue values. Quarterly P&L rows must equal the corresponding three monthly values.
9. Year-end MRR is a run-rate snapshot and must not be substituted for annual recognized revenue.
10. Markup, gross margin, contribution margin, operating margin and net margin must be separately named and calculated consistently.

## 5. Required sensitivity cases
Do not assign numerical values until evidence is sourced. Each scenario must vary at least:
- new client wins and sales-cycle delay;
- close rate and lead volume;
- recurring ARPC / service mix / discounts;
- churn and client ramp/partial-month timing;
- direct delivery cost, capacity utilization, revisions and contractor availability;
- commission terms, refunds, bad debt and collection delay;
- tool/OPEX and step-fixed hiring;
- FX rate, processor fees and cash conversion timing;
- tax assumptions after qualified review.

## 6. Reconciliation checklist
- [ ] Explain where the $68,500 narrative figure comes from.
- [ ] Map each Q1–Q4 P&L revenue row to underlying monthly/client/service drivers.
- [ ] Determine whether the two figures refer to different revenue definitions, periods, scope or versions.
- [ ] Tie each service's price, hours/capacity, contractor cost and commission to the same client example.
- [ ] Separate accrual revenue from invoice and cash collection.
- [ ] Reconcile delivery cost, gross profit, OPEX, EBITDA, tax and net profit from monthly rows.
- [ ] Build an independent cash roll-forward and minimum-cash/runway calculation.
- [ ] Have finance owner approve the baseline; obtain qualified tax review where required.
- [ ] Only then populate the model and create independent expected-output fixtures.

## 7. Current status
**Schema drafted; numeric forecast remains blocked.** No values have been approved, no model workbook created, and no workbook formulas executed. The next evidence dependency remains a binary-capable read-only inspection route for the Evaluation Sheet and Checklist candidates; their filenames alone do not establish financial-model suitability.

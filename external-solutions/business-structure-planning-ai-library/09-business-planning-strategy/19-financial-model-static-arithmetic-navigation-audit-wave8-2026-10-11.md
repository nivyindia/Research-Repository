# Financial Model Static Arithmetic & Navigation Audit — Wave 8
**Audit date:** 2026-10-11  
**Scope:** Read-only review of the Nivy Next financial-model index, main agency financial plan, Part 1/4/6/11 sections, mirror index, and existing Wave 7 assumption ledger.  
**Status:** Static review only. No workbook was executed, no formulas were recalculated in Excel/LibreOffice, no source file was modified, and no financial/tax/legal conclusion is approved.

## 1. New evidence reviewed

| Artifact | Evidence / disposition |
|---|---|
| `Notion - Nivy OS/Nivy Next Financial Model …md` | Index SHA `0499d9a1cbf60af4ea2f96f70df8bea5f631808d`; 13 named section links plus one blank-title link. |
| `Nivy Research Data/Nivy Next Financial Model …md` | Mirror index SHA `335e6ede5362984939decd31f95f19b5de3fc553`; same overall section pattern but target filenames/IDs differ. This is not an exact duplicate; compare child content before deciding canonical/mirror treatment. |
| `Notion - Nivy OS/10 0 Financial Plan …md` | SHA `2dd35d06ad74586e822d42a2448240ebd39d7dc1`; contains incompatible annual revenue claims and a quarterly P&L. |
| Part 1 Agency Overview | File exists; narrative-only source. |
| Section 4 Cost Structure & Unit Economics | File exists; unsourced price/cost/CAC benchmarks and inconsistent margin definitions. |
| Part 6 Currency Risk/Pricing | File exists; repeats a markup/margin formula error and unsupported FX volatility claims. |
| Section 11 Operational Cost Structure | File exists but is not linked from the index. |
| Untitled linked file | Exists, title is only `# Untitled`; no meaningful content or clear purpose found in the retrieved text. |

## 2. Index-link audit

- The canonical index links sections 2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 14, 15 and 16.
- Part 1 and Section 11 exist in the same folder but are not linked from the index.
- No Section 9 document is established by the current index or retrieved evidence. Treat it as a **navigation/source gap**, not proof the dashboard capability does not exist elsewhere.
- The final link has no link text and resolves to an `Untitled` document with no substantive content. Its origin/purpose is unresolved.
- The mirror index uses separate Notion-export IDs and paths. Do not use different file hashes alone to conclude that the body content is different; first normalize internal link targets and compare the substantive text.

## 3. Independent arithmetic spot-checks

### 3.1 Revenue baseline conflict
- Narrative Year-1 revenue claim: **$68,500**.
- Quarterly P&L revenue rows: $12,000 + $34,500 + $61,500 + $82,000 = **$190,000**.
- Difference: **$121,500**; quarterly total is about **2.77×** the narrative amount.
- The revenue rows sum arithmetically, but the forecast is not decision-grade until a monthly client/revenue bridge reconciles them.

### 3.2 P&L row arithmetic
- Quarterly cost of delivery totals: $3,900 + $11,200 + $20,000 + $26,650 = **$61,750**.
- Gross profit totals: $8,100 + $23,300 + $41,500 + $55,350 = **$128,250**; revenue less delivery cost reconciles.
- OPEX: $3,300 per quarter × 4 = **$13,200**.
- EBITDA: $128,250 − $13,200 = **$115,050**; reconciles.
- Listed taxes total **$28,762** and net profit totals **$86,288**; the sum reconciles to EBITDA less listed taxes, subject to rounding.
- These arithmetic checks do **not** validate the underlying revenue ramp, delivery capacity, tax assumptions, cash collection timing, balance sheet, or accounting treatment.

### 3.3 Delivery-cost driver mismatch
- The plan states a delivery pod costs about **$3,250/month** and serves **$10,000–$12,000 MRR**.
- The quarterly P&L has $3,900 of delivery cost in Q1, equivalent to $1,300/month over three months, while Q1 revenue is $12,000 total. This does not transparently map to the stated pod economics.
- Required: model delivery costs from active clients, service mix, hours/capacity, contractor rates, QA/account management, commissions, and client start dates—not as an unexplained percentage copied across quarters.

### 3.4 Markup is not margin
- The Part 6 formula multiplies cost by 1.20 and calls this a 20% profit margin.
- A 20% markup on cost gives a **16.67% gross margin** before FX buffer and fees.
- For a target gross margin (m), the basic price formula is `price = cost / (1 - m)`; FX buffer, payment fees and contingency should be explicit separate drivers to avoid double counting.

## 4. Additional static control issues confirmed
1. Main plan labels all costs as variable/freelance-driven while also assuming material fixed OPEX; separate fixed, variable, step-fixed and one-time costs.
2. “Zero overhead,” “zero cashflow risk,” and “margin collapse unlikely” style absolute claims are unsupported; replace with explicit risk cases and working-capital assumptions.
3. Year-2/Year-3 ending MRR targets cannot stand in for annual recognized revenue. A monthly bridge must account for opening clients, additions, churn, ARPC, ramp/discounts, revenue recognition and collection timing.
4. The main plan's ₹83/USD assumption is undated; do not treat it as a current exchange rate.
5. Tax at a flat approximate 25% is only a placeholder and cannot substitute for entity/jurisdiction-specific tax modeling and qualified review.
6. Price/cost/CAC benchmarks in Section 4 lack source dates, scope definitions, sample sizes and confidence. Keep them in the assumption ledger as low-confidence hypotheses.

## 5. Decisions and next actions

| ID | Priority | Action | Exit criterion | Status |
|---|---|---|---|---|
| FM-INV-02A | P0 | Resolve every canonical and mirror index link | Valid/broken target list with exact paths; classify all linked files | In progress |
| FM-INV-03A | P1 | Compare mirrored section bodies | Normalized content comparison, internal links excluded from body-difference checks; no originals removed | Open |
| FM-ASSUMP-01 | P0 | Resolve Year-1 forecast baseline | Monthly driver bridge reconciles revenue, MRR, costs, EBITDA, taxes and cash | Blocked |
| FM-ASSUMP-02 | P0 | Reconcile delivery capacity/cost | Service/client-level cost schedule ties to P&L and capacity | Blocked |
| FM-ASSUMP-03 | P0 | Correct pricing definitions | Separate markup, gross margin, contribution margin, net margin and FX buffer; tested examples | Open |
| FM-NAV-01 | P1 | Identify purpose of Untitled and missing Section 9 source | Evidence-backed mapping or explicit “missing/not applicable” disposition | Open |
| FM-TEST-01 | P0 | Inspect candidate XLSX files via a binary-capable local route | Read-only package/sheet/formula inventory; originals untouched | Blocked by binary access |
| FM-GOV-01 | P0 | Review jurisdiction-specific tax, refund and contract claims | Dated official sources plus qualified CA/legal review | Blocked |

## 6. Guardrails
- No workbook or source document was edited, deleted, or executed.
- No external workbook is approved for reuse until its asset-level license/NOTICE/dependency terms are recorded.
- Do not build a replacement workbook until the source assumptions and revenue baseline are reconciled.
- Release remains **BLOCKED** until an executable model, independent numerical fixtures, scenario tests, reconciliation evidence, qualified review where required, and explicit approval exist.

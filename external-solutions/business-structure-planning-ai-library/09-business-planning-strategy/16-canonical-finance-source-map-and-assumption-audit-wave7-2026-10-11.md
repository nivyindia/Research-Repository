# Canonical Finance Source Map & Assumption Audit — Wave 7
**Audit date:** 2026-10-11  
**Scope:** Read-only review of Nivy Next financial-model Markdown sections and the main Financial Plan.  
**Rule:** This is a source-of-truth proposal and static audit, not approval of assumptions, legal advice, or a tested financial model.

## 1. Canonical source decision (provisional)

Use **`Notion - Nivy OS/`** as the canonical *review location* for the Nivy Next agency financial narrative because its index, named sections, and financial-plan documents are grouped there. Do not delete, move, or overwrite any mirror. Keep `Nivy Research Data/` copies as reference/mirror candidates until a complete path + blob-SHA comparison is recorded.

| Capability / section | Provisional canonical file | Current disposition |
|---|---|---|
| Model index / navigation | `Notion - Nivy OS/Nivy Next Financial Model e4feb94b1a2a8214823701f5c30c9a4c.md` | Canonical index candidate; incomplete navigation |
| 1. Agency overview | `Notion - Nivy OS/💹 Financial Model — Part 1 Agency Overview 36beb94b1a2a837da5d50174154090ac.md` | Narrative only; assumptions require validation |
| 2. Cash flow | `Notion - Nivy OS/💹 Financial Model — Part 2 Cash Flow Clarity Syste 5d7eb94b1a2a83d1b02681d922e8b294.md` | Narrative + suggested workflow; no validated calculations |
| 3. Growth budget | `Notion - Nivy OS/💹 Financial Model — Part 3 Growth Budgeting Framew cb1eb94b1a2a83d898fb815a5800c316.md` | Narrative; allocation percentages are proposals, not evidence |
| 4. Unit economics | `Notion - Nivy OS/SECTION 4 — Cost Structure & Unit Economics 7c8eb94b1a2a828ca6ab81d82babc463.md` | Price/cost ranges un-sourced; examples need recalculation |
| 5. Tax/compliance | `Notion - Nivy OS/SECTION 5 — Taxation & Compliance (Global + India) e1ceb94b1a2a82cf84e681e1cbb8ff91.md` | High-risk claims; CA/legal verification required before use |
| 6. FX/pricing | `Notion - Nivy OS/💹 Financial Model — Part 6 Currency Risk, Pricing  abbeb94b1a2a833f9fc381d7cf645d5d.md` | Formula and FX claims need correction/verification |
| 7. Payments/refunds/bad debt | `Notion - Nivy OS/SECTION 7 — International Payments, Refunds & Bad  abbeb94b1a2a835ab25a01bb7ee5c27a.md` | Policy draft only; jurisdiction and contract review needed |
| 8. Risk/emergency planning | `Notion - Nivy OS/💹 Financial Model — Part 8 Risk & Emergency Planni 093eb94b1a2a832c9f65817d04ea4282.md` | Policy draft; reserve assumptions need cash model |
| 9. CFO dashboard / automation | No clearly linked section-9 file found in the index | Navigation gap; identify source or mark missing |
| 10. Financial automation | `Notion - Nivy OS/🧮SECTION 10 — Financial Automation Stack f94eb94b1a2a8311a7510139dcac31a4.md` | Tool/workflow specification; automation not implemented/tested |
| 11. Operational costs | `Notion - Nivy OS/🧾SECTION 11 — Operational Cost Structure 49beb94b1a2a83159e7e818f3c6f15ed.md` | Narrative cost bands; conflicts with lean-cost claims elsewhere |
| 12. Scaling milestones | `Notion - Nivy OS/SECTION 12 — Scaling Strategy & Milestones 44deb94b1a2a83a191938135e03e89b7.md` | Targets are aspirational, not forecast outputs |
| 13. LTV | `Notion - Nivy OS/SECTION 13 — LTV Maximization Plan 8bceb94b1a2a82eb9fec81cbd8bfec91.md` | Arithmetic spot-check: sample LTV totals reconcile; retention assumptions unproven |
| 14. Pricing experiments | `Notion - Nivy OS/SECTION 14 — Pricing Strategy & A B Experiments b89eb94b1a2a820f9ef301f1d6e4d2f3.md` | Price menu only; no experimental data |
| 15. Accountability | `Notion - Nivy OS/SECTION 15 — Accountability System 66aeb94b1a2a83c8b8a28148c75c73a1.md` | Roles/cadence described; owners and approval evidence absent |
| 16. Dashboards/reporting | `Notion - Nivy OS/SECTION 16 — Financial Dashboards & Reporting db1eb94b1a2a827cb67801b3f8a0ce92.md` | Metric specification; live dashboard not evidenced |
| Main agency financial plan | `Notion - Nivy OS/10 0 Financial Plan 33eeb94b1a2a83478eaf81c19e2bf7f4.md` | Contains material forecast inconsistencies; do not use for decisions yet |
| Separate ecosystem plan | `Notion - Nivy OS/Financial plan one to three years 280eb94b1a2a82f39431813a04db9cf2.md` | Different business model (events/creator agency); keep separate from Nivy Next agency model |

## 2. Navigation and completeness findings

1. The index links sections 2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 14, 15 and 16, but does not clearly link section 1, section 9, or section 11. A blank-title `Untitled ...md` link also exists and needs identification.
2. Section numbering skips 9 and 11 in the index, while a separate section-11 operational-cost file exists. This is a navigation/versioning issue, not proof that the underlying capability is absent.
3. Section documents repeatedly contain “If you want, I can now prepare…” drafting prompts. These are authoring leftovers and should not be interpreted as completed projections or controls.
4. No validated integrated workbook has yet been identified. The 14 XLSX candidate classification is in Wave 6; binary workbook contents remain uninspected through the current text-only GitHub connector.

## 3. Material static inconsistencies — resolve before modeling

| ID | Finding | Why it matters | Required correction / evidence |
|---|---|---|---|
| AUD-01 | Main Financial Plan states Year-1 total revenue about **$68,500** in the narrative projection, but the quarterly P&L totals **$190,000**. | Two incompatible Year-1 revenue baselines. | Choose one driver-based forecast; reconcile monthly client starts, churn, ARPC, ramp timing and quarterly totals. |
| AUD-02 | Year-1 P&L assumes 67.5% gross margin and 45.4% net margin while the cost section lists a roughly **$3,250/month delivery pod** serving **$10,000–$12,000 MRR**. | Could be compatible only with defined utilization/client mix; staffing and quarter-by-quarter delivery cost do not transparently follow the client ramp. | Build capacity-based delivery cost by service/client, then reconcile COGS and OPEX. |
| AUD-03 | Year-2/Year-3 end-of-year MRR targets are paired with annual revenue figures, but the bridge from opening MRR to ending MRR is not shown. | Ending run-rate is not annual recognized revenue. | Use monthly forecast rows with opening clients, additions, churn, ARPC, recognized revenue and ending MRR. |
| AUD-04 | FX formula says “20% profit margin” but multiplies cost by **1.20**. A 20% markup on cost yields a 16.7% margin before the FX buffer, not a 20% margin. | Misstates pricing and can underprice work. | If target gross margin is 20%, use price = cost / (1 − 0.20); apply any FX buffer explicitly and avoid double counting. |
| AUD-05 | The documents claim FX arbitrage creates 20–40% extra margin and that 2–5% monthly / 8–12% yearly USD-INR movement is typical, without dated sources. | Unsupported market claims can distort pricing and forecast risk. | Remove or label as unverified; add dated exchange-rate source, observed period, scenario range and sensitivity table. |
| AUD-06 | Section 1 describes 35–75% agency margin bands, while section 4 says 70%+ contribution margin is excellent and section 12 forecasts 20–45% net margin. Definitions differ or are not stated consistently. | Gross margin, contribution margin, delivery margin and net margin are not interchangeable. | Define each metric and its included costs; reconcile the same sample client across all sections. |
| AUD-07 | Section 2 says freelancers are paid only after client cash arrives and implies “zero cashflow risk.” | Timing gaps, refunds, chargebacks and contractual payment obligations can still create liquidity risk. | Replace absolute claim with a payment policy plus working-capital and downside stress test. |
| AUD-08 | Section 5 contains categorical GST, LUT, TDS, presumptive-tax and corporate-tax statements without dated official sources or caveats. | Tax applicability depends on facts, entity type, service, threshold and current law. | Treat as unapproved draft; validate every claim against current official sources with a qualified Indian CA/tax professional. |
| AUD-09 | Refund/late-fee policy proposes fixed windows, fees and non-refundable terms as “industry standard” without jurisdiction-specific contract/legal support. | Enforceability varies by contract and jurisdiction. | Legal review; document consumer/business status, scope, work-start definition and dispute rules. |
| AUD-10 | Growth plan recommends cold-email volumes of 5,000–10,000/month and LinkedIn automation without a deliverability/compliance cost model. | Reputation, consent/data protection, platform terms and tooling costs may be material. | Model sending infrastructure, bounce/complaint limits, lawful basis and platform-compliant workflows before forecasting. |

## 4. Assumption register — first pass

These are **documented assumptions**, not validated facts. Convert them to an input table with stable IDs before implementing formulas.

| ID | Assumption found | Current status | Required metadata |
|---|---|---|---|
| ASM-001 | USD/INR = ₹83 in the main financial plan | Stale/undated | Source, as-of date, conservative/base/upside rates |
| ASM-002 | Retainers of $1,500–$5,000 in main plan | Unverified target | ICP, service scope, market evidence, close rate |
| ASM-003 | Commission 15–25% first payment and 10–15% recurring in other sections | Conflicting policy ranges | Commission base, clawback/refund treatment, payout trigger, duration |
| ASM-004 | Agency margins 35–75% depending on section | Definitions inconsistent | Gross/contribution/net definition and service mix |
| ASM-005 | Tool spend ranges from $60–$120 lean in one section to $150–$250 lean in section 11, and $300/month in main plan | Conflicting versions | Named tools, seats, billing period, free-tier assumptions, currency |
| ASM-006 | Emergency reserve of 3 months; separate 90-day zero-revenue survival goal | Directionally consistent, not calculated | Fixed vs variable costs, reserve currency, owner approval |
| ASM-007 | Bad-debt reserve 2–5% of revenue | Unverified policy | Historical loss data or downside rationale |
| ASM-008 | 50/30/20 or 50/30/20 allocation models for operating/growth/owner or reserve | Conflicting allocation purposes | Define denominator (revenue, gross profit, or distributable profit) and precedence |
| ASM-009 | Growth milestones of $5k–$100k MRR within 3–12 months across docs | Aspirational, not probability-weighted | Funnel capacity, lead volume, conversion, churn, delivery capacity and cash requirement |
| ASM-010 | Freelancer/service price ranges in section 4 | Unverified benchmarks | Dated sources, skill/scope, geography, hours, revisions and QA cost |

## 5. Recommended decision

**Do not build the production model directly from the current prose.** First produce one normalized assumptions ledger and a month-by-month driver schedule. The initial model should have:
- 12–36 monthly periods;
- explicit client acquisition, churn, ARPC, service mix and ramp;
- revenue recognition and collection timing separated;
- direct delivery costs, commissions, tools, fixed overhead, taxes and FX fees separated;
- P&L, cash flow and a minimal balance sheet linked to the same drivers;
- base / downside / upside scenarios;
- formulas independently checked against a small hand-calculated fixture.

## 6. Next action queue

| Priority | Action | Status |
|---|---|---|
| P0 | Resolve AUD-01 Year-1 revenue conflict and establish one forecast baseline | Open |
| P0 | Create normalized assumption ledger with source/status/owner fields | Next |
| P0 | CA review of tax claims; legal review of refund/late-fee/commission terms | Blocked on qualified review |
| P1 | Compare all mirror candidates by exact path and blob SHA; preserve originals | Open |
| P1 | Repair index links and identify the untitled child document | Open |
| P1 | Read-only inspect workbook candidates using a binary-capable route/local copy | Blocked by connector |
| P1 | Decide reuse vs build after workbook classification and licensing review | Blocked |

## 7. Audit limitations

- This is static inspection of Markdown and repository metadata only.
- No live market price, current FX rate, tax law, or external benchmark was verified in this wave.
- No workbook was recalculated; no formulas were executed.
- No original files were deleted or modified.

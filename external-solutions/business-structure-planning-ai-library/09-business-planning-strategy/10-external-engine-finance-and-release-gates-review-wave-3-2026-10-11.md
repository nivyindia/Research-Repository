# External Engine Finance and Release-Gate Review — Wave 3
**Updated:** 2026-10-11  
**Scope:** Static inspection of additional exact files in Peter Bamuhigire's repository. No runtime tests performed by this review.

## Files inspected
- [Plan assembly skill](https://github.com/peterbamuhigire/business-plan-skills/blob/main/skills/pipeline/00-plan-assembly/SKILL.md) — blob SHA `e8906c614d8f939d04f94e8801567f7eec7c7766`.
- [Financial projections skill](https://github.com/peterbamuhigire/business-plan-skills/blob/main/skills/pipeline/10-financial-projections/SKILL.md) — blob SHA `a8ce2fbfcdb5600d8aca56644908c77715971717`.
- [Business model design skill](https://github.com/peterbamuhigire/business-plan-skills/blob/main/skills/meta-strategy/meta-business-model-design/SKILL.md) — blob SHA `2303806f66ce31b5c224ccfb9493dcb62325b694`.
- [Local output-readiness review dated 2026-09-06](https://github.com/peterbamuhigire/business-plan-skills/blob/main/docs/audits/2026-09-06-kaizen-readiness.md) — blob SHA `ac499819b463cbf20f0624cae1d504c97e77bf8e`.

## Findings that materially change the assessment

### 1. Orchestration and business-model selection are unusually explicit
The orchestrator and model-design skill specify an evidence-first, model-first sequence:
- No drafting before the decision, audience, jurisdiction, and authority are clear.
- Claims that carry the business case need evidence or must remain blocked.
- Alternative business models are compared; the selected model is scored against customer, channel, delivery, margin, after-sales burden, defensibility and funding constraints.
- Weak factors route into validation experiments; the model feeds product/service, marketing/sales and financial projection sections.
- Plan assembly is explicitly downstream of synthesis, stress testing, due diligence and financial review. Different recipient types require different packages.

**Recommendation:** Reuse the gate concepts and dependency ordering. Adapt the scoring scales and sector/country-specific methods only after checking the underlying references and evidence requirements. Do not copy numeric verdicts as if they were validated market facts.

### 2. The financial projection skill specifies a model, but that is not the same as an executed model
The skill requires Year 1 monthly projections, outer-year projections, P&L, cash flow, balance sheet, break-even, unit economics, ratios, sensitivities and assumption traceability. It also says to reconcile financials with market, operations, hiring and funding.

However, the inspected repository audit states that its workbook checks are structural rather than evidence of correct calculations:
- Seven workbooks passed checks for ZIP readability, expected sheet names/counts and formula-text checks.
- A read-only inventory found 4,385 formula cells and all cached values were zero.
- The audit identifies an example formula-map case where a scenario formula has a zero cached value despite its branches not returning zero.
- The audit explicitly says workbook calculation, document/deck rendering, professional acceptance and release authority were not established.
- Four sample audience packs remained blocked for release; a structurally valid release bundle is not release approval.

This is a valuable and candid audit trail. It also proves that a repository can contain sophisticated skill specifications and passing structural validators while financial execution remains unverified.

**Recommendation:** Treat this repository as a strong planning-method and gate library, not as proof of a fully calculation-validated finance engine. If borrowing its financial patterns, require recalculation of a controlled copy in a real spreadsheet engine, independent expected-value checks, scenario application evidence, narrative/model reconciliation and authorised reviewer sign-off.

### 3. Plan assembly has useful acceptance criteria
The assembly skill requires stable financials and prerequisite review, audience-specific packaging, a consistent funding story across letter/plan/appendices, a final TOC, attachment checklist, and an issue list when blockers remain. It warns against generic packaging across bank, investor, DFI and grant audiences.

**Recommendation:** Integrate these acceptance criteria into the universal release checklist, but keep “document assembled,” “structural validator passed,” “financial calculations verified,” and “authorised for external release” as separate states.

## Updated capability implications
| Capability | New evidence | Updated conclusion |
|---|---|---|
| Business-model design before drafting | Actual model-design skill inspected | Strong specification; scoring still requires evidence and human judgement |
| Integrated financial projection requirements | Actual finance skill inspected | Broad requirements are specified; calculation validity is not proven |
| Workbook formula and scenario integrity | Local audit file inspected | Explicit gap between formula-text/structure checks and executed scenario results |
| Audience-specific assembly | Actual assembly skill inspected | Strong packaging rules; release authority remains separate |
| Governance/release state | Audit records blocked/not-assessed states | Adopt status semantics; never treat simulated committee pass or structural validation as real-world approval |

## Next static-review steps
1. Inspect the financial skill's linked calculation/template artifacts and the release-gate validator/contract; record what each check actually verifies.
2. Inspect Musengimana's reference guides and script contents, not just their names; document the exact write/verify sequence and whether scripts assert calculated outputs or only formula preservation.
3. Inventory all linked Nivy financial-model documents and distinguish prose policy, sample benchmarks, spreadsheet formulas and actual outputs.
4. Update the master capability register after those inspections. Then design isolated runtime tests on copies; do not test or modify originals during this static phase.

## Limitation
This wave inspects only the four listed files and their claims. It is not a full repository audit, and it does not execute any code or independently recalculate any financial model.

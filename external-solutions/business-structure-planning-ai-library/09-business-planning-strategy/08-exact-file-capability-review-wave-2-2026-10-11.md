# Exact-File Capability Review — Wave 2
**Updated:** 2026-10-11  
**Scope:** Repository file inspection and declared capability assessment only. No runtime testing performed.

## 1. Summary of work completed in this wave
- Created a consolidated canonical blueprint from the two international-plan outline files and expanded it into an adaptable, gated 105-point master architecture with business-archetype overlays.
- Inspected the actual orchestrator skill and its stage-gate reference in `peterbamuhigire/business-plan-skills`.
- Inspected the actual `SKILL.md`, license, notice, and dependency declaration in `Musengimana/develop-a-business-plan-in-minutes`.
- Inspected Nivy’s financial-model index, cash-flow guidance, and cost/unit-economics guidance.
- No packages were installed; no scripts or workbook were run; no claim of runtime verification is made.

## 2. Canonical outline status
Canonical file: [07-canonical-international-business-plan-blueprint-2026-10-11.md](07-canonical-international-business-plan-blueprint-2026-10-11.md)

The two outline source files are **near-duplicates, not byte-identical in the current revision**:
- [Nivy Artisan outline](https://github.com/nivyindia/Research-Repository/blob/main/Nivy%20Artisan/International-Business-Plan-Topics.md) — current blob SHA `bee70411a70c72a50e257db5e67a3dc08acfe653`.
- [Claude chat outline](https://github.com/nivyindia/Research-Repository/blob/main/Chats/Claude/International-Business-Plan-Topics.md) — current blob SHA `bee70411a70c72a50e257db5e67a3dc08acfe653` was reported by an earlier index, but a fresh fetch returned `bee70411a70c72a50e257db5e67a3dc08acfe653` only for the Claude file; current contents differ in the timestamp/header. **Re-check both current blob SHAs before any destructive deduplication.** Do not delete either source. The canonical blueprint is a new consolidated derivative, preserving both sources.

## 3. External repository: Musengimana/develop-a-business-plan-in-minutes
Files inspected:
- [README.md](https://github.com/Musengimana/develop-a-business-plan-in-minutes/blob/main/README.md), SHA `efa258e30cc93274dd21c7e2c70efa450a193110`
- [build-client-business-plans/SKILL.md](https://github.com/Musengimana/develop-a-business-plan-in-minutes/blob/main/build-client-business-plans/SKILL.md), SHA `1f182e419314f98a4a9a2b2a94e10283a3b60439`
- [LICENSE](https://github.com/Musengimana/develop-a-business-plan-in-minutes/blob/main/LICENSE), SHA `7370859341ecf3cf279ddc2c9d908c73ff5535d6`
- [NOTICE.md](https://github.com/Musengimana/develop-a-business-plan-in-minutes/blob/main/NOTICE.md), SHA `4b46f86723bde322793f9d908ad99e383ef5bf53`
- [requirements.txt](https://github.com/Musengimana/develop-a-business-plan-in-minutes/blob/main/requirements.txt), SHA `59613cd23b1210fabd6c2e3f914c347c96d83493`
- A root-level `SKILL.md` and root-level `NOTICE` were requested and returned 404; actual paths are nested skill file and `NOTICE.md`.

### What is actually specified
- Hybrid intake with a short essential-question round, then labelled assumptions.
- Current web research with citations; research standards and claim/assumption separation.
- Editable Word business plan and Excel financial forecast using bundled templates.
- Financial model workflow is deliberately restricted to a dedicated workbook-writing script; formula-integrity, document-validation and model-audit scripts are named.
- Base/upside/downside scenario handling and narrative-to-workbook reconciliation are specified.
- Dependencies are declared: Python 3.10+, `openpyxl`, `lxml`, and LibreOffice/soffice; live web and file/shell access required for full behavior.
- README claims 1,064 formulas and 22 dropdown controls are verified by the included checks. This is a repository claim; this review did not run those checks.

### Suitability and caveats
- **Best reuse candidate for:** structured intake, assumption IDs, evidence/citation discipline, editable plan packaging, spreadsheet-integrity workflow and scenario appendix.
- **Major localization work:** Canada/CAD/BDC workbook is the default. The skill says it can adapt jurisdiction/currency, but UAE/India/other-country tax, legal, regulatory and financing assumptions still require source-by-source validation and local professional review.
- **License:** most repository content is MIT. The BDC financial workbook is explicitly excluded from MIT and governed by BDC terms; the notice says it is included with written permission. Do not redistribute or modify that workbook without checking the applicable terms and permissions.
- **Integration status:** candidate for selective adaptation; not yet approved as an integrated component. Need inspect all reference files, scripts, templates, dependency security, and actual output checks before adopting.
- **Runtime status:** not tested.

## 4. External repository: peterbamuhigire/business-plan-skills
Files inspected:
- [README.md](https://github.com/peterbamuhigire/business-plan-skills/blob/main/README.md), SHA `45e3ebead482a42ee6e675389b5c9f44a8497475` (SHA previously recorded in the first-pass catalog; refresh if pinning exact current revision).
- [Business Plan Orchestrator SKILL.md](https://github.com/peterbamuhigire/business-plan-skills/blob/main/skills/meta-strategy/business-plan-orchestrator/SKILL.md), SHA `9f6aef95c450848364427939c88c7398d1d81a83`.
- [End-to-end stage gates](https://github.com/peterbamuhigire/business-plan-skills/blob/main/skills/meta-strategy/business-plan-orchestrator/references/end-to-end-stage-gates.md), SHA `bcca23a83246677660374b603b07f4d97fefa703`.
- [LICENSE](https://github.com/peterbamuhigire/business-plan-skills/blob/main/LICENSE), SHA `39d69a62ca40ee161b47394ef5493d4c26b43331`.
- Paths `skills/00-plan-assembly/SKILL.md` and `skills/finance/build-financial-models/SKILL.md` returned 404; actual file locations must be discovered from repository references rather than guessed.

### What is actually specified
- Explicit intake gate for decision, audience, jurisdiction, scope and authority.
- Claim-and-evidence plan before prose; unsupported load-bearing claims block progress.
- Business-model and strategy gates before section drafting; includes PESTEL/forces/factor analysis/TOWS and international-entry overlay when applicable.
- Finance gate requires integrated statements, assumptions, formula map, scenarios, narrative/model reconciliation and stress tests.
- Challenge, due diligence, audience-specific red-team, assembly, rendering/QA, handoff evidence, release bundle and release-authority gates are described.
- Stage-gate reference includes distinct routes for banks, DFIs, equity/VC, grants, owner-managers and strategic partners, plus knockout conditions.

### Suitability and caveats
- **Best reuse candidate for:** orchestration, stage gates, evidence ownership, blocking rules, audience-specific review and controlled release.
- **Complementarity:** this is an orchestration/governance layer, while the Musengimana project emphasizes concrete Word/Excel deliverables and workbook-preservation procedures. They should not be blindly merged; map overlapping gates and choose one canonical state model.
- **Localization:** README notes regionally oriented material (Uganda/Kenya/Tanzania); validate country-specific assumptions and specialist content before UAE/global reuse.
- **License:** inspected LICENSE says MIT. Individual third-party assets and dependencies still need their own provenance/license review.
- **Runtime status:** not tested. README claims about skill counts and capabilities are not treated as proof every subskill is complete or works.

## 5. Nivy existing financial material: content review
Inspected:
- [Nivy Next Financial Model index](https://github.com/nivyindia/Research-Repository/blob/main/Nivy%20Research%20Data/Nivy%20Next%20Financial%20Model%2029bb3416c76d818bbe6ae31cc86e3929.md), SHA `335e6ede5362984939decd31f95f19b5de3fc553`.
- [Cash Flow Clarity System](https://github.com/nivyindia/Research-Repository/blob/main/Nivy%20Research%20Data/%F0%9F%92%B9%20Financial%20Model%20%E2%80%94%20Part%202%20Cash%20Flow%20Clarity%20Syste%202b1b3416c76d80c6b36bd2a972b2efcf.md), SHA `4369dac5e3653020901b61b69b8dc321672c50d6`.
- [Cost Structure & Unit Economics](https://github.com/nivyindia/Research-Repository/blob/main/Nivy%20Research%20Data/SECTION%204%20%E2%80%94%20Cost%20Structure%20&%20Unit%20Economics%202b1b3416c76d80ef9d8dceef8b03af78.md), SHA `f6338877a7962c6a02183e396fafd950667532f6`.

### Coverage already present in Nivy docs
- Cash received vs expected, invoice/payment dates, AR aging, multicurrency inflows and payment gateway fees.
- Expense categories, contractor/freelancer payouts, sales commissions, tool spend, reserve policies and dashboard/review cadence.
- Service-level price/delivery-cost examples, commission structures, CAC and contribution-margin concepts.
- The index links to growth budgeting, taxation/compliance, currency risk, bad debt, financial automation, scaling, LTV, pricing experiments, accountability and dashboards.

### Gaps / reliability flags
- These inspected files are narrative guidance and benchmark tables, **not proof of an executable integrated financial model**. No formula workbook was inspected or recalculated in this wave.
- Price, CAC, freelancer cost, margin and commission values are not accompanied in the inspected unit-economics section by dated source citations or a documented sampling methodology. Treat as unverified hypotheses, not current market facts.
- Some recommendations are overly categorical (for example, paying freelancers only after client payment or holding a fixed share of FX proceeds); cash, contracts, law, client SLAs and supplier terms may require different policies.
- The index skips numbering in its visible sections; inventory and reconcile the underlying linked files before calling it a complete model.
- Need verify tax/currency assumptions against each actual operating jurisdiction and distinguish accounting policy from business preference.

## 6. Initial cross-resource mapping
| Capability | Nivy materials | Musengimana skill | Peter Bamuhigire skill | Status |
|---|---|---|---|---|
| Business-plan section outline | Strong outline material | Template + section map referenced | Pipeline section skills | Available as design content; canonicalized in this wave |
| Intake + assumption register | Some draft context | Explicit intake/assumption rules | Explicit mandatory intake | Reuse/adapt |
| Live research + citations | Research-agent spec exists elsewhere | Explicitly specified | Claim/evidence gate specified | Design present; runtime unverified |
| Strategy/business-model choice | Outlines include SWOT/PESTLE/Five Forces | Some plan map | Dedicated strategy/model gates | Combine carefully |
| Integrated financial statements | Index and guidance only | BDC-based workbook workflow described | Model gate described, exact engine files not yet found | **Unverified gap: executable Nivy model** |
| Scenarios/stress tests | Some risk/forecast content | Base/upside/downside described | Scenario, stress and audience gates described | Specification exists; test required |
| Jurisdictional localization | Some global/India references | Canada default; adapt per client | Regional defaults need localization | Partial |
| Execution plan/roles/KPIs | Company-OS materials elsewhere | Deliverable plan focus | Gate/owner/release focus | Must map to company execution system |
| Legal/license provenance | Not consolidated | MIT + BDC exception documented | MIT LICENSE inspected | Build license register |
| Quality/release gates | Agent provenance principles elsewhere | Validator scripts named | Explicit stage/release gates | Strong patterns; no runtime proof |

## 7. Decisions and next work
1. Preserve both original outline files; use the new canonical blueprint as the primary reference.
2. Continue exact-path inspection of Peter’s referenced subskills using links in the orchestrator and actual repository paths; do not guess paths that return 404.
3. Inspect the remaining Musengimana reference files, templates, and scripts, with special focus on jurisdiction switch behavior, formula-integrity checks, model audit, workbook license, and document validation.
4. Inspect every linked file in Nivy’s financial-model index; create a financial-model inventory with file type, inputs, formulas/calculations, outputs, assumptions, citations, and runtime status.
5. Build a master capability register with one row per required capability and fields: requirement ID, business archetype, audience, existing source, exact path/revision, coverage grade, evidence, gaps, owner, validation method, priority, status.
6. Then define the universal data contract: Business Brief → Evidence/Claim Register → Assumption Register → Business Model → Section Work Products → Financial Model → Risk Register → Implementation Plan → QA/Release Bundle.
7. Only after the static review, run controlled tests on copies/sandboxed fixtures; never overwrite original workbooks or delete source resources.

## Review limitations
This is a static file-content review of the exact files listed above, not an exhaustive review of every resource in `external-solutions`, and not a runtime, security, legal or financial audit.

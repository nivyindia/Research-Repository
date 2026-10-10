# Master Capability Coverage Register — Wave 5 Update
**Updated:** 2026-10-11  
**Supersedes:** No previous file; this is a dated delta. Use it together with [Initial Master Capability Coverage Register](09-master-capability-coverage-register-initial-2026-10-11.md), [Wave 4 audit](11-financial-model-static-audit-wave-4-2026-10-11.md), and [Wave 5 inventory](13-nivy-financial-artifact-inventory-wave-5-2026-10-11.md).

## Status rules
- **Specified:** a document describes the requirement.
- **Artifact present:** file exists; no correctness claim.
- **Static inspected:** content/code has been read.
- **Runtime tested:** exact test and environment produced logs.
- **Independently reconciled:** key outputs match separate calculations within tolerance.
- **Blocked:** mandatory evidence or prerequisite is missing.
- **Released:** required gates passed and named authority approved.

## Updated financial and release coverage

| ID | Capability | Current evidence | Coverage | Main gap | Exit criteria | Priority |
|---|---|---|---|---|---|---|
| FIN-01 | Integrated P&L, balance sheet and cash flow | Nivy financial plans are Markdown; repository tree has 14 XLSX files but filename scan did not identify a dedicated integrated financial workbook | **Blocked / unresolved artifact search** | All XLSX candidates need read-only classification; no validated model yet | Exact workbook identified or explicit decision recorded to build; formula/input map and linked statements reconciled | P0 |
| FIN-02 | Revenue and cost drivers | Monthly CSV has planned revenue, outsourcing, commissions and profit; financial plan describes pricing and delivery assumptions | **Partial; planned values only** | Sources and formula derivation not standardized; actuals blank | Each driver has assumption/source ID, unit, currency, period, formula and independent check | P0 |
| FIN-03 | Unit economics | Narrative sections specify CAC, LTV, margins and cost-to-serve topics | **Specified, not tested** | Model-specific definitions and linked calculation evidence missing | Definitions locked per archetype and example cases independently reconciled | P1 |
| FIN-04 | Base/upside/downside and break-even | External engines specify scenarios; Nivy documents include planned targets | **Specified externally; Nivy unverified** | No Nivy scenario execution evidence | Scenario copies produce expected direction and independently checked outputs | P0 |
| FIN-05 | Formula integrity and calculation correctness | Musengimana exact audit and formula-integrity code inspected | **Control design inspected; runtime not tested** | No run logs or independent model result in Nivy workspace | Safe-copy test, zero formula regressions/errors, independent numeric checks and reconciliation | P0 |
| FIN-06 | Forecast-to-actual and variance workflow | Monthly planned/actual CSV present; actual fields blank in inspected rows | **Template present; workflow unverified** | Duplicate period rows; no verified close process or thresholds | One canonical month key, source-backed actuals, variance formula, owner, threshold and corrective action | P0 |
| FIN-07 | Finance data source of truth | Finance database CSV is header plus `Sample,0,` | **Gap / placeholder** | No meaningful ledger or populated finance dataset established | Defined schema, ownership, import validation and reconciled source records | P1 |
| FIN-08 | Currency, jurisdiction and tax | Narrative uses USD income/INR cost and `1 USD = 83 INR`; broad compliance topics listed | **Partial; key inputs stale/unverified** | FX timestamp, current rate, tax/legal source and jurisdiction-specific reviewer missing | Dated FX source and sensitivities; qualified India/UAE review as applicable | P0 |
| LIC-01 | Third-party asset and dependency license | Musengimana workbook is separately governed per existing review; external code not run | **Blocked before reuse** | Asset-level terms and dependencies need a recorded decision | License/NOTICE/dependency manifest and approved-use record | P0 |
| REL-01 | Release gate | Peter's release-gate contract inspected | **Specified; Nivy release not assessed** | No complete Nivy evidence bundle/authority record | All required handoffs and evidence pass; explicit release authority recorded | P0 |

## New data-quality controls required
1. **Unique period key:** each month has exactly one canonical forecast row per forecast version.
2. **Actuals provenance:** actual revenue/cost/profit values must point to source records; blank is not zero.
3. **Forecast versioning:** distinguish approved forecast, revised forecast and actuals; never overwrite historical forecast.
4. **Formula traceability:** each key output maps to inputs, formula, source/assumption IDs and independent expected result.
5. **Scenario isolation:** scenarios run on disposable copies and cannot mutate the approved baseline.
6. **FX discipline:** every foreign-currency amount has source currency, reporting currency, rate, date and treatment of fees/gains/losses.
7. **No silent policy assumptions:** tax, bad-debt, emergency reserve, commission and payout rules need owner approval and dated evidence.
8. **Release state integrity:** structural pass, calculation pass, professional review and authorized release remain distinct.

## Prioritized action queue

| Order | ID | Action | Status | Completion proof |
|---|---|---|---|---|
| 1 | FM-INV-01 | Classify all 14 XLSX files from repository tree | In progress | Path, size, purpose, sheets/formulas, owner, and disposition for every file |
| 2 | FM-INV-02 | Resolve all child links from Nivy Next Financial Model index | Open | Link map with valid/broken status and file classification |
| 3 | FM-INV-03 | Compare mirrored finance documents | Open | Blob-SHA/content comparison and canonical-pointer plan |
| 4 | FM-INV-04 | Extract assumption inventory from finance narrative/tracker | Open | ID, value, unit, date/source, confidence, owner, status |
| 5 | FM-INV-05 | Build revenue-to-cash driver map | Open | Inputs → formulas → outputs → evidence mapping |
| 6 | FM-INV-06 | Decide whether an existing workbook can be safely reused | Blocked by 1 | Read-only artifact inspection and license clearance |
| 7 | FM-TEST-01 | Prepare independent numeric fixture | Blocked by 6 | Expected revenue, costs, margin, ending cash and funding need documented |
| 8 | FM-TEST-02 | Run isolated tests on a disposable copy | Blocked by 1, 6, 7 | Pinned environment, logs, formula checks, scenario and reconciliation evidence |
| 9 | FM-GOV-01 | Complete license/dependency review | Open | Asset-level license and approved-use record |
| 10 | FM-GOV-02 | Create release evidence bundle | Blocked until finance QA | All required evidence and named approval; otherwise remain blocked |

## Current overall status
**Blueprint coverage:** broad and specified.  
**Nivy narrative financial coverage:** broad but unevenly evidenced.  
**Nivy executable financial-model status:** not yet established.  
**Financial calculation validation:** not run.  
**External release readiness:** not assessed / must remain blocked.

The next concrete step is to classify all 14 XLSX files and inspect every linked finance section. Do not build a replacement model until this inventory and the asset-level license review are complete.

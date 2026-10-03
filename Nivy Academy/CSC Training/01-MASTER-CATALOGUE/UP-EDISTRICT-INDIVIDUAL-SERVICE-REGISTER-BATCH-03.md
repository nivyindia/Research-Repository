# UP e-District Individual Service Register — Batch 03

## Purpose
This register starts the individual-service layer for UP CSC/Jan Seva operator training. It deliberately records only services that can be evidenced from current government sources; it does **not** invent a 353-row catalogue.

## Current catalogue context
The UP Department of IT & Electronics 2025 presentation states that **353 government services from 54 departments** were being delivered through e-District/Jan Seva, with expansion underway. The current individual service register is therefore maintained as a dated extraction, not as a permanent count. citeturn0search36

The National Government Services Portal currently exposes **257 Uttar Pradesh services** in its indexed state-service directory, but that directory is broader than the e-District/Jan Seva catalogue and includes department/municipal services. It must not be treated as the 353 e-District count. citeturn1search0

## Individual service records — currently verified

| ID | Exact / indexed service name | Category | Delivery ecosystem | Evidence status | CSC training status |
|---|---|---|---|---|---|
| UP-ED-REV-001 | Caste Certificate | Revenue / certificates | UP e-District / Jan Seva | **Verified** as an UP e-District service family; current government service directory explicitly identifies Caste as part of UP e-District. | Workflow family verified; exact current fee/SLA/docs checklist pending |
| UP-ED-REV-002 | Income Certificate | Revenue / certificates | UP e-District / Jan Seva | **Verified** as an UP e-District service family. | Workflow family verified; exact current fee/SLA/docs checklist pending |
| UP-ED-REV-003 | Residence (Domicile) Certificate | Revenue / certificates | UP e-District / Jan Seva | **Verified** as an UP e-District service family; Government Services Portal describes Residence/Domicile. | Workflow family verified; exact current fee/SLA/docs checklist pending |
| UP-ED-MUN-001 | Birth Certificate / Birth Registration | Birth & death | e-District / local registration ecosystem | **Verified** in the current Government Services Portal; individual UP entries are authority/district specific. | Authority routing and CSC workflow pending |
| UP-ED-MUN-002 | Death Certificate / Death Registration | Birth & death | e-District / local registration ecosystem | **Verified** in the current Government Services Portal; individual UP entries are authority/district specific. | Authority routing and CSC workflow pending |
| UP-ED-REG-001 | Marriage Certificate / Marriage Registration | Registration | Stamp & Registration / local ecosystem | **Verified** in the current Government Services Portal; online marriage registration is documented. | Exact Jan Seva/CSC operator workflow pending |
| UP-ED-CERT-001 | Handicap / Disability Certificate | Certificates / social welfare | UP government service ecosystem | **Verified as a UP certificate type** in the current Government Services Portal's UP certificate guidance; exact current e-District service identity pending. | Do not mark Training Ready until exact service/department is extracted |
| UP-ED-LAND-001 | Khatauni / certified land-record copy | Land / revenue | UP land-record / e-District ecosystem | **Verified service family** in UP e-District project material. | Exact current service variant and portal routing pending |
| UP-ED-REV-004 | Solvency Certificate | Revenue / certificates | UP e-District / Jan Seva | **Verified service family** in UP e-District project material. | Exact current service identity/workflow pending |
| UP-ED-REV-005 | Character Certificate | Certificates / police | UP government service ecosystem | **Candidate service family only**; not promoted to Training Ready because current UP e-District identity was not independently exposed by the indexed official directory in this extraction. | Pending exact verification |
| UP-ED-SOC-001 | Widow Pension | Pension / social welfare | UP social-welfare ecosystem | **Candidate service family only**; separate from the e-District count until current department/service mapping is verified. | Pending exact verification |
| UP-ED-SOC-002 | Old Age Pension | Pension / social welfare | UP social-welfare ecosystem | **Candidate service family only**; separate from the e-District count until current department/service mapping is verified. | Pending exact verification |
| UP-ED-SOC-003 | Disability Pension | Pension / social welfare | UP social-welfare ecosystem | **Candidate service family only**; separate from the e-District count until current department/service mapping is verified. | Pending exact verification |
| UP-ED-SOC-004 | Family/Dependent-related social welfare services | Social welfare | UP social-welfare ecosystem | **Family-level only**; exact current service names required. | Pending |
| UP-ED-FOOD-001 | Ration Card / PDS-related services | Food & Civil Supplies | UP food/PDS ecosystem | **Family-level only** in this batch; exact current service names required. | Pending |
| UP-ED-EDU-001 | Scholarship services | Education / welfare | UP scholarship ecosystem | **Family-level only**; exact current service names required. | Pending |
| UP-ED-EMP-001 | Employment registration / related services | Employment | Rojgaar Sangam / employment ecosystem | Current UP government FAQ confirms candidates can register from home, cyber cafe, Jan Suvidha and Lokvani Kendra and that registration/renewal are free. This is a separate employment ecosystem, not automatically part of the 353 e-District count. citeturn0search12 | Operator workflow can be developed separately |
| UP-ED-TRN-001 | Vehicle registration / RC services | Transport | Vahan | Current Vahan service menu exposes RC-related services; UP service count varies by current portal build. | Separate transport register |
| UP-ED-TRN-002 | Vehicle tax / fitness / permit services | Transport | Vahan | Current Vahan menu exposes tax/fee, fitness and permit-related areas. | Separate transport register |
| UP-ED-TRN-003 | Driving licence services | Transport | Sarathi | UP is exposed through the Sarathi ecosystem via mParivahan. | Separate transport register |
| UP-ED-TRN-004 | e-Challan | Transport | eChallan | UP is exposed through the eChallan ecosystem via mParivahan. | Separate transport register |

## Source notes

### Primary / high-confidence sources
1. **UP Department of IT & Electronics 2025 presentation** — states 353 services / 54 departments through e-District/Jan Seva and that expansion is underway. citeturn0search36
2. **National Government Services Portal — Uttar Pradesh e-District Services** — identifies Caste, Income, Residence/Domicile, Birth and Death certificate services and provides UP e-District guidance. Updated May 6, 2026. citeturn0search0
3. **National Government Services Portal — Uttar Pradesh state directory** — currently indexes 257 UP services and includes UP-specific municipal, welfare, certificate and other services. This is an index, not the e-District master count. citeturn1search0
4. **UP Rojgaar Sangam FAQ** — confirms employment registration/renewal can be done through home, cyber cafe, Jan Suvidha and Lokvani Kendra and are free. citeturn0search12

## Important separation rule
Do not merge these into one flat "CSC 353 services" list without evidence:

- **UP e-District / Jan Seva** — the 353-service / 54-department baseline.
- **Municipal / e-Nagarsewa services** — e.g. city-specific birth, death, property tax and trade services.
- **Transport** — Vahan / Sarathi / eChallan.
- **Employment** — Rojgaar Sangam.
- **Sewa Mitra** — a separate UP home/office local-services platform; it currently reports 3,500+ services and 75 districts and is not an e-District service count. citeturn0search5

## Required fields before a service becomes "Training Ready"

For each individual service, the next extraction pass must capture:

1. Exact official service name and current service ID (where exposed).
2. Department / authority.
3. Whether a CSC/Jan Seva operator is authorized to submit it.
4. Official portal URL.
5. Eligibility.
6. Required documents and file format/size rules.
7. Authentication / Aadhaar / biometric requirements.
8. Official fee and any operator/service charge.
9. Official SLA / expected processing time.
10. Exact operator workflow, including login and submission.
11. Payment, receipt and application-number handling.
12. Status tracking.
13. Correction / objection / rejection / resubmission process.
14. Certificate/document download and verification.
15. Escalation/helpdesk.
16. Current YouTube training reference, if available.
17. Practical test.
18. QC checklist.
19. Last verified date.

## Evidence labels

- **Verified** — exact service or service family is supported by a current official source.
- **Candidate** — plausible service family but current exact UP service identity is not yet independently verified.
- **Pending exact extraction** — must not be used as a final operator SOP.
- **Training Ready** — all required operational fields above are verified.

## Next batch
Batch 04 should focus on extracting the **exact current service names and department mapping** from the UP e-District/e-Sathi operator-facing catalogue, followed by one service card per service. The target is completeness, but no unverified names will be fabricated to make the list reach 353.

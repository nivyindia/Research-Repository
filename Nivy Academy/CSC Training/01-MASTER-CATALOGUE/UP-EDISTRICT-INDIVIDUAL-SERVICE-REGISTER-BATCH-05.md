# UP e-District Individual Service Register — Batch 05

## Scope
This batch adds **individually named UP government services** surfaced by the current National Government Services Portal (NGSP) and related official UP material. These are evidence-backed service records, but an NGSP listing is not automatically proof that the service is one of the 353 Jan Seva/e-District rows or that a CSC operator is authorized to submit it. That distinction is retained.

## Current evidence
The UP Department of IT & Electronics 2025 presentation states 353 government services from 54 departments are delivered through Jan Seva/e-District. citeturn0search24

The current NGSP UP directory shows 257 indexed UP services, which is a broader service index and must not be equated with the 353 e-District count. citeturn0search6

## Exact service records surfaced in this batch

| ID | Exact indexed service name | Department / ecosystem | Evidence | CSC / e-District status |
|---|---|---|---|---|
| UP-NGSP-CERT-001 | Apply for Caste Certificate, Uttar Pradesh | Revenue / e-District | Current NGSP lists the service as fully online and registration-required. citeturn0search7 | e-District family verified; exact operator authorization/fee/SLA pending |
| UP-NGSP-CERT-002 | Apply for Domicile Certificate, Uttar Pradesh | Revenue / e-District | Current NGSP UP directory lists this service as fully online and registration-required. citeturn0search6 | e-District family verified; exact operator authorization/fee/SLA pending |
| UP-NGSP-CERT-003 | Apply for Income Certificate, Uttar Pradesh | Revenue / e-District | Current NGSP UP directory lists this service as fully online and registration-required. citeturn0search6 | e-District family verified; exact operator authorization/fee/SLA pending |
| UP-NGSP-FCS-001 | Food and Civil Supplies Department, Uttar Pradesh | Food & Civil Supplies | Current NGSP describes NFSA, Ration Card Management System, Farmer registration and Supply Chain Management System links. citeturn1search0 | Department ecosystem verified; individual CSC service rows pending |
| UP-NGSP-LAND-001 | Uttar Pradesh Land Records information | Revenue / land records | Current NGSP UP directory lists online land-record information and states users can search by district and village. citeturn0search3 | Land-record ecosystem verified; exact CSC service/Khatauni row pending |
| UP-NGSP-MUN-001 | Property Tax Related Services for Prayagraj Municipal Corporation, Uttar Pradesh | Municipal / e-Nagarsewa | Current NGSP lists online property-tax information and payment for Prayagraj. citeturn1search2 | Municipal ecosystem; keep outside e-District 353 until mapping verified |
| UP-NGSP-MUN-002 | Online House Tax Payment by Lucknow Nagar Nigam, Uttar Pradesh | Municipal / e-Nagarsewa | Current NGSP lists online house-tax payment. citeturn1search2 | Municipal ecosystem; separate register |
| UP-NGSP-MUN-003 | Birth Registration for Agra Municipal Corporation, Uttar Pradesh | Municipal / birth-death | Current NGSP lists this fully online service. citeturn1search2 | Municipal service; authority-specific |
| UP-NGSP-MUN-004 | Registration of Marriage in Noida, Uttar Pradesh | Registration / municipal-local | Current NGSP lists online marriage registration for Noida. citeturn1search2 | Local service; authority-specific |
| UP-NGSP-DIV-001 | Online Application form for Marriage Incentive Award to Disabled Persons, Uttar Pradesh | Divyangjan welfare | Current NGSP lists this UP service as fully online. citeturn1search10 | Welfare ecosystem; exact CSC authorization pending |
| UP-NGSP-DIV-002 | Apply for Construction of Shops Rehabilitation Handicapped Persons, Uttar Pradesh | Divyangjan welfare | Current NGSP lists this UP service as fully online. citeturn1search10 | Welfare ecosystem; exact CSC authorization pending |
| UP-NGSP-DIV-003 | Subsidy for Prosthetic Limbs to Persons with Disabilities, Uttar Pradesh | Divyangjan welfare | Current NGSP lists this UP service as fully online and registration-required. citeturn1search10 | Welfare ecosystem; exact CSC authorization pending |
| UP-NGSP-DIV-004 | Application for Loan/Grant for Rehabilitation by Persons with Disabilities, Uttar Pradesh | Divyangjan welfare | Current NGSP lists this UP service as fully online and registration-required. citeturn1search11 | Welfare ecosystem; exact CSC authorization pending |
| UP-NGSP-WID-001 | Apply for Couple Award Scheme to Promote Widow Marriage, Uttar Pradesh | Social welfare | Current NGSP lists this UP service as fully online and registration-required. citeturn1search9 | Welfare ecosystem; not counted as e-District without mapping |
| UP-NGSP-MUN-005 | Obtain Birth Certificate at Uttar Pradesh, Ghaziabad | Birth & death / municipal | Current NGSP UP directory lists this online service. citeturn1search2 | Authority-specific; separate from generic e-District family until mapping verified |

## Important distinction
The exact names above are **real indexed government-service names**, but they are not automatically individual rows of the 353-service Jan Seva/e-District catalogue. The permanent master register must have an additional field:

**Catalogue Mapping = Confirmed e-District / Confirmed other UP department / Municipal / Partner / Unmapped**

No service should be marked "CSC Training Ready" until CSC/Jan Seva authorization and the operator workflow are independently verified.

## Data quality rules
1. Preserve the exact indexed title.
2. Keep the official URL/source attached to the record.
3. Do not merge municipal birth/death/property-tax services into generic e-District certificates without authority mapping.
4. Do not treat NGSP's 257 UP-service index as the e-District 353 count.
5. Do not freeze fees, SLAs or document checklists from third-party tutorials.
6. Use synthetic applicant data for training.

## Next extraction
Batch 06 should target the **remaining exact UP service titles** in the NGSP directory and cross-map them to the 353-service e-District/Jan Seva baseline, with department, authority and CSC authorization fields.

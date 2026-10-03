# CSC Individual Service Extraction Queue

Last updated: 2026-10-03

## Objective

Convert family-level CSC research into a maintainable individual-service register. The target is not an invented fixed number. Current Government of India material says 800+ services are delivered through CSCs, while Uttar Pradesh government material identifies 336 G2C services across 52 departments through its e-District layer.

## Master record fields

Every individual service should eventually have:

| Field | Required |
|---|---|
| Service ID | Yes |
| Exact official service name | Yes |
| Category | Yes |
| Central / State / Partner | Yes |
| Department / provider | Yes |
| State / district availability | Yes |
| CSC/VLE authorization required | Yes |
| Official portal | Yes |
| Citizen eligibility | Yes |
| Required documents | Yes |
| Authentication method | Yes |
| Fee / prescribed rate | Yes |
| Step-by-step workflow | Yes |
| Payment/receipt/refund process | Yes |
| Status/correction/escalation | Yes |
| Official documentation | Yes |
| YouTube training | Recommended |
| Practical exercise | Yes |
| QC checklist | Yes |
| Assessment | Yes |
| Last verified | Yes |

## Extraction batches

### Batch A — National core
Status: In progress

- Identity/document services
- Financial inclusion
- Insurance/pension
- Welfare
- Agriculture
- Health
- Education
- Legal
- Travel
- Utility/BBPS
- B2C/e-commerce
- Digital/computer services
- Transport
- Other authorized partner services

### Batch B — Uttar Pradesh e-District
Status: Queued

Source evidence: UP government presentation reports 336 G2C services across 52 departments through e-District.

First individual-service families:
- certificates
- revenue/land
- welfare
- scholarship
- labour
- agriculture
- local government
- social security
- licenses/permissions
- other department services

### Batch C — Uttar Pradesh Transport
Status: Queued

Current official Vahan portal reports 30 citizen services for Uttar Pradesh.

Extract separately:
- vehicle/RC services
- ownership/transfer services
- tax/fee services
- permit-related services
- fitness/other vehicle services

Then map Sarathi and eChallan separately.

### Batch D — State-specific service ecosystems
Status: Pending

After UP, repeat the same method for other states/UTs. Do not copy UP assumptions into other states.

### Batch E — Partner/authorization services
Status: Pending

Track separately:
- banking/BC
- AEPS/DigiPay
- insurance
- IRCTC/authorized travel
- DSC providers
- GeM-related facilitation
- other services where separate credentials/authorization are required

## Verification rule

A service cannot be marked Training Ready solely because it appears in a search result, YouTube video or generic CSC list.

Training Ready requires:
1. current official service identity
2. current availability/authorization
3. official workflow/documentation
4. current fee/rate information where applicable
5. practical workflow
6. QC and escalation
7. current training reference
8. last verification date

## Data protection rule

Never store real Aadhaar numbers, PAN numbers, bank credentials, OTPs, passwords, biometric information, private keys or other customer secrets in this repository. Use synthetic training data for exercises.

## Sources

Government of India, PIB: CSCs deliver 800+ citizen-centric services and district-wise service lists are available through csc.gov.in.

Government of India, PIB: CSCs cover G2C, B2C, financial, educational, healthcare, utility, agriculture and other services.

Government of Uttar Pradesh / UPLC: CSC 3.0 and e-District presentation reporting 336 G2C services from 52 departments.

Ministry of Road Transport & Highways: Vahan citizen portal showing 30 services for Uttar Pradesh and separate Sarathi/eChallan systems.

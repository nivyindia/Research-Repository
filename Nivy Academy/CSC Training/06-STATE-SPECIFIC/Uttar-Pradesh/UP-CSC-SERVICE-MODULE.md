# Uttar Pradesh CSC / Jan Seva Kendra Service Expansion

Last verified: 2026-10-03

## Why UP gets a dedicated module

A 2025 UP Government/UPLC presentation states that CSCs provide 336 G2C services from 52 departments through the e-District portal, with high-volume services including caste, income, domicile, Khatauni and solvency. Source: https://uplc.up.gov.in/policy/Department-of-IT-and-Electronics-2025.pdf

The national CSC programme currently reports 800+ services across India, so the UP layer should be maintained separately from the national catalogue and mapped to the exact state portal/service names.

## UP priority service families

| ID | UP service family | Training priority | What the operator must learn |
|---|---|---|---|
| CSC-UP-001 | Caste Certificate | Critical | Eligibility, documents, application, acknowledgement, status, correction/escalation |
| CSC-UP-002 | Income Certificate | Critical | Eligibility, documents, application, verification/status |
| CSC-UP-003 | Domicile Certificate | Critical | Eligibility, documents, application, verification/status |
| CSC-UP-004 | Khatauni / Land Record Services | Critical | Search, record extraction, applicant details, document/receipt workflow |
| CSC-UP-005 | Solvency Certificate | High | Eligibility, documents, application/status |
| CSC-UP-006 | Birth Certificate | High | Local-body/registrar workflow, documents, correction/status |
| CSC-UP-007 | Death Certificate | High | Local-body/registrar workflow, documents, correction/status |
| CSC-UP-008 | Marriage-related Certificate/Registration | High | Eligibility, documents, appointment/application/status |
| CSC-UP-009 | Ration/PDS Services | Critical | New/update/beneficiary/status workflows where enabled |
| CSC-UP-010 | Pension Services | High | Eligibility, application/status and scheme-specific workflow |
| CSC-UP-011 | Scholarship Services | High | Student eligibility, documents, application, correction/status |
| CSC-UP-012 | Labour/Worker Services | High | Worker registration/update and scheme application |
| CSC-UP-013 | Revenue / Tehsil Services | High | Service selection, application, document and status workflow |
| CSC-UP-014 | Municipal / Nagar Nikay Services | High | Property/utility/certificate workflows by local body |
| CSC-UP-015 | Transport / Driving Licence | High | Sarathi workflows, fees, appointments and status |
| CSC-UP-016 | Vehicle / RC Services | High | Vahan citizen services, fees, status and authentication |
| CSC-UP-017 | e-Challan Assistance | Medium | Challan lookup, payment/status and receipt |
| CSC-UP-018 | Digital Signature Certificate (DSC) | High | Provider-specific KYC/authorization, signer software and certificate workflow |
| CSC-UP-019 | e-Stamp / Registration | High | State availability, application/payment/registration workflow |
| CSC-UP-020 | Legal / Tele-Law | High | Citizen registration, consultation facilitation, privacy and escalation |
| CSC-UP-021 | Agriculture / Farmer Services | High | Farmer records, scheme applications and status |
| CSC-UP-022 | Welfare Scheme Applications | High | Scheme eligibility, document upload and tracking |
| CSC-UP-023 | Employment / Skill Services | Medium | Registration, profile/application and status |
| CSC-UP-024 | Local Utility Payments | Critical | Consumer lookup, bill validation, payment, receipt/refund |

## Transport module — current official evidence

The Ministry of Road Transport & Highways current Vahan citizen portal lists 30 services for Uttar Pradesh. The current mParivahan system exposes Vahan, Sarathi and eChallan service families and includes Uttar Pradesh in its state list. Source: https://staging.parivahan.gov.in/vahanservice and https://mparivahan.parivahan.gov.in/

The Vahan portal also states that where Aadhaar biometric authentication is the required mode for a service, the applicant may visit the nearest CSC or use an authorized biometric device.

Training action: extract the individual 30 UP Vahan services and map them to separate Service IDs rather than keeping Vahan Services as one generic row.

## DSC module — current UP evidence

UP Electronics Corporation currently publishes provider-specific DSC application processes for IDSign, PantaSign, nCode and Care4Sign, plus current digital-signer software documentation.

Training action: DSC must be treated as a provider/authorization-sensitive module. Do not train candidates to bypass authorization or handle private keys/passwords.

## UP service extraction rule

For every individual UP service:

1. Capture exact official service name.
2. Capture department.
3. Capture portal URL.
4. Capture whether CSC/VLE access is authorized.
5. Capture citizen eligibility.
6. Capture required documents.
7. Capture application/fee/payment workflow.
8. Capture acknowledgement/reference number.
9. Capture status/correction/refund process.
10. Add one current practical training video or official tutorial.
11. Create dummy practical case.
12. Create QC checklist.
13. Record last_verified.
14. Assign permanent CSC-UP-### Service ID.

## Important distinction

Do not assume that every service visible on a government website is automatically available to every CSC/VLE. Availability can depend on state integration, district configuration, service authorization, provider/agent status, equipment and authentication method.

The national government specifically notes that state/UT e-District services are being integrated with the CSC portal, so the repository must track availability/authorization as fields rather than hard-coding a universal availability claim.

## Next batch

UP-001 through UP-024 is the family-level queue.

Next extraction should create the individual service register for:
- 336 UP e-District G2C services
- 30 UP Vahan services
- UP Sarathi services
- UP e-Challan workflows
- UP PDS
- UP scholarship
- UP welfare
- UP labour
- UP municipal/local-body
- UP revenue/land
- UP DSC/e-procurement related services

The exact count of individually trainable CSC services will be finalized only after deduplication and authorization verification.

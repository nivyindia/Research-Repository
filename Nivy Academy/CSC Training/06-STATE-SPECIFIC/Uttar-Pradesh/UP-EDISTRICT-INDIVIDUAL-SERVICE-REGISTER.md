# UP e-District — Initial Individual Service Register

Last verified: 2026-10-03

Government of Uttar Pradesh/UPLC material states that 336 G2C services from 52 departments are available online through the e-District portal. High-volume services explicitly identified include Caste, Income, Domicile, Khatauni and Solvency. citeturn1search31

This file is the first individually named extraction batch. It is **not yet the complete 336-service register**.

| Service ID | Exact / working service name | Department/family | Priority | Training status | Official verification |
|---|---|---|---|---|---|
| CSC-UP-ED-001 | Caste Certificate | Revenue / e-District | Critical | Queue | UP e-District |
| CSC-UP-ED-002 | Income Certificate | Revenue / e-District | Critical | Queue | UP e-District |
| CSC-UP-ED-003 | Domicile / Residence Certificate | Revenue / e-District | Critical | Queue | UP e-District |
| CSC-UP-ED-004 | Khatauni / Land Record | Revenue / e-District | Critical | Queue | UP revenue/e-District |
| CSC-UP-ED-005 | Solvency Certificate | Revenue / e-District | High | Queue | UP e-District |
| CSC-UP-ED-006 | Birth Certificate | Local Government / e-District | High | Queue | UP e-District |
| CSC-UP-ED-007 | Death Certificate | Local Government / e-District | High | Queue | UP e-District |
| CSC-UP-ED-008 | Marriage-related Services | Registration / e-District | High | Queue | UP service menu |
| CSC-UP-ED-009 | Scholarship Services | Education/Welfare | High | Queue | UP service ecosystem |
| CSC-UP-ED-010 | Pension Services | Social Welfare | High | Queue | UP service ecosystem |
| CSC-UP-ED-011 | Ration/PDS Services | Food & Civil Supplies | Critical | Queue | UP service ecosystem |
| CSC-UP-ED-012 | Labour/Worker Services | Labour | High | Queue | UP service ecosystem |
| CSC-UP-ED-013 | Agriculture/Farmer Services | Agriculture | High | Queue | UP service ecosystem |
| CSC-UP-ED-014 | Welfare Scheme Services | Welfare | High | Queue | UP service ecosystem |
| CSC-UP-ED-015 | Municipal/Local Body Services | Urban/Local Government | High | Queue | UP service ecosystem |
| CSC-UP-ED-016 | Revenue/Tehsil Services | Revenue | High | Queue | UP e-District |
| CSC-UP-ED-017 | Legal/Tele-Law | Legal | High | Queue | CSC/Tele-Law |
| CSC-UP-ED-018 | Transport/Sarathi | Transport | High | Queue | MoRTH |
| CSC-UP-ED-019 | Vahan/Vehicle Services | Transport | High | Queue | MoRTH |
| CSC-UP-ED-020 | e-Challan | Transport | Medium | Queue | MoRTH |

## Immediate next extraction

The next research pass must replace family-level rows with exact portal menu names and department mappings. Priority order:

1. Revenue/e-District certificates
2. Land/Khatauni
3. Welfare/pension
4. PDS/ration
5. Scholarship
6. Labour
7. Agriculture
8. Local-body/municipal
9. Transport
10. Other department services

## Verification status

The 336 figure is verified from UP government material, but the individual 336 names were not exposed in the government source used for this batch. Therefore this register deliberately does not claim that the 20 rows above are the complete list.

No training SOP should be marked final until the exact current portal service name and authorization are verified.

## Sources

- UP Electronics Corporation / Government of Uttar Pradesh presentation: 336 G2C services from 52 departments through e-District. citeturn1search31
- Ministry of Road Transport & Highways Vahan portal: current state-specific service count and authentication notes. citeturn0search0turn0search2
- mParivahan: current Sarathi, Vahan and eChallan service families. citeturn0search1


## Batch 2 — verified transport/vehicle extraction

The current MoRTH Vahan Citizen Services portal currently shows **33 services for Uttar Pradesh** on the live/staging service selector, so the older 30-service figure should no longer be treated as current. citeturn0search1

Current Vahan service families exposed by the portal include:
- Tax/Fee Services
- RC Related Services
- Vehicle Related Services
- Apply for Certificates
- Additional Services
- Appointment
- Online Services
- Documents
- Status
- Know Your Vehicle Details
- Nominee/dealer-related services

The portal specifically exposes workflows for transfer of ownership, change of address, duplicate RC, hypothecation addition/termination, fitness certificate, NOC, duplicate fitness certificate, renewal of private registration, private/commercial conversion, home-state assignment, vehicle-parameter changes, appointment/reprint/reschedule, document upload/modification, application status, transaction history, payment re-verification and receipt reprint. citeturn0search4

### CSC training implications

| Service family | Operator must learn | Verification |
|---|---|---|
| Transfer of Ownership | seller initiation → buyer continuation → documents → fee → status | Official Vahan |
| Change of Address | application → documents → fee → status | Official Vahan |
| Duplicate RC | application → supporting documents → payment → status | Official Vahan |
| Hypothecation Addition/Termination | correct transaction type → documents → payment → status | Official Vahan |
| Fitness Certificate | application → fee → slot → vehicle/document verification | Official Vahan |
| NOC | application → fee → documents → status | Official Vahan |
| Registration Renewal | eligibility → application → fee → documents → status | Official Vahan |
| Private ↔ Commercial Conversion | correct conversion workflow → fee → documents | Official Vahan |
| Vehicle Parameter Change | parameter selection → supporting proof → fee → status | Official Vahan |
| Appointment | book/reprint/reschedule → slot handling | Official Vahan |
| Document Upload/Modification | upload rules → pending-doc workflow → status | Official Vahan |
| Payment Re-verification | identify pending bank transaction → re-verify safely | Official Vahan |
| Receipt/Forms | reprint receipt and pre-filled service forms | Official Vahan |

**Important authentication rule:** where a Vahan service requires Aadhaar biometric authentication, the applicant may use a nearest CSC or an attached biometric device. If Aadhaar authentication is used with an Aadhaar number belonging to someone other than the registered owner, the application can be rejected and fees may not be refundable. Contactless eKYC services can avoid an RTO visit for document verification when Aadhaar authentication is used; non-contactless services may require RTO/vehicle verification after application, fee payment, document upload and slot booking. citeturn0search0

### Current portal-count correction

- Previous research note: 30 UP Vahan services.
- Current portal observation: **33 UP Vahan services**.
- Therefore the training repository should use **33 as the current observed count**, with the date of verification recorded, rather than preserving 30 as a current figure. citeturn0search1

### Next extraction target

Continue with exact individual names from the live UP e-District menu rather than inferring service names from broad categories. The official UP Electronics Corporation presentation confirms 336 G2C services across 52 departments, with Caste, Income, Domicile, Khatauni and Solvency among high-volume services. citeturn0search12

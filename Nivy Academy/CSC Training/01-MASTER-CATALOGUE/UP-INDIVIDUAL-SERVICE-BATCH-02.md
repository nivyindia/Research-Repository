# UP CSC Individual Service Extraction — Batch 02

## Scope
Verified/priority service families for the UP CSC operator-training extraction cycle.

## Current evidence
The UP Department of IT & Electronics 2025 presentation describes e-District as providing **353 government services from 54 departments**. Earlier project material cited 336/52; therefore the repository now treats the catalogue size as **time-sensitive** and requires the current portal/service register to be the authority for the individual list. citeturn0search25

The National Government Services Portal currently lists UP e-District services including Caste, Income, Residence/Domicile, Birth/Death and Marriage services. citeturn1search0turn1search3turn1search13

## Verified service records

| Service ID | Service | Department / ecosystem | Current evidence | Training status |
|---|---|---|---|---|
| UP-ED-REV-001 | Caste Certificate | Revenue / e-District | UP district government pages identify CSC/e-District delivery; Kanpur district lists self-declaration, ward/Gram Panchayat letter and ration-card copy. citeturn1search16 | Workflow verified; current fee/SLA must be rechecked before final SOP |
| UP-ED-REV-002 | Income Certificate | Revenue / e-District | Etah district government page states citizens can apply through CSC/Lokvani/Jan Seva Kendra; requirements include self-certified declaration, ration-card copy and updated payslip where relevant. citeturn1search1 | Workflow verified; current fee/SLA must be rechecked |
| UP-ED-REV-003 | Domicile / Residence Certificate | Revenue / e-District | National Government Services Portal marks the UP service fully online; UP district pages identify CSC delivery. citeturn1search3turn1search14 | Workflow verified; current fee/SLA must be rechecked |
| UP-ED-REV-004 | Khatauni / certified land-record copy | Revenue / e-District / land records | UP e-District material explicitly lists Copy of Khatauni among major services. citeturn1search43 | Family verified; exact current variants pending |
| UP-ED-REV-005 | Solvency Certificate | Revenue / e-District | UP e-District material explicitly lists Solvency Certificate among major services. citeturn1search43 | Family verified; exact current workflow pending |
| UP-ED-MUN-001 | Birth / Death services | Local bodies / e-District | National Government Services Portal lists UP Birth and Death services; examples are district/municipality-specific. citeturn1search0 | Service family verified; district/authority routing pending |
| UP-ED-MUN-002 | Marriage Registration | Stamp & Registration / local service ecosystem | National Government Services Portal lists Marriage Certificate service for UP, with online registration. citeturn1search0 | Family verified; exact CSC workflow pending |
| UP-ED-TRN-001 | Vehicle registration / RC services | Transport / Vahan | UP Transport Department lists transfer, address change, hypothecation, duplicate RC, NOC and RC particulars; Vahan currently shows UP as 33-service state on its citizen portal. citeturn1search10turn0search0 | Workflow family verified |
| UP-ED-TRN-002 | Vehicle tax / fitness / permit services | Transport / Vahan | UP Transport Department lists tax, fitness-slot booking and permit services. citeturn1search10 | Workflow family verified |
| UP-ED-TRN-003 | e-Challan | Transport / eChallan | mParivahan exposes Uttar Pradesh through Vahan, Sarathi and eChallan ecosystems. citeturn0search1 | Service family verified |

## Practical workflow rules

1. **Use the current official portal as the source of truth.** Do not freeze a 336/353 count into the training system.
2. For every certificate service: identify citizen/operator login, exact service, applicant profile, document checklist, form fields, upload rules, payment, submission, application number, status, correction/objection, approval authority and certificate download/verification.
3. For transport services: identify whether the service is contactless/eKYC or requires RTO/vehicle verification. Vahan states that some services require Aadhaar authentication and that non-contactless services may require an RTO visit/vehicle verification. citeturn0search0
4. Never store real Aadhaar/PAN/bank credentials, OTPs, passwords, biometrics or private keys. Use synthetic training data.
5. YouTube is a **training aid, not the authority**. Re-check the current portal before using any video in operator training.

## YouTube training references

| Service | Training video | Use |
|---|---|---|
| Caste Certificate | [YouTube — E-District Portal se caste certificate kaise Online Karen](https://www.youtube.com/watch?v=ZD-DRURhWVY) | Form filling, documents, status and download walkthrough; published Apr 7, 2025. citeturn1youtube41 |
| Central Caste Certificate | [YouTube — Online Application for Central Caste Certificate 2025](https://www.youtube.com/watch?v=cEKjhaOWpIU) | e-Sathi/e-District workflow example; published Aug 25, 2025. citeturn1youtube42 |

## Pending exact extraction

- Current official e-District individual service list, with service IDs/names and department mapping.
- Current fee/SLA for each service.
- Exact document checklist from the current official service form/checklist.
- Current correction/objection/rejection workflow.
- Current YouTube reference for each service.
- Operator practical test and QC checklist.

## Source hierarchy
1. Current UP e-District / department portal.
2. UP Government / district government pages.
3. National Government Services Portal.
4. Current official manuals/checklists.
5. Current practical YouTube demonstrations, clearly marked as secondary.

## Data protection
Training repositories must contain synthetic examples only. Never upload real Aadhaar, PAN, bank account, OTP, password, biometric or private-key data.

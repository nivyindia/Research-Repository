# CSC High-Volume Service Reuse Audit — 2026-10-03

## Objective
Before building service-specific Nivy training, verify whether CSC Academy already provides reusable official training, manuals, FAQs or operator material.

Rule: **REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING**

## Verified findings

| Service / family | Existing reusable official material found | Decision | Missing Nivy layer |
|---|---|---|---|
| CSC/VLE fundamentals | TEC modules covering G2C/B2C, CSC scheme and Digital Seva | REUSE | practical QC |
| Banking / BC / AEPS | CSC Academy/IIBF training + BC capacity-building material includes AEPS workflow/payout examples | REUSE + VERIFY | current provider-specific workflow, QC |
| Basic computer | CSC Academy BCC with simulated hands-on training and e-governance applications | REUSE | CSC-specific practice |
| Education/skill enrolment | CSC Academy service catalogue + course workflows | REUSE | current service-specific checklist |
| Aadhaar | No service-specific current official CSC Academy training verified in this pass | VERIFY FIRST | do not build yet |
| PAN | No service-specific current official CSC Academy training verified in this pass | VERIFY FIRST | do not build yet |
| Ayushman | No service-specific current official CSC Academy training verified in this pass | VERIFY FIRST | do not build yet |
| PM-KISAN | No service-specific current official CSC Academy training verified in this pass | VERIFY FIRST | do not build yet |
| e-Shram | No service-specific current official CSC Academy training verified in this pass | VERIFY FIRST | do not build yet |
| Tele-Law | Service exists in CSC Academy catalogue, but a current operator-training package was not verified in this pass | REUSE SERVICE / VERIFY TRAINING | workflow + QC only after official verification |
| IRCTC/travel | No current service-specific training package verified in this pass | VERIFY FIRST | do not build yet |

## Important evidence

CSC Academy's current service list confirms existing academy/education offerings, while its VLE training page describes specialised VLE training and entrepreneurship support. citeturn0search0turn0search14

The TEC assignment guidelines explicitly cover G2C/B2C services and the Digital Seva Portal, so a duplicate general CSC-service theory module should not be created. citeturn0search61

CSC Academy's current BCC course includes simulated hands-on training and e-governance applications, so equivalent generic computer training should be reused rather than rebuilt. citeturn0search3

CSC Academy/IIBF currently provides BC/BF training, and an existing CSC Academy banking capacity-building document contains AEPS transaction material. Current limits/payouts must be rechecked before operational use because the document itself says they may change. citeturn0search7turn0search56

## Verification rule for the remaining services

A service is not marked **Training Ready** until all of these are verified:
- current official service identity
- current portal
- CSC/VLE authorization
- eligibility
- documents
- authentication
- fee/commission if applicable
- operator workflow
- payment/receipt
- status/correction
- escalation
- current practical training reference
- verification date

## Next priority

Search the official CSC Academy/Digipaathshala ecosystem and official department portals service-by-service for Aadhaar, PAN, Ayushman, PM-KISAN, e-Shram, Tele-Law and IRCTC before creating any new Nivy SOP.


## Deep-audit update — 2026-10-03

### Official resources verified in this pass

| Area | Verified official resource | Reuse status |
|---|---|---|
| TEC / CSC foundation | TEC portal + official 10-module assignment guidance | **REUSE** |
| Basic Computer / e-governance literacy | CSC Academy BCC, 36-hour course with simulated hands-on training and e-governance applications | **REUSE** |
| Skill-course operations | CSC Academy Skill pages document Digital Seva enrolment workflow for skill courses | **REUSE** |
| BC training | CSC Academy/IIBF BC portal; current rules include changed exam-centre process for candidates trained after 26-Aug-2026 | **REUSE + CURRENT-RULE CHECK** |
| DRA | CSC Academy/IIBF portal currently shows live DRA batches | **REUSE + CURRENT-BATCH CHECK** |
| NCS / general career services | CSC Academy service catalogue lists NCS | **REUSE SERVICE / TRAINING VERIFY** |
| Tele-Law | CSC Academy service catalogue lists Tele-Law | **REUSE SERVICE / TRAINING VERIFY** |
| Aadhaar | No current service-specific CSC Academy training source verified in this pass | **DO NOT BUILD YET** |
| PAN | No current service-specific CSC Academy training source verified in this pass | **DO NOT BUILD YET** |
| Ayushman | No current service-specific CSC Academy training source verified in this pass | **DO NOT BUILD YET** |
| PM-KISAN | No current service-specific CSC Academy training source verified in this pass | **DO NOT BUILD YET** |
| e-Shram | No current service-specific CSC Academy training source verified in this pass | **DO NOT BUILD YET** |
| IRCTC | No current service-specific CSC Academy training source verified in this pass | **DO NOT BUILD YET** |

### Important operational rule

The absence of a CSC Academy training page is **not proof that the service is unavailable through CSC**. It only means that a reusable official training resource was not verified in this audit. Service authorization and current Digital Seva availability must be checked separately before deployment.

### Newly captured current-change example

BC training rules are actively changing: the current CSC Academy/IIBF page states that candidates trained after 26-Aug-2026 receive credentials automatically upon batch enrollment and must follow the current IIBF e-KYC/exam process; candidates trained before that date have a different registration path. This demonstrates why Nivy SOPs must link to the authoritative source and store a verification date instead of freezing old screenshots/instructions.

### Build decision

Do not create a duplicate generic training curriculum for areas already covered by official CSC Academy material.

Nivy-owned content should focus on:
- state-specific service execution
- service-by-service operator checklist
- synthetic practice cases
- QC/error handling
- receipt/status/correction handling
- escalation
- practical assessment
- current-source verification record

### Sources
- CSC Academy Service List: https://www.cscacademy.org/service-list
- CSC Academy VLE Training: https://www.cscacademy.org/services/vle-training
- CSC Academy BCC: https://www.cscacademy.org/digital-education
- CSC Academy Skill Courses: https://www.cscacademy.org/skill-course
- CSC Academy/IIBF BC training: https://onboarding-bcbf.cscacademy.org/onboard-user-self
- CSC Academy/IIBF DRA training: https://onboarding-dra.cscacademy.org/onboard-user-self
- TEC portal: https://newcsctally.cscacademy.org/


## Deep-audit result — official CSC Academy search, 2026-10-03

Search scope: CSC Academy and Digipaathshala official domains for Aadhaar, PAN, Ayushman, PM-KISAN, e-Shram and IRCTC-specific training.

### Result by service

| Service | Official reusable training found in this search | Status | Action |
|---|---|---|---|
| Aadhaar | No current service-specific CSC Academy/Digipaathshala training course verified | **Not verified** | Keep on verification queue; do not build duplicate training yet |
| PAN | No current service-specific CSC Academy/Digipaathshala training course verified | **Not verified** | Keep on verification queue; do not build duplicate training yet |
| Ayushman | No current service-specific CSC Academy/Digipaathshala training course verified | **Not verified** | Keep on verification queue; do not build duplicate training yet |
| PM-KISAN | No current service-specific CSC Academy/Digipaathshala training course verified | **Not verified** | Keep on verification queue; do not build duplicate training yet |
| e-Shram | No current service-specific CSC Academy/Digipaathshala training course verified | **Not verified** | Keep on verification queue; do not build duplicate training yet |
| IRCTC / travel | No current service-specific CSC Academy/Digipaathshala training course verified | **Not verified** | Keep on verification queue; do not build duplicate training yet |

### Reusable adjacent training confirmed

1. **TEC** already covers Fundamentals of Telecentre, G2C/B2C Services, CSC Scheme, Digital Seva Portal, Digital Security/Wellness, Finance/Accounting, GST, Soft Skills and Business Communication. This is the reusable foundation for CSC operator training.
2. **BCC** provides simulated hands-on computer training and explicitly includes e-Governance applications.
3. **CSC Academy skill-course operations** already document Digital Seva enrolment/payment workflow.
4. **BC/BF** has official CSC Academy/IIBF training and an official Digipaathshala assignment guide covering Digital Seva registration, exam-centre workflow, service marketing, course details, commission and FAQs.
5. **DRA** currently has live CSC Academy/IIBF batches, demonstrating that current training availability can change and must be checked at deployment time.
6. **VLE Training** remains the official umbrella training source for VLE capability development.

### Interpretation

“No service-specific training found” means **not verified in the searched official CSC Academy/Digipaathshala material**, not “no training exists anywhere” and not “the service is unavailable through CSC”.

Before Nivy creates an SOP for any of these six services, perform a second-source check against:
- the relevant official government service portal
- current CSC/Digital Seva authorization/menu where accessible
- official department operator/manual/training material
- current official YouTube channel material, if available

Only then decide whether Nivy needs to create a practical SOP.

### Current-source links

- CSC Academy BCC: https://www.cscacademy.org/digital-education
- CSC Academy Skill Courses: https://www.cscacademy.org/skill-course
- CSC Academy VLE Training: https://www.cscacademy.org/services/vle-training
- CSC Academy BC/BF portal: https://onboarding-bcbf.cscacademy.org/onboard-user-self
- CSC Academy DRA portal: https://onboarding-dra.cscacademy.org/onboard-user-self
- TEC assignment guidance: https://digipaathshala.cscacademy.org/uploads/lmscourse/publisher/assignment_guidelines/0f9008fa5758e49500810cd16e2867c1.pdf
- BC/BF assignment guidance: https://digipaathshala.cscacademy.org/uploads/lmscourse/publisher/assignment_guidelines/efca0c0ec54fdd43b01a0ff70afc6b4c.pdf


## Government-side authorization/workflow audit — 2026-10-03

### Aadhaar
UIDAI confirms that Aadhaar enrolment/update centres exist through multiple registrars, including CSC, banks, post offices, BSNL and State Governments. Current UIDAI guidance says residents must use an Aadhaar Enrolment Centre and operators capture demographic and biometric information; new enrolment is free. This establishes the CSC ecosystem role but does **not** mean every CSC is currently authorised for Aadhaar. Nivy training must therefore verify the individual centre/operator's current authorization before marking Aadhaar operational.

Official sources:
- https://uidai.gov.in/en/enrolment-and-update
- https://uidai.gov.in/en/ecosystem/enrolment-documents/295-faqs/enrolment-update.html

### Ayushman Bharat PM-JAY
NHA material states that beneficiaries can visit a nearest CSC or PM-JAY empanelled hospital for assistance. NHA's current technical-support material specifically says CSC/VLEs can raise technical tickets through Digital Seva and identifies CSC district/state managers for support. Therefore a CSC operational workflow exists, but the exact current VLE menu/authorization and live transaction workflow must be checked inside the authenticated Digital Seva environment before training is frozen.

Official sources:
- https://nha.gov.in/img/resources/Ayushman-Mitra-Flyer-english.pdf
- https://supportbeta.nha.gov.in/

### PM-KISAN
The current PM-KISAN portal explicitly provides a status page for farmers registered through CSC and states that biometric eKYC is available for CSC VLE logins. The new farmer registration form authenticates Aadhaar before registration can proceed. This is sufficient to mark PM-KISAN as **CSC-supported and workflow-verifiable**, but the current Digital Seva operator sequence should still be captured from an authorised VLE account before creating the final Nivy SOP.

Official sources:
- https://pmkisan.gov.in/
- https://pmkisan.gov.in/farmerstatus.aspx
- https://pmkisan.gov.in/RegistrationFormupdated.aspx

### e-Shram
The current Ministry of Labour & Employment e-Shram FAQ explicitly states that workers can register through an assisted approach at a CSC, and that workers without an Aadhaar-linked mobile number may register through biometric authentication at a CSC/SSK. It also states that CSCs can update worker details. Registration is free. This is a strong basis for creating a CSC operator workflow after recording the current portal sequence.

Official sources:
- https://eshram.gov.in/faqs
- https://eshram.gov.in/help

### IRCTC rail e-ticketing
IRCTC's current authorised-principal-provider document identifies CSC e-Governance Services India Ltd. as a working principal service provider under the E-Governance Scheme. IRCTC's agent policy requires RSP registration through a Principal Service Provider, Aadhaar and PAN verification, OTP authentication and an authorisation certificate displayed at the outlet. Therefore rail ticketing is **authorization-dependent**, not a generic service that every CSC can perform without the required RSP/PSP relationship.

Official sources:
- https://contents.irctc.co.in/en/IRCTC%20Authorised%20Principal%20Service%20Providers.pdf
- https://contents.irctc.co.in/en/Agent_Policy.pdf

### PAN
No current official Protean/UTIITSL CSC-specific authorization source was sufficiently verified in this pass. Keep PAN in **VERIFY** status; do not infer CSC authorization from old tutorials.

## Updated service status

| Service | Government/official evidence | CSC authorization status | Nivy action |
|---|---|---|---|
| Aadhaar | Strong | Centre/operator-specific | Verify local authorization; then SOP |
| Ayushman | Strong | VLE workflow exists; exact live menu needs verification | Capture authenticated workflow |
| PM-KISAN | Strong | CSC VLE login explicitly supported | Capture authenticated workflow |
| e-Shram | Strong | CSC assisted registration explicitly supported | Build workflow from current portal |
| IRCTC | Strong | PSP/RSP authorization required | Train only authorised RSP/PSP centres |
| PAN | Not sufficiently verified | Unknown in current pass | Keep VERIFY |

### Data protection
These services involve Aadhaar, biometric, financial or welfare information. Repository training must use synthetic examples only and must never store real Aadhaar numbers, OTPs, bank credentials, biometric data or live customer documents.

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

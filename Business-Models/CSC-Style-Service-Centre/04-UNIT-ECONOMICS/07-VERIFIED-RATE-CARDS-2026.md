# Verified CSC Service Economics — 2026 Rate/Evidence Register

**Research date:** 2026-10-04

This file separates verified customer charges/programme rules from VLE income and distributor/state shares. A number is only treated as a VLE/distributor rate when the source explicitly identifies the beneficiary.

## Current verified evidence

| Service | Customer-facing fee / programme rule | VLE / operator remuneration | Distributor / State / CSC-SPV share | Status |
|---|---|---|---|---|
| Aadhaar new enrolment | Free | UIDAI confirms enrolment is free. A historical CSC-UIDAI MoU says UIDAI provides financial assistance to CSC-SPV for successful enrolment and specified compulsory biometric updates at Government-approved rates. | Historical MoU does not establish a current public VLE split. | Verified fee; remuneration split OPEN |
| Aadhaar demographic/biometric update | Applicable update charges are displayed at centre/acknowledgement. Current UIDAI FAQ confirms online address update ₹50 and document submission at centre ₹75. | Exact current operator/VLE share not established. | OPEN | Partial |
| Aadhaar print | ₹30 per print at Aadhaar centre. | Exact VLE share not established. | OPEN | Partial |
| Aadhaar PVC | ₹50 per PVC card. | Exact VLE share not established. | OPEN | Partial |
| e-Shram registration | Free; official FAQ says workers are not required to pay charges to the registering entity. Assisted registration is available through CSC. | CAG 2026 states e-Shram commission is transferred to VLE accounts periodically, but does not publish the exact current rate in the report. | OPEN | Mechanism verified; rate OPEN |
| PMFBY via CSC | Farmer must not be charged a fee for enrolment through CSC. Insurers pay service charges fixed by MoAFW; guidelines also mention requisite commission to CSC-SPV. | Exact current CSC-SPV to VLE rate not found in reviewed public PMFBY documents. | Exact insurer/CSC-SPV/VLE waterfall OPEN | Verified no-charge rule; rate OPEN |
| Banking / BC | Government-hosted CSC banking FAQ says banking commission is paid by CSC-SPV to VLE monthly based on bank report. | Exact current national percentage not established; cited FAQ lists ₹350 certification fee and ₹175 re-exam fee. TDS is described as 10% with PAN / 20% without PAN. | Bank/provider-specific; OPEN | Mechanism verified; rate OPEN |
| BBPS | CAG publishes BBPS as a CSC service category and aggregate ecosystem data. | Exact VLE rate not established. | OPEN | Rate OPEN |
| E-Recharge | CAG publishes E-Recharge as a CSC service category and aggregate ecosystem data. | Exact VLE rate not established. | OPEN | Rate OPEN |
| State G2C / e-District | CAG publishes State Government G2C as a CSC category and aggregate ecosystem data. | State/service-specific. | State-specific | Rate OPEN |
| Insurance | CAG says insurance commission is transferred to VLE accounts periodically. | Exact product/provider commission schedule required. | Provider/service agreement required | Mechanism verified; rate OPEN |
| DigiPay | CAG says commission is transferred to VLE accounts periodically. | Exact rate not established. | OPEN | Mechanism verified; rate OPEN |
| Scholarship verification | CAG says commission is transferred to VLE accounts periodically. | Exact rate not established. | OPEN | Mechanism verified; rate OPEN |

## Primary-source notes

### Aadhaar
UIDAI current FAQ confirms new enrolment is free, applicable update charges are displayed at the centre, Aadhaar print at a centre is ₹30, PVC is ₹50, online address update is ₹50, and document submission at an Aadhaar centre is ₹75.

A historical CSC-UIDAI MoU states that UIDAI provides financial assistance to CSC e-Governance Services India Ltd. for successful enrolment and specified compulsory biometric enrolment/updates at Government-approved rates.

### e-Shram
Official e-Shram FAQ confirms registration is free and assisted registration is available through CSC. CAG Report No. 5 of 2026 states that e-Shram commission is transferred to VLE accounts periodically.

### PMFBY
PMFBY Operational Guidelines state that CSC-SPV is the nodal agency for CSC engagement, insurers must enter an agreement with CSC-SPV and pay service charges fixed by MoAFW, and farmers enrolled through CSC must not be charged a fee. The guidelines also refer to requisite commission to CSC-SPV.

A related PMFBY operational document states that banks are paid a service charge of 4% of farmer premium and that requisite commission is payable to CSC-SPV. This 4% is a bank service charge, NOT a VLE commission.

## Still required before building the Nivy commercial waterfall

1. Current bank-wise BC/BCA commission schedules.
2. Current CSC insurance provider/product schedules.
3. Current BBPS/recharge partner schedules.
4. Current PAN/Protean/UTIITSL CSC commercial schedules.
5. Current IRCTC CSC agent schedule.
6. Current PMFBY CSC-SPV service-charge/commission schedule.
7. Current e-Shram VLE remuneration schedule.
8. State-specific G2C/e-District schedules, starting with Uttar Pradesh.
9. Current GeM CSC facilitation schedule.
10. Active distributor/SCA/state-partner agreements that explicitly create an intermediate revenue share.

## Nivy modelling rule

Do not create a fictional universal waterfall such as Customer Fee → VLE 80% → Distributor X% → State Y% → Nivy Z%.

Use a service-level ledger:

Customer Fee → Provider/Government Fee → Gross Service Commission → VLE Share → Network/Distributor Share (only if contractually documented) → Central Platform Share → Tax/TDS → Settlement.

The CSC 80:20 evidence is useful as a benchmark for VLE-versus-other-stakeholder economics, but it is not evidence for a universal distributor/state/franchise percentage.

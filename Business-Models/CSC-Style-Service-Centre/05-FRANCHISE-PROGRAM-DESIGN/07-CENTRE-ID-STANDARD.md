# Centre ID & Partner ID — Naming Standard

**Folder:** `05-FRANCHISE-PROGRAM-DESIGN/`  
**Created:** 2026-10-04  
**Status:** Convention for CRM, MIS, territory register, receipts

---

## 1. Centre ID

**Format:**

```
{STATE}-{DISTRICT}-{NNN}
```

| Part | Rule | Example |
|------|------|--------|
| STATE | 2-letter code (India postal-style where common) | UP, BR, MP |
| DISTRICT | Short uppercase slug, no spaces (max ~12 chars) | LKO, VNS, GZB |
| NNN | 3-digit zero-padded sequence per district | 001, 002 |

**Examples:** `UP-LKO-001`, `UP-VNS-014`, `BR-PAT-003`, `MP-BHO-001`

---

## 2. Partner ID (person / entity)

**Format:**

```
P-{STATE}-{NNNN}
```

Example: `P-UP-0042`

One partner may operate multiple centres later; link `partner_id` → one or more `centre_id`.

---

## 3. Territory grant ID

**Format:**

```
TG-{YYYY}-{NNNN}
```

Example: `TG-2026-0007`

Store on agreement and territory register.

---

## 4. Incident / ticket IDs

| Type | Format | Example |
|------|--------|--------|
| Incident | `INC-{YYYYMMDD}-{centre_id}-{##}` | `INC-20261004-UP-LKO-001-01` |
| Ticket | System-native ID; store centre_id on ticket | |

---

## 5. Rules

1. IDs are **immutable** after LIVE (do not reuse numbers for a different location).  
2. Suspended centres keep ID; status changes in CRM.  
3. District slug table maintained internally (document new districts when used).  
4. Never encode Aadhaar/PAN into IDs.

---

## 6. Pilot bootstrap

| Step | Action |
|------|--------|
| 1 | Fix STATE + DISTRICT slug for chosen pilot district(s) |
| 2 | Reserve `001`–`030` sequence block |
| 3 | Assign centre_id at AGR or ONB stage |
| 4 | Print centre_id on fee list and daily checklist |

---

## Cross-links

- CRM fields: `10-TECH-AND-SYSTEMS/03-CRM-STAGE-AND-FIELD-LIST.md`  
- MIS dictionary: `14-MONITORING-QC-SUSTAINABILITY/03-MIS-FIELD-DICTIONARY.md`  
- Territory register: `04-TERRITORY-GRANT-REGISTER-TEMPLATE.md`

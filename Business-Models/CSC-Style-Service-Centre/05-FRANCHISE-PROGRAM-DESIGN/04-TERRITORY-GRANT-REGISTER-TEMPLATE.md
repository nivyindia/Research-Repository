# Territory Grant Register — Template

**Folder:** `05-FRANCHISE-PROGRAM-DESIGN/`  
**Created:** 2026-10-04  
**Status:** Operational register template  
**Purpose:** Prevent double-granting territory and document soft exclusivity / density rules.

---

## 1. Register fields (one row per grant)

| Field | Description |
|-------|-------------|
| grant_id | Unique ID |
| tier | L1 / L2 / L3 |
| partner_id | Linked CRM ID |
| partner_legal_name | |
| state | |
| district | |
| sub_territory | Block / pincode list / “density only” |
| exclusivity_type | NONE / SOFT / HARD (only if agreement allows) |
| effective_from | Date |
| effective_to | Date or open |
| agreement_ref | Version / file ID |
| performance_gate | e.g. activation count, compliance |
| status | ACTIVE / SUSPENDED / EXPIRED / REVOKED |
| l2_support_id | For L3 rows |
| l1_id | If under master |
| notes | Conflicts, exceptions |
| last_review | Date |

---

## 2. Rules

1. No ACTIVE overlapping **HARD** exclusivity without HQ approval log.  
2. Density markets (e.g. high CSC presence states) default to **NONE** or **SOFT**.  
3. L1 statewide grant must list excluded districts if any L2 direct deals exist.  
4. Suspend territory in register when partner SUSPENDED in CRM.  
5. Register is internal; not a marketing map of “CSC territories”.

---

## 3. Pilot default

- L3: pincode or neighbourhood description; exclusivity **NONE** unless term sheet says otherwise.  
- L2: district or cluster list; soft performance review at day 90.

---

## 4. Review cadence

| Event | Action |
|-------|--------|
| New agreement signed | Add row |
| Monthly | Spot-check overlaps |
| Partner exit | Status REVOKED; open territory |
| Pilot end | Re-score capacity before scale grants |

---

## Cross-links

- Channel structure: `01-NIVY-CHANNEL-PROGRAMME-STRUCTURE.md`  
- L2 SLA: `03-L2-SUPPORT-SLA.md`  
- Pilot district criteria: `13-IMPLEMENTATION/04-PILOT-DISTRICT-SHORTLIST-CRITERIA.md`  
- Legal territory subjects: `09-LEGAL-COMPLIANCE/01-LEGAL-CLAUSE-SUBJECT-MAP.md`

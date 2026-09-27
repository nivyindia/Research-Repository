# Talent Pool Schema & Matching

**Created:** 2026-09-27  
**Purpose:** Hold people who are not active core staff but remain **re-hirable / project-ready**, without losing history.

---

## 1. Who enters the pool

| Trigger | Pool reason code |
|---------|------------------|
| Finished internship, no FT seat | `internship_complete_no_seat` |
| Strong practical, delayed headcount | `waitlist_headcount` |
| Left in good standing (notice served) | `alumni_good_exit` |
| Project / part-time interest only | `project_only` |
| Cooldown ended, re-apply allowed | `cooldown_cleared` |
| Developing band — nurture later | `nurture_65_79` |

**Do not pool by default:** ethics termination, falsified docs, active blacklist (Orientation fail/leave cooldown still active).

---

## 2. `talent_pool_profiles`

| Field | Type | Notes |
|-------|------|--------|
| pool_id | PK | |
| person_id | FK | |
| status | enum | active, paused, placed, do_not_contact |
| reason_code | enum | above |
| preferred_roles | string[] | BDE, HR, VA_SMM, … |
| work_mode | enum | remote, hybrid, onsite, any |
| availability | enum | full_time, part_time, project, flexible |
| last_score | numeric | latest normalized 0–100 |
| last_band | enum | strong / developing / below |
| skills_tags | string[] | e.g. smm, crm, hindi, english, excel |
| city | string | |
| willing_relocate | bool | |
| notice_days | int | if employed elsewhere |
| last_contacted_at | timestamptz | |
| next_contact_after | date | cadence |
| notes | text | short operational note |
| entered_at | timestamptz | |
| updated_at | timestamptz | |

---

## 3. Matching rules (job → pool)

When a **role opening** is approved:

### Hard filters (must pass)

1. `status = active`  
2. Role in `preferred_roles` **or** empty preferences  
3. Not in `do_not_contact` / active cooldown  
4. Eligibility still valid (education rules) unless waived  

### Soft score (rank candidates)

| Factor | Weight | How |
|--------|--------|-----|
| Last assessment score | 40 | last_score |
| Role fit tag match | 20 | skills_tags ∩ JD tags |
| Recency | 15 | fresher activity ranked higher |
| Availability match | 15 | FT opening vs FT availability |
| Location / mode | 10 | remote-first org → boost remote |

**Suggested cut:** show top 20 by soft score to HR; human picks outreach list.

### Matching output row

```
opening_id | person_id | soft_score | hard_pass | recommended_action
```

Actions: `message_wa`, `email`, `call`, `skip`.

---

## 4. Cadence

| Pool segment | Contact cadence |
|--------------|-----------------|
| waitlist_headcount | Every 2 weeks until seat or 90 days |
| internship_complete_no_seat | Monthly × 3, then quarterly |
| nurture_65_79 | Invite to next Academy batch calendar |
| alumni_good_exit | Quarterly “we’re hiring” |
| project_only | When project brief matches skills_tags |

Log every touch in `stage_history` or a `pool_contacts` table (person_id, channel, at, outcome).

---

## 5. Exit from pool

| Event | New status |
|-------|------------|
| Accepts FT/internship | `placed` + application stage advances |
| Asks to stop messages | `do_not_contact` |
| No reply × N cadence | `paused` |
| Ethics issue found | remove + flag persons |

---

## 6. MVP without code

Google Sheet tabs:

1. **Pool** — columns = schema fields  
2. **Openings** — role, seats, JD tags, mode  
3. **Match view** — FILTER / SORT by role + score  

Upgrade path: same fields → Postgres / ATS.

---

## 7. Related

- Lifecycle: `01-SYSTEM-ARCHITECTURE/lifecycle-alignment.md`  
- Intake DB: `20-DATABASE-SCHEMAS/candidate-database-spec.md`  
- Bands: Orientation ≥80 FT / 65–79 internship  
- Comms: `18-TEMPLATES/communication-screening-outcomes.md`

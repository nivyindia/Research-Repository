# Talent Acquisition & Partner Engine

## Purpose

Expand Talent Sourcing from only finding candidates to building a continuous acquisition network.

### Source categories

**Direct talent**
- Nivy Jobs
- Nivy Academy
- referrals
- job boards
- LinkedIn
- professional communities
- freelancer communities
- social communities

**Institutional partners**
- colleges/universities
- placement cells
- training institutes
- coaching centres
- skill academies
- bootcamps
- hostels/PG/student communities
- NGOs/community organisations

**Distribution partners**
- community admins
- career pages/groups
- campus ambassadors
- trainers/mentors
- referral partners
- local recruiters

### Partner funnel

```
Discover
→ Research
→ Verify
→ Add to Partner CRM
→ Prioritise
→ Outreach
→ Follow-up
→ Conversation
→ Proposal
→ Pilot
→ Active Partner
→ Recurring Campaign
```

### Public-contact research

For each organisation, capture only appropriate/public business contact information:

- organisation name
- type
- city/country
- website
- public business email
- public phone
- public social URLs
- placement/recruitment contact if publicly listed
- source URL
- date verified
- verification status

Do not collect or publish private/personal contact data without an appropriate basis.

### Partner quality dimensions

Track evidence separately:
- candidate volume
- candidate quality
- response rate
- turnaround time
- placement outcome
- repeat cooperation
- geographic coverage
- role relevance

Do not treat raw applicant volume as partner quality.

---

## Community acquisition

Maintain a canonical community directory:

| Channel | Purpose | Join destination | Owner | Automation |
|---|---|---|---|---|
| WhatsApp | urgent openings/community | official destination | Talent Ops | API/approved tools |
| Telegram | alerts/community | official destination | Talent Ops | bot/API |
| Facebook | community/recruitment | official group/page | Talent Ops | approved tools |
| LinkedIn | professional reach | official page/follow | Marketing/Talent | approved tools |
| Email | job/training alerts | mailing list | Talent Ops | email automation |

Track:
- invite source
- join date
- active/inactive
- preferences
- unsubscribe/leave
- last engagement
- applications generated

---

## Sourcing automation boundary

### Good automation candidates
- scheduled research tasks
- website/contact extraction from permitted public sources
- organisation deduplication
- data validation
- enrichment
- lead scoring
- CRM record creation
- email drafting
- follow-up task creation
- reminder scheduling
- candidate status updates
- community invite messages
- job-alert segmentation
- analytics

### Human/controlled actions
- bulk outreach approval
- partnership commitments
- candidate rejection at consequential stages
- compensation/offer decisions
- access to private candidate data
- platform actions where automation is restricted

### n8n role

n8n is the orchestration layer, not the talent database and not the AI brain.

```
Form / Website / Email / Approved APIs
              ↓
             n8n
              ↓
      CRM / ATS / Database
              ↓
        AI services/agents
              ↓
   Human approval when required
              ↓
 Email / approved messaging / CRM
              ↓
          Audit log
```

The existing n8n and multi-agent resources in the Research Repository should be reused before building new workflows.

---

## V1 acquisition workflows

### Workflow A — Candidate registration
Form → validate → duplicate check → Candidate ID → database → acknowledgement → screening queue.

### Workflow B — Partner lead
Research/manual entry → partner record → source URL → priority → outreach task → follow-up reminder.

### Workflow C — Job alert
New approved opening → role/city/skill segmentation → approved email/community distribution → application link → attribution.

### Workflow D — Community join
Application/partner/referral → relevant community invitation → join/status capture → alert preference.

### Workflow E — Institute campaign
Target list → contact verification → outreach → response → meeting → pilot cohort → candidate intake.

### Workflow F — Historical candidate reactivation
Old candidate → identity match → consent/contact preference check → relevant opening/training invitation → response → current pipeline.

---

## V1 minimum data objects

Candidate
Partner
Organisation
Source
Campaign
Community
Opening
Communication
Application
Screening
Assessment

V2+ can add richer CRM, employer, matching, internship, probation and marketplace objects.

---

## Reuse-first references

Known existing repository resources to reuse/adapt:
- `Nivy Jobs/Talent Recruitment Plan 1 0 ...md`
- `Nivy Academy/NA-PP-02 Institute College Pitch Deck ...md`
- `Notion - Nivy OS/Institute & College Target List ...md`
- `Nivy Talent System/15-CITY-SOURCING/`
- `Nivy Talent System/14-INSTITUTE-PARTNERSHIPS/`
- `Nivy Talent System/13-AUTOMATION/`
- `Chats/ChatGPT/Multi Agent AIOS/09-runtime/n8n/`
- `Chats/Claude/growth-engine-automation*/`
- `Nivy Talent System/10-TALENT-POOL/`

These remain source material until version comparison/consolidation is complete.

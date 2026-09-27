# Nivy Talent System — Version Roadmap

**Purpose:** Build the smallest executable system first, validate it, then expand toward a fully integrated international talent-acquisition and talent-management platform.

## Core principle

**V1 = operational minimum, not a prototype.** It must actually find the right candidates, capture them, communicate with them, assess them, observe consistency, and move evidence-backed talent into the Talent Pool.

**P0 priority:** Candidate Discovery & Qualification Engine. Before scaling acquisition volume, Nivy must define what success looks like for each role, where suitable candidates can be found, and how job-relevant evidence will distinguish strong candidates from merely polished applicants.

Build in this order:

**Find → Capture → Engage → Screen → Test → Observe → Train → Intern → Probation → Pool → Match**

---

## Architecture

```
                    NIVY TALENT SYSTEM
                         CORE ENGINE
                              |
       +----------------------+----------------------+
       |                      |                      |
   TALENT ACQUISITION     TALENT DEVELOPMENT     TALENT DELIVERY
       |                      |                      |
   Sourcing + Partners     Nivy Academy          Nivy Jobs
       |                      |                      |
       +----------------------+----------------------+
                              |
                        CANONICAL TALENT
                              |
             Internal Work / Employers / Projects
```

Nivy Academy and Nivy Jobs remain front ends/modules over one shared Talent System and one canonical talent identity.

---

# V1 — Talent Acquisition MVP

**Goal:** Start sourcing and processing candidates immediately with minimal infrastructure.

### 0. Candidate Discovery & Qualification — P0
- Role Success Profile for each priority role.
- Source-to-quality tracking, not applicant-volume tracking.
- Evidence hierarchy: observed work > practical assessment > repeated tasks > structured interview > CV/self-report.
- Structured screening for role fit, availability, expectations, learning behaviour and reliability signals.
- Paid practical assessment + three-task consistency stage.
- Candidate Research Agent design with human approval for consequential actions.
- Downstream outcome tracking back to source and qualification evidence.

### 1. Talent sourcing
- Define 5–10 priority role families.
- Candidate sources: referrals, LinkedIn, job groups, Facebook groups, WhatsApp/Telegram communities, colleges, institutes, hostels/local networks, Nivy Academy.
- Simple source/campaign tracking.
- Manual + semi-automated research of public institute/college/training-centre contact details.

### 2. Partner sourcing
Create a basic Partner CRM for:
- colleges/universities
- placement cells
- training institutes
- coaching/skill centres
- hostels/PG/student communities
- freelancer communities
- career/community admins
- referral partners

Minimum fields:
Partner ID, organisation, type, city, website, public phone, public email, contact person, source URL, status, last contact, next action, notes.

### 3. Candidate community
Create official joining destinations:
- WhatsApp community/channel
- Telegram channel
- Facebook group
- LinkedIn page/follow/join instructions
- email/job-alert list

Every candidate source should be able to route people into the community.

### 4. Candidate intake
One master form:
- identity/contact
- city
- education/experience
- skills
- role interests
- work mode
- availability
- expected pay
- resume/portfolio link
- source
- consent/preferences
- WhatsApp/Telegram/community status

### 5. Basic pipeline
```
Lead
→ Registered
→ Screening
→ Assessment
→ 3-task consistency
→ Academy/Training (if needed)
→ Paid Internship
→ Probation
→ Talent Pool
→ Job/Project
```

### 6. Communication
Templates + controlled automation for:
- application received
- screening invitation
- assessment invitation
- reminder
- result/status
- community invitation
- new opening alert
- interview scheduling
- internship/probation updates

### 7. Assessment
Use existing role packs and scoring system. Start with 3–5 roles, not every role.

### 8. Automation
n8n V1:
- form → database/CRM
- candidate ID generation
- duplicate check
- acknowledgement email
- screening invite
- reminder
- status update
- community invite
- basic dashboard
- human approval gates

### V1 success criteria
- first 100 candidates can enter without manual re-entry
- every candidate has one canonical ID
- every source/campaign is attributable
- partner leads are trackable
- screening/assessment status is visible
- community joins can be tracked
- no raw candidate PII is stored in GitHub
- human can override automation

---

# V2 — Sourcing & Partner Engine

**Goal:** Make talent acquisition repeatable instead of dependent on the founder.

Add:
- city-wise sourcing campaigns
- institute/college database
- hostel/PG/community database
- partner scoring
- partner pipeline
- outreach sequences
- follow-up scheduling
- referral programme
- campus ambassador programme
- recruiter/VA operating queues
- source-quality analytics
- public-web research/enrichment workflow
- duplicate organisation/contact detection

Automation:
```
Target definition
→ Research
→ Organisation record
→ Contact enrichment
→ Validation
→ Outreach queue
→ Follow-up
→ Response classification
→ Partner pipeline
→ Campaign metrics
```

AI assists research, enrichment, classification and drafting; sending remains governed by channel rules and human approval where required.

---

# V3 — Talent Community & Distribution Engine

**Goal:** Build a continuously reachable talent audience.

Add:
- WhatsApp community/channel operations
- Telegram channel/bot where permitted
- Facebook group operations
- LinkedIn page/follow/follower workflows
- email newsletter/job alerts
- role-specific communities
- city-specific communities
- referral links
- invite tracking
- community engagement metrics
- opening-alert distribution
- re-engagement campaigns
- unsubscribe/opt-out controls

Key model:

```
Candidate / Partner
       ↓
Community
       ↓
Job / Training / Assessment Alert
       ↓
Application
       ↓
Talent System
```

Important: use official APIs, approved integrations and platform rules. Do not design V3 around bulk unsolicited messaging, fake accounts, credential sharing or prohibited scraping.

---

# V4 — AI-Assisted Talent Acquisition

**Goal:** Let agents perform repetitive research and coordination while humans control consequential actions.

Agent roles:
1. Sourcing Research Agent
2. Organisation/Institute Research Agent
3. Contact Enrichment Agent
4. Candidate Intake Agent
5. Candidate Profile Agent
6. Screening Assistant
7. Outreach Drafting Agent
8. Follow-up Agent
9. Community Distribution Agent
10. Data Quality/Dedup Agent
11. Assessment Coordination Agent
12. Talent Matching Agent
13. Reporting Agent

Agent loop:

```
Goal
→ Research
→ Retrieve
→ Validate
→ Score/route
→ Draft
→ Human approval (where required)
→ Execute
→ Log
→ Learn
```

AI should not independently make irreversible hiring/rejection decisions.

---

# V5 — Talent Marketplace & Employer Engine

**Goal:** Connect verified talent to Nivy and external demand.

Add:
- employer onboarding
- job intake
- job requirement parsing
- candidate matching
- shortlist generation
- interview coordination
- placement workflow
- project/freelance allocation
- rate/availability matching
- employer feedback
- candidate feedback
- placement analytics
- recurring employer accounts

Nivy Jobs becomes a marketplace/front end; the Talent System remains the underlying engine.

---

# V6 — International Talent Network

**Goal:** Operate across countries, time zones and talent markets.

Add:
- country/region/city sourcing
- timezone availability
- language profiles
- international role packs
- remote-work readiness
- international partner network
- institute/university networks
- compliance/consent rules by market
- country-specific communication rules
- multi-currency rate fields
- international employer workflows
- source/channel benchmarking by market

---

# V7 — Fully Integrated Talent OS

**Goal:** Mature international-company operating model.

Integrated systems:
- ATS/CRM
- forms
- email
- WhatsApp/approved messaging
- Telegram/approved bots
- calendar
- assessment platform
- Academy/LMS
- internship/work management
- HRIS
- payroll/accounting where required
- document/e-signature
- analytics/BI
- n8n automation
- agent runtime
- audit/event log

End-to-end:

```
Demand / Hiring Need
        ↓
AI-assisted Research & Sourcing
        ↓
Partners + Communities + Direct Applicants
        ↓
Candidate Identity
        ↓
Screening
        ↓
Practical Assessment
        ↓
Observed Paid Work
        ↓
Training / Academy
        ↓
Internship
        ↓
Probation
        ↓
Verified Talent Pool
        ↓
AI-assisted Matching
        ↓
Employer / Nivy Work
        ↓
Performance / Feedback
        ↓
Re-engagement / Re-hire
```

---

# Version gates

| Version | Primary objective | Must work before next version |
|---|---|---|
| V1 | Start acquisition | Candidate + partner intake and basic pipeline work |
| V2 | Scale sourcing | Repeatable partner/city sourcing |
| V3 | Build audience | Communities and job-alert distribution |
| V4 | Add agents | AI safely handles repetitive work |
| V5 | Monetize talent | Employer/job matching works |
| V6 | Internationalize | Multi-market operation works |
| V7 | Full Talent OS | Integrated end-to-end operating system |

## Implementation rule

Do not wait for V7 to start hiring.

**Build V1 → run real candidates → measure → fix → release V2 → repeat.**

Every version gets:
1. implementation plan
2. configuration
3. test plan
4. pilot
5. acceptance criteria
6. KPI review
7. change log
8. next-version backlog

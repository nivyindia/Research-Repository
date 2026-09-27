# S2 — Google Form with Screening

**Source:** Google Drive — Virtual Assistant Hiring Funnel  
**Drive ID:** `1yj4-KsgagGDOhdcNFafh22HzjlHc-UD7XKllG6yYuUg`  
**Export date:** 2026-09-27  
**Status:** MIGRATED

---

# VA Hiring Google Form – Terms & Conditions + Screening

## Section 1: Basic Details

- Full Name, Phone, Email, Location
- Student / Working / Freelancer?

## Screening Quiz Structure (Knowledge + Commitment)

### Earnings & Structure
- Min performance for stipend: **65%**
- Below 65%: Performance-based payout $10–$35/sales
- Full-time salary starts: **Month 4**

### Eligibility
- VA certification: **Mandatory**
- Device: Laptop/Desktop + stable internet
- Skills required: Google Sheets, Communication, Research (NOT advanced coding)
- Fluent English: Required

### Work Commitment
- Willing 8–9 hours daily fixed schedule?
- Available fixed working hours?
- OK with NO flexible timing?

### Training & 6-Month Commitment
- Complete structured onboarding?
- Miss sessions without notice = cancel selection?
- Minimum 6 months commitment?
- Early leave → pay $25–$50 training compensation?
- Sign formal 6-month agreement?

### Work Structure & Reporting
- Hours: 8–9/day
- Daily reporting mandatory
- Working hours NOT flexible
- Tasks: Lead gen, data research, etc.
- Tracking via reports/screenshots/activity logs OK?
- No report = No work counted

### Performance Rules
- ≥75% → Promotion + incentives
- <50% → Exit + certificate only
- Min 65% to continue
- Payment strictly sales/target based

### Discipline
- Inform unavailability in advance
- Frequent absence → termination
- Leaves pre-approved 24 hrs prior
- 2 days no work without notice → Immediate removal

### Final Declaration (Checkbox)
- Serious about opportunity
- Will attend training regularly
- Will work daily as per schedule
- Will submit reports on time
- Agree to 6-month commitment + compensation rule
- Understand non-performance → removal

### Optional High-Filter
- 30-second voice note introducing yourself

---

## VA Pre-Interview MCQ Test (25 Questions)

**Passing:** 70% (reference: 31/45 in some variants)

**Sections:** Basic VA Knowledge | Communication | Tools & Technical | Work & Productivity | Discipline & Ethics

**Strict:** No AI tools / external help. Suspicious activity → lifetime ban.

---

## Apps Script Snippet (Pass/Fail Email)

```javascript
var totalMarks = 45;
var passingMarks = 31;
var percentage = Math.round((score / totalMarks) * 100);

if(result === "PASSED"){
  subject = "Virtual Assistant Application Update – Shortlisted for Next Stage";
  // ... HTML body with score, percentage, status PASSED
} else {
  subject = "Virtual Assistant Application Update – Selection Status";
  // ... HTML body with status NOT QUALIFIED + reapply encouragement
}
MailApp.sendEmail({ to: email, subject: subject, htmlBody: htmlBody });
```

See original Drive doc for full question bank and sample answers.

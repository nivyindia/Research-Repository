# Database Schemas

Core entities:
Candidate, Application, Source, Consent, CommunicationPreference, Screening, Assessment, Submission, Score, Task, Skill, Role, TrainingEnrollment, Internship, ProbationReview, Job, Assignment, Institute, Campaign, Availability, CompensationExpectation and AuditLog.

Use one stable Candidate ID across the lifecycle. Record state transitions with timestamp, actor/system and evidence.
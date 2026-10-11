# F1/F2 Static Validation Note — 2026-10-11

**Roadmap continuity:** Main roadmap unchanged. F1/F2 detour for Phase-1 safety. Return to business-plan Phase 0/1 after this batch.

## Phase-1 F2 retry staging — COMPLETE (all inactive)

| Module | Path | HTTP retries | Key open risks |
|---|---|---|---|
| 1.1 Content/Social | `F1-replacements/1.1-content-social-factory/workflow.json` | 5/5 | WF-CONTENT-02 AI publish without approval |
| 1.2 SEO Automation | `F1-replacements/1.2-seo-automation/workflow.json` | 5/5 | WF-SEO-03 AI meta direct DB UPDATE |
| 1.3 Website Lead Capture | `F1-replacements/1.3-website-lead-capture/workflow.json` | 2/2 | **WF-SEC-01** webhook `typebot-lead-capture` no auth |
| 1.4 Inbound Form Qualification | `F1-replacements/1.4-inbound-form-qualification/workflow.json` | 3/3 | **WF-SEC-01** webhook `lead-qualification` no auth |
| 1.5 Central CRM Sync | `F1-replacements/1.5-central-crm-sync/workflow.json` | 1/1 | Empty IF false branches; REPLACE_WITH_* workflow IDs; Discuss only after matched execute paths |

## Shared assets
- `automation_errors_migration.sql` — idempotent, not executed
- `0.0-error-handler/workflow.json` — parses, inactive, placeholder credential

## Validation performed
- JSON parse all five staged files: pass
- Node counts match originals
- Retry on every HTTP Request node in Phase 1
- IF false branches and placeholders documented (not silently rewritten)

## Validation NOT performed
- n8n import, live execution, webhook HMAC tests, errorWorkflow runtime, production activation, DB migrate

## Open risks (do not activate until addressed)
1. WF-SEC-01 (1.3 + 1.4 public webhooks)
2. WF-CONTENT-02 (1.1)
3. WF-SEO-03 (1.2)
4. 1.5 REPLACE_WITH_* Phase-2 workflow IDs
5. 1.5 stage-name string fragility + silent non-routed stages
6. errorWorkflow ID only after Shared Error Handler import

## Next exact tasks
1. F5 — locate and reconcile master DB migration sources (`clients_master`, `00-COMBINED-DB-SCHEMA-ADDENDUM.sql`, `001_phase4_sms_calling_schema.sql`, etc.)
2. Continuity record update
3. Resume business-plan roadmap Phase 0/1 mapping (or Phase-2 F2 retries if authorized)

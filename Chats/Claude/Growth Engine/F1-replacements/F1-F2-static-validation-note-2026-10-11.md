# F1/F2 Static Validation Note — 2026-10-11

**Roadmap continuity:** Main roadmap unchanged. Detour justified by Wave 22 + N8N-Workflow-Audit-and-Fix-Plan F1/F2. Return after Phase-1 safety stages to business-plan Phase 0/1.

## Staged replacements (all inactive, originals not overwritten)

| Module | Path | HTTP retries | Key open risk |
|---|---|---|---|
| 1.1 Content/Social | `F1-replacements/1.1-content-social-factory/workflow.json` | 5/5 | WF-CONTENT-02 AI publish without approval |
| 1.2 SEO Automation | `F1-replacements/1.2-seo-automation/workflow.json` | 5/5 | WF-SEO-03 AI meta direct DB UPDATE |
| 1.3 Website Lead Capture | `F1-replacements/1.3-website-lead-capture/workflow.json` | 2/2 | **WF-SEC-01** webhook `typebot-lead-capture` no auth |
| 1.4 Inbound Form Qualification | `F1-replacements/1.4-inbound-form-qualification/workflow.json` | 3/3 | **WF-SEC-01** webhook `lead-qualification` no auth |

## Shared assets verified
- `automation_errors_migration.sql` — idempotent, no secrets, not executed
- `0.0-error-handler/workflow.json` — parses, placeholder credential, inactive

## Validation performed
- JSON parse all staged files: pass
- Node counts match originals
- Retry properties on all HTTP Request nodes
- Webhook paths confirmed; no auth config in exports

## Validation NOT performed
- n8n import, live webhooks, HMAC tests, production activation, DB migrate

## Open risks
1. WF-SEC-01 (1.3 + 1.4 public webhooks)
2. WF-CONTENT-02 (1.1)
3. WF-SEO-03 (1.2)
4. errorWorkflow ID post-import only
5. 1.5 still needs staged retry
6. F5 master migration consolidation

## Next exact task
Stage 1.5 Central CRM Sync (scheduled; no public webhook; check IF unwired branches + retries).

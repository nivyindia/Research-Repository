# F1/F2 Static Validation Note — 2026-10-11

**Roadmap continuity:** Main roadmap unchanged. Detour justified by Wave 22 static audit + N8N-Workflow-Audit-and-Fix-Plan F1/F2 (error handling + HTTP retry). Return point: after Phase-1 safety stages, resume business-plan Phase 0/1 mapping.

## Verified existing assets

| Asset | Exact path | Blob SHA (at inspection) | Result |
|---|---|---|---|
| Error migration | `Chats/Claude/Growth Engine/automation_errors_migration.sql` | `ff8907e882d7285a5cf0433023b388cfb51b4496` | SQL parses; idempotent; no secrets; focused migration. **Not executed.** |
| Shared error-handler | `Chats/Claude/Growth Engine/0.0-error-handler/workflow.json` | `e240fae536d29026d36ab7ab7f32a6590c7ac8f4` | JSON parses; placeholder credential; inactive. |
| Original 1.1 | `.../1.1-content-social-factory/workflow.json` | `aa879bfddaf185d750439ede01096f07e192d43b` | 9 nodes; 5 HTTP; no retry; WF-CONTENT-02. |
| Original 1.2 | `.../1.2-seo-automation/workflow.json` | `898a66ef45e866fa8396ab013a4a6ff493e0f761` | 15 nodes; 5 HTTP; no retry; WF-SEO-03. |
| Original 1.3 | `.../1.3-website-lead-capture/workflow.json` | `a1b09f0f4aa1877306b530c4783ac405f983540c` | 7 nodes; 2 HTTP; no retry; webhook path `typebot-lead-capture` with **no HMAC/auth** (WF-SEC-01). |

## Staged replacements created

| Module | Path | HTTP retries | Key open risk |
|---|---|---|---|
| 1.1 Content/Social | `F1-replacements/1.1-content-social-factory/workflow.json` | 5/5 | WF-CONTENT-02 AI publish without approval |
| 1.2 SEO Automation | `F1-replacements/1.2-seo-automation/workflow.json` | 5/5 | WF-SEO-03 AI meta direct DB UPDATE |
| 1.3 Website Lead Capture | `F1-replacements/1.3-website-lead-capture/workflow.json` | 2/2 | **WF-SEC-01** public webhook no signature; no email dedup before Odoo create |

All staged files: `active: false`; original not overwritten; no invented errorWorkflow ID; no secrets.

## Validation performed

- JSON parse of 1.1, 1.2, 1.3 staged files: success.
- Node counts match originals (9 / 15 / 7).
- HTTP retry properties present on all identified HTTP Request nodes.
- Connections preserved.
- Webhook path `typebot-lead-capture` confirmed; options empty (no auth config in export).

## Validation NOT performed

- n8n import / credential bind / live execution
- Webhook negative tests (unsigned, replay, malformed)
- errorWorkflow runtime
- Production activation
- DB migration execution

## Open risks (carry forward)

1. WF-CONTENT-02 (1.1)
2. WF-SEO-03 (1.2)
3. **WF-SEC-01 (1.3)** — highest priority before any public webhook activation
4. errorWorkflow ID post-import only
5. 1.4 and 1.5 still need staged retry
6. F5 master migration consolidation

## Next exact task

Stage 1.4 Inbound Form Qualification (also has public webhook `lead-qualification` — same WF-SEC-01 class).

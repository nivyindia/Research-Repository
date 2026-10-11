# F1/F2 Static Validation Note — 2026-10-11

**Roadmap continuity:** Main roadmap unchanged. Detour justified by Wave 22 static audit + N8N-Workflow-Audit-and-Fix-Plan F1/F2 (error handling + HTTP retry). Return point: after Phase-1 safety stages, resume business-plan Phase 0/1 mapping.

## Verified existing assets

| Asset | Exact path | Blob SHA (at inspection) | Result |
|---|---|---|---|
| Error migration | `Chats/Claude/Growth Engine/automation_errors_migration.sql` | `ff8907e882d7285a5cf0433023b388cfb51b4496` | SQL parses; `CREATE TABLE IF NOT EXISTS` + `CREATE INDEX IF NOT EXISTS` → idempotent. Columns: id, workflow_name, workflow_id, execution_id, execution_url, failed_node, error_message, error_stack, occurred_at (TIMESTAMPTZ DEFAULT NOW()), acknowledged, acknowledged_at, resolution_note. COMMENT explicitly forbids secrets/full request payloads. Focused migration only — does not replace full funnel schema. **Not executed against any live DB.** |
| Shared error-handler | `Chats/Claude/Growth Engine/0.0-error-handler/workflow.json` | `e240fae536d29026d36ab7ab7f32a6590c7ac8f4` | JSON parses. 2 nodes: Error Trigger → Log Failure to Postgres. Credential is named placeholder `Odoo Postgres` (no secret). Query uses sanitized string interpolation with length limits; maps workflow/execution/error fields. No `active: true`. Failure path of the handler itself is unhandled (known residual risk). Keep inactive until import + credential + migration done. |
| Original 1.1 | `Chats/Claude/growth-engine-automation-phase1-2/growth-engine-automation/phase-1/1.1-content-social-factory/workflow.json` | `aa879bfddaf185d750439ede01096f07e192d43b` | 9 nodes; 5 HTTP Request; `active: false`. No retry settings. AI rewrite → Mixpost publish with no human approval node (WF-CONTENT-02). |

## Staged replacement created

- **Path:** `Chats/Claude/Growth Engine/F1-replacements/1.1-content-social-factory/workflow.json`
- **Change:** Added node-level `retryOnFail: true`, `maxTries: 3`, `waitBetweenTries: 2000` on all 5 HTTP Request nodes only.
- Node count, IDs, connections, credentials placeholders, business logic, and `active: false` preserved.
- No invented `errorWorkflow` ID (must be set post-import after Shared Error Handler receives a real ID).
- Staging notes embedded under `_nivy_staging_notes` for provenance.

## Validation performed

- JSON parse of staged file: success.
- Node count: 9 (same as original).
- HTTP nodes with retry: 5/5.
- Connections map keys preserved.
- No secrets introduced.
- Original file not overwritten.

## Validation NOT performed

- n8n import
- Credential binding
- Live HTTP calls / Ollama / Mixpost
- errorWorkflow wiring runtime
- Human-approval gate implementation
- Production activation
- Database migration execution

## Open risks (carry forward)

1. **WF-CONTENT-02:** AI-generated social posts still publish without human review. Do not activate until approval queue or documented policy exception.
2. **errorWorkflow ID:** Must be configured after Shared Error Handler is imported.
3. **1.2–1.5:** Still lack retries and shared error-handler linkage; stage next.
4. **Webhook auth (1.3/1.4):** No HMAC demonstrated (Wave 22 WF-SEC-01).
5. **Master migration consolidation (F5):** Still required; source schemas not yet fully located/verified in this session.

## Next exact task

Stage retry + error-handler linkage notes for 1.2 SEO Automation (highest next HTTP surface after 1.1), still inactive and non-destructive.

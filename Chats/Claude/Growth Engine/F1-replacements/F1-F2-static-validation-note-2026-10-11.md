# F1/F2 Static Validation Note — 2026-10-11

**Roadmap continuity:** Main roadmap unchanged. Detour justified by Wave 22 static audit + N8N-Workflow-Audit-and-Fix-Plan F1/F2 (error handling + HTTP retry). Return point: after Phase-1 safety stages, resume business-plan Phase 0/1 mapping.

## Verified existing assets

| Asset | Exact path | Blob SHA (at inspection) | Result |
|---|---|---|---|
| Error migration | `Chats/Claude/Growth Engine/automation_errors_migration.sql` | `ff8907e882d7285a5cf0433023b388cfb51b4496` | SQL parses; `CREATE TABLE IF NOT EXISTS` + `CREATE INDEX IF NOT EXISTS` → idempotent. Columns: id, workflow_name, workflow_id, execution_id, execution_url, failed_node, error_message, error_stack, occurred_at (TIMESTAMPTZ DEFAULT NOW()), acknowledged, acknowledged_at, resolution_note. COMMENT explicitly forbids secrets/full request payloads. Focused migration only — does not replace full funnel schema. **Not executed against any live DB.** |
| Shared error-handler | `Chats/Claude/Growth Engine/0.0-error-handler/workflow.json` | `e240fae536d29026d36ab7ab7f32a6590c7ac8f4` | JSON parses. 2 nodes: Error Trigger → Log Failure to Postgres. Credential is named placeholder `Odoo Postgres` (no secret). Query uses sanitized string interpolation with length limits; maps workflow/execution/error fields. No `active: true`. Failure path of the handler itself is unhandled (known residual risk). Keep inactive until import + credential + migration done. |
| Original 1.1 | `Chats/Claude/growth-engine-automation-phase1-2/growth-engine-automation/phase-1/1.1-content-social-factory/workflow.json` | `aa879bfddaf185d750439ede01096f07e192d43b` | 9 nodes; 5 HTTP Request; `active: false`. No retry settings. AI rewrite → Mixpost publish with no human approval node (WF-CONTENT-02). |
| Original 1.2 | `Chats/Claude/growth-engine-automation-phase1-2/growth-engine-automation/phase-1/1.2-seo-automation/workflow.json` | `898a66ef45e866fa8396ab013a4a6ff493e0f761` | 15 nodes; 5 HTTP Request; `active: false`. No retry settings. AI meta → direct UPDATE website_page with no approval (WF-SEO-03). |

## Staged replacements created

### 1.1 Content/Social Factory
- **Path:** `Chats/Claude/Growth Engine/F1-replacements/1.1-content-social-factory/workflow.json`
- **Change:** retryOnFail/maxTries/waitBetweenTries on all 5 HTTP Request nodes.
- Node count, IDs, connections, credentials placeholders, business logic, `active: false` preserved.
- Open risk: WF-CONTENT-02 (AI social publish without approval).

### 1.2 SEO Automation
- **Path:** `Chats/Claude/Growth Engine/F1-replacements/1.2-seo-automation/workflow.json`
- **Change:** retryOnFail/maxTries/waitBetweenTries on all 5 HTTP Request nodes (GSC, Ollama cluster, Ollama meta, Fetch Sitemap, Check URL Status).
- 15 nodes preserved; connections preserved; `active: false`.
- **Open risk WF-SEO-03:** AI-generated meta descriptions written directly to `website_page` via UPDATE with no human approval, preview/diff, backup, or rollback. Do not activate until gate added.

## Validation performed

- JSON parse of both staged files: success.
- Node counts: 1.1 = 9, 1.2 = 15 (match originals).
- HTTP nodes with retry: 5/5 in each.
- Connections maps preserved.
- No secrets introduced.
- Original files not overwritten.

## Validation NOT performed

- n8n import
- Credential binding
- Live HTTP / GSC / Ollama / Mixpost / DB writes
- errorWorkflow wiring runtime
- Human-approval gate implementation
- Production activation
- Database migration execution

## Open risks (carry forward)

1. **WF-CONTENT-02:** AI social posts publish without human review.
2. **WF-SEO-03:** AI meta descriptions write directly to production DB without review/rollback.
3. **errorWorkflow ID:** Must be configured after Shared Error Handler is imported.
4. **1.3–1.5:** Still lack retries and shared error-handler linkage; stage next.
5. **Webhook auth (1.3/1.4):** No HMAC demonstrated (Wave 22 WF-SEC-01).
6. **Master migration consolidation (F5):** Source schemas not yet fully located/verified.

## Next exact task

Stage retry + notes for 1.3 Website Lead Capture (webhook auth review priority), still inactive and non-destructive.

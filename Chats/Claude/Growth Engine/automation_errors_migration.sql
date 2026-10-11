-- F1.2 — shared n8n error log table
-- Safe to re-run. Run in the same PostgreSQL database used by the Growth Engine
-- before importing/activating the shared Error Handler workflow.
-- This is a focused migration; it does NOT replace/reconcile the full funnel migration set.

CREATE TABLE IF NOT EXISTS automation_errors (
    id BIGSERIAL PRIMARY KEY,
    workflow_name TEXT NOT NULL DEFAULT 'unknown',
    workflow_id TEXT,
    execution_id TEXT,
    execution_url TEXT,
    failed_node TEXT,
    error_message TEXT NOT NULL DEFAULT 'Unspecified workflow error',
    error_stack TEXT,
    occurred_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    acknowledged BOOLEAN NOT NULL DEFAULT FALSE,
    acknowledged_at TIMESTAMPTZ,
    resolution_note TEXT
);

CREATE INDEX IF NOT EXISTS idx_automation_errors_occurred_at
    ON automation_errors (occurred_at DESC);

CREATE INDEX IF NOT EXISTS idx_automation_errors_unacknowledged
    ON automation_errors (acknowledged, occurred_at DESC)
    WHERE acknowledged = FALSE;

COMMENT ON TABLE automation_errors IS
    'Operational log for n8n workflow failures; do not store secrets or full request payloads here.';

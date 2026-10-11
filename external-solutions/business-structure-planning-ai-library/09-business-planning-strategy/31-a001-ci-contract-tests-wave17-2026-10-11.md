# Wave 17 — A001 CI Contract Tests — 2026-10-11

## Objective

Move from documentation-only contract work toward repeatable automated checks, without overstating runtime readiness.

## Changes committed

1. Added `.github/scripts/validate_a001_contracts.py`.
   - Uses the PyYAML dependency already installed by repository CI.
   - Checks the 12 SK001 fixture IDs/categories, draft event contracts and canonical envelope fields, fail-closed A001 mapping, SK001/SK002 lifecycle states, research-tool planned status, A001 required inputs/downstream event, `runtime_verified: false`, inactive n8n workflow, and key validation guards.
   - This is a static consistency validator; it is not a full JSON Schema validator or live runtime test.
2. Added `.github/scripts/test_a001_trigger.js`.
   - Executes the exact JavaScript source stored in the n8n A001 normalization Code node using Node's built-in runtime.
   - Includes one valid envelope test and ten negative tests for wrong event type/version, missing event ID, invalid timestamp, missing metadata, missing required research inputs, malformed source policy/competitor set and missing company ID.
   - Confirms the placeholder reports `validated_pending_runtime` and `runtime_invoked: false`.
3. Updated `.github/workflows/ci.yml` to run both checks after dependencies are installed.
4. Tightened the A001 trigger to require an object-valued `metadata` field, matching the canonical event envelope requirement.

## Commit evidence

- A001 static consistency validator: `b8f53d9cbff0326587f49ae4e07d64a205f0f5b7`
- Trigger metadata guard: `e4053f3a0aa0f9cc5cd3ab5e9fa56cf9cf7e815c`
- Executable trigger tests: `282349044dad4c7b7ff7cef477a2542e03644ae4`
- Static validator metadata check: `863d358394841b6384b710d6a0baeec8919b02dd`
- CI workflow integration: `9efd948e5c4fefb11e1e8106287e836852c6b4ce`

## Verification status

- The changed workflow JSON was fetched back and parsed successfully; the workflow remains inactive and the runtime status remains pending.
- **Direct code-node execution check now passed:** fetched the committed workflow JSON, executed the exact JavaScript stored in the `a001-normalize` Code node in an isolated JavaScript runtime, and observed 11/11 expected outcomes: one valid envelope accepted and ten malformed envelopes rejected. This verifies the current validation function's behavior for these cases; it is not a live n8n run and does not test the committed `.github/scripts/test_a001_trigger.js` file as a standalone Node process.
- The latest commit's combined GitHub status endpoint returned an empty status list, and the available workflow-run lookup returned no run. Therefore the full GitHub Actions CI job and the Python static validator's result are **not confirmed**.
- No n8n instance, A001 executor, research tool adapter or event-store persistence was exercised.

## Next actions

1. Obtain a real GitHub Actions run for commit `9efd948e5c4fefb11e1e8106287e836852c6b4ce` (or a later commit), inspect each step and fix failures before treating the checks as passing.
2. If repository push commits do not trigger Actions, use an authorized manual workflow dispatch or PR path; do not fabricate a green status.
3. Add actual JSON Schema validation for event payload/envelope contracts after selecting/confirming the canonical schema format.
4. Keep the A001 mapping blocked, SK001 specified but unapproved, the three research tools planned, and `runtime_verified: false` until live evidence exists.
5. Continue the main roadmap's cross-functional requirement reconciliation and integration work; these agent tests are only one supporting workstream.

## Status

**CI checks authored and wired; execution result not surfaced/verified. Runtime remains unverified.**

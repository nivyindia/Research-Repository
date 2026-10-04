# Deep Dive: Social Media + pendpost + MCP Agent Stack — 2026-10

**Goal:** Let an AI agent (Claude, Cursor, etc.) draft, schedule and queue social posts across many platforms while a human keeps a hard approval gate. Nothing goes live until you approve it.

**Why pendpost:** Local-first, MIT license, MCP-native, fail-closed human approval, brand-lint, anti-ban circuit breakers, no phone-home.

**Related catalogs:** `100-social-media-accounts-growth-agents-catalog-2026-10.md`, `23-jarvis-...`

---

## 1. Quick start (zero config)

```bash
npx pendpost
# then open http://127.0.0.1:8090
```

First run creates an example “Acme Launch” campaign so you can see the full flow immediately. No accounts needed yet.

Alternative installs:
```bash
# git
git clone https://github.com/pendpost/pendpost
cd pendpost && npm start

# docker
docker compose up
```

---

## 2. Connect an MCP client (agent control)

### Claude Desktop (one-click)
Download the `.mcpb` bundle from the GitHub releases and install it. It self-boots `npx -y pendpost --stdio`.

### Any stdio MCP client (Cursor, Claude Code, etc.)
```json
{
  "mcpServers": {
    "pendpost": {
      "command": "npx",
      "args": ["-y", "pendpost", "--stdio"]
    }
  }
}
```

### HTTP transport (when the dashboard is already running)
```bash
claude mcp add --transport http pendpost http://127.0.0.1:8090/mcp
```

---

## 3. The human approval gate (non-negotiable)

- Every post starts as `draft`.
- Only `approve_post` or `reject_post` can change the state.
- The actor that created a post **cannot** approve it (no self-approval).
- Auto-approve is **owner-only** and revocable.
- `publish_due_run` requires explicit `confirm:true`.

This is the core safety model of the project. Do not bypass it.

---

## 4. Connect real platforms

1. Copy `.env.example` → `.env`
2. Fill only the platforms you need (Instagram, Facebook, LinkedIn, YouTube, X, Telegram, Discord, Mastodon, Nostr, WordPress, Ghost, etc.)
3. Credentials stay local; nothing is sent to pendpost servers.

Supported (and growing): Instagram, Facebook, LinkedIn, YouTube, X, Telegram, Discord, Mastodon, Nostr, WordPress, Ghost, Reddit, Pinterest, TikTok (beta), Google Business Profile.

---

## 5. Typical agent workflow

1. You (or the agent) ask: “Plan a week of LinkedIn + Instagram posts about our new feature.”
2. Agent calls pendpost tools → creates drafts + schedules them.
3. You open the dashboard (http://127.0.0.1:8090) or ask the agent to list pending approvals.
4. You approve / edit / reject.
5. pendpost publishes approved posts at the scheduled time (uses native scheduling where the platform supports it).
6. Agent can later pull analytics / insights.

**Useful agent tools (examples):**
- plan_create_post / plan_update_post
- approve_post / reject_post
- list calendar / pending queue
- publish_due_run (with confirm)
- config_set (non-secret only)

---

## 6. Safety & anti-ban features

- Platform action-block circuit breaker (especially Meta) — halts the lane and does not auto-resume.
- Cadence caps and lane pause kill-switch.
- Caption brand-lint (editable rules) that can block publish.
- Local-first (127.0.0.1), secrets in your `.env`, no telemetry.

**Still your responsibility:** Follow each platform’s Terms of Service. Aggressive automation can still get accounts limited or banned.

---

## 7. Combining with other tools

- Content generation → use catalog 23 / 97 free tools, then hand the copy to pendpost.
- Research / competitor listening → Browser Use or XActions, then feed insights into the agent.
- Full end-to-end: Research agent → Content agent → pendpost drafts → Human approval → Publish → Analytics feedback.

**Last updated:** 2026-10-04

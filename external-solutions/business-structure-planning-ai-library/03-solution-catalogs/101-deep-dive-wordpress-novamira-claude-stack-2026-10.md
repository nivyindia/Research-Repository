# Deep Dive: WordPress + Novamira + Claude / Cursor Stack — 2026-10

**Goal:** Give any MCP-compatible AI agent (Claude Desktop, Claude Code, Cursor, Codex, ChatGPT, etc.) full native access to a WordPress site so it can create pages, edit content, run WP-CLI, execute PHP, manage plugins/themes, and build real sites — all from natural language.

**Recommended for:** Staging / development environments only. Always keep backups. Never enable full PHP/file access on a live production site without strict controls.

**Related catalog:** `99-website-development-wordpress-html-agents-catalog-2026-10.md`

---

## 1. Prerequisites

- WordPress **6.9+** (Abilities API is required)
- PHP 8.0+
- HTTPS (or local development)
- Administrator account
- Staging site strongly preferred
- Claude Desktop / Claude Code / Cursor / any MCP client

---

## 2. Install Novamira (5 minutes)

1. Download the free plugin ZIP from https://novamira.ai
2. In WordPress admin → **Plugins → Add New → Upload Plugin** → activate
3. Go to **Novamira → Configuration**
4. Enable **AI Capabilities / AI Abilities** (read the security warning)
5. Choose your preferred client (Claude, Cursor, etc.) — Novamira shows the exact connection method and URL

---

## 3. Connect your AI client

### Option A — Claude Desktop (easiest)
- On the Novamira Configuration page select Claude Desktop
- Download the one-click `.mcp` / `.mcpb` bundle (contains the application password)
- Open the bundle → Claude Desktop installs it
- Or manually add the OAuth URL: `https://your-site.com/wp-json/mcp/novamira-oauth`

### Option B — Claude Code (terminal)
```bash
claude mcp add novamira-your-site --transport http https://your-site.com/wp-json/mcp/novamira-oauth
```
Sign in when the browser opens.

### Option C — Cursor
Add to `~/.cursor/mcp.json` or project `.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "novamira-your-site": {
      "url": "https://your-site.com/wp-json/mcp/novamira-oauth"
    }
  }
}
```

### Option D — Application Password (fallback / local bridge)
```json
{
  "mcpServers": {
    "novamira-your-site": {
      "command": "npx",
      "args": ["-y", "@automattic/mcp-wordpress-remote@latest"],
      "env": {
        "WP_API_URL": "https://your-site.com/wp-json/mcp/novamira",
        "WP_API_USERNAME": "your-username",
        "WP_API_PASSWORD": "your-application-password"
      }
    }
  }
}
```

### Option E — Novamira CLI (for any coding agent)
```bash
curl -fsSL https://raw.githubusercontent.com/use-novamira/novamira-cli/main/install.sh | sh
```
Then connect any terminal agent (Claude Code, Codex, Gemini CLI, OpenCode, etc.).

---

## 4. What the agent can now do

Once connected, the agent has tools for:
- Execute arbitrary PHP (full WordPress environment)
- Run WP-CLI commands
- Query the database
- Read / write theme and plugin files
- Create / edit posts, pages, custom post types
- Manage menus, widgets, media
- Work with Elementor, Bricks, Oxygen, Divi, ACF, WooCommerce, etc.
- Generate Gutenberg blocks or builder-native structures

**Example prompts:**
- “Create a new landing page with hero, features, testimonials and CTA using native blocks.”
- “Rewrite the homepage hero in clean Elementor containers and update the SEO title.”
- “List all plugins that are outdated and tell me which ones affect performance.”
- “Generate 5 product descriptions for the Summer 2026 category and set them as drafts.”

---

## 5. Safety workflow (mandatory)

1. Work only on **staging** first.
2. Take a full backup before enabling AI abilities.
3. Prefer draft / sandbox theme workflows when available.
4. Review every change in the WordPress admin or front-end preview before promoting to production.
5. Disable AI abilities or remove the plugin when not actively using it.
6. Never share the application-password bundle or OAuth credentials.

---

## 6. Next-level combinations

- Pair with **Block Runner** to convert free-form HTML into validated Gutenberg blocks.
- Use **elementor-headless** skill for pure Elementor JSON generation.
- Combine with **Automattic wordpress-agent-skills** for full theme generation from a one-line prompt.
- For headless: use the agentic-wordpress-app-builder CrewAI pipeline (catalog 99).

**Last updated:** 2026-10-04

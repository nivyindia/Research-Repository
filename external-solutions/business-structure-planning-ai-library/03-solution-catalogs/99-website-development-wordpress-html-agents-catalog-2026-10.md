# Website Development, WordPress & HTML Agents Catalog — 2026-10

**Purpose:** Open-source agents, skills, MCP servers, plugins and frameworks that let AI agents create, edit, and manage websites — WordPress (Gutenberg, Elementor, Bricks, Oxygen, etc.), plain HTML/CSS/JS, headless setups, and full site generation from natural language.

**Reuse rule:** Prefer tools that output native, editable WordPress blocks or real files (not locked black-box builders). Always run on staging first. Use human approval for production publishes.

**Related:** Browser automation catalog `98-...`, content factory catalogs.

---

## 1. WordPress MCP servers & full agent access

| Resource | Type | What agents can do | Link |
|----------|------|--------------------|------|
| **Novamira** | Free OSS MCP | Full WordPress access: PHP execution, WP-CLI, DB queries, file edits, any plugin/theme/builder | https://novamira.ai |
| **WPVibe / NIBWP** | WordPress plugin MCP server | Secure MCP endpoint for Claude/ChatGPT/Cursor etc. Content, themes, draft workflows | WordPress.org / sandywp.com |
| **Automattic wordpress-agent-skills** | Official prototypes | Theme/site generation skills + Studio MCP server for local WordPress management | https://github.com/Automattic/wordpress-agent-skills |
| **WordPress Abilities API + MCP Adapter** | Core + plugin | Official way agents discover and call site abilities (WP 6.9+) | WordPress core docs + GitHub MCP Adapter |
| **SD AI Agent / SuperDav** | WordPress plugin | Agentic loop via Abilities API — content, WooCommerce, SEO, media, users, analytics | https://github.com/Ultimate-Multisite/sd-ai-agent |

---

## 2. Site builders & generators from natural language

| Resource | Type | Output | Link |
|----------|------|--------|------|
| **Automattic minimalistic-site-builder / builder2** | CLI + plugin | Multi-page block theme + content plugin from one-line prompt | https://github.com/Automattic/minimalistic-site-builder |
| **nik-hil/agentic-wordpress-app-builder** | CrewAI multi-agent | Natural language → full headless WordPress + Faust.js/Next.js site (Docker) | https://github.com/nik-hil/agentic-wordpress-app-builder |
| **AgenticWP** | Free OSS plugin | Topic → SEO-ready Gutenberg posts, images, meta, structured data | https://agenticwp.org |
| **Frontman** | WordPress plugin (GPLv2) | Agentic editor for existing sites — copy, blocks, Elementor, menus, CSS, SEO | https://wordpress.org/plugins/frontman-agentic-ai-editor/ |
| **Oxygen Builder AI** | Commercial + MCP | Any MCP agent builds real Oxygen pages, templates, content types on live WP | https://oxygenbuilder.com/build-with-ai/ |
| **Block Runner** | Open-source skill (npm) | HTML → valid Gutenberg blocks, validates against headless Gutenberg | https://www.accelerateplugin.com/block-runner/ |

---

## 3. Page-builder specific skills & converters

| Resource | Builder | Capability | Link |
|----------|---------|------------|------|
| **elementor-headless** | Elementor | Agent skill: natural language / HTML → Elementor page.json, schema query | https://github.com/Moksa1123/elementor-headless |
| **Elementor MCP** (community) | Elementor | 97 MCP tools for widgets, structure, settings, templates | Search msrbuilds/elementor-mcp |
| **Bricks HTML & CSS → Bricks** | Bricks 2.3+ | Paste HTML/CSS → native Bricks elements + variables | Bricks builder docs |
| **Code2Bricks** | Bricks | Bidirectional code ↔ Bricks editing | code2bricks.com |
| **CrocoBuilder MCP** | CrocoBuilder | Prompt / Figma → structured editable pages + design system | crocoblock.com |

---

## 4. General HTML / frontend agent patterns

- Use **Playwright + Browser Use / Stagehand** to visually inspect and iterate on any site.
- Pair with coding agents (Cursor, Claude Code, Codex) + MCP for file edits.
- Common flow: Prompt → HTML/CSS/JS generation → validation → deploy via WP-CLI or Git.
- For pure static sites: any LLM coding agent + static host (Vercel, Netlify, GitHub Pages).

---

## 5. Recommended Nivy website stacks

**Stack A — Pure open-source WordPress agent**
1. Novamira or NIBWP MCP server
2. Claude / Cursor / any MCP client
3. Staging site + human approval gate
4. Optional: Block Runner for HTML→blocks

**Stack B — Full site from prompt**
1. Automattic site-builder or agentic-wordpress-app-builder
2. Review generated theme + content
3. Deploy to staging → production

**Stack C — Existing site editing**
1. Frontman or SD AI Agent plugin
2. Or Elementor/Bricks-specific skills
3. Always preview before publish

---

## 6. Safety notes

- Never give production write access without approval + backups.
- Prefer draft/theme sandbox workflows (many MCP servers support this).
- Validate commercial rights on generated images/content.
- Keep WP core, plugins and PHP updated; agents can introduce insecure code if unconstrained.

**Last updated:** 2026-10-04

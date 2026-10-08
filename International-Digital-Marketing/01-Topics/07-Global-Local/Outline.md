# Global-Local — Outline (stronger points)

> Sources: Google multi-regional/multilingual guidance; hreflang best practices.

## 1. URL architecture (choose one pattern and stick)
- **ccTLD** (example.de) — strong country signal, more ops, equity split
- **Subdomain** (de.example.com) — clear split, flexible hosting
- **Subdirectory** (example.com/de/) — shared authority, simpler for most scalers
- Document decision + why (ops cost vs SEO signal)

## 2. Hreflang rules (must-haves)
- Reciprocal links (A→B and B→A)
- Self-reference on every page in the set
- Valid codes (language ISO + optional region, e.g. en-GB not en-UK)
- **x-default** for intentional fallback
- Implementation place: HTML head / HTTP header / **XML sitemap at scale**
- Each locale **self-canonical** (do not canonical localized page to another language)

## 3. Page mapping
- Table of equivalent URLs across locales
- Only annotate **commercially ready** locales (half-translated = avoid)
- Pages that exist in one language only: no fake alternate to homepage

## 4. Real localization checklist
- Currency, tax, payment methods
- Contact, shipping, legal pages
- Imagery, examples, proof (local case studies/reviews)
- Offers and holidays
- Support language and hours
- Local platforms (search/social/messaging) — not US-only defaults

## 5. Rollout steps
1. Pick URL pattern
2. Prioritize markets (link Market-Research scores)
3. Map equivalents
4. Ship complete locales first
5. hreflang + sitemaps + Search Console checks
6. Measure by country/language

## 6. Outputs
- Architecture decision note
- Equivalence mapping sheet
- Localization QA checklist
- Rollout order table

# Run 2026-09-02T09-16Z Analysis

**Fetch time:** 2026-09-02T09:16Z–09:20Z UTC (root index + 36 sub-sitemaps + 298 page fetches)
**Baseline:** 2026-09-01T09-16Z (consecutive day; `sitemaps/openai.com/latest.xml` + `sitemaps/openai.com/sub/latest/`)
**Stats:** 1627 total URLs (union across 36 sub-sitemaps) | 4 added | 294 updated | 2 removed | 0 anomalies | 298 page fetches attempted, 298 succeeded, 0 failures

## Anomalies

None. Checked and clear:
- No `<lastmod>` later than fetch time (latest observed lastmod: `path-to-astra` at 2026-09-02T09:15:12.328Z, ~4 minutes before fetch).
- No `<lastmod>` moved backwards vs. the prior snapshot on any of the 294 updated URLs.
- No new URL with a `<lastmod>` predating first_seen by more than a few days — all 4 added URLs carry lastmods from 2026-09-01/09-02 (same day as first appearance).
- No reappeared URLs (neither of the 2 removed-this-run URLs, nor any newly-added URL, exists in `state/known_urls.json` with a prior last_seen gap).
- No sub-sitemap section migrations detected.

One item worth flagging even though it isn't a strict lastmod anomaly: [`/index/introducing-b2b-signals/`](../../pages/openai.com/index/introducing-b2b-signals/index.md) gained a new "## Update" block dated **August 12, 2026** ("B2B Signals is now called Enterprise Signals") that is only appearing in our snapshots today, three weeks after the date it claims. The page's `<lastmod>` did update in step with this run, so it's not a backdating anomaly by the strict rule, but the claimed content-update date is notably older than our observation date — likely this rename note simply wasn't indexed/crawled until now, or the CMS re-touched a batch of old redirect/rename notices today.

## Significant updates

- **[`/index/path-to-astra/`](../../pages/openai.com/index/path-to-astra/index.md)** *(new page — see below, but also drives most of the day's "updated" hub-page changes)* — OpenAI designates its Astra model as the first to meet the **Critical** cybersecurity-capability threshold under its Preparedness Framework.
- **[`/index/apple-is-getting-this-wrong/`](../../pages/openai.com/index/apple-is-getting-this-wrong/index.md)** — new inline update: "September 1, 2026 update: You can read our opposition to Apple's motion for preliminary injunction [here]" linking to a CourtListener-hosted PDF (`gov.uscourts.cand.474095`). This is the ongoing OpenAI–Apple legal dispute over App Store/ChatGPT integration terms; OpenAI has now filed formal opposition to Apple's injunction motion.
- **[`/solutions/industries/healthcare/`](../../pages/openai.com/solutions/industries/healthcare/index.md)** — the healthcare industry landing page was rewritten to reflect the new EHR/Healthcare Public Data launch: old copy about "standardize AI across your health system" / "reduce risk" replaced with new sections "Connect healthcare's trusted systems and sources," "Accelerate work across care and operations," and "Deploy AI with healthcare-ready controls" (EHR workflows, clinical evidence, public healthcare data, BAA-covered HIPAA workflows).
- **[`/products/release-notes/`](../../pages/openai.com/products/release-notes/index.md)** — rolling window advanced; new GA entry added: "Healthcare plugins for ChatGPT and Codex" (Sep 1, 2026) — Healthcare Public Data (9 public healthcare sources, read-only, no chart access) and an Epic EHR integration (read-only, admin-configured, requires BAA for PHI). The oldest entry in the window (Aug 27, "Centralized identity management in Admin Console") rolled off.
- **[`/business/customer-stories/`](../../pages/openai.com/business/customer-stories/index.md)** — customer-story grid refreshed: **+Gilbert + Tobin** (Australian law firm; 87% active ChatGPT usage among enabled users), **+Polimill** (Japan public-sector AI); dropped Circles and Univé from the featured set (still live as standalone pages).

## Routine, low-signal updates

- **~115 of 294** updated pages: diff is confined entirely to the "## Keep reading" related-articles widget (card images/titles/dates swapped to surface the day's new posts: Path to Astra, the healthcare plugin post, and the AI-native-workflows post). No change to the page's own body content. Includes the homepage and the `/news/*` hub/listing pages.
- **160 of 294** updated pages: byte-for-byte identical content — pure `<lastmod>` bump with no markdown-visible change (metadata/cache-bust touch).
- **4 partner pages** ([endava](../../pages/openai.com/business/partners/endava/index.md), [ernst-and-young](../../pages/openai.com/business/partners/ernst-and-young/index.md), [ntt-data](../../pages/openai.com/business/partners/ntt-data/index.md), [pwc](../../pages/openai.com/business/partners/pwc/index.md)) — only their partner-tier badge SVG's CDN deployment-hash query string changed (`dpl_BdRxAz7...` → `dpl_BF5Kd1Y...`); same badge image, pure cache-bust.
- **[`/index/how-agents-are-transforming-work/`](../../pages/openai.com/index/how-agents-are-transforming-work/index.md)** and **[`/signals/enterprise-data/`](../../pages/openai.com/signals/enterprise-data/index.md)** — a stray "Guides" nav label appears concatenated onto the "Company" nav link text; looks like a markdown-conversion artifact of a sitewide nav-menu addition, not a content change.
- **[`/index/reducing-bias-and-improving-safety-in-dall-e-2/`](../../pages/openai.com/index/reducing-bias-and-improving-safety-in-dall-e-2/index.md)** — this ~4-year-old DALL·E 2 post finally picked up the current sitewide footer nav (latest-model link bumped GPT-5.3 Instant → GPT-5.6; footer gained Customer Stories/Partner Network/Supply Co. links that other pages already carry).
- **[`/signals/data/`](../../pages/openai.com/signals/data/index.md)** — page-template restructure only: sidebar table-of-contents rendered as an explicit bullet list, section headings downgraded from H2 to H4, a "Download data and methodology" link promoted above the fold. No dataset changes.
- Remaining updates are `/news/*` hub pages ([news/](../../pages/openai.com/news/index.md), [news/company-announcements/](../../pages/openai.com/news/company-announcements/index.md), [news/product-releases/](../../pages/openai.com/news/product-releases/index.md), [news/safety-alignment/](../../pages/openai.com/news/safety-alignment/index.md), [news/security/](../../pages/openai.com/news/security/index.md)) and the homepage simply surfacing the day's new posts in their card grids.

## New pages

- **[`/index/path-to-astra/`](../../pages/openai.com/index/path-to-astra/index.md)** — Safety/Security. OpenAI states its Astra model now meets the **Critical** cybersecurity-capability threshold under the Preparedness Framework (the first model so designated): it can find and exploit previously-unknown vulnerabilities in hardened systems without step-by-step human guidance, scored 100% on ExploitBench, and discovered two real zero-days during evaluation (now being disclosed to maintainers). Development was partly paused after the OpenAI–Hugging Face incident to harden training infrastructure and safeguards; Astra ships with strengthened refusal training (91.5% vs. 59% refusal rate on cyber-jailbreak evals for the prior model), stricter behavior boundaries for high-risk accounts, and production misalignment monitoring/chain-of-thought review. Advanced cyber capability access will be limited initially to alpha testers, then expand via "Daybreak Blue."
- **[`/index/chatgpt-connects-health-records-and-healthcare-sources/`](../../pages/openai.com/index/chatgpt-connects-health-records-and-healthcare-sources/index.md)** — Product. Announces an Epic EHR integration and a "Healthcare Public Data" plugin for ChatGPT for Healthcare/Clinicians and HIPAA-enabled Enterprise workspaces — both read-only, admin-gated, BAA-required for PHI. Companion launch to the release-notes GA entry and the healthcare industry page rewrite above.
- **[`/index/gilbert-tobin/`](../../pages/openai.com/index/gilbert-tobin/index.md)** — customer story. Australian law firm Gilbert + Tobin: 87% active usage among enabled ChatGPT users (2x their prior adoption target), CEO-led governance model, uses ChatGPT + Codex.
- **[`/index/ai-native-company-workflows/`](../../pages/openai.com/index/ai-native-company-workflows/index.md)** — AI Adoption. Editorial piece profiling Basis, Clay, and Exa Labs on turning agent workflows into "operating capability" (onboarding, account management, developer integrations) — a template/playbook piece rather than a product or customer announcement.

## Removals

- **[`/form/trusted-access-for-biology-research/`](../../pages/openai.com/form/trusted-access-for-biology-research/index.md)** — biosecurity-research access request form, dropped from the sitemap. Last-good snapshot preserved in git history.
- **[`/index/openai-campus-network-student-club-interest-form/`](../../pages/openai.com/index/openai-campus-network-student-club-interest-form/index.md)** — student-club interest-collection form, dropped from the sitemap. Last-good snapshot preserved in git history.

Both were confirmed absent from every current sub-sitemap (not merely relocated to a different section) — genuine removals, most likely closed/expired intake forms rather than a content strategy shift.

## Fetch failures

None. All 298 page fetches (4 added + 294 updated) succeeded on the first attempt via `tools/html_to_md.py`.

# Run 2026-07-31T09-16Z — Analysis

**Fetch time (sitemap):** 2026-07-31T09:17:28Z (root index + all 34 sub-sitemaps)
**Baseline:** 2026-07-30T09-16Z (consecutive day)
**Totals:** 1,499 URLs currently live (was 1,492) | 34 sub-sitemaps (unchanged) | +9 added | -2 removed | 190 lastmod-updated | 0 anomalies

All 199 added/updated URLs were fetched via `tools/html_to_md.py` (curl-cffi, Chrome impersonation). Zero Cloudflare blocks, zero fetch errors. 106 of the 199 differed from their prior snapshot at the markdown level; 93 were byte-identical republishes (a fresh `<lastmod>` with no visible content change).

---

## 1. Anomalies

**None this run.** Checked explicitly:

- No `<lastmod>` later than fetch time (no future-dated pages).
- No `<lastmod>` moved backwards vs. its own prior value across any of the 190 updated URLs.
- No URL in the Added set that previously existed in `state/known_urls.json` (i.e., no reappearances) — all 9 additions are genuinely first-seen.
- No URL migrated between sub-sitemap sections (compared full URL sets across all 34 files — identical membership for every URL present in both snapshots).

The two Removed URLs (`/api-priority-processing/` and `/business/plugins/adobe-photoshop/`) both look like clean renames rather than deletions — see §2 and §4.

**Soft note (not a sitemap anomaly, but a docs/sitemap gap worth flagging):** two newly-linked pages are referenced from freshly updated content but do not yet exist in any sub-sitemap: `/business/solutions/finance/workflows/` (linked from the updated `/business/solutions/finance/` hub) and `/product-compliance-status/` (linked from the updated `/security-and-privacy/` page). Both may simply not be published yet, or may be intentionally excluded from the sitemap. Worth checking again tomorrow — if either appears in tomorrow's sitemap, note the lag between "linked" and "indexed."

---

## 2. Significant updates — a coordinated "Fast mode" rename + price cut (July 30)

The single biggest story this run is a same-day, multi-page rollout:

- **Terminology rename:** "Priority Processing" → **"Fast mode"** across the API product surface. Confirmed explicitly in the new `/api-fast-mode/` page copy: *"Priority processing was renamed Fast mode on July 30, 2026. You can use either service_tier: priority or service_tier: fast in your API requests."*
  - `/api-priority-processing/` (removed from sitemap) ↔ `/api-fast-mode/` (new page) — same slot in the site, renamed.
  - `/api-reserved-tier/`, `/api-scale-tier/`, and `/api/` all had every "Priority"/"Priority processing" reference swapped to "Fast mode" in place.
  - `/products/release-notes/` gained a matching GA entry: **"GPT‑5.6 price reductions and Fast mode for the API"** (Jul 30).
- **Price cuts, same day:** GPT‑5.6 Terra dropped from $2.50/$15.00 to **$2.00/$12.00** per 1M input/output tokens (20% cheaper); GPT‑5.6 Luna dropped from $1.00/$6.00 to **$0.20/$1.20** (80% cheaper). Sol pricing unchanged. New page **[Advancing the price-performance frontier with GPT‑5.6](../../pages/openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/index.md)** is the announcement, explicitly framed as "passing on" the efficiency gains described in yesterday's GPT‑5.6-optimizes-itself post. Customer quotes from Replit, Notion, Ramp, Blitzy, Cognition, and Dust included.
  - The `/index/gpt-5-6/` launch post itself picked up a dated "Update on July 30" banner pointing to the new price-performance post.
- **Also new July 29, surfaced via `/products/release-notes/`:** GA release of the **official OpenAI Terraform provider** for the API Platform (projects, users, groups, roles, service accounts, rate limits as infrastructure-as-code), linking to `github.com/openai/terraform-provider-openai` and the Terraform Registry.

Read together: this is a routine "ship efficiency gains as lower prices, retire the old name" cycle, immediately following the GPT‑5.6 self-optimization post from the prior run — a two-day narrative arc (model optimizes its own serving cost → OpenAI passes the savings to customers + renames the premium tier).

## 3. Notable additions (9 new URLs)

- **[Advancing the price-performance frontier with GPT‑5.6](../../pages/openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/index.md)** (Jul 30) — see §2.
- **[api-fast-mode](../../pages/openai.com/api-fast-mode/index.md)** (Jul 30) — new product page for the renamed Fast mode tier; replaces `/api-priority-processing/`.
- **[Advancing responsible AI across Europe](../../pages/openai.com/index/advancing-responsible-ai-across-europe/index.md)** (Jul 31) — Global Affairs post on OpenAI's alignment with the EU AI Act's General-Purpose AI Code of Practice and the Code of Practice on Transparency of AI-Generated Content, covering the Preparedness Framework, Frontier Governance Framework, Red Teaming Network, and work with the Frontier Model Forum / US CAISI / UK AISI. Companion to a new intake form (next item) as the EU AI Act "enters its next phase."
- **[form/eu-ai-act](../../pages/openai.com/form/eu-ai-act/index.md)** (new) — "Submit an EU AI Act inquiry" intake form for requesting model documentation or filing a Copyright-Chapter compliance complaint under the GPAI Code of Practice. New legal/compliance infrastructure paired with the post above.
- **[How avatarin built a 24/7 retail agent with GPT‑Realtime](../../pages/openai.com/index/avatarin/index.md)** (Jul 30) — customer story: Japanese startup avatarin used GPT‑Realtime to give Yamada Denki (electronics retailer) multilingual, 24/7 shopping support; cites 30,000 shoppers engaged in a two-week public trial with 92% positive post-use survey responses.
- **[Univé builds an AI-ready workforce](../../pages/openai.com/index/unive/index.md)** (Jul 31) — customer story: Dutch mid-market insurer Univé on ChatGPT Enterprise rollout — 97% of licenses activated, 85% weekly active users, ~1,500 employee-built custom GPTs, and pet-insurance claims now prepared in minutes instead of hours.
- **[business/plugins/adobe](../../pages/openai.com/business/plugins/adobe/index.md)** (Jul 30) — replaces `/business/plugins/adobe-photoshop/` (see §4 for the rebrand context, first spotted via content diff on 2026-07-30 and now confirmed as a URL-level rename).
- **[business/partners/booz-allen-hamilton](../../pages/openai.com/business/partners/booz-allen-hamilton/index.md)** — new Select-tier partner listing (government/defense-focused technology and AI consultancy, 20,000+ technologists).
- **[business/partners/mantel](../../pages/openai.com/business/partners/mantel/index.md)** — new Select-tier partner listing (Australia/NZ enterprise AI consultancy, 850+ experts, engages 60%+ of ASX Top 200).

## 4. Notable updates

- **`/security-and-privacy/`** reworded its compliance-portal pointer and added a second link: **"View product compliance status"** → `/product-compliance-status/` (not yet in the sitemap — see anomalies note).
- **`/business/solutions/finance/`** picked up the ongoing "Business" nav-variant rollout (see below) plus a new callout linking to **"Finance workflows"** → `/business/solutions/finance/workflows/` (also not yet in the sitemap).
- **`/business/why-openai/small-business/`** hub had a substantive refresh: swapped its lead testimonial (The Floral Hire), replaced its webinar lineup (dropped a past July 30 sales webinar, added an August 25 "OpenAI on OpenAI: How Our Marketing Team Uses ChatGPT Work" session), and rebuilt its "Learn how teams are using AI today" section into a new "Resources" block linking a downloadable "First AI Workflow" PDF guide and the "How AI is expanding what people do at work" research post, replacing three older customer-story tiles (Neuro, Plex Coffee, Singular Bank) with a link to a new **[Small business stories](https://openai.com/index/small-business-stories/)** hub (not yet in the sitemap either — a small pattern of "hub pages exist and are linked before they're indexed").
- **`/business/customer-stories/`** and **`/business/partners/`** listing pages both grew to surface today's new customer stories (avatarin, Univé) and partner listings (Booz Allen Hamilton, Mantel); two older stories (Notion, Endava) rolled off the visible listing (pages remain live, just no longer linked from this widget).
- **Sitewide "Latest Advancements" sidebar module** (appears on most `/index/*` posts) now lists **GPT‑5.6** in place of **GPT‑5.3 Instant** — a template-level content change touching every article page that includes this module, not per-page editorial activity.
- **Sitewide article table-of-contents template tweak:** many `/index/*` pages (e.g., `balyasny-asset-management`, `promega`, `virgin-atlantic`, `bbva`, `netomi`) had their in-page ToC rendering change slightly — the redundant "Table of contents" label was dropped and bullet-list spacing tightened; on pages with H3-level subsections (e.g., `balyasny-asset-management`) the ToC now also lists numbered sub-headings that were previously omitted. Reads as a frontend/template change rather than content editing, since it applies uniformly across unrelated pages with no wording changes.
- **`/api-priority-processing/` → `/api-fast-mode/`, `/api-reserved-tier/`, `/api-scale-tier/`, `/api/`:** see §2.
- **`/products/release-notes/`:** see §2 (two new GA entries; also dropped six older entries that scrolled off the visible list — content remains in git history).
- **`/policies/uk-online-safety-act/`:** trivial copy-edit — a straight apostrophe was replaced with a curly apostrophe in "isn't." No substantive change.
- **`/student-collective/`:** added "500 characters max" helper text under two open-ended application questions — minor form-UX polish, no scope change.

### Continuing nav A/B test (not a new anomaly — same pattern flagged 2026-07-28)

The "Business" nav variant ("Why OpenAI / Solutions / Resources / Customers / Pricing") continues to flip in both directions on individual `/business/plugins/*` and `/business/partners/*` pages rather than settling:
- Reverted **new → old** nav this run: `bain-and-company`, `cognizant`, `dentsu-japan`, `fujitsu`, `slalom`, `business/plugins/cloudinary` (6 pages).
- Flipped **old → new** nav this run: `cdw`, `fellow-intelligence`, `hcltech`, `business/plugins/salesforce`, `business/plugins/creative-production`, `business/plugins/netlify`, `business/plugins/spaceship` (7 pages).

Net effect is a wash (13 pages flipped, split roughly evenly), consistent with live A/B testing/feature-flagging rather than a directional rollout — same conclusion as the 07-28 run, now with a third data point.

## 5. Routine updates

- **93 pages** fetched fresh but came back byte-identical to their prior snapshot — pure republish/cache-resync with zero visible change (full list in the accompanying `diff.json`).
- **~55 partner-directory pages** (`/business/partners/*`) picked up only the nav-variant flip and/or a "Keep reading"/case-study carousel image rotation surfacing today's new customer stories — no prose changes.
- **6 `/index/*` article pages** (`cisco`, `deutsche-telekom`, `doppel`, `nvidia`, `netomi`, `trustbank`) changed only their "Keep reading" carousel to surface `advancing-responsible-ai-across-europe`, `unive`, and `advancing-the-price-performance-frontier-with-gpt-5-6` — zero prose changes.
- **Homepage (`/`)** rotated its "Company announcements" feed to add the new price-performance post and drop the (now dated) confidential-S-1-filing card from June.
- **`/news/company-announcements/`** and `/index/previewing-gpt-5-6-sol/`** similarly rotated feed/carousel widgets to surface new posts.

## 6. Removals

- **`/api-priority-processing/`** — superseded by `/api-fast-mode/` (rename, see §2). Last snapshot: `git log -- pages/openai.com/api-priority-processing/index.md`.
- **`/business/plugins/adobe-photoshop/`** — superseded by `/business/plugins/adobe/`; the underlying content rebrand (Photoshop-only → full Adobe suite) was first observed on 2026-07-30 as a content diff at the old URL, and this run confirms it as a full URL-level move. Last snapshot in git history at the old path.

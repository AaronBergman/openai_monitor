# Run 2026-08-01T09-16Z — Analysis

Fetch time (UTC): 2026-08-01T09:17:39Z
Baseline: 2026-07-31T09-16Z
Sub-sitemaps: 35 (was 34; `sitemap.xml_disrupting-malicious-uses` is new)
URLs: 1546 total (was 1499) — 47 added, 0 removed, 93 updated, 4 migrated between sub-sitemaps

## Anomalies (highest signal first)

### 1. A hidden archive of 44 threat-intel takedown reports surfaced in the sitemap for the first time

A brand-new sub-sitemap, `sitemap.xml/disrupting-malicious-uses/`, appeared today. It contains 44
URLs of the form `/index/disrupting-malicious-uses-of-ai-<codename>/` — OpenAI's recurring
"influence operations / malicious use disrupted" reports (e.g. "Storm-2035", "Bad Grammar",
"Doppelganger", "Spamouflage", "Zero Zeno", "Nine Emdash Line").

These are **not new reports**. Spot-checking page bodies shows genuine historical publish dates —
e.g. `disrupting-malicious-uses-of-ai-storm-2035-2024` is dated October 1, 2024, and
`disrupting-malicious-uses-of-ai-bad-grammar` covers a Russian-linked Telegram operation from
early 2024. The content already existed on openai.com; it simply had **no sitemap entry at all**
until now, so it was invisible to this monitor.

All 44 share a near-identical `<lastmod>` cluster: 42 of them fall between
2026-07-31T16:31:19Z and 2026-07-31T16:32:33Z (about 74 seconds), one more at 2026-07-31T20:27:39Z,
plus 2 unrelated pages published July 31 – Aug 1 that happened to land in the same "added" batch
(`business/partners/clarinet/`, `index/building-abundant-intelligence/`, `index/ten-advances-in-mathematics/` —
see below). The tight clustering is the signature of a single backend migration/re-platforming
event (e.g., these reports being moved into a dedicated content type), not 44 independent edits.
This closely resembles the "sitemap taxonomy reorg" already logged on 2026-07-25 (#82, 122
anomalies) — OpenAI appears to be incrementally re-organizing its content taxonomy, and each
reorg pass exposes previously-untracked archive pages to sitemap-based monitoring.

**Practical effect on this repo:** these 44 URLs are recorded as "added" today with
`first_seen = 2026-08-01`, but that reflects when *we* first saw them in a sitemap, not when they
were published. Do not read "added" as "new content" for this batch.

### 2. Global Affairs category split (sub-sitemap migration, no content change)

4 URLs moved from `sitemap.xml/global-affairs/` to a new `sitemap.xml/global-affairs-news-listed/`
sub-sitemap, with **no `<lastmod>` change**, meaning it's a pure taxonomy re-file rather than a
content edit:

- `https://openai.com/global-affairs/new-economic-analysis/`
- `https://openai.com/index/equipping-workers-with-insights-about-compensation/`
- `https://openai.com/index/how-countries-can-end-the-capability-overhang/`
- `https://openai.com/index/understanding-ai-and-learning-outcomes/`

Likely a split between "news-style" Global Affairs posts and op-ed/analysis posts.

### 3. Bookkeeping gap in state/known_urls.json (repo hygiene, not a site change)

47 URLs already present in the previously-committed sitemap baseline had never been recorded in
`state/known_urls.json` (44 of them are the disrupting-malicious-uses batch above; 3 were reachable
elsewhere). Backfilled today with `first_seen = 2026-08-01T09-16Z` — treat that date as "first time
this monitor recorded it," not a claim about when it actually appeared on the site. No lastmod-based
anomalies (no future-dated timestamps, no backward-moving lastmods, no disappear/reappear
patterns) were found among the remaining 1499 previously-tracked URLs.

## Significant updates

**Content verification tool expanded from images to audio, and promoted out of "Research preview"**
(`research/verify/`): The tool was "Verify OpenAI-generated images" (Research preview) supporting
PNG/JPG/WEBP and C2PA-metadata detection only. It's now "Verify OpenAI-generated content", drops the
"Research preview" label, adds audio support (MP3, WAV, AAC, FLAC, OPUS, PCM), and now also detects
**SynthID watermarks** in addition to C2PA metadata. This lines up with a same-day update note added
to `index/introducing-gpt-live/`: *"Update July 31, 2026: Supported audio generated with GPT-Live
through ChatGPT Voice and the OpenAI API now includes SynthID watermarking."* Together these read as
a coordinated rollout: GPT-Live-generated audio now carries a detectable watermark, and the public
verification tool was updated same-day to check for it.

**New "Sponsored Agents" ad product, defined in the Ad Tools Terms** (`policies/ad-tools-terms/`,
republished July 31, 2026, was last published June 12, 2026): a new Section 4 states that when
"OpenAI creates, configures, or makes available a Sponsored Agent on your behalf," the advertiser is
deemed the builder of that agent under the GPT-builder terms and is responsible for its content,
configuration, and outputs. A new definition was added: *"Sponsored Agent" means advertiser-sponsored
conversational experiences that allow users to interact with an AI-generated representative for an
Advertiser's business, products, or services.* This is the clearest signal yet that OpenAI is building
branded, advertiser-sponsored chatbot personas into its ads product. Companion update: 
`policies/ad-tools-subprocessors/` added a new subprocessor, Teleperformance Europe Middle East and
Africa SAS (Canada/Spain, Customer Support), same day.

**New partner network feature: "Joint partners" cross-referencing** (`business/partners/*`): ~30 of
OpenAI's consulting/SI partner pages (Accenture, KPMG, Capgemini, EY, BCG, Infosys, etc.) gained a new
"Joint partners" field naming which cloud hyperscaler(s) — AWS and/or Oracle — that partner is also
certified with. Rolled out in the same deployment (`dpl_2nDwFBphwWZQZcYgWgpfCWCFJgWW`) that added a
new partner, **Clarinet** (an AI-enablement/training firm, Select tier, global/cross-industry) — see
New pages below.

## Routine updates

- `index/how-two-settings-tripled-our-arc-agi-3-scores/`, `index/australian-payments-plus/`,
  `index/avatarin/`, `index/deutsche-telekom/`, `index/how-news-organizations-are-using-ai/`,
  `index/scientific-computing-agentic-ai/`, `index/unive/` — only their "Keep reading" / related-articles
  sidebar changed, reflecting newly published posts (Ten advances in mathematics, Building abundant
  intelligence, Advancing responsible AI across Europe). No change to the articles' own content.
- `business/solutions/sales/` — swapped a "Live webinar, July 30 9:30am PT — Register now" banner for
  a post-event "Watch the webinar" link now that the webinar has happened.
- `gpt-rosalind/`, `index/advancing-content-provenance/`, `student-collective/` — minor nav-link /
  wording tweaks (conflict-of-interest clause reworded on the Student Collective / Campus Leads
  application; nothing substantive).
- 19 pages (including the homepage `/`, `api/`, `api/pricing/`, `business/pricing/`, `devday/`,
  `science/`, `products/release-notes/`, several `gpt-5-6`-related pages) show a `<lastmod>` bump with
  **zero markdown content difference** — consistent with a platform-wide redeploy on 2026-07-31 that
  touched build/cache metadata without changing rendered content.
- ~27 of the ~57 partner detail pages show only a partner-tier badge image URL cache-bust
  (`?dpl=...` query param change) with no other diff — same deployment as the Joint-partners rollout
  above, just partners that didn't get the new field.
- A handful of partner pages (e.g. `altimetrik/`, `bain-and-company/`) show a swapped top-nav variant
  between two fetches (old-style vs. new-style global nav) — this looks like server-side A/B
  nav-variant randomization rather than a real content change, and was excluded from the counts above.

## New pages

- **[Ten advances in mathematics and theoretical computer science](../../pages/openai.com/index/ten-advances-in-mathematics/index.md)**
  (Aug 1, 2026, Publication) — links out to a paper PDF ("ten-proofs-oai.pdf") and a "reasoning
  walkthroughs" PDF. Article body is client-side-rendered and wasn't captured in the static fetch
  (page shows "Loading…" — a known limitation of this tool, not a fetch failure); title/date/links
  were captured. Fits with the recent research/model post cadence (ARC-AGI-3, GPT-5.6).
- **[Building abundant intelligence](../../pages/openai.com/index/building-abundant-intelligence/index.md)**
  (Jul 31, 2026, Company) — subtitle: "A full-stack approach to making advanced AI more capable, more
  affordable, and more widely useful." Reads as a company strategy/vision post. Body not captured
  (client-rendered); title/date/subtitle captured.
- **[Clarinet — new OpenAI partner](../../pages/openai.com/business/partners/clarinet/index.md)**
  (Aug 1, 2026) — Select-tier partner, AI-enablement/training firm, global/cross-industry, "worked
  with more than 85 organizations." Added same-day as the Joint-partners rollout above.
- 44 historical `disrupting-malicious-uses-of-ai-*` reports — see Anomaly #1. Full list in `diff.json`.

## Removals

None this run.

## Fetch notes

139/140 page fetches succeeded on first attempt; `business/partners/fujitsu/` hit a transient
`curl_cffi` SSL/connection-reset error and succeeded on an immediate retry within the same run. No
pages were Cloudflare-blocked.

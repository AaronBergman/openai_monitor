# openai.com sitemap monitor — analysis for run 2026-09-11T09-15Z

Fetch time (this run): 2026-09-11T09:16Z (UTC). Baseline: prior run `2026-09-10T09-17Z` (PR #129, merged same day).

Sitemap index: 38 sub-sitemaps (up from 36 two runs ago / 38 as of yesterday — two new sections `plugins-education` and `plugins-operations` appeared *within* yesterday's Apps→Plugins rename but weren't separately called out; today's crawl is the first to see all 38 populated). Total unique URLs across all sections: 1,697 (up from 1,685).

Diff stats: **13 added, 311 lastmod-updated (254 with an actual content diff, 57 lastmod-only/no visible content change), 1 removed, 6 section migrations, 1 low-severity anomaly, 0 fetch failures** (324/324 page fetches succeeded via curl-cffi Chrome impersonation).

## Anomalies

Only one flagged item, and it's benign:

- **`removed_url`** — `https://openai.com/devday/` disappeared from the sitemap (known since 2026-05-07, last lastmod 2026-09-07). This is a URL restructuring, not a deletion of content: a new page `https://openai.com/devday/2025/` appeared today as a retrospective/archive of last year's event ("OpenAI DevDay 2025"), with a link out to `devday.openai.com` for "OpenAI DevDay 2026". No future-dated or backwards-moving `<lastmod>` values were found anywhere in the 1,697-URL set, and no backdated new URLs or true reappearances were detected.

## Site-wide footer/nav noise (explains most of the 311 "updated" count)

A global site component changed today: the "Latest Advancements" footer list (present on nearly every page) gained a new entry, **GPT-6**, linking to `/index/gpt-6-astra/`, ahead of GPT-5.6. Because this component is part of the rendered HTML of almost every page, it alone accounts for a large fraction of the 254 pages with a real (but trivial) content diff — visible as a single `+  * [GPT-6](</index/gpt-6-astra/>)` line. Similarly, many pages' "Keep reading" article carousels reshuffled to surface newer articles (Financial Services launch, Data agent, antimicrobials story) — this is expected, cosmetic, and was excluded from the "significant updates" list below. The 57 pages whose `<lastmod>` changed with zero visible content diff are most likely re-renders triggered by this same shared-component change where html2text happened to normalize to byte-identical output.

## Significant updates

### A financial-services product launch (major, multi-page, coordinated)
OpenAI announced **"Introducing ChatGPT for Financial Services"** (new page, Sep 10) — a vertical product positioning GPT-6 Astra for financial analysis, backed by:
- A new sales-contact page: `/business/contact-sales-financial-services/`
- A new legal terms page: `/policies/financial-services-terms/`
- A new **Section 13 ("Financial Plugins and ChatGPT for Financial Services")** added to `/policies/service-terms/` — a liability disclaimer clarifying that financial plugin output is "for informational purposes only," not investment advice, and pointing to the new Financial Services Terms.
- `/business/solutions/data/` was substantially rewritten (160 insertions / 83 deletions): repositioned from "AI for your data team's most ambitious work" (data-team-only framing) to **"Data intelligence for every team's most ambitious work"** (broadened audience), with a big expansion of the connected-plugin ecosystem list (added AWS Data Analytics, Sigma, Datadog Experiments, and others) and new CTAs ("Install data agent", link to the new `/index/put-data-to-work/` announcement).
- New companion announcement: **"Now everyone can put data to work"** (`/index/put-data-to-work/`) — introduces a new "Data agent" for ChatGPT Work that turns natural-language questions into dashboards/reports across a connected data stack.

This reads as a single coordinated go-to-market push spanning a new industry vertical (financial services) and a broadened "Data" product pitch, both dated Sep 10.

### New enterprise/data plugins
Three new plugin listing pages appeared, all tagged "Data & Research" and all cross-linked from the rewritten `/business/solutions/data/` page:
- `/business/plugins/aws-data-analytics/` — AWS Glue/Athena/S3 Tables/Redshift/Snowflake/BigQuery/DynamoDB connectivity, made by Amazon Web Services.
- `/business/plugins/sigma/` — Sigma Computing's BI/dashboarding tool.
- `/business/plugins/datadog-experiments/` — Datadog experimentation platform.

Six existing plugin pages were **re-categorized** (section migrations, not content changes — see diff.json `section_migrations`): `amplitude` moved productivity→data-research; `conductor`, `g2`, `highlevel`, `mailchimp` moved productivity→operations; `openai-certified` moved data-research→education. This looks like an ongoing refinement of yesterday's Apps→Plugins category taxonomy rather than a new event.

### New API products
- **"Introducing the Agents API"** (`/index/introducing-the-agents-api/`, Sep 10) — a fully-managed cloud-agent API built on the Codex harness, with OpenAI-hosted sandboxes, long-running session support, and subagent parallelization. Positioned as "build cloud agents with a single API call."
- **"Build more natural voice experiences with GPT‑Live‑1 in the API"** (`/index/introducing-gpt-live-1-in-the-api/`, Sep 10) — brings the full-duplex, listen-while-speaking voice model first shown in ChatGPT (`/index/introducing-gpt-live/`) to the developer API.

### US government access expansion
**"Expanding AI access and cyber defense for federal, state, local, and tribal governments"** (`/index/expanding-ai-access-us-government/`, Sep 10) — a new multi-year agreement between OpenAI for Government and the GSA: $0 license fee (normally $15/user/month) and 50% off usage for federal, state, local, and tribal government employees, plus expanded support for public-sector cyber defenders. Extends the offer to an estimated 23 million public-sector workers. Backed by a new lead-gen page `/form/openai-for-government/` and a new "Government" industry-solutions page that was already tracked but updated.

### Privacy-policy refresh across multiple jurisdictions (legal/compliance, same day)
On Sep 10, OpenAI pushed coordinated updates to several privacy policies (`kr-privacy-policy`, `communications-privacy-policy`, `us-privacy-policy`, plus `cookie-policy`, `ad-policies`, and `service-terms`):
- **Removed the "Additional U.S. state disclosures" section** from the Korea privacy policy and the general "communications" privacy policy (it correctly remains in the US-specific policy) — cleanup of US-specific boilerplate that didn't belong in non-US policies.
- **Trimmed Atlas-browser-specific language**: removed mentions of "Atlas incognito browsing history" and Atlas-specific data controls from the US and Korea policies, replacing with generic "in-app browser" phrasing.
- **Trimmed Sora-specific language**: removed references to sharing "Sora videos" and "Sora characters" from the content-sharing sections of the US and Korea policies (the underlying data-collection bullet for Sora characters as User Content remains in the Korea policy, just consolidated).
- Renamed "Saved Memories" → "Memories" throughout (branding consistency).
- Reworded the ads-data-collection description to be more direct ("We receive information..." instead of "We may receive...").
- `cookie-policy` added new cookie-table rows: two first-party OpenAI cookies (`oai-form-submissions`, 180 days; `__oailb`, 1 hour — likely a load-balancer cookie) and **nine new Snapchat marketing-measurement cookies** on chatgpt.com (`ScCid`, `_scid`, `_scid_r`, `_sctr`, `sc_at`, `u_sclid`, `u_sclid_r`, `u_scsid`, `u_scsid_r`) — indicates OpenAI has added Snapchat as an ad-measurement/conversion-tracking partner, joining existing partners like Bing.
- `ad-policies` bumped to v1.6: added explicit language that "OpenAI reserves the right to decline, restrict, or remove advertisers... where they conflict with our advertising principles, business interests, or competitive position" — a policy tightening giving OpenAI broader discretion over who can advertise.

Net effect: this looks like a routine but coordinated quarterly-style legal cleanup pass (removing stale Atlas/Sora references as those product surfaces evolve) bundled with real new disclosures (financial services terms, expanded ad-partner and ad-discretion language).

### New research/applied-AI story
**"How a researcher uses Codex and ChatGPT to search for new antimicrobial molecules"** (`/index/using-codex-chatgpt-to-search-for-new-antimicrobials/`, Sep 10) — profile of bioengineer César de la Fuente's lab using AI to mine genomic "dark matter" for novel antimicrobial candidates, framed against a ~5M annual death toll from drug-resistant infections. Fits OpenAI's recurring "AI for science" applied-AI content series.

## Routine/noise updates (not itemized individually)

- ~250 pages picked up the site-wide "GPT-6" footer-nav link and/or a reshuffled "Keep reading" carousel (see above) — cosmetic only.
- `/index/introducing-4o-image-generation/` (the March-2025-era announcement page) showed a 1,293-line diff, but on inspection this is **not a real content change** — it's the same image-example gallery items re-rendered in a different DOM order by a client-side carousel, a known noise pattern for this page. The one substantive change is a single link bump: "ChatGPT Images 2.0" → "ChatGPT Images 2.5" (pointing to a product page from an earlier run).
- `/news/`, `/news/product-releases/`, `/business/customer-stories/`, and similar index/listing pages picked up the day's new articles in their listings — expected, not itemized per-page.

## New pages (full list, 13)

| URL | Category (inferred) |
|---|---|
| `/index/introducing-chatgpt-financial-services/` | Product — Financial Services launch |
| `/business/contact-sales-financial-services/` | Sales contact — Financial Services |
| `/policies/financial-services-terms/` | Legal — Financial Services |
| `/index/put-data-to-work/` | Product — Data agent |
| `/index/introducing-the-agents-api/` | Product — Agents API |
| `/index/introducing-gpt-live-1-in-the-api/` | Product — GPT-Live-1 API |
| `/index/expanding-ai-access-us-government/` | Global Affairs — Government access |
| `/form/openai-for-government/` | Lead-gen form — Government |
| `/index/using-codex-chatgpt-to-search-for-new-antimicrobials/` | Applied AI — research story |
| `/business/plugins/aws-data-analytics/` | Plugin — Data & Research |
| `/business/plugins/sigma/` | Plugin — Data & Research |
| `/business/plugins/datadog-experiments/` | Plugin — Data & Research |
| `/devday/2025/` | Archive page (replaces removed `/devday/`) |

## Removals (1)

- `https://openai.com/devday/` — superseded by `/devday/2025/` (archive) as OpenAI shifts the bare `/devday/` URL toward next year's event, hosted externally at `devday.openai.com`. Last snapshot preserved in git history (`git log -- pages/openai.com/devday/index.md`).

## Section migrations (6, not counted as adds/removes)

| URL | Old section | New section |
|---|---|---|
| `/business/plugins/amplitude/` | plugins-productivity | plugins-data-research |
| `/business/plugins/conductor/` | plugins-productivity | plugins-operations |
| `/business/plugins/g2/` | plugins-productivity | plugins-operations |
| `/business/plugins/highlevel/` | plugins-productivity | plugins-operations |
| `/business/plugins/mailchimp/` | plugins-productivity | plugins-operations |
| `/business/plugins/openai-certified/` | plugins-data-research | plugins-education |

## Fetch failures

None. All 324 added/updated pages fetched and converted successfully on the first attempt.

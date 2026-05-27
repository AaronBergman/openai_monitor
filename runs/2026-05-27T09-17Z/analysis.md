# Run Analysis: 2026-05-27T09-17Z

**Fetch time:** 2026-05-27T09:17:36.616191Z
**Total URLs in sitemap:** 1,324
**True changes vs yesterday (2026-05-26T09-16Z):** 206 lastmod bumps, 1 removal, 0 additions
**Fetch failures:** 2 (`deployco/` and `deployco/privacy-policy/`)

> **Note on inflated "updated" count:** The automated script reported 746 updated URLs
> because the prior `latest/` directory contained duplicate sub-sitemap files from
> multiple naming conventions (5 variants × 32 sitemaps = 160 files), some dating to
> May 23. The correct comparison is against `state/known_urls.json`, which shows
> **206 URLs** with changed lastmods since yesterday's run.

---

## Anomalies

None detected.

**Continuing anomaly (day 8):** `https://openai.com/deployco/` now has an updated
lastmod (`2026-05-27T08:02:56.608Z`) and the URL was attempted to be fetched —
but the curl-cffi request returned an HTTP error (non-200). The sibling URL
`deployco/privacy-policy/` also failed. DeployCo (OpenAI's AI deployment subsidiary)
is publishing timestamps for both URLs into the sitemap daily, but neither page
is currently serving content. This strongly suggests active staging/pipeline work,
not accidental sitemap inclusion.

---

## Significant Content Changes

### 1. Ad Policies Expanded: Financial Services, Healthcare, Legal Now Allowed
**URL:** `https://openai.com/policies/ad-policies/`
**lastmod:** `2026-05-01T10:31:33.280Z` → `2026-05-27T09:15:18.582Z`
**Date stamp on page:** "Updated: May 22, 2026" → "Updated: May 26, 2026"

The most substantive change of this run. Section 2 ("Ad content policy") added the
following sentence:

> "We may approve ads from approved advertisers within the financial services,
> healthcare & medicine, and legal services categories. These categories are being
> rolled out gradually with approvals being reviewed manually on a case-by-case basis."

This is a significant expansion. The prior policy listed financial services, healthcare,
and legal as **explicitly disallowed** at launch ("All other categories are disallowed
at launch, including ads that violate OpenAI's usage policies and those related to
sensitive or regulated areas such as... healthcare, financial or legal services...").
The new language carves out a selective exception: these categories can now appear
in ChatGPT advertising, but only for **approved advertisers** through a manual review
process. This implies OpenAI is moving ChatGPT advertising beyond consumer/lifestyle
verticals into regulated professional services.

---

## Routine Content Updates

### 2. "Keep Reading" / Related Content Carousels Updated (Many Pages)
Dozens of customer story pages, product pages, and index pages had their "Keep reading"
/ "Related content" sidebar updated to rotate in newer posts and rotate out older ones.
The pattern is consistent across many pages:
- **Removed from sidebars:** Malta partnership (May 16), "Ramp engineers code review" (May 20),
  "OpenAI launches Deployment Company" (May 11), "What Parameter Golf taught us" (May 12)
- **Added to sidebars:** Virgin Atlantic + Codex story (May 22), Grupo Folha/UOL partnership
  (May 25), Gartner Magic Quadrant Leader (May 22), Dell Technologies Codex partnership (May 18)

This is a CMS-driven content refresh: as new articles are published, older "related content"
links are automatically replaced with more recent ones. Affects ~50+ pages including
cisco, adventhealth, bny, choco, cisco, ramp, healthify, lifespan, philips, whoop, oscar,
paradigm, summer-health, waymark, genmab, color-health, and many others.

### 3. News Index and Category Pages Updated
The main news pages (`/news/`, `/news/ai-adoption/`, `/news/company-announcements/`,
`/news/engineering/`, etc.) show rotated featured articles:
- Added: Gartner MQ recognition, geometry conjecture disproof, content provenance,
  Dell/Codex partnership
- Removed: "What Parameter Golf taught us" (May 12)

### 4. ChatGPT Futures Class of 2026 Page Minor Update
**URL:** `https://openai.com/index/introducing-chatgpt-futures-class-of-2026/`
Related content sidebar updated (OpenAI Deployment Company link → Dell Technologies Codex link).
No change to core content.

---

## Removed Pages

### `https://openai.com/policies/plugin-terms/`
Plugin Terms policy page removed. This was first noted in the 2026-05-26 run analysis.
The stale baseline files (from May 23, with old naming conventions) still referenced this
URL, causing it to show up again today as "removed." The removal actually happened
between the May 23 and May 26 snapshots. ChatGPT Plugins were deprecated in early 2024;
this is the final cleanup of the associated legal infrastructure.

---

## Fetch Failures

- `https://openai.com/deployco/` — HTTP error (non-200). Page not yet live.
- `https://openai.com/deployco/privacy-policy/` — HTTP error (non-200). Page not yet live.

Both DeployCo URLs are in the sitemap with fresh timestamps but return errors when fetched.
This is the 8th consecutive day of tracking this anomaly.

---

## Date Distribution of lastmod Changes

| Wave Date | # URLs | Interpretation |
|---|---|---|
| 2026-05-27 (today) | 157 | Large CMS deploy touching research, news indexes, customer stories, and policy pages |
| 2026-05-26 (yesterday) | 49 | Overnight batch: customer stories (bny, cisco, uber), business pages |

---

## Summary for README

The headline change today is a **significant expansion of OpenAI's ChatGPT advertising policy**: financial services, healthcare & medicine, and legal services advertisers can now be manually approved to run ads in ChatGPT — categories that were previously explicitly prohibited. This represents a careful but meaningful expansion of ChatGPT's ad business into regulated professional verticals. Beyond that, a large CMS sweep (157 pages) refreshed "related content" sidebars across research, customer story, and product pages to surface newer articles.

# Run Analysis: 2026-06-21T09-15Z

**Fetch time:** 2026-06-21T09:16:55Z  
**Baseline:** 2026-06-19T09-15Z  
**Sub-sitemaps fetched:** 34  
**Total URLs in current sitemap:** 1,357  
**Diff:** +0 added, ~122 updated, -0 removed  
**Anomalies:** 0  
**Fetch failures:** 0

---

## Anomalies

None detected. No future-dated `<lastmod>` values, no backwards-moving `<lastmod>`, no URLs disappearing and reappearing.

---

## Significant Updates

### 1. CMS Template Change — Table of Contents Reordering (62+ pages, batch ~2026-06-19T14:16 UTC)

The single largest event is a **CMS template update** that touched at least 62 pages simultaneously around 14:16 UTC on June 19. The structural change:

- **Before:** Pages rendered with just an inline TOC list; the article date, category tags, and title appeared below the TOC.
- **After:** Pages now show date/category/title at the top, then the inline TOC, then the body content — AND a second, explicitly labeled "Table of contents" block also appears. This is a duplicate TOC, likely caused by the CMS now rendering a sidebar TOC in-line alongside the existing in-page TOC.

The **substantive content of all affected pages is unchanged**. This is a cosmetic template/layout change in OpenAI's CMS (likely Contentful). Representative affected pages include:

- [`/index/equip-responses-api-computer-environment/`](../../pages/openai.com/index/equip-responses-api-computer-environment/index.md)
- [`/index/democratic-inputs-to-ai/`](../../pages/openai.com/index/democratic-inputs-to-ai/index.md)
- [`/index/unrolling-the-codex-agent-loop/`](../../pages/openai.com/index/unrolling-the-codex-agent-loop/index.md)
- [`/index/sharing-the-latest-model-spec/`](../../pages/openai.com/index/sharing-the-latest-model-spec/index.md)
- [`/index/emergent-tool-use/`](../../pages/openai.com/index/emergent-tool-use/index.md)
- [`/index/openai-support-model/`](../../pages/openai.com/index/openai-support-model/index.md)
- [`/index/computer-using-agent/`](../../pages/openai.com/index/computer-using-agent/index.md)
- [`/index/introducing-operator/`](../../pages/openai.com/index/introducing-operator/index.md)
- [`/index/introducing-the-stateful-runtime-environment-for-agents-in-amazon-bedrock/`](../../pages/openai.com/index/introducing-the-stateful-runtime-environment-for-agents-in-amazon-bedrock/index.md)

...and approximately 53 more.

### 2. "Keep Reading" Widget Rotation (many pages)

The three "Keep reading" cards at the bottom of most article/index pages rotated to reflect newer content. The slot changed from:

| Before (Jun 17 articles) | After (Jun 18 articles) |
|---|---|
| A near-autonomous AI chemist improves a challenging reaction | New usage analytics and updated spend controls for enterprises |
| Introducing LifeSciBench | Improving health intelligence in ChatGPT |
| Predicting model behavior before release by simulating deployment | Using AI to help physicians diagnose rare childhood diseases |

This is an automatic CMS update — the widget always shows the 3 most recent items. The newly surfaced Jun 18 articles are:
- [`/index/chatgpt-enterprise-spend-controls/`](../../pages/openai.com/index/chatgpt-enterprise-spend-controls/index.md) — Enterprise spend controls and usage analytics
- [`/index/improving-health-intelligence-in-chatgpt/`](../../pages/openai.com/index/improving-health-intelligence-in-chatgpt/index.md) — Health intelligence features in ChatGPT
- [`/index/diagnose-rare-childhood-diseases/`](../../pages/openai.com/index/diagnose-rare-childhood-diseases/index.md) — AI-assisted rare childhood disease diagnosis

### 3. Heading Level Fix in Codex Engineering Post

[`/index/unrolling-the-codex-agent-loop/`](../../pages/openai.com/index/unrolling-the-codex-agent-loop/index.md) had two section headings corrected from H4 (`####`) to H3 (`###`):
- "Building the initial prompt"
- "The first turn"

This is a minor editorial/formatting fix in the Codex agent loop engineering post.

---

## Routine Updates (lastmod changed, content unchanged)

Many pages showed `<lastmod>` bumps with **no detectable change in rendered content**, suggesting backend/CMS metadata revalidation. Notable examples:

| Page | Old lastmod | New lastmod | Inferred reason |
|------|-------------|-------------|-----------------|
| `/products/release-notes/` | 2026-06-19T06:50 | 2026-06-21T09:07 | CMS cache/CDN revalidation |
| `/policies/commerce-policies/` | 2026-06-19T03:56 | 2026-06-21T07:34 | Backend metadata update |
| `/index/gpt-5-safe-completions/` | 2026-06-18T10:58 | 2026-06-21T05:06 | Same |
| `/index/introducing-life-sci-bench/` | 2026-06-18T20:06 | 2026-06-21T05:06 | Same |
| `/index/introducing-new-capabilities-to-gpt-rosalind/` | 2026-06-18T14:22 | 2026-06-21T05:06 | Keep reading widget (see §2) |
| `/index/deployment-simulation/` | 2026-06-19T03:51 | 2026-06-21T04:57 | Same |
| `/index/diagnose-rare-childhood-diseases/` | 2026-06-18T17:38 | 2026-06-21T02:58 | Same |
| `/index/chatgpt-enterprise-spend-controls/` | 2026-06-19T07:40 | 2026-06-21T02:36 | Same |
| `/business/partners/` | 2026-06-19T07:19 | 2026-06-20T16:56 | Same |
| `/index/introducing-openai-partner-network/` | 2026-06-18T15:30 | 2026-06-20T16:32 | Same |
| `/startups/` | 2026-06-15T22:36 | 2026-06-20T11:19 | Same |
| `/daybreak/request-a-vulnerability-scan/` | 2026-06-15T00:06 | 2026-06-20T00:13 | Same |
| `/index/approach-to-data-and-ai/` | 2026-05-22T19:16 | 2026-06-19T15:55 | TOC template change (see §1) |

---

## New Pages

None.

## Removed Pages

None.

---

## Summary

This run is predominantly **infrastructure/CMS noise**: a template update that triggered mass `<lastmod>` bumps, plus an automatic "Keep reading" widget rotation. The one minor editorial change is a heading-level correction in an engineering post. No new content or product announcements were published since the June 19 baseline run.

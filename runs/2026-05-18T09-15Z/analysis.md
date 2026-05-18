# Analysis: 2026-05-18T09-15Z

**Fetch time:** 2026-05-18T09:16:52Z UTC
**Baseline:** 2026-05-17T09-15Z
**Total URLs (current):** 1,314
**Sub-sitemaps crawled:** 32

## Summary

| Metric | Count |
|--------|-------|
| Added | 0 |
| Removed | 0 |
| Updated (lastmod) | 36 |
| Anomalies | 0 |
| Fetch failures | 0 |

## Anomalies

None detected.

## Updated Pages

36 pages had `<lastmod>` changes vs. the 2026-05-17T09-15Z baseline. Breakdown by section:

| Section | Count |
|---------|-------|
| safety | 15 |
| page (news hubs) | 6 |
| security | 5 |
| product | 4 |
| global-affairs | 2 |
| research | 1 |
| release | 1 |
| company | 1 |
| engineering | 1 |

### Cluster 1: Teen/Child Safety Sweep (15 pages, ~08:33–34 UTC)

For the third consecutive day, the teen-safety content cluster received a simultaneous batch lastmod refresh. All 15 pages were touched within ~1 minute of each other (~08:33:51–08:34:57 UTC). Content diffs show no substantive changes — only "Keep reading" recommendation carousels rotated. This is consistent with an automated CMS republish.

Affected URLs:
- `https://openai.com/index/introducing-child-safety-blueprint/`
- `https://openai.com/index/introducing-the-teen-safety-blueprint/`
- `https://openai.com/index/teen-safety-policies-gpt-oss-safeguard/`
- `https://openai.com/index/updating-model-spec-with-teen-protections/`
- `https://openai.com/index/update-on-mental-health-related-work/`
- `https://openai.com/index/our-commitment-to-community-safety/`
- `https://openai.com/index/teen-safety-freedom-and-privacy/`
- `https://openai.com/index/building-more-helpful-chatgpt-experiences-for-everyone/`
- `https://openai.com/index/chatgpt-study-mode/`
- `https://openai.com/index/helping-people-when-they-need-it-most/`
- `https://openai.com/index/how-chatgpt-protects-privacy/`
- `https://openai.com/index/optimizing-chatgpt/`
- `https://openai.com/index/our-approach-to-age-prediction/`
- `https://openai.com/index/building-towards-age-prediction/`
- `https://openai.com/index/japan-teen-safety-blueprint/`

`ai-literacy-resources-for-teens-and-parents` also updated (08:15 UTC) — original Dec 2025 article contained a "Update from May 14" note about a new parent guide; today's bump shows no additional text.

### Cluster 2: Routine CMS Refresh (news hubs, product pages)

Six news/hub pages updated at ~08:33–34 UTC with no substantive content changes (carousel rotation):
- `https://openai.com/news/` (08:32)
- `https://openai.com/news/company-announcements/` (08:33)
- `https://openai.com/news/engineering/` (08:33)
- `https://openai.com/news/global-affairs/` (08:33)
- `https://openai.com/news/product-releases/` (08:34)
- `https://openai.com/news/safety-alignment/` (08:34)
- `https://openai.com/podcast/` (08:32)

Product pages touched:
- `https://openai.com/index/running-codex-safely/` (May 8 article about Codex sandboxing)
- `https://openai.com/index/work-with-codex-from-anywhere/` (May 14 article about Codex mobile)
- `https://openai.com/index/accelerating-science-gpt-5/` (science article)

### Substantive Update: GPT-5.5 "Keep Reading" Rotation

`https://openai.com/index/introducing-gpt-5-5/` — lastmod `2026-05-12T05:18Z` → `2026-05-17T14:19Z`

The "Keep reading" recommendation at the bottom of the GPT-5.5 page changed:
- **Removed:** "Testing ads in ChatGPT" (May 7, 2026)
- **Added:** "A new personal finance experience in ChatGPT" (May 15, 2026)

Main article content unchanged. This reflects normal editorial rotation as newer articles displace older recommendations.

### Notable: Prism lastmod Jump

`https://openai.com/index/introducing-prism/` — lastmod `2026-05-05T21:23Z` → `2026-05-18T08:05Z` (13-day gap)

Prism is OpenAI's free, AI-native scientific writing workspace (LaTeX-native, powered by GPT-5.2, built on the acquired Crixet platform). No visible text changes detected in rendered markdown. Possible causes: asset refresh, backend metadata update, or pre-staged content change not visible in rendered output.

### Security Posts Touched

- `https://openai.com/index/axios-developer-tool-compromise/` — lastmod `2026-05-16T09:25Z` → `2026-05-18T07:26Z`
- `https://openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack/` — lastmod `2026-05-16T09:25Z` → `2026-05-18T07:26Z`

Both touched at exactly the same time. No content change detected. The Axios post covers an npm supply chain incident involving the Axios developer tool (North Korea-linked, per Google Threat Intelligence). The TanStack post covers a similar npm supply chain attack on the TanStack package.

### Form Updates

- `https://openai.com/form/enterprise-trusted-access-for-cyber/` (lastmod `2026-05-17T09:40Z`) — Application form for vetted enterprise customers and cybersecurity practitioners seeking higher-risk dual-use cybersecurity capabilities. Requires organization ID, legal entity details, and government entity status disclosure. Described as a risk-mitigation measure enabling "higher-risk, higher-impact capabilities available to a broader community of defenders."

- `https://openai.com/form/codex-for-oss/` (lastmod `2026-05-17T09:39Z`) — Open-source maintainer access form. Selected maintainers receive 6 months ChatGPT Pro (includes Codex), conditional access to Codex Security, and API credits.

### Conversion Policy Refresh

Three advertising/measurement policy pages updated between 05:13–09:14 UTC. Published dates (May 14) unchanged; no text differences detected:
- `https://openai.com/policies/conversion-terms/`
- `https://openai.com/policies/conversion-dpa/`
- `https://openai.com/policies/conversion-subprocessors/`

These govern OpenAI's Conversion Tools product, which allows advertisers to provide conversion event data to OpenAI for audience measurement and ad optimization.

## New Pages

None.

## Removed Pages

None.

## Fetch Failures

None. All 36 pages fetched successfully.

## Pattern Notes

- **Teen-safety daily sweep**: This is the 3rd consecutive day where the teen-safety cluster has received a batch lastmod update. Days: May 16 (~05:35 UTC), May 17 (~05:35 UTC), May 18 (~08:33 UTC). The timing shifted by ~3 hours today. This pattern suggests background CMS activity in the teen-safety cluster, possibly related to a staged content rollout that hasn't fully materialized in visible page text yet.
- **Timestamp discipline**: All `<lastmod>` values cited above are OpenAI's CMS claims. Fetch time was 09:16 UTC. All claimed timestamps are prior to fetch time (no future-dated anomalies).

# Analysis: 2026-06-08T09-15Z

**Fetch time:** 2026-06-08T09:18:03Z  
**Total current URLs:** 1331  
**Baseline URLs:** 1331  
**Added:** 0  
**Removed:** 0  
**Updated (sitemap lastmod):** 109  
**Pages with actual visible content changes:** 2  
**Anomalies:** 0  
**Fetch failures:** 0  

---

## Anomalies

None detected.

---

## Significant Updates

### 1. Release Notes — Multiple New Announcements (Jun 2–4, 2026)

**URL:** https://openai.com/products/release-notes/  
**Page:** [pages/openai.com/products/release-notes/index.md](../../pages/openai.com/products/release-notes/index.md)  
**lastmod:** `2026-06-05T21:27:25.027Z` → `2026-06-08T08:26:28.602Z`

The release notes page now surfaces the following new entries (previously showing Codex app updates 26.602 at the top of the visible window):

**API — Jun 4, 2026**
- **Added moderation scores to API generation requests**: The Responses API and Chat Completions API now accept a `moderation` object in generation requests, returning moderation results for both input and output in the same response. Eliminates the need for a separate moderation call.

**ChatGPT — Jun 4, 2026**
- **Memory that stays more up to date**: Upgraded memory system that automatically keeps context current, reduces stale/contradictory memories, and tracks preferences and ongoing work. Rolling out to Plus/Pro users in the US first; Free/Go plans and additional countries coming in weeks. Memory capacity doubled for Plus/Pro. Legacy saved-memories mode remains available as an opt-out fallback from Settings > Memory.

- **Lockdown Mode available to all logged-in users**: Previously limited, Lockdown Mode is now available across all account types and workspaces. An opt-in advanced security setting (Settings > Security) that disables web browsing, deep research, agent mode, file downloads, and web-derived image support to reduce prompt-injection data-exfiltration risk. Workspace admins can configure access via role-based controls.

- **Rolling out ads in the UK**: Ads beginning to roll out for Free and Go plan users in the UK. Plus, Pro, Business, Enterprise, and Education plans remain ad-free.

**ChatGPT — Jun 2, 2026**
- **Active account session controls**: New security feature (Settings > Security > Active sessions). Users can review all first-party sessions with details including device, app, approximate location, sign-in time, and trusted-device status; can sign out of individual or all sessions. Covers ChatGPT, Codex, and API Platform sessions. Does **not** cover third-party app sessions, connected apps, Sign in with ChatGPT sessions used only for third-party services, or Codex CLI sessions.

*Note: The prior top entry "Codex app updates 26.602" (Jun 4) — which featured activity insights, share cards, and Computer Use fixes — has been pushed below the "Load more" boundary.*

---

### 2. Site-Wide Footer Navigation Overhaul

**URL (representative page that diffed):** https://openai.com/index/dall-e-3/  
**Page:** [pages/openai.com/index/dall-e-3/index.md](../../pages/openai.com/index/dall-e-3/index.md)  
**lastmod:** `2026-04-22T23:54:17.638Z` → `2026-06-08T07:47:21.242Z`

A site-wide footer navigation update was deployed, touching 109 pages. The DALL-E 3 page is the representative example where markdown diffed (its footer had been captured prior to this update). All other page content was already current.

**Key changes:**

- **New "Developers" section** added to footer:
  - Apps SDK (`developers.openai.com/apps-sdk`)
  - Open Models (`/open-models/`)
  - Docs (`developers.openai.com/`)
  - Resources (`developers.openai.com/learn`)
  - Developer Forum (`community.openai.com/`)

- **"ChatGPT" section renamed to "Products"** with URL restructuring:
  - Old links: `chatgpt.com/business/business-plan`, `chatgpt.com/business/enterprise`, `chatgpt.com/business/education`
  - New links: `chatgpt.com/business/`, `chatgpt.com/business/enterprise/`, `chatgpt.com/business/education/` (canonical trailing-slash URLs)
  - **Codex** (`/codex/`) and **Release Notes** (`/products/release-notes/`) added to this section

- **"Our Research" renamed to "Research"**; **Research Residency** link (`/residency/`) removed

- **"Latest Advancements" section**: **GPT-5.3-Codex** removed from the featured model list (GPT-5.5, GPT-5.4, GPT-5.3 Instant remain)

- **"Safety" section**: **Deployment Safety** link added (`deploymentsafety.openai.com`)

- **"API Platform" section simplified**: Pricing link removed; Developer Forum moved to new Developers section

- **"For Business" renamed to "Business"**: "Resources" (`/business/learn/`) added

- **"Company" section**: Foundation and Brand links removed; **News** (`/news/`) added

- **"More" section**: News link removed (now in Company)

---

## Routine Sitemap Updates (107 URLs — lastmod bumped, no visible content change)

109 URLs received sitemap lastmod bumps; 107 had no actual visible content change. These represent the CMS publishing the footer nav update (described above) across the site. Breakdown by section:

| Section | Count |
|---------|-------|
| index/ (case study/research/announcement pages) | 81 |
| academy/ | 11 |
| policies/ | 5 |
| stories/ | 4 |
| business/ | 2 |
| form/ | 2 |
| gpt-rosalind/ | 1 |
| podcast/ | 1 |
| products/ | 1 |
| startups/ | 1 |

Policy pages with lastmod bumps (no content change detected):
- `https://openai.com/policies/privacy-policy/` (`2026-06-07T19:46:36.563Z`)
- `https://openai.com/policies/ad-policies/` (`2026-06-08T07:07:19.928Z`)
- `https://openai.com/policies/chatgpt-sites-terms/` (`2026-06-08T09:09:57.368Z`)
- `https://openai.com/policies/eu-services-privacy-policy/` (`2026-06-07T13:29:22.795Z`)
- `https://openai.com/policies/merchant-feed-terms-of-service/` (`2026-06-08T06:27:41.775Z`)

*Policy lastmod changes without visible content changes may indicate backend metadata updates or CMS template changes rather than actual policy text edits.*

---

## New Pages

None.

## Removed Pages

None.

## Fetch Failures

None.

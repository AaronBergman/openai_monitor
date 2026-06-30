# Run Analysis — 2026-06-30T09-15Z

**Fetch time:** 2026-06-30T09:15:00Z  
**Baseline:** 2026-06-29T09-15Z (sitemaps/openai.com/sub/latest/ as of git HEAD)  
**Stats:** 1382 total URLs | +1 added | 35 updated (lastmod changed) | 0 removed | 0 anomalies | 34 sub-sitemaps

---

## Anomalies

None detected.

- No future-dated `<lastmod>` values.
- No backwards-moving `<lastmod>` values.
- No newly-appeared URLs with old (backdated) lastmod.
- No sub-sitemap migrations.

---

## New Pages (1)

### [Mapping Europe's AI Workforce Opportunity](../../pages/openai.com/index/mapping-ai-jobs-transition-eu/index.md)

- **URL:** https://openai.com/index/mapping-ai-jobs-transition-eu/
- **`<lastmod>`:** 2026-06-29T10:24:03.638Z
- **Published:** June 29, 2026
- **Section:** Global Affairs / Economic Research

OpenAI Economic Research released the EU extension of its AI Jobs Transition Framework, first developed for the U.S. in April 2026. This report applies the ESCO occupational taxonomy (the European equivalent of O*NET) and Eurostat employment data to map how AI capabilities may translate into near-term occupational change across EU member states.

Key findings:
- **~12%** of EU employment is in occupations *likely to grow* with AI.
- **~14%** is in occupations with *higher near-term automation potential*.
- **~27%** is in occupations *likely to reorganize* (AI changes workflows, but humans remain central).
- **~47%** has *less immediate change* expected.

Country-level variation: Luxembourg, Sweden, Netherlands skew toward growth occupations; Germany, Greece, Italy have larger shares in higher-automation-potential occupations. The full PDF is linked from the page.

**Context:** This follows the U.S. framework from April 2026 (first_seen ~2026-04). The EU report's appearance on the Signals landing page (rotating out the "New tools for understanding AI and learning outcomes" card) suggests it is the featured economic-research output this week.

---

## Significant Updates

### Health Privacy Policy — Expanded for "Connect Health" Feature

- **URL:** https://openai.com/policies/health-privacy-policy/
- **`<lastmod>`:** 2026-06-29T21:00:42.787Z (was 2026-06-26T09:01:53.947Z)

Substantial rewrite. The prior policy described only "Health" (ChatGPT's dedicated Health space). The updated policy covers two distinct offerings:

1. **ChatGPT Health** — the existing dedicated health conversation space with its own memory store, connected apps (Apple Health, EHR providers via b.well), and isolated memory.
2. **Connect Health** (new) — a feature that allows health data to be used in *regular ChatGPT conversations* when enabled. Connect Health conversations use main-account memory settings rather than a separate memory store.

Key changes:
- Scope broadened from "the Health feature" to "ChatGPT Health and Connect Health offerings" collectively called "Health Features."
- Updated policy link from `row-privacy-policy` to `privacy-policy` (a single global policy rather than the rest-of-world variant).
- Data training default: now explicitly lists *which* data is excluded from foundational model training: medical records from third-party accounts, conversations in ChatGPT Health, and conversations with Health Connect enabled.
- Removed the section describing the `b.well` EHR integration partner by name; replaced with more general language about "linked third-party data sources."
- Removed the specific mention of apps in the standalone Apps section; merged into "Linked Accounts."
- Memory section now describes the two-tier memory model: ChatGPT Health has its own memory separate from main account; Connect Health uses main-account memory settings.

This is the clearest public signal yet of "Connect Health" as a distinct product feature — health context flowing into regular ChatGPT conversations rather than requiring a separate Health mode.

### Signals Landing Page — Featured Article Rotated

- **URL:** https://openai.com/signals/
- **`<lastmod>`:** 2026-06-29T10:27:05.766Z

"Mapping Europe's AI Workforce Opportunity" (new, Jun 29) has replaced "New tools for understanding AI and learning outcomes" as the featured article card on the OpenAI Signals economic-research hub. Consistent with the new URL being added to the sitemap.

---

## Routine Updates (No Visible Content Change)

The following pages had updated `<lastmod>` timestamps but showed **no visible content difference** vs. yesterday's snapshot. These appear to be CMS touch/cache-bust operations:

### Pricing Pages (batch ~18:39 UTC, June 29)
- https://openai.com/api/pricing/ — `2026-06-29T08:01:41.745Z` → `2026-06-29T18:39:03.367Z`
- https://openai.com/business/pricing/ — `2026-06-29T09:16:32.861Z` → `2026-06-29T18:39:21.950Z`
- https://openai.com/business/chatgpt-pricing/ — `2026-06-29T09:16:52.925Z` → `2026-06-29T18:39:36.019Z`

Third consecutive day these three pricing pages have received intraday lastmod bumps. The 18:39 batch corresponds to late afternoon US time. Consistent with ongoing pricing system updates following the June 24 ChatGPT Business price reduction to $20/seat.

### Policy Pages
- `/policies/professional-services-security-measures/` — new lastmod `2026-06-30T08:46:21.910Z`, no content change
- `/policies/uk-online-safety-act/` — new lastmod `2026-06-29T23:30:44.015Z`, no content change

### Codex Product Page
- `/codex/` — new lastmod `2026-06-29T23:56:36.315Z`, no content change (still shows $500 referral offer, macOS/Windows availability)

### 11 Codex Academy Pages (batch ~22:55 UTC, June 29)
All updated to timestamps around `2026-06-29T22:55:xx.xxxZ` with no visible content changes. This is a repeated pattern — these pages received batch touches on June 28 as well. Likely a CMS pipeline re-publish triggered by content system updates elsewhere.

Pages:
- `academy/how-to-use-codex-for-everyday-work/`
- `academy/codex-for-work/how-sales-teams-use-codex/`
- `academy/how-finance-teams-use-codex/`
- `academy/codex-automations/`
- `academy/working-with-codex/`
- `academy/what-is-codex/`
- `academy/codex-plugins-and-skills/`
- `academy/codex-for-work/how-data-science-teams-use-codex/`
- `academy/codex-for-work/how-business-operations-teams-use-codex/`
- `academy/codex-settings/`
- `academy/codex-how-to-start/`

### Form Pages (batch ~22:05-22:06 UTC, June 29)
No content changes detected:
- `/form/100-chats-book-request/`
- `/form/chatgpt-pro-community/`
- `/form/rosalind-biodefense-program/`
- `/form/life-sciences-access/`
- `/form/openai-campus-leaders-interest-form/`
- `/form/openai-campus-network-student-club-interest-form/`

### Index / Article Pages (related-article card rotations)
Several article pages had their "Keep reading" related-article carousels updated. The actual article content did not change — these are CMS-side related-article suggestions being refreshed:

- `/index/samsung-electronics-chatgpt-codex-deployment/` — HP article added, Daybreak article rotated out
- `/index/chatgpt-enterprise-spend-controls/` — GPT-5.6 Sol preview added, memory/dreaming article rotated out
- `/index/helping-build-shared-standards-for-advanced-ai/` — EU AI Jobs mapping added, "Industrial policy for the Intelligence Age" rotated out
- `/index/gpt-5-immunology-mystery/` — no visible change
- `/index/hp-frontier-partnership/` — no visible change (lastmod `2026-06-30T09:09:54.014Z`, very fresh)
- `/index/openai-broadcom-jalapeno-inference-chip/` — no visible change
- `/index/how-agents-are-transforming-work/` — no visible change
- `/index/previewing-gpt-5-6-sol/` — no visible change (fourth consecutive daily touch on this page)

### Signals Research
- `/signals/research/` — new lastmod `2026-06-29T10:04:48.257Z`, no visible content change

### Trademark Form
- `/form/trademark-counterfeit-disputes/` — no content change

---

## Removals

None.

---

## Fetch Failures

None. All 36 URLs (1 added + 35 updated) fetched successfully.

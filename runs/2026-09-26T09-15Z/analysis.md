# Analysis — run 2026-09-26T09-15Z

Fetch window: 2026-09-26T09:15–09:24Z. Baseline: 2026-09-25T09-16Z (1 day prior — no gap).
Sitemap index: 42 sub-sitemaps, 1,985 URLs total (up from 1,984 in the baseline).

## Anomalies

1. **Sub-sitemap migration.** `business/plugins/activecampaign/` moved from
   `sitemap.xml/plugins-operations/` to `sitemap.xml/plugins-marketing/`, with its
   `<lastmod>` bumped in the same run (2026-09-25T00:34:21Z → 2026-09-25T15:12:07Z).
   Simple recategorization — ActiveCampaign is a marketing-automation tool, so this
   reads as a correction of a miscategorized listing rather than anything suspicious.

No future-dated `<lastmod>` values and no backwards-moving `<lastmod>` values were
found in this run. No URLs disappeared and none reappeared.

## Significant updates (real content changes, verified by markdown diff)

Of 300 URLs with a changed `<lastmod>`, **123** had an actual rendered-content
difference; the other **177** were byte-identical to the prior snapshot (pure
`<lastmod>` bump with no visible change, most likely a cache/CDN regeneration sweep;
not reported individually below). Of those 123 real diffs, 80 were pure
"related articles" sidebar rotation (older posts on the page's recommendation widget
swapped for newer ones like "Two years of OpenAI Academy" or "Sam Altman's remarks at
the United Nations Security Council") — routine noise, not treated as page-level news
below.

### Asana Codex case study quietly rewritten, dollar claim softened

[`/index/asana/`](../../pages/openai.com/index/asana/index.md) — the headline changed from
**"Asana cleared 5 years of engineering work in 2 weeks with Codex"** to **"Asana
completed a years-long code migration in 2 weeks with Codex."** The stat tiles were
also rewritten: the old page led with "Model and infrastructure cost versus Asana's
~$6M staffing estimate" as a headline comparison; the new version drops the $6M
figure from the stat tiles entirely (it now only appears once, deeper in the body
copy, phrased as "roughly $6M in fully loaded engineering effort"). The intro
sentence "In about two weeks, Asana completed work it expected to take five years"
was cut. Reads as OpenAI toning down a bold, easily-quotable marketing claim
("5 years of work in 2 weeks", "$6M vs $12K") in favor of softer framing — possibly in
response to scrutiny of the estimate's plausibility.

### `/products/release-notes/` — new entry, one rolled off

New (Sep 24, 2026): **"External access controls"** — Global admins in ChatGPT Business
and Enterprise organizations can now manage whether ChatGPT Sites can use members'
connected apps, and whether applications can access ChatGPT Ads, via a redesigned
"External access" page in the OpenAI Admin Console. Both permissions are off by
default during the admin preview. The Sep 21 "Privacy Center in ChatGPT" entry
scrolled out of the visible window.

### `/signals/` swapped its featured economic research report

The old featured link, "The AI jobs transition framework" (April 2026), was replaced
by **"Work at the Frontier: How workers are unlocking new ways of working"**
(September 2026) — a new report analyzing how workers use AI for tasks outside their
typical job description and which new tasks they fold into their workflows
([PDF](https://cdn.openai.com/pdf/work-at-the-frontier-report-202609.pdf)).

### Small-business solutions page drops webinar list for a plugin showcase

[`/business/why-openai/small-business/`](../../pages/openai.com/business/why-openai/small-business/index.md)
replaced its "Live and virtual events" webinar list with a new "Make ChatGPT work the
way you work" section showcasing plugin integrations (Dropbox, Slack, Docusign,
ClickUp, Intuit QuickBooks) for small businesses, plus a new customer quote from
Larissa Guetter (ATV Big Air Tour). Continues the ChatGPT Work / plugins push into
solution-specific landing pages.

### Continued rollout of "Plugins" and "GPT-6" global nav links

24 pages (mostly older model/research archive pages — GPT-4, DALL·E 2/3, Whisper,
Sora, o1, o3/o4-mini system card, consistency models, Rubik's Cube solver, etc. — plus
`enterprise-privacy/`, `business-data/`, `solutions/industries/healthcare/`) gained a
new **"Plugins"** link (`/business/plugins/`) in their footer/nav. 15 of those same
pages also gained a **"GPT-6"** link (`/index/gpt-6-astra/`). This is template
propagation of nav changes that started appearing on the plugin-directory pages in
the 2026-09-25 run, now reaching legacy archive pages — cosmetic/navigational, not new
news itself.

### Minor / low-signal changes

- **`/index/browsecomp/`**, **`/index/our-approach-to-the-model-spec/`**,
  **`/index/how-confessions-can-keep-language-models-honest/`**,
  **`/index/separating-signal-from-noise-coding-evaluations/`**,
  **`/index/extracting-concepts-from-gpt-4/`**: these pages embed client-rendered
  "example" widgets (a random Q&A, a random Model Spec compliant/violation pair, a
  random chain-of-thought excerpt, a random eval task, a random GPT-4 feature
  activation). Each showed a *different* example than the prior snapshot. This looks
  like the widgets serve a randomized example per page load rather than the page
  content actually changing — flagged here for transparency but not treated as
  substantive.
- **`/index/healthbench/`**: the "Languages spoken / Medical specialties" data table
  present in the prior snapshot did not render in this fetch (page now cuts off after
  "Countries of practice"). Likely a client-side chart that didn't finish loading
  before the scrape captured the page, similar to past render-timing anomalies. Not
  treating as a deliberate content removal; will re-check next run.
- Four pages (`business/partners/exl-service/`, `business/why-openai/startups/`,
  `index/chatgpt-for-academic-researchers/`, `index/higgsfield-from-prompt-to-production-with-astra/`)
  had only image alt-text changes (more descriptive AI-style captions replacing plain
  filenames/titles) — accessibility/SEO polish, no visible content change.
- `api-fast-mode/`: GPT-6 Astra/Sol/Luna batch-pricing table cells changed from blank
  to em-dash (`—`) placeholders — formatting only, no price change.
- `index/introducing-b2b-signals/` and `index/the-defenders-window/` gained a new
  "## Keep reading" section linking to `/news/` — minor template addition, isolated
  to these two pages this run.

## New pages

### `/index/proaction/` — new customer story

**"Proaction boosts sales 60% and saves 75+ hours with Codex"** (lastmod
2026-09-25T22:07Z). Immediately promoted to the top slot of the
`/business/customer-stories/` carousel, bumping the 1Password story (Sep 8) out of
the visible set. Fits the ongoing steady cadence of Codex customer-story publishing.

## Removed pages

None this run.

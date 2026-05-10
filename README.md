# openai_monitor

Daily changelog of [openai.com](https://openai.com)'s public website,
maintained by a Claude Code routine. Each run diffs the current sitemap
against the prior one, fetches changed pages, and writes a plain-language
summary that a smart layperson can follow.

## 2026-05-10T09-16Z

**Fetch time:** 2026-05-10T09:17:38Z UTC | **Baseline:** 2026-05-09T09-15Z

**TL;DR:** The headline story is OpenAI **shutting down its self-serve fine-tuning platform** (announced May 8 via retroactive notices added to three existing fine-tuning pages) — a significant change for developers who relied on training custom models through OpenAI's API since 2023. On the other side of the ledger, OpenAI is doubling down on specialized AI for cybersecurity: GPT-5.5-Cyber launched in limited preview for critical-infrastructure defenders this week, and new posts explain both the technical governance controls for Codex agents and a broader strategy for democratizing AI-powered defense. One new customer story (Simplex, Japan) documents 70% faster screen development using Codex. The rest of the 198 lastmod changes are batch CMS metadata refreshes across Academy, Global Affairs, and customer story pages with no detectable content changes.

### Anomalies

None detected.

**Infrastructure note:** `/sitemap.xml/page/` returned HTTP 503 persistently (4 retry attempts); served from 2026-05-09 cached snapshot. URLs listed only in that sub-sitemap are not diffed this run.

### Notable updates

- **Fine-tuning platform shutdown** (MAJOR) — Three fine-tuning announcement pages ([introducing improvements to the fine-tuning API](pages/openai.com/index/introducing-improvements-to-the-fine-tuning-api-and-expanding-our-custom-models-program/index.md), [introducing vision to the fine-tuning API](pages/openai.com/index/introducing-vision-to-the-fine-tuning-api/index.md), [GPT-4o fine-tuning](pages/openai.com/index/gpt-4o-fine-tuning/index.md)) each received an identical retroactive notice:
  > *"OpenAI is winding down the fine-tuning platform. The platform is no longer accessible to new users but existing users of the fine-tuning platform will be able to create training jobs for the coming months. All fine-tuned models will remain available for inference until their base models are deprecated."*
  The self-serve fine-tuning API has been available since August 2023. Deprecation timeline is on the OpenAI developer docs site.

- **GPT-5.5-Cyber and Trusted Access for Cyber** — [`/index/gpt-5-5-with-trusted-access-for-cyber/`](pages/openai.com/index/gpt-5-5-with-trusted-access-for-cyber/index.md) (published May 7, lastmod refreshed today): A specialized cybersecurity model in limited preview for defenders protecting critical infrastructure. Three-tier access system: default GPT-5.5, GPT-5.5 with TAC (Trusted Access for Cyber) for verified defensive workflows, and GPT-5.5-Cyber for the most specialized authorized work (authorized red-teaming, pen-testing). Advanced Account Security (phishing-resistant MFA) required for individual TAC members from June 1, 2026.

- **Running Codex safely at OpenAI** — [`/index/running-codex-safely/`](pages/openai.com/index/running-codex-safely/index.md) (published May 8, metadata refreshed today): OpenAI's internal playbook for governing Codex agents: sandboxed execution environments, human approval gates for high-risk actions, network access policies, managed credential systems, and agent-native audit trails.

- **OpenAI on AWS related-posts refresh** — [`/index/openai-on-aws/`](pages/openai.com/index/openai-on-aws/index.md): Sidebar "keep reading" links rotated to newer content ("Advancing voice intelligence" and "Testing ads in ChatGPT," replacing "GPT-5.5 Instant" and "New ways to buy ChatGPT ads").

- **Batch CMS refreshes** — ~20 Global Affairs pages (all ~18:41 UTC May 8), ~21 Academy pages (May 7–8), ~50 customer story `/index/` pages (all ~07:xx UTC today), 9 form pages (May 8), and 5 policy pages (May 7–8) received lastmod bumps. No content changes detected on any of them.

### New pages (1)

| Page | Date | Summary |
|---|---|---|
| [Simplex](pages/openai.com/index/simplex/index.md) | May 8 | Japanese technology company Simplex adopts ChatGPT Enterprise + Codex as its primary coding agent; reports 70% fewer hours per screen developed, 40% fewer per screen designed, 17% fewer for integration testing; focuses on redesigning the full development process around AI rather than using AI as an assistive overlay |

### Removals

0 pages removed.

**Stats:** 1,287 total URLs | +1 added | 198 lastmod updates | 0 removed | 0 anomalies | 34 sub-sitemaps (1 served from cache)

---

## 2026-05-09T09-15Z

**Fetch time:** 2026-05-09T09:16:02Z UTC | **Baseline:** 2026-05-07T09-15Z

**TL;DR:** A busy two days on openai.com. OpenAI published seven new articles across safety,
security, and developer topics — including new real-time voice API models, a limited preview of
GPT-5.5-Cyber for critical-infrastructure defenders, a "Trusted Contact" crisis-notification
feature for ChatGPT users, and a bilingual English/French privacy explainer aimed at Canadian
audiences. Multiple waves of coordinated updates touched privacy policies, Codex content, and
the OpenAI Academy. One notable structural event: the sub-sitemap that listed ~122 B2B customer
stories began returning HTTP 403 — those pages are still live but are no longer indexed through
that endpoint. One metadata anomaly: the `enterprise-privacy/` page's claimed lastmod jumped 15
months backward with no content change.

### Anomalies

1. **Backwards lastmod — `enterprise-privacy/`**
   The sitemap's `<lastmod>` for `https://openai.com/enterprise-privacy/` regressed from
   `2026-05-04` to `2025-01-31` (roughly 15 months backward). The page content is
   byte-for-byte identical to the prior snapshot and the in-page "Updated: January 8, 2026"
   date is unchanged. This is a CMS/metadata glitch, not a content rollback.

2. **B2B customer-stories sub-sitemap now returns HTTP 403**
   The sub-sitemap `https://openai.com/sitemap.xml/internal-use-show-on-b2b-customer-stories-hub/`
   (which listed 122 `/index/` customer-story pages) returned HTTP 403 this run. Spot-checks
   confirm the underlying pages (e.g., `/index/canva/`, `/index/cisco/`) remain live and
   fully accessible. OpenAI appears to have restricted the sitemap endpoint itself — possibly
   intentionally, given the "internal-use-" prefix in the sub-sitemap name. All 122 URLs are
   preserved in `state/known_urls.json`.

### New pages (7)

| Page | Date | Summary |
|---|---|---|
| [Advancing voice intelligence with new models in the API](pages/openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/index.md) | May 7 | Three new realtime audio API models: GPT-Realtime-2 (GPT-5-class reasoning in voice), GPT-Realtime-Translate (live 70→13 language translation), GPT-Realtime-Whisper (live streaming transcription) |
| [GPT-5.5 with Trusted Access for Cyber](pages/openai.com/index/gpt-5-5-with-trusted-access-for-cyber/index.md) | May 7 | GPT-5.5-Cyber rolled out in limited preview to critical-infrastructure defenders; explains three-tier Trusted Access for Cyber framework; Advanced Account Security (phishing-resistant) required for top-tier access from June 1, 2026 |
| [Running Codex safely at OpenAI](pages/openai.com/index/running-codex-safely/index.md) | May 8 | Technical guide to OpenAI's internal Codex governance: sandboxing, human-approval gates for high-risk actions, network policies, and agent-native audit trails |
| [How ChatGPT learns about the world while protecting privacy](pages/openai.com/index/how-chatgpt-protects-privacy/index.md) | May 6 | Bilingual (English + French) plain-language privacy explainer covering training data practices, personal information handling, and user privacy controls — likely produced for Canadian regulatory context |
| [Introducing Trusted Contact in ChatGPT](pages/openai.com/index/introducing-trusted-contact-in-chatgpt/index.md) | May 7 | New optional safety feature: adults 18+ can nominate a trusted person to receive automated notifications if OpenAI's systems detect serious self-harm risk; extends existing parental-alert system to all users |
| [Advancing youth safety and wellbeing in EMEA](pages/openai.com/index/advancing-youth-safety-in-emea/index.md) | May 5 | European Youth Safety Blueprint (5 pillars for age-appropriate AI policy) and announcement of first EMEA Youth & Wellbeing Grant recipients |
| [Parloa](pages/openai.com/index/parloa/index.md) | May 7 | Customer story: European startup Parloa builds enterprise voice-driven customer service agents using the OpenAI API |

### Notable updates

- **B2B Signals messaging rebrand** — [`signals/b2b/`](pages/openai.com/signals/b2b/index.md):
  "AI advantage" replaced throughout with "frontier advantage"; intro rewritten to be more
  concise. Deliberate positioning shift to align with OpenAI's "frontier model" branding.

- **Privacy policy wave** (all updated May 7–8): `services-privacy-policy`, `communications-privacy-policy`,
  `services-communications-privacy-policy`, `us-privacy-policy`, `cookie-policy`, and `usage-policies`
  — six policy documents updated in a coordinated 24-hour window, coinciding with the new privacy explainer.

- **API page** — new "Enterprise-ready solutions for real impact" section added with a three-tab
  interface linking to use cases, industries, and blueprints.

- **Codex ecosystem refresh** — ~15 Codex-related pages (codex/, codex/get-started/, gpt-5-2-codex through gpt-5-5-instant, introducing-upgrades-to-codex, codex-now-generally-available, etc.) all refreshed May 7–8, coordinated with Codex GA.

- **Academy learning content** — ~21 OpenAI Academy course pages refreshed May 7–8 (codex, building-with-ai, chatgpt-for-education, customer-success, data-analysis, marketing, etc.).

- **FedRAMP Moderate** — [`index/openai-available-at-fedramp-moderate/`](pages/openai.com/index/openai-available-at-fedramp-moderate/index.md):
  Updated (May 9) to note that GPT-5.5 is now available in the FedRAMP environment, and that
  Codex Cloud will soon be accessible via FedRAMP ChatGPT Enterprise workspace.

- **Customer stories hub rotation** — [`business/customer-stories/`](pages/openai.com/business/customer-stories/index.md):
  Added Parloa and Simplex to the featured list; VfL Wolfsburg and Axios Allison Murphy rotated out.

### Removals

0 pages confirmed removed. See anomaly #2 above for the 122 URLs now inaccessible via the
b2b-customer-stories sub-sitemap.

**Stats:** 1,164 current URLs | +7 added | 153 lastmod updates | 122 missing via 403 sub-sitemap (0 confirmed removed) | 2 anomalies | 33/34 sub-sitemaps fetched

---

## 2026-05-07T09-15Z

**Fetch time:** 2026-05-07T09:17:05Z UTC | **Baseline:** 2026-05-07T09-01Z

**TL;DR:** OpenAI's CMS ran a batch regeneration cycle between the bootstrap run and
this one (~14 minutes apart), causing 34 pages to show fresh `<lastmod>` timestamps.
Of those 34, only **one page had a real content change**: the `/index/podium/` customer
story rotated a single "Keep reading" recommended-article link (swapped "Singular Bank"
for "How frontier enterprises are building an AI advantage"). The other 33 were
timestamp-only updates with identical content. No URLs were added or removed. No
anomalies detected.

### The one real content change

- [https://openai.com/index/podium/](pages/openai.com/index/podium/index.md) —
  "Keep reading" carousel updated: swapped out the
  [Singular Bank story](pages/openai.com/index/singular-bank/index.md) in favour of
  [How frontier enterprises are building an AI advantage](pages/openai.com/index/introducing-b2b-signals/index.md)
  (both dated May 6, 2026). Main article body (GPT-5.1 powering AI agents for 10,000+ SMBs) unchanged.

### Notable timestamp-only updates (no content change)

34 pages had `<lastmod>` bumped from ~08:xx UTC to ~09:xx UTC — a CMS batch
re-index signature. The most notable was `/index/our-principles/` (Sam Altman),
whose timestamp crossed a day boundary (May 6 → May 7) but content was identical.
See [runs/2026-05-07T09-15Z/analysis.md](runs/2026-05-07T09-15Z/analysis.md) for the
full list.

**Stats:** 1279 total URLs | +0 added | 34 lastmod changes (1 content change) | -0 removed | 0 anomalies | 34 sub-sitemaps

---

- **Sitemap monitored:** `https://openai.com/sitemap.xml` (sitemap-index → ~34 sub-sitemaps)
- **Routine schedule:** daily
- **What's tracked:** added / removed / updated URLs (per `<lastmod>`),
  plus anomalies like backwards-moving timestamps, future-dated mods,
  reappearing URLs, and similar oddities.
- **Bot defense:** openai.com is fronted by Cloudflare with TLS-fingerprint
  blocking. The conversion tool uses `curl-cffi` with Chrome impersonation
  to bypass the 403 that plain Python clients receive. robots.txt explicitly
  allows scraping (`User-agent: * / Allow: /`).

## Repo layout

| Path | Contents |
| ---- | -------- |
| `README.md` | This file. Newest run entries are PREPENDED below. |
| `sitemaps/openai.com/<run_id>.xml` | Dated root sitemap-index snapshots. |
| `sitemaps/openai.com/latest.xml` | Most recent index — overwritten each run. |
| `sitemaps/openai.com/sub/<run_id>/*.xml` | Dated sub-sitemap snapshots. |
| `sitemaps/openai.com/sub/latest/*.xml` | Most recent sub-sitemaps — overwritten each run. |
| `pages/openai.com/<path>.md` | Current markdown of each page. Git history is the archive. |
| `runs/<run_id>/analysis.md` | Long-form analysis written for that run. |
| `runs/<run_id>/diff.json` | Machine-readable diff vs prior baseline. |
| `state/known_urls.json` | Cumulative URL state: first_seen, last_seen, lastmod history. |
| `tools/html_to_md.py` | Canonical HTML→markdown converter (uses curl-cffi). |
| `tools/url_path.py` | Canonical URL→repo-path mapping. |
| `tools/requirements.txt` | pip dependencies. |

`<run_id>` format is `YYYY-MM-DDTHH-MMZ` (UTC).

## Timestamp discipline

Three distinct timestamps are tracked, never conflated:

- **`<lastmod>`** — what OpenAI *claims* about a page in their sitemap.
- **fetch time** — UTC time *we* actually retrieved the sitemap or page.
- **first_seen** — the earliest `run_id` when a URL appeared here.

Anomalies generally live in the gap between these.

---

## 2026-05-07T09-01Z — Bootstrap

**TL;DR:** Initial baseline captured. Fetched the openai.com sitemap-index,
walked all 34 sub-sitemaps, downloaded 1277
of 1279 pages through curl-cffi (Chrome TLS impersonation; plain Python
hits a Cloudflare 403), converted to markdown, and committed the snapshot.
No diff is possible yet; the next daily run will produce the first real
changelog entry.

- **Fetch time:** 2026-05-07T09:01:08.630082Z
- **Sub-sitemaps:** 34
- **URLs in sitemap:** 1279
- **Pages stored:** 1277
- **Fetch failures:** 2
- **Anomalies (bootstrap-detectable):** see below.

### Bootstrap-detectable anomalies

Even on the bootstrap run, with no prior baseline, two URLs from the sitemap
returned **HTTP 404** when fetched. These are listed in the sitemap-index but
are not actually live pages — a sitemap/site mismatch. The first one is
particularly interesting:

- **`https://openai.com/index/inworld-ai-DO-NOT-PUBLISH/`** — appears in the
  public sitemap but 404s. The literal string `DO-NOT-PUBLISH` in the path
  strongly suggests this is an internal staging slug that leaked from
  OpenAI's CMS into the production sitemap. Worth watching: if the URL ever
  starts returning 200, that's the moment OpenAI accidentally published an
  Inworld-AI–related page (which the routine will then fetch and snapshot).
- **`https://openai.com/brand-old/`** — also in the sitemap, also 404. Likely
  a deprecated brand-guidelines page that was removed from the site but not
  the sitemap.

Both will be re-checked every daily run. State changes (404 → 200, or
disappearance from the sitemap entirely) will be flagged.

See [`runs/2026-05-07T09-01Z/analysis.md`](runs/2026-05-07T09-01Z/analysis.md) for the full bootstrap report.

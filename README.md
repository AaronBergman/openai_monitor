# openai_monitor

Daily changelog of [openai.com](https://openai.com)'s public website,
maintained by a Claude Code routine. Each run diffs the current sitemap
against the prior one, fetches changed pages, and writes a plain-language
summary that a smart layperson can follow.

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

## 2026-05-08T09-15Z — Voice AI trio, GPT-5.5-Cyber, Trusted Contact safety feature

**TL;DR:** A busy 24 hours for OpenAI. Three new realtime audio models launched in the API (GPT-Realtime-2, GPT-Realtime-Translate, GPT-Realtime-Whisper) with pricing now live. A new cybersecurity tier — GPT-5.5-Cyber — is rolling out to vetted defenders of critical infrastructure. ChatGPT gains a "Trusted Contact" feature that lets adults designate someone to be notified in a mental health crisis. Four privacy policies quietly updated (likely to cover Trusted Contact data handling). One sub-sitemap returned HTTP 403 (a CMS access control for B2B customer stories), so 122 URLs have unknown status this run — they are not confirmed removed.

### Anomalies

- **Near-future `<lastmod>` on Microsoft Partnership page** — `https://openai.com/index/next-phase-of-microsoft-partnership/` had a `<lastmod>` of `2026-05-08T09:16:43.129Z`, which is 0.6 seconds *after* our sitemap fetch began (`2026-05-08T09:16:42.532Z`). Almost certainly a CMS timestamp race; page content shows only sidebar rotation. Documented per protocol, but almost certainly benign.

- **Sub-sitemap HTTP 403 (needs follow-up)** — `https://openai.com/sitemap.xml/internal-use-show-on-b2b-customer-stories-hub/` returned 403 on all 4 retry attempts. The 122 B2B customer story URLs previously sourced from this sub-sitemap are **not confirmed removed** — their on-site status is unknown. Monitor for recovery in the next run. The prior snapshot of this sub-sitemap is preserved in git.

### New pages (4)

1. **[Scaling Trusted Access for Cyber with GPT-5.5 and GPT-5.5-Cyber](pages/openai.com/index/gpt-5-5-with-trusted-access-for-cyber/index.md)** (Security, 2026-05-07) — OpenAI launches GPT-5.5-Cyber in limited preview for vetted cybersecurity defenders. Introduces a three-tier access framework: default GPT-5.5, GPT-5.5 with "Trusted Access for Cyber" (for verified defenders), and GPT-5.5-Cyber (most permissive; for red teaming and pen testing). Users in the top tier must enable phishing-resistant authentication (Advanced Account Security) by June 1, 2026. Security industry partners announced: Cisco, CrowdStrike, Palo Alto Networks, Zscaler, Cloudflare, Akamai, Fortinet.

2. **[Advancing Voice Intelligence with New Models in the API](pages/openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/index.md)** (Product/Release, 2026-05-07) — Three new realtime audio API models: **GPT-Realtime-2** (GPT-5-class reasoning, 128K context, parallel tool calls, adjustable reasoning effort), **GPT-Realtime-Translate** (live translation across 70+ input languages / 13 output languages), **GPT-Realtime-Whisper** (streaming live transcription). Partner customers: Zillow, Glean, Deutsche Telekom, Vimeo, Priceline, Intercom.

3. **[Introducing Trusted Contact in ChatGPT](pages/openai.com/index/introducing-trusted-contact-in-chatgpt/index.md)** (Safety, 2026-05-07) — Optional feature: any adult ChatGPT user can nominate one trusted contact (friend, family, caregiver) who may receive an alert if OpenAI's systems — after trained human review (target: under 1 hour) — detect a serious self-harm crisis in the user's conversations. Notifications do not include chat transcripts. Developed with the American Psychological Association and 260+ physicians across 60 countries.

4. **[Parloa](pages/openai.com/index/parloa/index.md)** (Startup story, 2026-05-08) — Berlin-based Parloa builds an enterprise AI Agent Management Platform (AMP) for voice-driven customer service, using GPT-4.1, GPT-5-mini, and GPT-5.4. Published alongside the voice AI launch as a coordinated customer story.

### Notable updates

- **API Pricing** (`/api/pricing/`) — GPT-realtime-1.5 replaced by **GPT-Realtime-2** at $24/1M output tokens (up from $16/1M, a **+50% price increase**). Two new per-minute models added: GPT-Realtime-Translate at $0.034/min and GPT-Realtime-Whisper at $0.017/min.

- **Advanced Account Security** (`/index/advanced-account-security/`) — Minor but potentially meaningful edit: references to enrolling "on web" were removed, suggesting the feature may now be available beyond the web interface (mobile, etc.).

- **Four privacy policies** all updated on 2026-05-07 (evening UTC): `/policies/services-privacy-policy/`, `/policies/communications-privacy-policy/`, `/policies/services-communications-privacy-policy/`, `/policies/us-privacy-policy/`. Page content diffs show no visible text change — likely metadata/backend CMS update, possibly reflecting data handling for the new Trusted Contact feature.

- **B2B Signals article title changed** — "How frontier enterprises are building an AI advantage" renamed to "How frontier firms are pulling ahead." This propagated as a sidebar update across ~25 Global Affairs, news, and policy pages, accounting for most of the 127 `<lastmod>` updates.

### Removals

None confirmed. The 122 apparent absences trace entirely to the 403-blocked B2B customer stories sub-sitemap.

### Stats

| Metric | Count |
|---|---|
| Total URLs (verified sitemaps) | 1,161 |
| Sub-sitemaps | 33 of 34 fetched (1 × HTTP 403) |
| URLs added | 4 |
| URLs removed | 0 confirmed |
| URLs with lastmod updated | 127 |
| Anomalies | 1 (near-future timestamp) + 1 fetch failure |
| URL status unknown (failed sitemap) | 122 |

Full analysis: [`runs/2026-05-08T09-15Z/analysis.md`](runs/2026-05-08T09-15Z/analysis.md) | Diff: [`runs/2026-05-08T09-15Z/diff.json`](runs/2026-05-08T09-15Z/diff.json)

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

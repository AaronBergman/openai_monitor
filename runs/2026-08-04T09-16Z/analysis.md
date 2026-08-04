# Run 2026-08-04T09-16Z — Analysis

**Fetch time:** 2026-08-04T09:16:57Z
**Baseline:** 2026-08-03T09-18Z (consecutive day)
**Sitemap totals:** 1551 URLs (was 1547) across 35 sub-sitemaps — +4 added, 97 updated, 0 removed

## Anomalies

None. Specifically checked and clear:
- **Future-dated lastmod:** none. Latest lastmod observed was `https://openai.com/science/` at 2026-08-04T09:15:39Z, ~78s before fetch time (2026-08-04T09:16:57Z) — plausible, not future-dated.
- **Backward-moving lastmod:** none. All 97 updated URLs' new lastmod > old lastmod (verified programmatically).
- **Backdated new URLs:** none. All 4 added URLs have lastmod within the last day (2026-08-03T20:21Z through 2026-08-04T07:59Z), consistent with first_seen today.
- **Reappeared URLs:** none. Cross-checked all 4 added URLs against `state/known_urls.json` — none previously seen.
- **Sub-sitemap migrations:** none. Full multi-membership comparison (a URL can legitimately belong to more than one sub-sitemap) found zero URLs whose set of containing sub-sitemaps changed between snapshots.
- **Sub-sitemap count:** unchanged at 35 (same set of section names as 2026-08-03).

## Significant updates

### "Apple is getting this wrong" (new page, see below) — headline event
Not a sitemap "update" (it's new), but the most newsworthy item of the run: OpenAI published a public, combative rebuttal to Apple's trade-secrets lawsuit against two former Apple employees (Chang Liu, Tang Tan) now at OpenAI. The post includes screenshots of iMessages and OpenAI-vs-Apple-counsel email threads that OpenAI says undercut Apple's account of events. See "New pages" below for detail.

### Sitewide nav/template update (propagated to every page refetched this run)
Every one of the 97 refetched pages that render the standard header/footer picked up the same navigation change versus their last-captured snapshot:
- Footer "More" section gained a **"Supply Co."** link (`/supply/`) — this section (OpenAI's branded merch store) already existed in the sitemap (e.g. `/supply/product/blossom-hat/`) from earlier runs; today's change is only that it's now linked from the global footer nav, not that it's new.
- "Business" nav menu gained **"Customer Stories"** (`/business/customer-stories/`) and **"Partner Network"** (`/business/partners/`) links.
- The "Latest Advancements" sidebar widget now lists **GPT-5.6** in place of **GPT-5.3 Instant** (GPT-5.5 and GPT-5.4 unchanged in the list).
- A rendering artifact appeared on at least two pages (`model-disproves-discrete-geometry-conjecture`, `academy/research`, `academy/writing`): the in-page table-of-contents block now renders twice in a row. Likely a template regression from the same deploy, not a content change; flagged for awareness, not fixed by us.

This is template-level, not unique to any one page — it shows up in the diff only for the 97 pages whose sitemap lastmod happened to bump this run (the sitemap-lastmod signal under-counts template-wide changes, consistent with prior runs' findings, e.g. 2026-06-07).

### research/verify — new audio format supported
The upload widget's supported-formats list gained **OGG**: "PNG, JPG, WEBP, MP3, WAV, AAC, FLAC, OPUS, PCM" → "...FLAC, OGG, OPUS, PCM". Small but genuine product change to the AI-content-detection tool.

### business/partners/ (directory index) — roster change
**SK Inc. AX** added (new partner page, see below) and **TCS** (Tata Consultancy Services) removed from the partner logo grid. TCS never had its own dedicated partner subpage in this repo's tracked sitemap history, so this is a listing-level removal only — no URL was removed from the sitemap.

### index/disrupting-malicious-uses-of-ai-stop-news-2024 — formatting change to malicious-domain list
The four domains listed as associated with the described scam operation had their bracket-defanging removed: `Euronewstop[.]co[.]uk` → `Euronewstop.co.uk` (and similarly for the other three). Same domains, same content — just re-formatted from the security-community convention of "defanging" domains (to prevent accidental clicks/auto-linking) to plain dotted form. Not itself a link (no markdown anchor), so low risk, but worth noting as a formatting regression on a security-content page.

### index/ten-advances-in-mathematics — further micro-copyedit
Third day in a row this page has changed. Today: item 2's list-item punctuation changed from a colon to a period ("Binary and spherical codes:" → "Binary and spherical codes."), matching the style of the other list items. Purely cosmetic, no wording or claim change (unlike the 2026-08-03 softening of the lead paragraph).

### index/how-ai-is-expanding-what-people-do-at-work — related-content rotation
"Keep reading" strip swapped in a link to "Building abundant intelligence" (Jul 31) in place of "How news organizations use AI to advance their vital missions" (Jul 22). Routine editorial rotation.

## Routine updates (noise)

- **76 `/business/partners/*` pages** (Accenture, Accenture Federal Services, AIWorks, Algorithmic Intelligence, Altimetrik, Altudo, Artefact, Artium, Bain, Blank Metal, Booz Allen Hamilton, BCG, Capco, Capgemini, CDW, Chieftns, Clarinet, Cloudwerx, Cognita Reply, Cognizant, Corca, Deepsense.ai, Dentsu Japan, Eliza, Endava, EPAM, Ernst & Young, Fellow Intelligence, Fractal, Fujitsu, Globant, HCLTech, Infosys, Insurgence, KPMG, Mantel, McKinsey, Merantix Momentum, ML6, Nablon AI, NTT DATA, Pathfindr, PwC, Recursive, Rosetree Solutions, Samsung SDS, SB OAI Japan GK, Sia, Slalom, Snorkel AI, Statworx, Thinking Machines Data Science, Tredence, Tribe AI, Unit8, ZS) — picked up only a partner-tier-badge image cache-busting parameter (`?dpl=...`) from a platform redeploy, no text changed.
- **3 of those partner pages** (Blend360, Boston Consulting Group, CGI) additionally rendered a different nav/header A/B variant on this fetch vs. their last snapshot — same server-side experiment already logged in the 2026-08-01 and 2026-08-03 runs, not a new site change.
- **26 pages had `<lastmod>` bumped with zero detectable content change** (silent CMS touch, consistent with a pattern seen in prior runs): homepage, `academy/` (and 5 sub-pages: chatgpt-for-work, codex-for-work, research, using-chatgpt, writing — though `academy/research`, `academy/chatgpt-for-education`, and `academy/writing` did carry the sitewide nav diff described above), `api-fast-mode`, `api-reserved-tier`, `api-scale-tier`, `api/pricing`, `business/`, `business/openai-presence`, `business/partners/` (nav change only, logo-grid change covered above), `business/pricing`, `business/solutions/finance`, `business/why-openai/enterprises`, `form/enterprise-trusted-access-for-cyber`, `index/advancing-responsible-ai-across-europe`, `index/advancing-the-price-performance-frontier-with-gpt-5-6`, `index/chatgpt-for-academic-researchers`, `index/disrupting-malicious-uses-of-ai-criminal-scam-operation`, `index/introducing-gpt-live`, `index/scientific-computing-agentic-ai`, `policies/ad-tools-subprocessors`, `policies/ad-tools-terms`, `products/release-notes`, `student-collective`.
- **3 pages (`avatarin`, `bbva`, `unive`)** only rotated their "Keep reading" sidebar cards (now featuring the day's 3 new posts). No body-text changes.

## New pages

- **[Apple is getting this wrong](../../pages/openai.com/index/apple-is-getting-this-wrong/index.md)** (`/index/apple-is-getting-this-wrong/`, Company, published Aug 3) — OpenAI's public rebuttal to Apple's lawsuit alleging trade-secret theft by two former Apple employees (Chang Liu, Tang Tan) who now work at OpenAI. The post disputes Apple's account point-by-point: says Apple's outside counsel emailed the wrong person in February due to a name mix-up, that a claimed conversation with OpenAI's General Counsel never happened, and that Apple never raised the lawsuit's specific allegations until suing five months later. It publishes screenshotted iMessages (with most technical content redacted) showing Apple employees, after Liu's last day, asking him to help locate files via AirDrop/iCloud — which OpenAI frames as evidence Apple mismanaged its own offboarding access rather than Liu improperly retaining data. Also publishes the email chain between Apple's outside counsel and OpenAI's General Counsel Che Chang. This is an unusually combative, evidence-publishing post for OpenAI's blog and a notable escalation in the Apple dispute.
- **[Circles powers telco personalization with OpenAI technology](../../pages/openai.com/index/circles/index.md)** (`/index/circles/`, Customer story, Aug 3) — Singapore-based telco SaaS platform Circles (14 countries) built "CareX," a multi-agent support system on the OpenAI API delivering 65% autonomous resolution, plus "Xplore IQ" for personalized recommendations (22% ARPU increase, 9% churn reduction in Singapore). Also uses Codex internally for engineering (claims 29% efficiency gain). Standard enterprise customer-story format.
- **[How we built a realtime system for responsive voice AI in six months](../../pages/openai.com/index/continuous-voice-interaction-with-gpt-live/index.md)** (`/index/continuous-voice-interaction-with-gpt-live/`, Engineering, Aug 3, byline Justin Uberti & Zahan Malkani) — deep engineering writeup on GPT-Live, OpenAI's third-generation voice system (referenced as already "introduced" via `/index/introducing-gpt-live/`, first tracked in this repo since 2026-07-09). Describes moving from turn-based to full-duplex streaming voice inference, asynchronous delegation to frontier text models (e.g. GPT-5.5) without blocking the audio path, and a new open transport protocol they call WARP (WebRTC Abridged Roundtrip Protocol, submitted to IETF TSVWG) that cuts WebRTC session startup from 6 round trips to 1. Says this architecture already powers ChatGPT Voice's new computer-control/agent-coordination features and will underpin an upcoming "GPT-Live API."
- **[SK Inc. AX](../../pages/openai.com/business/partners/sk-inc-ax/index.md)** (`/business/partners/sk-inc-ax/`, Select-tier partner) — Korean "AX" (Advanced eXperience) services provider serving manufacturing, energy/chemicals, semiconductors, utilities, finance, and telecom, joint partner with AWS. New addition to OpenAI's partner directory (see roster-change note above re: TCS removal same run).

## Removals

None this run.

## Fetch failures

None. All 101 fetches (4 new + 97 updated pages) succeeded via `tools/html_to_md.py`; all passed sanity checks (no Cloudflare challenge pages, no sub-100-byte outputs).

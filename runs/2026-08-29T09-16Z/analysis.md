# Run 2026-08-29T09-16Z — Analysis

**Fetch time:** 2026-08-29T09:17:28Z UTC
**Baseline:** 2026-08-28T09-15Z (consecutive day)
**Sitemap sections:** 36 sub-sitemaps, 1622 -> 1622 unique URLs (2 added, 2 removed, net 0)

## Anomalies

### 1. Batch forward-lastmod touch across the entire `business/guides-and-resources/` collection
All 8 remaining untouched guides in that collection got their `<lastmod>` moved forward 15–38 days,
landing within a ~3-second window of each other (2026-08-28T19:01:19.258Z through 19:01:22.192Z):

| URL | old lastmod | new lastmod | delta |
|---|---|---|---|
| a-practical-guide-to-building-ai-agents | 2026-08-14T02:43:27.913Z | 2026-08-28T19:01:19.954Z | 14.7d |
| a-practical-guide-to-building-with-ai | 2026-07-28T02:04:33.745Z | 2026-08-28T19:01:19.426Z | 31.7d |
| chatgpt-business-smb-guide | 2026-08-13T23:37:27.545Z | 2026-08-28T19:01:20.117Z | 14.8d |
| chatgpt-usage-and-adoption-patterns-at-work | 2026-07-25T07:05:47.743Z | 2026-08-28T19:01:22.192Z | 34.5d |
| how-enterprises-are-scaling-ai | 2026-07-21T16:15:43.184Z | 2026-08-28T19:01:21.181Z | 38.1d |
| how-openai-uses-codex | 2026-08-13T23:14:42.985Z | 2026-08-28T19:01:21.175Z | 14.8d |
| identifying-and-scaling-ai-use-cases | 2026-08-13T23:48:03.947Z | 2026-08-28T19:01:19.258Z | 14.8d |
| inside-gpt5-our-best-model-for-work | 2026-08-14T02:10:06.423Z | 2026-08-28T19:01:20.775Z | 14.7d |
| staying-ahead-in-the-age-of-ai | 2026-08-13T23:37:37.303Z | 2026-08-28T19:01:20.146Z | 14.8d |
| the-state-of-enterprise-ai-2025-report | 2026-07-23T20:46:09.653Z | 2026-08-28T19:01:21.394Z | 35.9d |

Rendered-text diff on all 10 pages: byte-for-byte identical content. This reads as a bulk CMS
republish/reindex of the whole guides collection (e.g., a shared template or tagging update touching
every record without altering the article bodies), not a wave of real edits. Flagged so none of these
get mistaken for updated guides.

### 2. Large lone forward-lastmod jump, zero content change
[`/index/core-dump-epidemiology-data-infrastructure-bug/`](../../pages/openai.com/index/core-dump-epidemiology-data-infrastructure-bug/index.md):
lastmod jumped from 2026-07-06T16:30:57.356Z to 2026-08-28T18:51:36.224Z (+53.1 days) with no
rendered-text change. Same pattern as yesterday's GPT Rosalind false-alarm case — flagged explicitly
so it is not read as a new infrastructure incident.

### 3. URL rename: `/gpt-rosalind/` → `/rosalind/`
The GPT-Rosalind product landing page moved from `/gpt-rosalind/` (removed from the sitemap today) to
a new `/rosalind/` URL, which now carries a full rebrand: "Rosalind" as OpenAI's life-sciences brand,
"Rosalind Workbench" as the orchestrated product, and a new "Rosalind Biodefense" program section. This
is a page migration, not a real removal — see Notable updates below. The original announcement post
`/index/introducing-gpt-rosalind/` is untouched and still lives at its original URL.

No future-dated `<lastmod>` values, no backwards-moving `<lastmod>` values, no backdated new URLs (both
of today's 2 new URLs carry Aug 28–29, 2026 lastmods, consistent with same-day publication), no
disappeared-then-reappeared URLs, and no genuine sub-sitemap section membership changes (0 URLs moved
between sections). The two long-standing 404s (`/brand-old/`, `/index/inworld-ai-DO-NOT-PUBLISH/`)
remain listed, unchanged from every prior run since bootstrap. All 65 page fetches (2 new + 63 updated)
succeeded on the first attempt — 0 fetch failures.

## Significant updates

### Cursor loses access to OpenAI models following SpaceX acquisition
New page: [`/index/our-decision-on-cursor-following-its-acquisition-by-spacex/`](../../pages/openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/index.md)
(Aug 28, 2026). OpenAI notified SpaceX it will wind down the contract supplying OpenAI models to
Cursor, with a proposed shutoff date of **November 12, 2026** — the maximum notice period the contract
allows, given to maximize the transition window for developers. OpenAI's stated reason: it "cannot be
confident that SpaceX will use our technology within our terms of service," citing (1) Twitter/X
(now part of SpaceX) breaking a prior OpenAI contract after Musk's 2022 acquisition, and (2) Musk's
2026 sworn admission that xAI (also now part of SpaceX) had distilled OpenAI data in violation of
OpenAI's terms. The post also references an unreleased upcoming model codenamed **"Astra"** and links
to a page titled "Responding to next-frontier critical cyber capabilities," framing the decision partly
as heightened pre-release scrutiny of who gets access to more capable future models. OpenAI says it
worked with Cursor for "nearly four years" and wants to support affected developers through the
transition.

### GPT-Rosalind rebrands as "Rosalind," gains a Workbench product and a Biodefense program
`/gpt-rosalind/` is gone; [`/rosalind/`](../../pages/openai.com/rosalind/index.md) is the new landing
page. Rosalind is now positioned as OpenAI's full life-sciences brand rather than a single model page:
- **Rosalind Workbench** — an "orchestrated workspace" combining GPT-Rosalind with connected scientific
  tools, offering an "Explore mode" (open, general scientific Q&A) and a gated "Research mode" (apply
  for access) for more complex biological work.
- **GPT-Rosalind access widened**: copy now reads "now with expanded access for eligible organizations,"
  vs. the original April "research preview... for qualified customers" framing.
- **Rosalind Biodefense** — a new named program for "trusted developers and public-health teams
  building defensive applications," covering early detection, preparedness, diagnostics, response, and
  medical countermeasures, with its own application form (`/form/rosalind-biodefense-program/`, which
  already existed in the sitemap — this is the first page to link to it).
- The old dedicated request form, `/form/life-sciences-access/`, was removed outright; access now
  routes through `chatgpt.com/r/...` request links embedded directly on `/rosalind/`.
- New customer quote from Novo Nordisk CEO Mike Doustdar; other named partners: Thermo Fisher
  Scientific, Moderna, Oracle Health and Life Sciences.
- Benchmark figures shown: +53.7% (Genebench), +18.0% (Medchem Bench), +19.6% (Labworkbench), +4.42%
  (LifeSci Bench) — all framed as "increase in performance per token," presumably vs. a prior model.

### Collective cyber-defense letter gains 28 more signatories
[`/collective-cyberdefense/`](../../pages/openai.com/collective-cyberdefense/index.md) (published
yesterday) grew from 128 to **156** co-signing organizations, with zero signatories removed. Notable
new joiners: GitHub, Databricks, Datadog, CoreWeave, PayPal, Nokia, AT&T, BCG, Booz Allen, Mizuho,
Samsara, Tailscale, Bugcrowd, Chainguard, Netskope, Dragos, and others — a mix of major cloud/dev-tool
platforms, consultancies, and additional security vendors continuing to sign on.

## Routine, low-signal updates

- **31 of 63** updated pages: zero rendered-text difference — pure `<lastmod>`/rebuild touches (see
  Anomalies above for the two flagged outlier cases within this set).
- **27 of 63** updated pages: `business/partners/*` badge images only — a CDN cache-busting deployment
  query string (`?dpl=...`) changed on the partner-tier badge SVG, no visible content change.
- **~10 of 63** updated pages: related-articles carousel picked up today's new Cursor/SpaceX post
  (and, on a couple of pages, yesterday's Thailand post) — routine carousel rotation following any new
  publication, not independent news on those pages.
- `/index/how-enterprises-put-ai-to-work/` and `/signals/enterprise-data/`: a "key findings" bullet
  ("Early-career employees use AI more... a potential comparative advantage") appears to have moved
  from a shared summary widget on `/signals/enterprise-data/` to also render inline on
  `/index/how-enterprises-put-ai-to-work/` — looks like shared-component content placement, not a
  new finding.

## New pages

- [`/index/our-decision-on-cursor-following-its-acquisition-by-spacex/`](../../pages/openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/index.md) — see Significant updates above.
- [`/rosalind/`](../../pages/openai.com/rosalind/index.md) — see Significant updates above (replaces `/gpt-rosalind/`).

## Removals

- [`/gpt-rosalind/`](../../pages/openai.com/gpt-rosalind/index.md) — superseded by `/rosalind/` (rebrand; last-known snapshot preserved locally, see Anomalies #3).
- [`/form/life-sciences-access/`](../../pages/openai.com/form/life-sciences-access/index.md) — the old GPT-Rosalind request-access form was retired; access now routes through external `chatgpt.com/r/...` request links on `/rosalind/` (last-known snapshot preserved locally).

## Fetch failures

None. All 65 fetches (2 new + 63 updated) succeeded on the first attempt.

**Stats:** 1622 total URLs | 2 added | 63 updated | 2 removed | 3 anomalies | 36 sub-sitemaps | 2 persistent pre-existing 404s (unchanged)

# openai.com sitemap monitor — run 2026-07-19T09-17Z

**Fetch time:** 2026-07-19T09:21:47Z (root index + all 34 sub-sitemaps)
**Baseline:** 2026-07-18T09-15Z (prior committed run, PR #75)
**Sub-sitemaps:** 34/34 fetched successfully, 0 failures
**Total URLs:** 1,459 (unchanged from baseline)

## Anomalies

None. Checked:
- Future `<lastmod>` (later than fetch time): none.
- Backwards `<lastmod>` (moved earlier than the prior snapshot): none.
- Backdated new URLs: N/A — no URLs were added this run.
- Disappear/reappear against `state/known_urls.json`: N/A — no URLs were added or removed.
- Sub-sitemap migration (URL moving between sections): none. (Note: an early pass of this run's tooling flagged 121 apparent "migrations" and even a spurious 1,459 — both were artifacts of a bug in the analysis script, not real changes. Root cause: many OpenAI URLs legitimately appear in *more than one* sub-sitemap section simultaneously — e.g. `/index/gpt-5-6/` is listed in both `sitemap.xml_product` and `sitemap.xml_release`. A first script version tracked only a single "last writer wins" section per URL, which produced false migration signals purely from dict/glob iteration order. Fixed by tracking the *set* of sections each URL appears in and comparing sets; the corrected comparison found zero real differences. Recorded here for anyone reviewing `diff.json` from an earlier draft of this run.)

## Significant updates

None. All 10 lastmod-touched URLs were checked by diffing freshly fetched markdown against the prior git-committed version.

## Routine updates (10 total, lastmod-only or trivial)

| URL | Old lastmod | New lastmod | Content diff |
|---|---|---|---|
| `/api-priority-processing/` | 2026-07-10T12:21:29.541Z | 2026-07-19T08:27:42.409Z | 1-line: gained `Supply Co.` link in footer "More" nav (catching up to the site-wide nav rollout from 2026-07-16, PR #73 — this page had missed that batch) |
| `/devday/terms-and-conditions/` | 2026-07-18T08:34:05.248Z | 2026-07-19T08:26:08.416Z | none (byte-identical) |
| `/index/a-scorecard-for-the-ai-age/` | 2026-07-17T21:15:49.458Z | 2026-07-18T13:17:15.032Z | none (byte-identical) |
| `/index/advancing-ai-safety-through-state-and-federal-action/` | 2026-07-17T14:02:34.421Z | 2026-07-18T14:27:13.055Z | none (byte-identical) |
| `/index/cars24/` | 2026-07-18T08:11:39.400Z | 2026-07-19T01:28:14.536Z | none (byte-identical) |
| `/index/gpt-5-6/` | 2026-07-18T08:08:52.358Z | 2026-07-19T01:39:52.487Z | none (byte-identical) |
| `/index/previewing-gpt-5-6-sol/` | 2026-07-15T22:59:03.470Z | 2026-07-18T13:16:36.556Z | none (byte-identical) |
| `/index/unlocking-self-improvement-gpt-red/` | 2026-07-18T06:28:27.194Z | 2026-07-18T13:55:28.109Z | none (byte-identical) |
| `/index/why-teens-deserve-access-safe-ai/` | 2026-07-18T06:53:24.643Z | 2026-07-18T13:30:51.206Z | none (byte-identical) |
| `/products/release-notes/` | 2026-07-18T08:28:31.086Z | 2026-07-19T07:26:48.238Z | none (byte-identical) |

These read as backend cache-invalidation / republish timestamp bumps with no visible content change, except the one footer-nav catch-up noted above.

## New pages

None.

## Removals

None.

## Fetch failures

None. All 10 updated URLs fetched successfully via `tools/html_to_md.py` (curl-cffi, Chrome impersonation); no Cloudflare challenge pages encountered.

## Summary

A quiet consecutive day. No pages added or removed; 1,459 total URLs, same as yesterday. Ten pages received lastmod bumps but only one had a (trivial) visible change — a stray page picking up a footer nav link it had missed in an earlier site-wide rollout. No anomalies.

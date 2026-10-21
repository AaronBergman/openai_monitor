# Run 2026-10-21T09-16Z Analysis

**Fetch time:** 2026-10-21T09:16:43Z start (sitemap fetched ~09:17:01Z) | **Baseline:** 2026-09-28T09-17Z (23-day gap; routine missed Sep 29–Oct 20)
**Stats:** 2069 URLs | 88 added | 1519 updated | 4 removed | 60 anomalies | 43 sub-sitemaps | 0 fetch failures (1607 pages fetched)

## Anomalies
- 23-day observation gap; all deltas cumulative.
- 48 future_lastmod: all 1–26 s after recorded run start; pages re-rendered during fetch (957 URLs carry a 2026-10-21 lastmod). Benign timing artifact (recorded fetch time was run start, not sitemap fetch).
- 9 backdated_new_url (lastmod 11–20 days before first_seen; real publish during gap): board-guide-cybersecurity-ai, using-codex-across-the-software-development-lifecycle, plugins/sandstone, codex-originals, devday/2026, form/private-intelligence-interest, form/sign-in-with-chatgpt-interest, basis-tax-workbook-with-astra, lenfest-ai-collaborative-expansion.
- 3 reappeared: plugins/alpaca (last seen 2026-09-24), form/codex-ambassadors (2026-06-24), policies/row-privacy-policy (2026-05-27).
- No backwards lastmod, no sub-sitemap migrations (no URL both removed and added). New sub-sitemap count 43 vs 42.

## Significant updates
- Global footer rewrite on ~1,516 pages (GPT-6.1 Sol, GPT-6 Astra, GPT-5.4, Codex, Dots, OpenAI Status); Plugins link on ~793; "(opens in a new window)" labels.
- Legacy launch posts (o1, o3/o4-mini) gained "historical post / model retired" banners with links to current API models.
- Homepage lead rotated: GPT-6 and Intelligent UI for everyone (Oct 7), math results (Oct 6), Dots (Sep 29), Chip Ganassi Racing (Oct 7), Orchestra Bio (Oct 20).
- genebench-pro/case-studies: inline data tables dropped.

## Routine updates
Remaining ~1,500 pages: footer/nav-only diffs or image-URL query-string changes (e.g. `?w=3840&q=90` removed on SVGs).

## New pages (88)
Key: introducing-gpt-6-1-sol; gpt-6-for-everyone (Intelligent UI); introducing-dots; devday-2026-recap, devday/2026, practical-guide-building-gpt-6; openai-to-acquire-orchestra-bio; rosalind academic plan; disrupting-a-coordinated-model-distillation-campaign; disrupting-ai-enabled-false-front-operations; towards-safety-cases-for-frontier-ai-training; sharing-ai-progress-in-mathematics; new-chatgpt-ads-format-and-measurement; eu-text-provenance (opt-in API text watermarking); atlassian-partnership; business/marketplace; codex-originals; policies brazil-advertising-terms, sign-in-with-chatgpt-terms (+ interest form), row-privacy-policy. Also ~19 older business/learn guides (likely re-indexed), 6 business/partners, ~20 customer stories, new plugin pages. Full list in diff.json.

## Removals (4)
business/partners/pathfindr, business/plugins/mcp-server-for-wordpress, business/plugins/wordpress-com (apparently consolidated into plugins/wordpress and jetpack), form/ultrafast. Prior snapshots in git history.

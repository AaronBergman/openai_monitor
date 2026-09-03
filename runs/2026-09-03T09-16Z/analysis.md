# Run 2026-09-03T09-16Z — analysis

**Fetch time:** 2026-09-03T09:16:33Z – 09:17:40Z UTC (root index + 35 sub-sitemaps, all succeeded on first try; UA `Mozilla/5.0` over plain HTTP — no Cloudflare TLS-fingerprint challenge on the sitemap XML endpoints)
**Baseline:** 2026-09-02T09-16Z (consecutive day)
**Union of `<url><loc>` across all sub-sitemaps:** 1623 current vs. 1627 baseline

## 1. Anomalies

None found on any of the strict checks:

- **Future-dated `<lastmod>`** — zero URLs with a `<lastmod>` later than the 09:17:40Z fetch time.
- **Backwards-moving `<lastmod>`** — zero URLs whose `<lastmod>` regressed vs. its previously recorded value (checked all 212 updated URLs against `state/known_urls.json` history).
- **Backdated new URLs** — the 2 newly added URLs both have `<lastmod>` timestamps (2026-09-02T23:13:38Z and 2026-09-02T22:54:36Z) within hours of first appearing in our snapshot; no evidence of pre-existing content surfacing late.
- **Reappeared URLs** — neither added URL has any prior `known_urls.json` entry; they are genuinely new, not previously-removed pages coming back.
- **Section migrations** — zero URLs moved from one sub-sitemap section to another between this run and the baseline.
- **Fetch failures** — all 214 page fetches (212 updated + 2 added) via `tools/html_to_md.py` succeeded on the first attempt; none returned a Cloudflare challenge page or sub-100-char response.

## 2. Diff summary

- **Added:** 2
- **Removed:** 6
- **Updated (`<lastmod>` changed):** 212
  - Of these, only **50** produced any visible difference in the fetched markdown; **162** are byte-for-byte identical to their prior snapshot (pure `<lastmod>`/CDN metadata touch, no content change).
  - Of the 50 with visible diffs, **37** are pure reorderings — the exact same set of lines/images present in both versions, just in a different order (client-rendered image galleries and "related content" carousels that render a different subset/order on each server pass). Confirmed by sorting normalized lines from both snapshots and finding identical multisets.
  - The remaining **13** contain genuinely new or removed text/links, detailed below.

## 3. Significant updates (real content changes)

- **[`/api/`](../../pages/openai.com/api/index.md)** — primary header/footer CTA changed from **"Try ChatGPT"** (linking to chatgpt.com) to **"Start building"** (linking to `platform.openai.com/?utm_internal_source=openai_api`). This shifts the API landing page's top call-to-action from driving ChatGPT signups to driving platform/API signups. A "Realtime API" paragraph and a Zillow customer blurb also moved position on the page (no text change).
- **[`/products/release-notes/`](../../pages/openai.com/products/release-notes/index.md)** — new dated entry: **"ChatGPT for iOS updates: cross-host attachments, task priority, and reliability"** (Codex, Sep 1 2026, GA). New features: attachments now work across all connected hosts including Windows/Linux and support Photo Library videos; press-and-hold to attach recent photos; a new Priority view for running/unread/awaiting-response tasks; queued prompts now sync with the connected host and send even while backgrounded; long-running tasks show live working time; task menus can copy the thread ID. Plus reliability fixes to task-list loading, reconnects, streaming, and side-chat persistence.
- **[`/index/chatgpt-ads-expands-across-europe/`](../../pages/openai.com/index/chatgpt-ads-expands-across-europe/index.md)** — existing Aug 18 article picked up an **"Update on August 31, 2026"** note: self-service access to ChatGPT Ads via Ads Manager is now live across the 31 European markets originally announced, with a signup pointer to `ads.openai.com`.
- **[`/business/plugins/`](../../pages/openai.com/business/plugins/index.md)** — the connector/plugin directory listing dropped its **Azure DevOps** card and added/promoted an **Aha!** card (`/business/plugins/aha/` already existed in the sitemap with an unchanged `<lastmod>` — it was simply newly surfaced in this listing, not newly published). This tracks with the sitemap removal below.
- **[`/index/gpt-5-6/`](../../pages/openai.com/index/gpt-5-6/index.md)** — minor editorial reformat: six inline benchmark callouts (Agents' Last Exam, Artificial Analysis Coding Agent Index, BrowseComp, ExploitBench, GeneBench Pro, Aggregate RSI capability) were moved from scattered inline positions earlier in the article to a single consolidated block near the end. No wording or claims changed — pure restructuring.
- **[`/business/partners/slalom/`](../../pages/openai.com/business/partners/slalom/index.md)** — bio copy lightly edited (curly-quote apostrophes, and a closing sentence added: "Learn more about Slalom's AI consulting services."). Partner-tier badge image also cache-busted (new CDN deploy hash, same badge).
- **[`/business/partners/ernst-and-young/`](../../pages/openai.com/business/partners/ernst-and-young/index.md)** — partner-tier badge image cache-busted only; no visible content change.
- **Related-content carousel refresh, 5 pages** — [`stampli`](../../pages/openai.com/index/stampli/index.md), [`gilbert-tobin`](../../pages/openai.com/index/gilbert-tobin/index.md), [`polimill`](../../pages/openai.com/index/polimill/index.md), [`loveholidays`](../../pages/openai.com/index/loveholidays/index.md), and [`daybreak`](../../pages/openai.com/daybreak/index.md) all swapped one "you might also like"-style card: the new **ATV Big Air Tour** customer story replaced an older Healthcare-connect card. `daybreak/` and [`business/learn/`](../../pages/openai.com/business/learn/index.md) also picked up a card for the new **Agent security in the enterprise** guide, displacing older cards (Cybersecurity in the Intelligence Age; the "Inside GPT-5" guide). This is a downstream effect of today's two additions, not an independent editorial change.

## 4. Routine, low-signal updates

- **37 of 212** updated pages: pure carousel/gallery reordering — same images/examples, different display order. Affected pages include several GPT model announcements (`gpt-5-4`, `gpt-5-5`, `gpt-5-5-instant`, `introducing-gpt-5-4-mini-and-nano`, `introducing-new-capabilities-to-gpt-rosalind`, `strengthening-societal-resilience-with-rosalind-biodefense`, etc.), the ChatGPT Images galleries, the health-intelligence Q&A widget, and several product/solutions hub pages. No underlying content change.
- **162 of 212** updated pages: `<lastmod>` bumped in the sitemap but the fetched markdown is byte-for-byte identical to the prior snapshot — pure metadata/CDN cache-bust touches with no visible page change.

Full machine-readable breakdown: [`diff.json`](diff.json).

## 5. New pages

- **[Agent security in the enterprise](../../pages/openai.com/business/learn/agent-security-enterprise/index.md)** (`/business/learn/agent-security-enterprise/`, lastmod 2026-09-02T23:13:38Z) — a practical guide to deploying autonomous agents safely in enterprise settings. Fits the same "business/learn" guide format as recent enterprise-focused content, and is immediately cross-linked from the `/business/learn/` and `/daybreak/` hub pages (see §3).
- **[ATV Big Air Tour turned 3 days of work into 3 hours with ChatGPT](../../pages/openai.com/index/atv-big-air-tour/index.md)** (`/index/atv-big-air-tour/`, lastmod 2026-09-02T22:54:36Z) — customer story about an events/motorsports company using ChatGPT to compress a multi-day production workflow into hours. Immediately cross-linked from several customer-story pages (see §3).

## 6. Removals

Six third-party app/plugin integration pages dropped out of the sitemap entirely, all previously listed under either `apps-project-management` or `apps-go-to-market`:

- `/business/plugins/azure-devops/` (was `apps-project-management`)
- `/business/plugins/basecamp/` (was `apps-project-management`)
- `/business/plugins/help-scout/` (was `apps-go-to-market`)
- `/business/plugins/intercom/` (was `apps-go-to-market`)
- `/business/plugins/teamwork-com/` (was `apps-project-management`)
- `/business/plugins/zoho-desk/` (was `apps-go-to-market`)

All six had been stable in the sitemap since at least 2026-07-10 (or 2026-08-15 for Azure DevOps). Their removal coincides with the `/business/plugins/` index page dropping its Azure DevOps card the same day (§3) — this reads as a deliberate pruning of the third-party connector catalog rather than an accidental drop. Last known snapshots remain in git history (`git log -- pages/openai.com/business/plugins/<name>/index.md`).

## 7. Fetch failures

None. All 214 page fetches succeeded on the first attempt.

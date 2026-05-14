# Run Analysis: 2026-05-14T09-15Z

**Fetch time:** 2026-05-14T09:15:53Z  
**Baseline:** 2026-05-13T09-15Z  
**Sub-sitemaps:** 32  
**Total URLs (current):** 1,301  
**Added:** 3 | **Removed:** 1 | **Updated:** 340 | **Anomalies:** 2

---

## 1. Anomalies

### Near-future `lastmod` timestamps (minor timing artifact)

Two existing pages had their `lastmod` timestamp advance by ~15–22 seconds beyond the fetch time (i.e., OpenAI's CMS updated the timestamp while we were fetching the sitemap):

| URL | Claimed `lastmod` | Our fetch time |
|-----|-------------------|----------------|
| `https://openai.com/index/accelerating-cyber-defense-ecosystem/` | 2026-05-14T09:16:15.304Z | 2026-05-14T09:15:53Z |
| `https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/` | 2026-05-14T09:16:11.604Z | 2026-05-14T09:15:53Z |

**Assessment:** This is a benign race condition — the sitemap XML was generated fractionally before these pages' cache-bust timestamps propagated. Both are known, existing pages about OpenAI's cybersecurity products (GPT-5.5 for cyber defense). No action required; will resolve in tomorrow's run.

---

## 2. New Pages (3 added)

### HIGH SIGNAL: TanStack npm Supply Chain Attack Response
**URL:** `https://openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack/`  
**Lastmod:** 2026-05-14T04:36:33Z  
**Saved:** `pages/openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack/index.md`

OpenAI published a security disclosure on May 13, 2026, regarding the ["Mini Shai-Hulud"](https://digital.nhs.uk/cyber-alerts/2026/cc-4781) supply chain attack that compromised the TanStack npm library. Key details:

- **Two OpenAI employee devices** were infected by malware delivered via the compromised TanStack npm package.
- Attackers gained **unauthorized access to a limited subset of internal source code repositories**.
- **Credential material was exfiltrated** from those repositories, including code-signing certificates for iOS, macOS, and Windows applications.
- OpenAI found **no evidence of compromise to user data, production systems, or intellectual property**.
- **Action required for macOS users:** Update all OpenAI macOS apps (ChatGPT Desktop, Codex App, Codex CLI, Atlas) **by June 12, 2026**. Apps not updated will stop working on that date when the compromised certificate is revoked.
- Windows and iOS users do not need to take action.
- OpenAI has blocked further notarization using the compromised certificates, and is coordinating with Apple to monitor for misuse.

This is a significant security disclosure. The incident also references a prior "Axios incident" (previously documented as `/index/axios-developer-tool-compromise/`) suggesting an ongoing pattern of supply chain targeting against OpenAI's development infrastructure.

Context: OpenAI's new page `accelerating-cyber-defense-ecosystem` and `gpt-5-5-with-trusted-access-for-cyber` (about cybersecurity products and partnerships) are updating their related-article carousels to feature this new disclosure prominently.

---

### Codex Engineering Deep-Dive: Windows Sandbox
**URL:** `https://openai.com/index/building-codex-windows-sandbox/`  
**Lastmod:** 2026-05-13T22:05:30Z  
**Saved:** `pages/openai.com/index/building-codex-windows-sandbox/index.md`

An engineering blog post by David Wiesen (Member of Technical Staff), published May 13, 2026, detailing the technical challenge of building a secure sandbox for the Codex coding agent on Windows. Key points:

- **Problem:** Windows lacks built-in sandbox primitives comparable to macOS Seatbelt or Linux seccomp/bubblewrap. Windows AppContainer, Windows Sandbox VM, and Mandatory Integrity Control labels were all evaluated and rejected as inadequate for Codex's needs.
- **Solution:** OpenAI built a custom two-phase sandbox:
  1. "Unelevated sandbox" (first prototype): Used Windows ACLs + low-integrity tokens + firewall rules to restrict writes and network access — no admin elevation required.
  2. "Elevated sandbox" (final): Redesigned with better compatibility across enterprise developer environments.
- **Goal:** Give Windows Codex users the same default "safe" mode (file reads everywhere, writes inside workspace only, no internet by default) that macOS and Linux Codex users already had.

This post fits with OpenAI's ongoing push to make Codex a first-class experience on all platforms. The `gpt-5-5-with-trusted-access-for-cyber` and `accelerating-cyber-defense-ecosystem` pages updated their related-article carousels to surface this post.

---

### American Express × ChatGPT Business Credit Card
**URL:** `https://openai.com/business/amex-chatgpt-business-credit/`  
**Lastmod:** 2026-05-13T17:13:46Z  
**Saved:** `pages/openai.com/business/amex-chatgpt-business-credit/index.md`

A new co-branded landing page for American Express Business Platinum and Business Gold cardholders. Key details:

- Offers **up to $300/year in statement credits** on US purchases of ChatGPT Business.
- Promoted via data from an "Amex Trendex survey" claiming 87% of small business owners using AI save time, 81% reduce manual work, 73% improve productivity.
- Replaces/migrates the previous URL `https://openai.com/amex-chatgpt-business/` (removed this run), which was the old Amex partnership page with a different URL structure.

---

## 3. Removed Pages (1)

### `https://openai.com/amex-chatgpt-business/`
**Last known lastmod:** 2026-05-12T16:14:03Z

This URL has been removed from the sitemap. It is directly replaced by the newly added `https://openai.com/business/amex-chatgpt-business-credit/`, which moves the Amex partnership page into the `/business/` URL hierarchy and sharpens the page around the "business credit" benefit specifically. The page title changed from the generic "amex-chatgpt-business" framing to "The first-of-its-kind ChatGPT Business Credit."

---

## 4. Notable Updates (selected from 340)

**340 URLs show updated `lastmod` timestamps** compared to yesterday's baseline. However, diffing the actual markdown content of a representative sample (homepage, API pricing, brand, codex, workspace-agents, and both cyber pages) shows **zero substantive content changes** — the timestamps are being bumped by OpenAI's CMS cache-invalidation pipeline without real page edits. This is a routine pattern seen on previous runs and is not significant.

Exceptions (carousel/related-article updates only):

- **`https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/`** — Related articles carousel updated: replaced "Running Codex safely at OpenAI" with "Building a safe, effective sandbox to enable Codex on Windows" (new post), and "Introducing Advanced Account Security" with "Our response to the TanStack npm supply chain attack" (new post). Content is otherwise unchanged.
- **`https://openai.com/index/accelerating-cyber-defense-ecosystem/`** — Same related-articles carousel update as above.
- **`https://openai.com/`** (homepage) — Minor CTA reordering: "Learn about ChatGPT Business" link added to the hero section CTA row; "Stories" link removed from that row. The quick-access buttons now read: Learn about ChatGPT Business | Talk with ChatGPT | Research | API Platform.

---

## 5. Summary Statistics

| Metric | Value |
|--------|-------|
| Sub-sitemaps | 32 |
| Total URLs (current) | 1,301 |
| Added | 3 |
| Removed | 1 |
| Updated (lastmod) | 340 |
| Substantive content changes | ~3 (carousel updates + homepage CTA) |
| Anomalies | 2 (benign near-future timestamps) |
| Fetch failures | 0 |

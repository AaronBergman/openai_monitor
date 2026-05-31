Skip to main content

[](</>)

  * [Research](</research/index/>)
  * Products
  * [Business](</business/>)
  * [Developers](</api/>)
  * [Company](</about/>)
  * [Foundation(opens in a new window)](<https://openaifoundation.org>)



Log in[Try ChatGPT(opens in a new window)](<https://chatgpt.com/>)

  * Research
  * Products
  * Business
  * Developers
  * Company
  * [Foundation(opens in a new window)](<https://openaifoundation.org>)



[Try ChatGPT(opens in a new window)](<https://chatgpt.com/>)Login

OpenAI

Table of contents

  * How Codex Security works
  * Supporting the open source community
  * Get started
  * Appendix



March 6, 2026

[Product](</news/product-releases/>)[Security](</news/security/>)

# Codex Security: now in research preview

Loading…

Share

Today we’re introducing Codex Security, our application security agent. It builds deep context about your project to identify complex vulnerabilities that other agentic tools miss, surfacing higher-confidence findings with fixes that meaningfully improve the security of your system while sparing you from the noise of insignificant bugs.

Context is essential when evaluating real security risks, but most AI security tools simply flag low-impact findings and false positives, forcing security teams to spend significant time on triage. At the same time, agents are accelerating software development, making security review an increasingly critical bottleneck. Codex Security addresses both challenges. By combining agentic reasoning from our frontier models with automated validation, it delivers high-confidence findings and actionable fixes so teams can focus on the vulnerabilities that matter and ship secure code faster.

Formerly known as [_Aardvark_ ⁠](<https://openai.com/index/introducing-aardvark/>), Codex Security began last year as a private beta with a small group of customers. In early internal deployments, it surfaced a real SSRF, a critical cross-tenant authentication vulnerability, and many other issues which our security team patched within hours. Early deployments with external testers helped us improve how users provide relevant product context and move from onboarding to securing their code. We also significantly improved the quality of our findings over the course of the beta: scans on the same repositories over time show increasing precision, in one case cutting noise by 84% since initial rollout. We’ve reduced the rate of findings with over-reported severity by more than 90%, and false positive rates on detections have fallen by more than 50% across all repositories. These improvements help Codex Security better align reported severity with real-world risk and reduce unnecessary triage burden for security teams, and we expect the signal-to-noise ratio to continue to improve.

Starting today, Codex Security is rolling out in research preview to ChatGPT Pro, Enterprise, Business, and Edu customers via Codex web with free usage for the next month.

## How Codex Security works

Codex Security leverages OpenAI’s frontier models and the Codex agent. It can reduce noise and accelerate remediation by grounding vulnerability discovery, validation, and patching in system-specific context.

  1. **Build system context and create an editable threat model:** After configuring a scan, it analyzes your repository to understand the security-relevant structure of the system and generates a project-specific threat model that can capture what the system does, what it trusts, and where it is most exposed. Threat models can be edited to keep the agent aligned with your team.
  2. **Prioritize and validate issues:** Using the threat model as context, it searches for vulnerabilities and categorizes findings based on expected real-world impact in your system. Where possible, it pressure-tests findings in sandboxed validation environments to distinguish signal from noise. Users can see this analysis in the validated findings. When Codex Security is configured with an environment tailored to your project, it can validate potential issues directly in the context of the running system. That deeper validation can reduce false positives even further and enable the creation of working proof-of-concepts, giving security teams stronger evidence and a clearer path to remediation.
  3. **Patch issues with full system context:** Finally, Codex Security proposes fixes to the discovered issues that align with system intent and surrounding behavior. This enables patches that can improve security while minimizing regressions, making them safer to review and land. Users can filter the findings so they stay focused on what matters most to their team and has the highest security impact.



Codex Security can also learn from your feedback over time to improve the quality of its findings. When you adjust the criticality of a finding, it can use that feedback to refine the threat model and improve precision on subsequent runs as it learns what matters in your architecture and risk posture.

It’s designed to operate at scale and surface the highest-confidence findings with easy-to-accept patches. Over the last 30 days, Codex Security scanned more than 1.2 million commits across external repositories in our beta cohort, identifying 792 critical findings and 10,561 high-severity findings. Critical issues appeared in under 0.1% of scanned commits, showing that the system can identify security impacting issues in large volumes of code while minimizing noise to reviewers.

NETGEARvLLMRaptive

> "As a company laser-focused on product security, NETGEAR was pleased to join the early access program, and the results exceeded expectations. Codex Security integrated effortlessly into our robust security development environment, strengthening the pace and depth of our review processes. Its findings were impressively clear and comprehensive, often giving the sense that an experienced product security researcher was working alongside us."

— Chandan Nandakumaraiah, Head of Product Security at NETGEAR and Member of CVE Board

## Supporting the open source community

Open source software forms the foundation of modern systems, including our own. We've been using Codex Security to scan the open-source repositories we rely on most, sharing high impact security findings we identify with maintainers to help strengthen that foundation.

In our conversations with maintainers, a consistent theme emerged: the challenge isn’t a lack of vulnerability reports, but too many low-quality ones. Maintainers told us they need fewer false positives and a more sustainable way to surface real security issues without creating additional triage burden. These conversations helped shape how we’re supporting the open source community with Codex Security. Rather than generating large volumes of speculative findings, we are building a system that prioritizes high-confidence issues that maintainers can act on quickly.

As part of this work, we reported critical vulnerabilities to a number of widely used open-source projects including [_OpenSSH_ ⁠(opens in a new window)](<https://github.com/openssh/openssh-portable/commit/c991273c18afc490313a9f282383eaf59d9c13b9>), [_GnuTLS_ ⁠(opens in a new window)](<https://lists.gnupg.org/pipermail/gnutls-help/2025-July/004883.html>), [_GOGS_ ⁠(opens in a new window)](<https://github.com/gogs/gogs/security/advisories/GHSA-p6x6-9mx6-26wj>), [_Thorium_ ⁠(opens in a new window)](<https://www.cve.org/CVERecord?id=CVE-2025-35430>) libssh, PHP, and Chromium, and more. Fourteen CVEs have been assigned with dual reporting on two — we've shared some examples in the Appendix.

We recently started onboarding an initial cohort of open-source maintainers into Codex for OSS, our program to support the ecosystem with free ChatGPT Pro and Plus accounts, code review, and Codex Security. Projects like vLLM have already used Codex Security to find and patch issues as part of their normal workflow.

We plan to expand the program in the coming weeks so more maintainers have a direct path to better security, stronger review workflows, and support for the open-source work the ecosystem depends on. If you’re an open-source maintainer and interested, [_please get in touch_ ⁠](<https://openai.com/form/codex-for-oss>).

## Get started

We’ll be rolling out Codex Security access to ChatGPT Enterprise, Business, and Edu customers over the coming days. Check out [_our docs_ ⁠(opens in a new window)](<https://developers.openai.com/codex/security>) to learn more about setting up Codex Security for your team.

## Appendix

Examples of high impact OSS vulnerabilities discovered by Codex Security:

  * GnuTLS certtool Heap-Buffer Overflow (Off-by-One) — [CVE-2025-32990⁠(opens in a new window)](<https://www.cve.org/CVERecord?id=CVE-2025-32990>)
  * GnuTLS Heap Buffer Overread in SCT Extension Parsing — [CVE-2025-32989⁠(opens in a new window)](<https://www.cve.org/CVERecord?id=CVE-2025-32989>)
  * GnuTLS Double-Free in otherName SAN Export — [CVE-2025-32988⁠(opens in a new window)](<https://www.cve.org/CVERecord?id=CVE-2025-32989>)
  * 2FA Bypass GOGS — [CVE-2025-64175⁠(opens in a new window)](<https://github.com/advisories/GHSA-p6x6-9mx6-26wj>)
  * Unauth bypass GOGS — [CVE-2026-25242⁠(opens in a new window)](<https://github.com/advisories/GHSA-fc3h-92p8-h36f>)
  * Path traversal (arbitrary write) — download_ephemeral, download_children (agent) — [CVE-2025-35430⁠(opens in a new window)](<https://www.cve.org/CVERecord?id=CVE-2025-35430>)
  * LDAP injection (filters & DN) — LdapUserMap::new / get_unix_info / basic_auth_ldap — [CVE-2025-35431⁠(opens in a new window)](<https://www.cve.org/CVERecord?id=CVE-2025-35430>)
  * Unauthenticated DoS & mail abuse — resend_email_verification — [CVE-2025-35432⁠(opens in a new window)](<https://www.cve.org/CVERecord?id=CVE-2025-35432>) , [CVE-2025-35436⁠(opens in a new window)](<https://nvd.nist.gov/vuln/detail/CVE-2025-35436>)
  * Session not rotated on password change — User::update_user — [CVE-2025-35433⁠(opens in a new window)](<https://www.cve.org/CVERecord?id=CVE-2025-35433>)
  * Disabled TLS verification — Elasticsearch client — [CVE-2025-35434⁠(opens in a new window)](<https://www.cve.org/CVERecord?id=CVE-2025-35433>)
  * DoS: division by zero — /api/streams/depth/.../{split} — [CVE-2025-35435⁠(opens in a new window)](<https://www.cve.org/CVERecord?id=CVE-2025-35435>)
  * gpg-agent stack buffer overflow via PKDECRYPT --kem=CMS (ECC KEM) — [CVE-2026-24881⁠(opens in a new window)](<https://www.cve.org/CVERecord?id=CVE-2026-24881>)
  * Stack-based buffer overflow in TPM2 PKDECRYPT for RSA and ECC due to missing ciphertext length validation — [CVE-2026-24882⁠(opens in a new window)](<https://www.cve.org/CVERecord?id=CVE-2026-24881>)
  * CMS/PKCS7 AES-GCM ASN.1 params stack buffer overflow — [CVE-2025-15467⁠(opens in a new window)](<https://www.cve.org/CVERecord?id=CVE-2026-24881>)
  * PKCS#12 PBMAC1 PBKDF2 keyLength overflow + MAC bypass — [CVE-2025-11187⁠(opens in a new window)](<https://www.cve.org/CVERecord?id=CVE-2025-11187>)



  * [2026](</news/?tags=2026>)
  * [Codex](</news/?tags=codex>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

![1x1](https://images.ctfassets.net/kftzwdyauwt9/6ui4uYfTTbR4xbiFRcqEfo/81d973f14bea720820f692271f6c6834/square.png?w=3840&q=90&fm=webp)

[Strengthening societal resilience with Rosalind BiodefenseProductMay 29, 2026](</index/strengthening-societal-resilience-with-rosalind-biodefense/>)

![Personal finance in ChatGPT > Media > Cover](https://images.ctfassets.net/kftzwdyauwt9/4zSr4YNWXIEYz20piN2bxf/6f9a561be6055802914aee0a3bb671d7/ArtCard-Personal-Finance.png?w=3840&q=90&fm=webp)

[A new personal finance experience in ChatGPTProductMay 15, 2026](</index/personal-finance-chatgpt/>)

![1x1 Art Card](https://images.ctfassets.net/kftzwdyauwt9/7qVT9WlLKfgGLPC5W77ei6/a24fd3f13b754378759959aa77cd8f5d/1_1.png?w=3840&q=90&fm=webp)

[Work with Codex from anywhereProductMay 14, 2026](</index/work-with-codex-from-anywhere/>)

Our Research

  * [Research Index](</research/index/>)
  * [Research Overview](</research/>)
  * [Research Residency](</residency/>)
  * [Economic Research](</signals/>)



Latest Advancements

  * [GPT-5.5](</index/introducing-gpt-5-5/>)
  * [GPT-5.4](</index/introducing-gpt-5-4/>)
  * [GPT-5.3 Instant](</index/gpt-5-3-instant/>)
  * [GPT-5.3-Codex](</index/introducing-gpt-5-3-codex/>)



Safety

  * [Safety Approach](</safety/>)
  * [Security & Privacy](</security-and-privacy/>)
  * [Trust & Transparency](</trust-and-transparency/>)



ChatGPT

  * [Explore ChatGPT(opens in a new window)](<https://chatgpt.com/overview>)
  * [Business](<https://chatgpt.com/business/business-plan>)
  * [Enterprise](<https://chatgpt.com/business/enterprise>)
  * [Education](<https://chatgpt.com/business/education>)
  * [Pricing(opens in a new window)](<https://chatgpt.com/pricing>)
  * [Download(opens in a new window)](<https://chatgpt.com/download>)



API Platform

  * [Platform Overview](</api/>)
  * [Pricing](</api/pricing/>)
  * [API log in(opens in a new window)](<https://platform.openai.com/login>)
  * [Documentation(opens in a new window)](<https://developers.openai.com/api/docs>)
  * [Developer Forum(opens in a new window)](<https://community.openai.com/>)



For Business

  * [Business Overview](</business/>)
  * [Solutions](</solutions/>)
  * [Contact Sales](</contact-sales/>)



Company

  * [About Us](</about/>)
  * [Our Charter](</charter/>)
  * [Foundation(opens in a new window)](<https://openaifoundation.org>)
  * [Careers](</careers/>)
  * [Brand](</brand/>)



Support

  * [Help Center(opens in a new window)](<https://help.openai.com/>)



More

  * [News](</news/>)
  * [Stories](</stories/>)
  * [Academy](</academy/>)
  * [Livestreams](</live/>)
  * [Podcast](</podcast/>)
  * [RSS](<https://openai.com/news/rss.xml>)



Terms & Policies

  * [Terms of Use](</policies/terms-of-use/>)
  * [Privacy Policy](</policies/privacy-policy/>)
  * [Other Policies ](</policies/>)



[(opens in a new window)](<https://x.com/OpenAI>)[(opens in a new window)](<https://www.youtube.com/OpenAI>)[(opens in a new window)](<https://www.linkedin.com/company/openai>)[(opens in a new window)](<https://github.com/openai>)[(opens in a new window)](<https://www.instagram.com/openai/>)[(opens in a new window)](<https://www.tiktok.com/@openai>)[(opens in a new window)](<https://discord.gg/openai>)

OpenAI © 2015–2026Your privacy choices

EnglishUnited States

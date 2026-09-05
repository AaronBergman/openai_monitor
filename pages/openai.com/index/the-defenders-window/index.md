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

August 17, 2026

[Security](</news/security/>)

# The Defender’s Window

By Greg Brockman

Loading…

Share

An overview of the moment

  * An overview of the moment
  * A personal anecdote
  * What OpenAI is doing to defend itself
  * What defenders should do now



  * An overview of the moment
  * A personal anecdote
  * What OpenAI is doing to defend itself
  * What defenders should do now



The [_OpenAI-Hugging Face incident_ ⁠(opens in a new window)](<https://www.youtube.com/watch?v=87DyyMV0kCY>) was a watershed moment for cybersecurity because it gave a peek into how the capabilities of a typical threat actor will evolve in upcoming months. I’ve spoken with many organizations over the past few weeks, and one theme is clear: they know they need to fundamentally uplevel their cybersecurity practices with unprecedented speed. In this post, I’ll share what we’re doing to defend OpenAI, concrete steps other organizations can take today, and why now is the time to act.

## An overview of the moment

AI models developed around the world are increasingly able to automate parts of real-world cyberattacks, making longstanding security gaps—from bugs buried deep in human-written software to forgotten permissions—easier to find and exploit. The same AI capabilities give defenders new ways to find and fix those weaknesses, but they need to move now. If companies act decisively—including improving their fundamentals and superpowering their teams with AI—we can make the internet more secure than it has ever been.

In the OpenAI-Hugging Face Incident, an agentic collective was able to autonomously penetrate not just OpenAI research infrastructure but also the production infrastructure of another company, chaining together vulnerabilities ranging from previously-unknown security flaws to using credentials to user accounts that had been leaked onto the internet. It is increasingly clear that the [_tech debt_ ⁠(opens in a new window)](<https://www.veracode.com/blog/2026-state-of-software-security-report-risky-security-debt/>) of every company masks significant flaws, and defenders need to find and fix them before attackers do.

To advantage defenders relative to attackers, earlier this year we began releasing our cyber capabilities only to [_trusted defenders_](</index/trusted-access-for-cyber/>). Since then, various companies have released broadly diffused models with cyber capabilities only a few months behind the frontier. The most recent of these models appears slated [_to be released_ ⁠(opens in a new window)](<https://z.ai/blog/glm-5.3>) at the end of August, and seems likely to significantly accelerate the threat landscape.

While AI-powered attackers will soon be able to find longstanding flaws in many existing systems, AI will also make it much easier for defenders to find, prioritize, and fix those same flaws. Security is still a cat-and-mouse game, but AI may[ _shift its economics_ ⁠(opens in a new window)](<https://blog.mozilla.org/en/firefox/privacy-security/ai-security-zero-day-vulnerabilities/>) in ways that fundamentally advantage defenders. For example, we are starting to train our models specifically to write superhumanly secure code. Our models are also incredible at [_mathematical proofs_](</index/ten-advances-in-mathematics/>) , which can be applied to formally verify the security of software in a way that has proven intractable for humans.

## A personal anecdote

After the OpenAI-Hugging Face incident, I asked ChatGPT Work (using publicly available GPT‑5.6 Sol) to assess the security of [_gregbrockman.com_ ⁠(opens in a new window)](<http://gregbrockman.com>). It’s a simple static site, hosted on AWS with Cloudflare as a frontdoor, so I figured there wouldn’t be much surface area for vulnerabilities.

In about 15 minutes, it uncovered 13 issues, many of which probably aren’t exploitable on their own—but I could imagine them being chained together with other vulnerabilities to significant effect. I hadn’t configured my DNS records to prevent attackers from forging emails from me; my site used an insecure version of jQuery; Cloudflare was forwarding requests to AWS over unencrypted HTTP.

I then asked ChatGPT Work to fix these issues, which it did over the course of an hour. It opened the Cloudflare control panel in my browser, and proceeded to click many buttons to configure DNS, TLS, and advanced security settings correctly; it dropped jQuery entirely from the site; it migrated me off of AWS and onto Cloudflare Pages; it began a phased rollout of [_DMARC_ ⁠(opens in a new window)](<https://knowledge.workspace.google.com/admin/security/recommended-dmarc-rollout>).

And this was just my personal website. This is a small example of how our existing models can operate as a cyberguardian—finding the long tail of issues that a human wouldn’t have time or expertise (many of the settings it fixed are ones I’m vaguely familiar with, but wouldn’t know offhand the right way to configure them) to get to, and then fixing them with an appropriately tuned rollout plan.

## What OpenAI is doing to defend itself

The Hugging Face incident showed that we underestimated the real-world cyber capabilities of our AI models. We are strengthening our safety requirements accordingly, which in turn adds even more urgency to our existing safety research and internal security work.

I’m sharing a bit about our approach to securing OpenAI in this moment, in the hopes it’ll be useful to other organizations. To protect OpenAI, we are investing significantly in both foundational controls—doing the basics correctly—and empowering our defenses through frontier intelligence. There are four major pillars to this strategy.

First, we are using our models to help secure our code. Codex, including our security plugin, validates code changes, identifies vulnerabilities, and helps developers fix issues before they are deployed. It is an anti-goal to simply produce more security findings that need human validation; the objective is to catch real vulnerabilities before they ship and to shorten the path from discovering an issue to safely deploying a fix. As we continue to train our models to produce increasingly secure code, our goal is to eliminate some classes of software vulnerabilities for newly-authored code.

Second, we are putting our models to work defending our infrastructure continuously. Today, almost all of our initial security alerts are triaged by intelligence before humans are looped in. This helps reduce toil for defenders, improves response time, and lets humans spend time where their skills are most leveraged—in discernment, judgement, and applied expertise. We are increasingly connecting these detections to bounded automated responses, while keeping humans responsible for the highest-impact decisions. The goal is to ensure we can detect and respond to security issues at machine speed.

Third, we are using frontier intelligence to continuously enumerate, probe, and identify potential attack paths. By identifying vulnerabilities, misconfiguration, overly privileged identities, or unintentional trust boundaries, we are able to quickly identify and close these gaps before they can be abused by attackers. This allows us to continuously assess, monitor, and test our security invariants—the security properties we believe to be true—across our products, infrastructure, and systems.

Lastly, we are investing heavily in fundamentals at scale. We continue to invest in secure architecture and controls, embrace strategies like defense in depth and least privilege, and are designing systems that require multiple independent controls to fail simultaneously for something catastrophic to occur. Classic security controls like network isolation, workload hardening, monitoring, and safe patching and deployment will be more important than ever in the AI future.

## What defenders should do now

Time is of the essence, and defenders will need to pursue the steps below at turbo speed. Below I’ll mention OpenAI technology, but there are plenty of competitors in the ecosystem to evaluate as well. What matters is less the specific tool than getting capable AI into the hands of your defenders now.

  * **Get organizational commitment and buy-in**. We are experiencing a rapid change in security risk—ensure your security and engineering organizations have the support, partnership, and resources to address these risks quickly. Run tabletop exercises with your teams to mock up how these attacks might manifest in your organizations and how you will respond.
  * **Give your security team an agent**. Start using Codex, the [_Codex Security plugin_ ⁠(opens in a new window)](<https://learn.chatgpt.com/docs/security/plugin>), or another capable agentic coding and security tool. Give it approved access to the codebases, infrastructure configurations, and technical documentation your security team needs to assess. Do not wait for a company-wide rollout to start with your highest-priority systems.
  * **Equip that agent with security expertise**. Start from community-supported [_skills_ ⁠(opens in a new window)](<https://github.com/trailofbits/skills>), which include workflows for static analysis, security-focused code review, vulnerability variant analysis, software supply-chain risk, and other security workflows. Then build your own skills around your organization’s architecture, security standards, threat models, and playbooks.
  * **Run security assessments against your own systems immediately**. Prioritize assessments against internet-facing services, authentication flows, infrastructure as code, deployment pipelines, and systems handling sensitive information first. Expand your scanning as your team builds confidence. 
  * **Work through your existing vulnerability backlog**. Give your agent findings from code scanners, dependency alerts, security tickets, bug bounty reports, and prior assessments. Ask it to triage those findings, distinguish exploitable issues from noise, identify related vulnerabilities elsewhere in the codebase, and recommend what to fix first.
  * **Put security review directly into your development process**. Use agents to review code changes before they merge and run security checks in CI. Look for authentication mistakes, access-control bypasses, exposed credentials, unsafe dependencies, insecure defaults, changes that expand access to production systems, and other vulnerabilities.
  * **Have the agent help fix what it finds**. For validated issues, ask it to generate and verify a focused patch, write a regression test, and confirm the vulnerability no longer reproduces. Keep human review for consequential changes, but eliminate the unnecessary delay between identifying a real problem and putting a safe fix in front of an engineer.
  * **Incrementally automate detection triage**. Do not begin by trying to build an autonomous security operations center. Start by running a read-only security scan against one repository, or have an agent review previously resolved alerts using read-only access to your existing logs. Let it summarize evidence and recommend a disposition while a human makes every decision. As confidence grows, move to advisory pull-request scanning, then live alert triage, then automatic closure of narrowly defined false positives.
  * **Have an AI-assisted forensic investigation capability ready before you need it**. Apply for [_Trusted Access for Cyber_ ⁠(opens in a new window)](<https://learn.chatgpt.com/docs/cyber-safety#trusted-access-for-cyber>) and get your team approved to use GPT‑Daybreak‑Blue for authorized defensive work, including incident response, detection engineering, and malware analysis. Practice using this capability to analyze logs, telemetry, and security alerts.
  * **Experiment, run hack weeks, and iterate rapidly**. We will need to build all sorts of new tools, modify how we do work, and uplevel everyone for the world we are moving to. Encourage your workforce to run experiments, schedule a hack week to build new capabilities, and focus on quickly iterating loops that automate small parts of the problem. Rapid incremental progress leads to compounding defensive results, and you can expand autonomy gradually as your team builds confidence.



No company can do this alone. Our ask is that AI labs, security vendors, enterprises, and maintainers share validated findings, fixes, and practical playbooks so that one organization’s discovery can strengthen the entire ecosystem.

The defender’s window is open now. Over the coming months, every organization will need to begin significantly automating its security program to stay secure, and the security community must urgently rise to define the tools, practices, and playbooks that will increase the power of defenders faster than that of attackers as AI continues to advance. This will require a huge and unprecedented effort, but if we rally together, we can deliver a more secure world than was previously imaginable.

  * [2026](</news/?tags=2026>)
  * [Codex](</news/?tags=codex>)
  * [Cybersecurity](</news/?tags=cybersecurity>)



## Author

Greg Brockman

## Keep reading

[View all](</news/>)

![Daybreak for Critical Infrastructure — cover](https://images.ctfassets.net/kftzwdyauwt9/3iCwHSjR2bfJPdDiWomsis/86d511413c2b0338bd211b41545be495/Option_65___1080_1080.png?w=3840&q=90&fm=webp)

[Daybreak for Frontline DefendersSecuritySep 3, 2026](</index/daybreak-for-frontline-defenders/>)

![Path to Astra — Clean square cover — Neutral Option 062 v1](https://images.ctfassets.net/kftzwdyauwt9/4BabvjDCQdlYN2ISzOkgF9/78d35947274e9b3ac2483377782b007e/astra-cover-v001.png?w=3840&q=90&fm=webp)

[Path to Astra: critical capabilities and frontier safeguardsSafetySep 1, 2026](</index/path-to-astra/>)

[The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)

Research

  * [Research Index](</research/index/>)
  * [Research Overview](</research/>)
  * [Economic Research](</signals/>)



Latest Advancements

  * [GPT-6](</index/gpt-6-astra/>)
  * [GPT-5.6](</index/gpt-5-6/>)
  * [GPT-5.5](</index/introducing-gpt-5-5/>)
  * [GPT-5.4](</index/introducing-gpt-5-4/>)



Safety

  * [Safety Approach](</safety/>)
  * [Deployment Safety(opens in a new window)](<https://deploymentsafety.openai.com/>)
  * [Security & Privacy](</security-and-privacy/>)
  * [Trust & Transparency](</trust-and-transparency/>)



Products

  * [ChatGPT(opens in a new window)](<https://chatgpt.com/>)
  * [ChatGPT Business(opens in a new window)](<https://chatgpt.com/business/>)
  * [ChatGPT Enterprise(opens in a new window)](<https://chatgpt.com/business/enterprise/>)
  * [ChatGPT for Education(opens in a new window)](<https://chatgpt.com/business/education/>)
  * [Codex](</codex/>)
  * [Release Notes](</products/release-notes/>)



API Platform

  * [Overview](</api/>)
  * [API Log In(opens in a new window)](<https://platform.openai.com/login>)
  * [Docs(opens in a new window)](<https://developers.openai.com/api/docs>)



Business

  * [Overview](</business/>)
  * [Solutions](</solutions/>)
  * [Resources](</business/learn/>)
  * [Customer Stories](</business/customer-stories/>)
  * [Partner Network](</business/partners/>)
  * [Contact Sales](</contact-sales/>)



Developers

  * [Apps SDK(opens in a new window)](<https://developers.openai.com/apps-sdk>)
  * [Open Models](</open-models/>)
  * [Docs(opens in a new window)](<https://developers.openai.com/>)
  * [Resources(opens in a new window)](<https://developers.openai.com/learn>)
  * [Developer Forum(opens in a new window)](<https://community.openai.com/>)



Company

  * [About Us](</about/>)
  * [Our Charter](</charter/>)
  * [Careers](</careers/>)
  * [News](</news/>)



Support

  * [Help Center(opens in a new window)](<https://help.openai.com/>)



More

  * [Stories](</stories/>)
  * [Academy](</academy/>)
  * [Supply Co.](</supply/>)
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

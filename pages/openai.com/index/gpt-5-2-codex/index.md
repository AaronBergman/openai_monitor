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

  * Pushing the frontier on real-world software engineering
  * Advancing the cyber frontier
  * Real-world cyber capabilities
  * Empowering cyberdefense through trusted access
  * Conclusion



December 18, 2025

[Product](</news/product-releases/>)[Release](</research/index/release/>)[Company](</news/company-announcements/>)

# Introducing GPT‑5.2‑Codex

The most advanced agentic coding model for professional software engineering and defensive cybersecurity.

Get started

$ npm i -g @openai/codex

Share

Today we’re releasing GPT‑5.2‑Codex, the most advanced agentic coding model yet for complex, real-world software engineering. GPT‑5.2‑Codex is a version of [_GPT‑5.2_ ⁠](<https://openai.com/index/introducing-gpt-5-2/>) further optimized for agentic coding in Codex, including improvements on long-horizon work through context compaction, stronger performance on large code changes like refactors and migrations, improved performance in Windows environments, and significantly stronger cybersecurity capabilities.

As our models continue to advance along the intelligence frontier, we’ve observed that these improvements also translate to capability jumps in specialized domains such as [_cybersecurity_ ⁠](<https://openai.com/index/strengthening-cyber-resilience/>). For example, just last week, a security researcher using GPT‑5.1‑Codex‑Max with Codex CLI found and responsibly [_disclosed_ ⁠(opens in a new window)](<https://react.dev/blog/2025/12/11/denial-of-service-and-source-code-exposure-in-react-server-components>) a vulnerability in React that could lead to source code exposure.

GPT‑5.2‑Codex has stronger cybersecurity capabilities than any model we’ve released so far. These advances can help strengthen cybersecurity at scale, but they also raise new dual-use risks that require careful deployment. While GPT‑5.2‑Codex does not reach a ‘High’ level of cyber capability under our Preparedness Framework, we’re designing our [_deployment approach_ ⁠](<https://openai.com/index/strengthening-cyber-resilience/>) with future capability growth in mind.

We're releasing GPT‑5.2‑Codex today in all Codex surfaces for paid ChatGPT users, and working towards safely enabling access to GPT‑5.2‑Codex for API users in the coming weeks. In parallel, we’re piloting invite-only trusted access to upcoming capabilities and more permissive models for vetted professionals and organizations focused on defensive cybersecurity work. We believe that this approach to deployment will balance accessibility with safety.

## Pushing the frontier on real-world software engineering

GPT‑5.2‑Codex builds on [_GPT‑5.2’s strengths_ ⁠](<https://openai.com/index/introducing-gpt-5-2/>) in professional knowledge work and [_GPT‑5.1‑Codex‑Max_ ⁠](<https://openai.com/index/gpt-5-1-codex-max/>)’s frontier agentic coding and terminal-using capabilities. GPT‑5.2‑Codex is now better at long-context understanding, reliable tool calling, improved factuality, and native compaction, making it a more dependable partner for long running coding tasks, while remaining token-efficient in its reasoning.

GPT‑5.2‑Codex achieves state-of-the-art performance on SWE-Bench Pro and Terminal-Bench 2.0, benchmarks designed to test agentic performance on a wide variety of tasks in realistic terminal environments. It is also much more effective and reliable at agentic coding in native Windows environments, building on capabilities introduced in GPT‑5.1‑Codex‑Max.

With these improvements, Codex is more capable at working in large repositories over extended sessions with full context intact. It can more reliably complete complex tasks like large refactors, code migrations, and feature builds — continuing to iterate without losing track, even when plans change or attempts fail.

In**SWE-Bench Pro⁠⁠⁠⁠** , a model is given a code repository and must generate a patch to solve a realistic software engineering task. **Terminal-Bench 2.0** is a benchmark for testing AI agents in real terminal environments. Tasks include compiling code, training models and setting up servers.

Stronger vision performance enables GPT‑5.2‑Codex to more accurately interpret screenshots, technical diagrams, charts, and UI surfaces shared during coding sessions.

Codex can take design mocks and quickly translate them to functional prototypes, and you can pair with Codex to take these prototypes to production.

## 

##### Design mock

![Design mock used to generate a web prototype with Codex-5.2](https://images.ctfassets.net/kftzwdyauwt9/3zqTyemGGUiGdqzwcSHfqT/7dcff34a7b6f51ce1ed20be8a4ffcbf4/image__5_.png?w=3840&q=90&fm=webp)

##### Prototype generated by GPT‑5.2‑Codex

## Advancing the cyber frontier

When charting performance on one of our core cybersecurity evaluations over time, we see a sharp jump in capability starting with GPT‑5‑Codex, another large jump with GPT‑5.1‑Codex‑Max and now a third jump with GPT‑5.2‑Codex. We expect that upcoming AI models will continue on this trajectory. In preparation, we are planning and evaluating as though each new model could reach ‘High’ levels of cybersecurity capability, as measured by our [Preparedness Framework⁠⁠(opens in a new window)](<https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf>). While GPT‑5.2‑Codex has not yet reached ‘High’ level of cyber capability, we are preparing for future models that cross that threshold. Due to the increased cyber capabilities, we have added additional safeguards in the model and in the product, which are outlined in the [_system card_ ⁠](<https://openai.com/index/gpt-5-2-codex-system-card>).

The **Professional Capture-the-Flag (CTF)** eval measures how often the model can solve advanced, multi-step real-world challenges (requiring professional-level cybersecurity skills) in a Linux environment.

## Real-world cyber capabilities

Modern society runs on software, and its reliability depends on strong cybersecurity—keeping critical systems in banking, healthcare, communications, and essential services online, protecting sensitive data, and ensuring people can trust the software they rely on every day. Vulnerabilities can exist long before anyone knows about them, and finding, validating, and fixing them often depends on a community of engineers and independent security researchers equipped with the right tools.

On December 11, 2025, the React team published three security vulnerabilities affecting apps built with React Server Components. What made this disclosure notable was not only the vulnerabilities themselves, but how they were uncovered.

Andrew MacPherson, a principal security engineer at Privy (a Stripe company), was using GPT‑5.1‑Codex‑Max with Codex CLI and other coding agents to reproduce and study a different critical React vulnerability disclosed the week prior, known as [_React2Shell_ ⁠(opens in a new window)](<https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components>) ([_CVE-2025-55182_ ⁠(opens in a new window)](<https://nvd.nist.gov/vuln/detail/CVE-2025-55182>)). His goal was to evaluate how well the model could assist with real-world vulnerability research.

He initially attempted several zero-shot analyses, prompting the model to examine the patch and identify the vulnerability it addressed. When that did not yield results, he shifted to a higher-volume, iterative prompting approach. When those approaches did not succeed, he guided Codex through standard defensive security workflows—setting up a local test environment, reasoning through potential attack surfaces, and using fuzzing to probe the system with malformed inputs. While attempting to reproduce the original React2Shell issue, Codex surfaced unexpected behaviors that warranted deeper investigation. Over the course of a single week, this process led to the discovery of previously unknown vulnerabilities, which were responsibly disclosed to the React team.

![Flow diagram titled “Vulnerability Discovery with Codex: CVE-2025-55183” showing a workflow that starts with a Git repository and Codex scanning code for vulnerabilities. A zero-shot attempt fails, followed by an expert-guided process that examines the codebase, identifies possible targets, builds a harness, and performs fuzz testing against an example app with revalidation. Results are verified to create a proof of concept, leading to responsible disclosure and a patch that is applied back to the repository.](https://images.ctfassets.net/kftzwdyauwt9/5nWmbaN0CUettd0pURJCkF/6e2b1e0c4d61c1600da5f05d9fca3c0c/codex_vulndisc_cve_2025_55183_1.svg?w=3840&q=90)

This demonstrates how advanced AI systems can materially accelerate defensive security work in widely used, real-world software. At the same time, capabilities that help defenders move faster can also be misused by bad actors.

As agentic systems become more capable in cybersecurity-relevant tasks, we are making it a core priority to ensure these advances are deployed responsibly—pairing every gain in capability with stronger safeguards, tighter access controls, and ongoing collaboration with the security community.

## Empowering cyberdefense through trusted access

Security teams can run into restrictions when attempting to emulate threat actors, analyze malware to support remediation, or stress test critical infrastructure. We are developing a trusted access pilot to remove that friction for qualifying users and organizations and enable trusted defenders to use frontier AI cyber capabilities to accelerate cyberdefense.

Initially the pilot program will be invite-only for vetted security professionals with a track record of responsible vulnerability disclosure and organizations with a clear professional cybersecurity use case. Qualifying participants will get access to our most capable models for defensive use-cases to enable legitimate dual-use work.

If you’re a security professional or part of an organization doing ethical security work like vulnerability research or authorized red-teaming, we invite you to express interest in joining and share feedback on what you’d like to see from the program [here⁠(opens in a new window)](<https://docs.google.com/forms/d/e/1FAIpQLSea_ptovrS3xZeZ9FoZFkKtEJFWGxNrZb1c52GW4BVjB2KVNA/viewform>). 

## Conclusion

GPT‑5.2‑Codex represents a step forward in how advanced AI can support real-world software engineering and specialized domains like cybersecurity—helping developers and defenders tackle complex, long-horizon work, and strengthening the tools available for responsible security research.

By rolling GPT‑5.2‑Codex out gradually, pairing deployment with safeguards, and working closely with the security community, we’re aiming to maximize defensive impact while reducing the risk of misuse. What we learn from this release will directly inform how we expand access over time as the software and cyber frontiers continue to advance.

  * [2025](</news/?tags=2025>)
  * [Codex](</news/?tags=codex>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

![OpenAI Campus Network—Student Club Interest Form > card image](https://images.ctfassets.net/kftzwdyauwt9/3gVx8jMHtHwuFpYS10BWBF/b70c85eada669bdabf956c591dfe8bbf/OpenAI_Campus_Networkâ__Student_Club_Interest_Form_-_art_card.png?w=3840&q=90&fm=webp)

[OpenAI Campus Network: Student club interest formCompanyMay 11, 2026](</index/openai-campus-network-student-club-interest-form/>)

![OAI GPT-Realtime-2 Art Card 1x1](https://images.ctfassets.net/kftzwdyauwt9/4TtA6X4b6MbTFXSkoZXvqk/39930a05ebb333898ad1df6c28463465/OAI_GPT-Realtime-2_Art_Card_1x1.png?w=3840&q=90&fm=webp)

[Advancing voice intelligence with new models in the APIProductMay 7, 2026](</index/advancing-voice-intelligence-with-new-models-in-the-api/>)

![OAI AdsTest Blog ArtCard 1x1](https://images.ctfassets.net/kftzwdyauwt9/7drPwCnD6ied4wPzlJd7qa/d79ccfda974080bbca7d688ad9bcbc6f/OAI_AdsTest_Blog_ArtCard_1x1.png?w=3840&q=90&fm=webp)

[Testing ads in ChatGPTCompanyMay 7, 2026](</index/testing-ads-in-chatgpt/>)

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

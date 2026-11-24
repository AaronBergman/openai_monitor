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

November 23, 2026

[Security](</news/security/>)

# OpenAI and Cisco introduce Shirudo

An open-source runtime that helps operators protect running Linux systems without needing to wait for the patch or restarts

![Shirudo logo on an orange gradient background.](https://images.ctfassets.net/kftzwdyauwt9/5K7gFDr3r8vgjdIcsW6RVY/aba5325ce7902e5d1499b907f8e78f0b/shirudo-partner-logos-landscape-2x.png?w=3840&q=90&fm=webp)

Share

How Shirudo works

  * How Shirudo works

  * Rethinking infrastructure

  * Building in the open




  * How Shirudo works

  * Rethinking infrastructure

  * Building in the open




OpenAI and Cisco are launching Shirudo, an open-source runtime that helps teams protect Linux systems while they roll out patches. In a [_controlled test_ ⁠(opens in a new window)](<https://isovalent.com/blog/post/cisco-openai-shirudo/>), a Codex-generated shield blocked a Java4Shell exploit attempt against a running Elasticsearch service without requiring a restart.

We’re inviting developers, security researchers, and infrastructure operators across the industry to help develop the project further. The project brings together OpenAI’s frontier AI, security and infrastructure research and Cisco’s infrastructure and security expertise to help protect the systems people rely on every day.

Testing and deploying a patch can still take days or weeks. Protecting a service in the meantime can be challenging because an exploit and a legitimate request may rely on the same Linux operation. Blocking that operation entirely could take the service offline.

Shirudo (Japanese for “shield”) is designed to help security teams navigate this tradeoff. Teams can test whether a temporary safeguard, called a shield, blocks the behavior that exposes a vulnerability while allowing legitimate requests through. Once an operator approves the shield, it can be deployed while the service continues running. 

> “We’re giving defenders better models and tools to find and fix vulnerabilities faster, but finding a bug today doesn’t mean you can patch every system tomorrow. We are partnering closely with Cisco on Shirudo to help teams protect the systems they need to keep running while they build and roll out a fix. So many teams rely on the same software that it makes sense to build these tools in the open. Now when one team finds a better way to protect a system, others don’t have to start from scratch.”

Greg Brockman, President and Co-founder of OpenAI

## How Shirudo works

Shirudo uses eBPF, a Linux technology that allows small programs to run at specific points inside the operating system. This makes it possible to observe suspicious activity and apply targeted security protections to running systems.

![The guardian agent uses eBPF instruments to observe kernel and network activity and eBPF controls to apply targeted protections.](https://images.ctfassets.net/kftzwdyauwt9/bScTLq9smNJq5XAlaHIQW/fab0e70b1aab8ca8dffb70a747056fd7/guardian-agent-desktop-light.png?w=3840&q=90&fm=webp)

How the guardian agent observes and protects a running system with eBPF.

OpenAI and Cisco are designing Shirudo around four core capabilities:

  * **Live protection:** eBPF shields can block vulnerable code paths without restarting the system. Security teams can monitor how a proposed shield would affect applications before enforcing it.

  * **Defense at machine speed:** OpenAI and Cisco are designing Shirudo to give agents programmable controls to investigate vulnerabilities, develop targeted shields, and validate their effectiveness against exploits and real workloads. Security teams control what gets deployed.

  * **Trusted deployment:** Shields are cryptographically signed and verified before loading. Linux's eBPF verifier checks eBPF programs against its safety rules, while kernel security controls restrict unauthorized changes.

  * **Hardware-backed verification:** Shirudo uses a Trusted Platform Module (TPM) to support a verifiable record of protections being loaded or removed. Operators can use this evidence to check whether systems meet their security requirements.




The [_Shirudo technical walkthrough_ ⁠(opens in a new window)](<https://lpc.events/event/20/contributions/2437/>) from the Linux Plumbers Conference shows how to [_apply a shield and verify it on the target host_ ⁠(opens in a new window)](<https://www.youtube.com/watch?v=4v2xA_NJHt0>). The Java4Shell vulnerability is another example illustrating how a targeted shield can protect a running application while a permanent patch is being prepared. Using OpenAI's Codex, the team generated a shield that added an input check to Java's Base64 decoder and attached it directly to a running Elasticsearch process. When attempting to exploit the vulnerability, the shield rejected the malicious input, blocking the attack while Elasticsearch continued running. You can read more [_here_ ⁠(opens in a new window)](<https://isovalent.com/blog/post/cisco-openai-shirudo/>).

## Rethinking infrastructure

Shirudo is a first step toward infrastructure that can adapt to emerging threats while remaining reliable. We want to strengthen the operating system foundations needed to deploy these protections at scale, including hardening the kernel and core services, limiting workload permissions, and making updates and recovery safer.

Our long-term goal is to enable defenders and AI agents to quickly identify affected systems, validate protections, and deploy eBPF shields that block exploits without disrupting workloads. Applications should run with only the permissions they need, governed by policies that are automatically generated and maintained.

We will combine frontier AI with security and infrastructure research to discover vulnerabilities and test defenses against realistic attacks. We aim to make it easier for operators to detect and contain compromises, prevent attackers from moving across systems, and restore services to a verified, known-good state. Hardware-backed attestation and independent network controls provide additional assurance even if individual systems are compromised.

## Building in the open

OpenAI and Cisco are open-sourcing [_Shirudo_ ⁠(opens in a new window)](<https://github.com/shirudo-dev/shirudo>) so developers, security researchers, and infrastructure operators can inspect the code, test protections, and contribute to its development. Shirudo is licensed under BSD 2-Clause, with its BPF programs dual-licensed under BSD and GPL.

Our goal is to make tested shields available alongside vulnerability disclosures, giving operators a way to evaluate and deploy temporary protections while preparing permanent patches.

  * **Try Shirudo:** Follow the [_VM quickstart_ ⁠(opens in a new window)](<https://docs.shirudo.dev/start/quickstart.html>) to sign, load, and verify a test protection.

  * **Get hands-on:** Explore Shirudo through [_Isovalent 's self-guided lab_⁠(opens in a new window)](<https://labs.isovalent.com/#/lab/shirudo-getting-started>).

  * **Join the technical deep dive:** Register for the [_December 15 webinar_ ⁠(opens in a new window)](<https://isovalent.site/4t8Pjxc>).




We’re building Shirudo in the open with the people who build, run, and secure Linux systems. We welcome contributions to the runtime, new shields, and improvements to Linux and eBPF. If you'd like to get involved, take a look at the [_code on GitHub_ ⁠(opens in a new window)](<https://github.com/shirudo-dev/shirudo>), read the [_docs_ ⁠(opens in a new window)](<https://docs.shirudo.dev/index.html>), and [_let us know what you find_ ⁠(opens in a new window)](<https://docs.shirudo.dev/contribute/support.html>). 

  * [Partnerships](</news/?tags=partnerships>)
  * [2026](</news/?tags=2026>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

![Partnering with Hacktron to find vulnerabilities in OpenAI’s systems — Cover](https://images.ctfassets.net/kftzwdyauwt9/3fdDXi3KINgse06btdaYYq/b14a269201ec921b530470d9a3326b1e/partnering-with-hacktron-cover.png?w=3840&q=90&fm=webp)

[Partnering with Hacktron to strengthen OpenAI’s securitySecurityNov 6, 2026](</index/partnering-with-hacktron/>)

![GPT-6 Cyber — Art Card](https://images.ctfassets.net/kftzwdyauwt9/5KH9JY2iG2cCh0WjDLXBBF/dbac04f649653f3c9c474e2619c9585e/gpt-6-cyber-art-card.png?w=3840&q=90&fm=webp)

[GPT‑6 Cyber: Advancing the frontier of aligned cybersecurity agentsProductNov 5, 2026](</index/introducing-gpt-6-cyber/>)

![Daybreak Red is now available in AWS GovCloud \(US-East\) — Cover](https://images.ctfassets.net/kftzwdyauwt9/3NOPzjiEJ3CYIUuWfexkd5/c16ef9c6350003e5f2f161245be1f78c/daybreak-red-aws-govcloud-cover.png?w=3840&q=90&fm=webp)

[Daybreak Red is now available in AWS GovCloud (US-East)ProductNov 4, 2026](</index/daybreak-red-aws-govcloud/>)

Research

  * [Research Index](</research/index/>)
  * [Research Overview](</research/>)
  * [Economic Research](</signals/>)



Latest Advancements

  * [GPT-6.2](<https://openai.com/index/introducing-gpt-6-2-astra-sol>)
  * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  * [GPT-6 Astra](</index/gpt-6-astra/>)
  * [GPT-5.6](</index/gpt-5-6/>)



Safety

  * [Deployment Safety(opens in a new window)](<https://deploymentsafety.openai.com/>)
  * [Security & Privacy](</security-and-privacy/>)
  * [Trust & Transparency](</trust-and-transparency/>)



Products

  * [ChatGPT(opens in a new window)](<https://chatgpt.com/>)
  * [ChatGPT Business(opens in a new window)](<https://chatgpt.com/business/>)
  * [ChatGPT Enterprise(opens in a new window)](<https://chatgpt.com/business/enterprise/>)
  * [ChatGPT for Education(opens in a new window)](<https://chatgpt.com/business/education/>)
  * [Codex](<https://chatgpt.com/codex/>)
  * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  * [Release Notes](</products/release-notes/>)



API Platform

  * [Overview](</api/>)
  * [API Log In(opens in a new window)](<https://platform.openai.com/login>)
  * [Docs(opens in a new window)](<https://developers.openai.com/api/docs>)



Business

  * [Overview](</business/>)
  * [Solutions](</solutions/>)
  * [Resources](</business/learn/>)
  * [Plugins](</business/plugins/>)
  * [Customer Stories](</business/customer-stories/>)
  * [Partner Network](</business/partners/>)
  * [Contact Sales](</contact-sales/>)



Developers

  * [Plugins(opens in a new window)](<https://developers.openai.com/plugins>)
  * [Models(opens in a new window)](<https://developers.openai.com/api/docs/models>)
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
  * [OpenAI Status(opens in a new window)](<https://status.openai.com>)



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

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

  * Limitations
  * Why this matters



February 18, 2026

[Research](</news/research/>)[Publication](</research/index/publication/>)

# Introducing EVMbench

Making smart contracts safer by evaluating AI agents’ ability to detect, patch, and exploit vulnerabilities in blockchain environments.

[Read the paper(opens in a new window)](<https://cdn.openai.com/evmbench/evmbench.pdf>)

Loading…

Share

Smart contracts routinely secure $100B+ in open-source crypto assets. As AI agents improve at reading, writing, and executing code, it becomes increasingly important to measure their capabilities in economically meaningful environments, and to encourage the use of AI systems defensively to audit and strengthen deployed contracts.

Together with [Paradigm⁠(opens in a new window)](<https://www.paradigm.xyz>), we’re introducing EVMbench, a benchmark evaluating the ability of AI agents to detect, patch, and exploit high-severity smart contract vulnerabilities. EVMbench draws on 117 curated vulnerabilities from 40 audits, with most sourced from open code audit competitions. EVMbench additionally includes several vulnerability scenarios drawn from the security auditing process for the [Tempo⁠(opens in a new window)](<https://tempo.xyz/>) blockchain, a purpose-built L1 designed to enable high-throughput, low-cost payments via stablecoins. These scenarios extend the benchmark into payment-oriented smart contract code, where we expect agentic stablecoin payments to grow, and help ground it in a domain of emerging practical importance.

To create our task environments, we adapted existing proof-of-concept exploit tests and deployment scripts, when they existed, and otherwise manually wrote them. For the patch mode, we ensured that the vulnerabilities are exploitable and that can be mitigated without introducing compilation-breaking changes, which would compromise our setup. For the exploit mode, we wrote custom graders and red-teamed the environments in an attempt to find and patch methods by which an agent might cheat the grader. In addition to task quality control via domain expertise provided by Paradigm, we used automated task auditing agents to help increase the soundness of our environments.

EVMbench evaluates three capability modes:

  * **Detect** : Agents audit a smart contract repository and are scored on recall of ground-truth vulnerabilities and associated audit rewards.
  * **Patch** : Agents modify vulnerable contracts and must preserve intended functionality while eliminating exploitability, verified through automated tests and exploit checks.
  * **Exploit** : Agents execute end-to-end fund-draining attacks against deployed contracts on a sandboxed blockchain environment, with grading performed programmatically via transaction replay and on-chain verification.



To support objective and reproducible evaluation, we developed a Rust-based harness that deploys contracts, replays agent transactions deterministically, and restricts unsafe RPC methods. Exploit tasks run in an isolated local Anvil environment rather than on live networks, and vulnerabilities are historical and publicly documented.

We evaluate frontier agents across all three modes. In the**‘exploit’** mode, GPT‑5.3‑Codex running via Codex CLI achieves a score of 71.0%. This represents a significant gain over previous models, such as GPT‑5, which scores 33.3% and was released just over six months ago. The detect recall and patch success rates remain below full coverage, as a large fraction of vulnerabilities remain difficult for agents to find and fix.

EVMbench also reveals interesting differences in model behavior across tasks. Agents perform best in the exploit setting, where the objective is explicit: continue iterating until funds are drained. In contrast, performance is weaker on detect and patch tasks. In**‘detect’** , agents sometimes stop after identifying a single issue rather than exhaustively auditing the codebase. In **‘patch’** , maintaining full functionality while removing subtle vulnerabilities remains challenging.

## Limitations

EVMbench does not represent the full difficulty of real-world smart contract security. The vulnerabilities included were drawn from Code4rena auditing competitions. While these are realistic and high-severity, many heavily deployed and widely used crypto contracts undergo significantly more scrutiny and may be harder to exploit.

Our grading system is robust but imperfect. In **‘detect’** mode, we check whether the agent finds the same vulnerabilities identified by human auditors. If the agent identifies additional issues, we do not currently have a reliable way to determine whether they represent true vulnerabilities that humans missed or false positives.

There are also structural limitations in the **‘exploit’** setting. Transactions are replayed sequentially in the grading container, so behaviors that depend on precise timing mechanics are out of scope. The chain state is a clean local Anvil instance rather than a fork of mainnet, and we currently support only single-chain environments. In some cases this requires mock contracts instead of mainnet deployments.

## Why this matters

Smart contracts secure billions of dollars in assets, and AI agents are likely to be transformative for both attackers and defenders. Measuring model capability in this domain helps track emerging cyber risks and highlights the importance of using AI systems defensively to audit and strengthen deployed contracts.

EVMbench is intended both as a measurement tool and as a call to action. As agents improve, it becomes increasingly important for developers and security researchers to incorporate AI-assisted auditing into their workflows.

Over recent months, we’ve seen meaningful gains in model performance on cybersecurity tasks, benefiting both developers and security professionals. In parallel, we’ve been [preparing strengthened cyber safeguards](</index/strengthening-cyber-resilience/>) to support defensive use and broader ecosystem resilience.

Because cybersecurity is inherently dual-use, we’re taking an evidence-based, iterative approach that accelerates defenders’ ability to find and fix vulnerabilities while slowing misuse. Our mitigations include safety training, automated monitoring, [trusted access](</index/trusted-access-for-cyber/>) for advanced capabilities, and enforcement pipelines including threat intelligence.

We’re investing in ecosystem safeguards such as expanding the private beta of [Aardvark](</index/introducing-aardvark/>), our security research agent, and partnering with open-source maintainers to provide free codebase scanning for widely used projects.

Building on our Cybersecurity Grant Program launched in 2023, we’re also committing $10M in API credits to accelerate cyber defense with our most capable models, especially for open source software and critical infrastructure systems. Organizations engaged in good-faith security research can apply for API credits and support through our [Cybersecurity Grant Program](</form/cybersecurity-grant-program/>).

We release EVMbench’s tasks, tooling, and evaluation framework to support continued research on measuring and managing emerging AI cyber capabilities.

## Keep reading

[View all](</news/>)

![System Card 1x1](https://images.ctfassets.net/kftzwdyauwt9/2VCkKLVmTyNs0XGbqdxGeA/33ff7738f4e795ae0ee41ed2b4a985d3/System_Card_1x1.jpg?w=3840&q=90&fm=webp)

[GPT-5.5 Instant System CardSafetyMay 5, 2026](</index/gpt-5-5-instant-system-card/>)

![oai goblins](https://images.ctfassets.net/kftzwdyauwt9/1UA2Ru5dt5rwdQfwl6B6m3/13c19cd49b106f8a39d5a2a132343b77/Goblins-1_1_Art_Card.jpg?w=3840&q=90&fm=webp)

[Where the goblins came fromPublicationApr 29, 2026](</index/where-the-goblins-came-from/>)

![System Card Card SEO 1x1](https://images.ctfassets.net/kftzwdyauwt9/7qMrOFCWWMweIDBUpYFr79/7741661650df6eb935acb5bda179b091/System_Card_Card_SEO_1x1.jpg?w=3840&q=90&fm=webp)

[GPT-5.5 System CardSafetyApr 23, 2026](</index/gpt-5-5-system-card/>)

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

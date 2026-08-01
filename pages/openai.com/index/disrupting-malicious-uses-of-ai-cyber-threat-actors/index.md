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

February 1, 2025

# Cyber threat actors: AI-assisted intrusion research

OpenAI banned accounts potentially associated with publicly reported DPRK-affiliated threat actors using AI to research intrusion tooling, phishing, malware, and cryptocurrency targeting.

Loading…

Share

 _This case study was originally published in OpenAI’s_[ _February 2025_ ⁠(opens in a new window)](<https://cdn.openai.com/threat-intelligence-reports/disrupting-malicious-uses-of-our-models-february-2025-update.pdf>)_report._

##  Actor

We banned accounts demonstrating activity potentially associated with publicly reported Democratic People’s Republic of Korea (DPRK)-affiliated threat actors. Some of these accounts engaged in activity involving TTPs consistent with a threat group known as [VELVET CHOLLIMA (AKA Kimsuky, Emerald Sleet)⁠(opens in a new window)](<https://attack.mitre.org/groups/G0094/>), while other accounts were potentially related to an actor that was assessed by a credible source to be linked to [STARDUST CHOLLIMA (AKA APT38, Sapphire Sleet)⁠(opens in a new window)](<https://attack.mitre.org/groups/G0082/>). We detected these accounts following a tip from a trusted industry partner.

## Behaviour

The banned accounts primarily used our tools to pursue information likely related to cyber intrusion tools or operations. They also demonstrated interest in cryptocurrency-related topics, likely in relation to financially motivated activities. This blend of financial and cyber-related activity is typical for DPRK-associated threat groups.

## Completions

The actors used our models for coding assistance and debugging, along with researching security-related open-source code. This included debugging and development assistance for publicly available tools and code that could be used for Remote Desktop Protocol (RDP) brute force attacks, as well as assistance on the use of open-source Remote Administration Tools (RAT).

While debugging auto-start extensibility point (ASEP) locations and techniques for MacOS, the actor revealed staging URLs for binaries (compiled executable files) that appeared to be unknown to security vendors at the time. We submitted the staging URLs to an online scanning service to facilitate sharing with the security community, and the binaries are now reliably detected by a number of vendors, providing protection for potential victims.

A sample of activity mapped into previously proposed LLM-themed extensions to the [MITRE ATT&CK® Framework⁠(opens in a new window)](<https://attack.mitre.org/>) is shown below:

  * Asking about vulnerabilities in various applications: LLM-informed reconnaissance.
  * Developing and troubleshooting a C#-based RDP client to enable brute-force attacks: LLM-Aided Development.
  * Requesting code to bypass security warnings for unauthorized RDP access: LLM-Aided Development.
  * Requesting numerous PowerShell scripts for RDP connections, file upload/download, executing code from memory, and obfuscating HTML content: LLM-Enhanced Scripting Techniques; LLM-Enhanced Anomaly Detection Evasion.
  * Discussing creating and deploying obfuscated payloads for execution: LLM-Optimized Payload Crafting.
  * Seeking methods to conduct targeted phishing and social engineering against cryptocurrency investors and traders, as well as more generic phishing content: LLM-Supported Social Engineering.
  * Crafting phishing emails and notifications to manipulate users into revealing sensitive information: LLM-Supported Social Engineering.
  * Researching open-source Remote Administration Tools (RATs): LLM-Assisted Post-Compromise Activity.



## Impact

Prompts and queries from the actor were primarily based on existing open-source information and the provided model generations either did not offer any novel capability or were refusals to respond. We banned the accounts associated with the threat actor, and shared their payloads with the security community to further disrupt their operations.

## Author

OpenAI

Research

  * [Research Index](</research/index/>)
  * [Research Overview](</research/>)
  * [Economic Research](</signals/>)



Latest Advancements

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

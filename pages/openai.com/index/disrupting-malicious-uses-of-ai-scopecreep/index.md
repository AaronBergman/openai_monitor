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

June 1, 2025

# Operation “ScopeCreep”: Russian-speaking malware development

OpenAI banned Russian-language accounts using AI to build malware, refine loaders, and troubleshoot cyber tooling.

Loading…

Share

 _This case study was originally published in OpenAI’s_[ _June 2025_ ⁠(opens in a new window)](<https://cdn.openai.com/threat-intelligence-reports/5f73af09-a3a3-4a55-992e-069237681620/disrupting-malicious-uses-of-ai-june-2025.pdf>)_report._

##  Actor

We banned a cluster of ChatGPT accounts that appeared to be operated by a Russian-speaking threat actor. This actor used our models to assist with developing and refining Windows malware, debugging code across multiple languages, and setting up their command-and-control infrastructure.

The actor demonstrated knowledge of Windows internals and exhibited some operational security behaviors. Based on the operation’s focus on using a trojanized “crosshair” gaming tool and its stealthy tactics, we have dubbed it “ScopeCreep.”

## Behavior

This threat actor had a notable approach to operational security. They utilized temporary email addresses to sign up for ChatGPT accounts, limiting each ChatGPT account to one conversation about making one incremental improvement to their code. They then abandoned the original account and created a new one.

The actor distributed the ScopeCreep malware through a publicly available code repository that impersonated a legitimate and popular crosshair overlay tool (Crosshair-X) for video games. Unsuspecting users who downloaded and ran the malicious version would initiate the malware loader on their system, resulting in additional malicious files being downloaded from attacker infrastructure and executed.

From there, the malware was designed to initiate a multi-stage process to escalate privileges, establish stealthy persistence, notify the threat actor, and exfiltrate sensitive data while evading detection.

The threat actor utilized our model to assist in developing the malware iteratively, by continually requesting ChatGPT to implement further specific features. ScopeCreep showcased a range of techniques across delivery, execution, evasion, and exfiltration, including:

  * C2 payloads designed to avoid signature-based detections.
  * Stealthy execution via DLL side-loading.
  * Obfuscation via custom packing with Themida.
  * Privilege escalation and evasion.
  * HTTPS over port 80.
  * Credential and session theft.
  * Attacker notifications via Telegram.
  * Proxy-based traffic obfuscation.



Despite the threat actor’s operational security efforts and detection evasion mechanisms in the malware itself, we were able to detect the activity due to our scaled cyber abuse detection process. We coordinated with the code hosting provider to take down the malicious repository and banned all ChatGPT accounts associated with this activity.

## Completions

The model interactions from this cluster covered a wide range of development tasks. One included a snippet of Go code where the threat actor was struggling with an HTTPS request, and asked the model to debug it. In a separate instance, the threat actor asked for assistance in using PowerShell commands via Go to modify Windows Defender settings, looking for a way to programmatically add AV exclusions.

Representative examples of these activities can be mapped to the LLM ATT&CK framework as follows:

  * Using LLMs to compile a file, python310.dll, so that their code is executed whenever python.exe runs: LLM Aided Development.
  * Troubleshooting errors with SSL/TLS certificates designed to serve HTTPS traffic on port 80: LLM Aided Development.
  * Model-assisted migration of a Flask-based C2 server to a production-ready WSGI server: LLM Aided Development.
  * Developing PowerShell commands in Go to modify Windows Defender settings and add AV exclusions: LLM-Enhanced Anomaly Detection Evasion.
  * Debugging errors in code to notify an attacker-controlled Telegram channel when a new victim is compromised: LLM-Assisted Post-Compromise Activity.



## Impact

At this stage, the impact of ScopeCreep may have been mitigated by quick reporting and close collaboration with industry partners who were able to take down the malicious repository. We banned the OpenAI accounts used by this adversary.

We assess this threat actor utilized our models in an attempt to speed up their malware development operations. Paradoxically, this also provided an opportunity for us to identify and disrupt the threat quickly and in what looked like its early stages.

While this malware’s capabilities include privilege escalation, persistence, credential harvesting, and remote access, these are not particularly novel. Although this malware was likely active in the wild, with some samples appearing on VirusTotal, we did not see evidence of any widespread interest or distribution.

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

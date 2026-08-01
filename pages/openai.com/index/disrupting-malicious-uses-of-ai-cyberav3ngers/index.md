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

October 1, 2024

# CyberAv3ngers: Iran-linked cyber research activity

OpenAI banned accounts that appeared to belong to CyberAv3ngers using AI to research industrial control systems, default credentials, and targets.

Loading…

Share

 _This case study was originally published in OpenAI’s_[ _October 2024_ ⁠(opens in a new window)](<https://cdn.openai.com/threat-intelligence-reports/influence-and-cyber-operations-an-update_October-2024.pdf>)_report._

##  Actor

We banned accounts, which based on an assessment from a credible source, appear to belong to an adversary known as CyberAv3ngers that has been publicly reported as affiliated with Iran’s IRGC. Accounts operated by this threat actor used our models to research vulnerabilities, debug code, and ask for scripting advice.

## Behavior

Based on open-source information, the CyberAv3ngers group is known for its disruptive attacks against industrial control systems (ICS) and programmable logic controllers (PLCs) used in water systems, manufacturing, and energy systems. Infrastructure targeted by this group is typically associated with Israel, the United States, or Ireland.

Recent attacks have included compromise of PLCs at the Municipal Water Authority of Aliquippa in Pennsylvania (November 2023) and a two-day disruption of water services in County Mayo, Ireland (December 2023). These campaigns often take advantage of default / weak passwords or well documented vulnerabilities in PLCs in combination with open-source tools for scanning and exploiting industrial control systems.

Much of the behavior observed on ChatGPT consisted of reconnaissance activity, asking our models for information about various known companies or services and vulnerabilities that an attacker would have historically retrieved via a search engine. We also observed these actors using the model to help debug code.

## Completions

The tasks the CyberAv3ngers asked our models in some cases focused on asking for default username and password combinations for various PLCs. In some cases, the details of these requests suggested an interest in, or targeting of, Jordan and Central Europe.

The operators also sought support in creating and refining bash and python scripts. These scripts sometimes leveraged publicly available pentesting tools and security services to programmatically find vulnerable infrastructure. CyberAv3nger accounts also asked our models high-level questions about how to obfuscate malicious code, how to use various security tools often associated with post-compromise activity, and for information on both recently disclosed and older vulnerabilities from a range of products. While previous public reporting on this threat actor focused on their targeting of ICS and PLCs, from these prompts we were able to identify additional technologies and software that they may seek to exploit, which can be found in the table below.

Activity| LLM ATT&CK Framework Category  
---|---  
Asking to list commonly used industrial routers in Jordan.| LLM-informed reconnaissance  
Asking to list industrial protocols and ports that can connect to the Internet.| LLM-informed reconnaissance  
Asking for the default password for a Tridium Niagara device.| LLM-informed reconnaissance  
Asking for the default user and password of a Hirschmann RS Series Industrial Router.| LLM-informed reconnaissance  
Asking for recently disclosed vulnerabilities in CrushFTP and the Cisco Integrated Management Controller as well as older vulnerabilities in the Asterisk Voice over IP software.| LLM-informed reconnaissance  
Asking for lists of electricity companies, contractors and common PLCs in Jordan.| LLM-informed reconnaissance  
Asking why a bash code snippet returns an error.| LLM enhanced scripting techniques  
Asking to create a Modbus TCP/IP client.| LLM enhanced scripting techniques  
Asking to scan a network for exploitable vulnerabilities.| LLM assisted vulnerability research  
Asking to scan zip files for exploitable vulnerabilities.| LLM assisted vulnerability research  
Asking for a process hollowing C source code example.| LLM assisted vulnerability research  
Asking how to obfuscate vba script writing in excel.| LLM-enhanced anomaly detection evasion  
Asking the model to obfuscate code (and providing the code).| LLM-enhanced anomaly detection evasion  
Asking how to copy a SAM file.| LLM-assisted post compromise activity  
Asking for an alternative application to mimikatz.| LLM-assisted post compromise activity  
Asking how to use pwdump to export a password.| LLM-assisted post compromise activity  
Asking how to access user passwords in MacOS.| LLM-assisted post compromise activity  
  
## Impact

In line with our findings from other investigations into state-sponsored threat actors using our models, we believe that these interactions did not provide CyberAv3ngers with any novel capability, resource, or information, and only offered limited, incremental capabilities that are already achievable with publicly available, non-AI powered tools.

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

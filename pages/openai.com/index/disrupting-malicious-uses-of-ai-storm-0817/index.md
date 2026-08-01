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

# STORM-0817: Iran-linked malware and scraping activity

OpenAI banned Iran-linked STORM-0817 accounts using AI to debug Android malware, scrape social platforms, and translate tooling.

Loading…

Share

 _This case study was originally published in OpenAI’s_[ _October 2024_ ⁠(opens in a new window)](<https://cdn.openai.com/threat-intelligence-reports/influence-and-cyber-operations-an-update_October-2024.pdf>)_report._

##  Actor

We disrupted a network of accounts operated by an Iran-based threat actor, which based on an assessment from a credible source is attributable to STORM-0817. We believe this is the first time this actor has been publicly identified as using AI models.

## Behavior

This actor used our models to debug malware, for coding assistance in creating a basic scraper for Instagram, and to translate LinkedIn profiles into Persian. This included working on malware that was still in development, and looking for information on potential targets.

These behaviors gave us unique insights into this adversary’s operations, including into infrastructure and capabilities that were being developed and weren’t yet fully operational.

## Completions

STORM-0817 asked our models for debugging and coding support in implementing Android malware and the corresponding command and control infrastructure. The malware targeted Android and was relatively rudimentary. Code snippets in attacker supplied prompts indicated it had standard surveillanceware capabilities and could retrieve:

  * Contacts
  * Call logs
  * Installed packages
  * Media on external storage
  * Screenshots
  * Device IMEI and model
  * Browsing history
  * Latitude / longitude
  * Files off external storage (pdf, excel docs)
  * Content downloaded to external storage including files sent by secure messaging apps like WhatsApp and IMO.



STORM-0817 was using this code in two Android packages—com.example.myttt and com.mihanwebmaster.ashpazi.

In parallel, STORM-0817 used ChatGPT to support the development of server side code necessary to handle connections from compromised devices. This allowed us to see that the command and control server for this malware is a WAMP (Windows, Apache, MySQL & PHP/Perl/Python) setup and during testing was using the domain stickhero[.]pro.

STORM-0817 also sought help to debug code to scrape Instagram profiles via the Selenium webdriver. This python code would accept an IG username and attempt to retrieve details from all followers. An Iranian journalist, critical of the Iranian government, appeared to be one of those individuals that this adversary was testing this tooling out on.

This threat actor also used our models to translate into Persian the LinkedIn profiles of individuals and academics that worked at the National Center for Cyber Security in Pakistan. This aligned with a subset of STORM-0817’s reconnaissance prompts that focused on the National Cybercrime and Forensics Lab at the Air University in Pakistan which supports various branches of the Pakistan military including the Air Force, Navy, and Police.

Some examples of these interactions and their associated TTP categories are below:

Activity| LLM ATT&CK Framework Category  
---|---  
Seeking help debugging and implementing an Instagram scraper| LLM-enhanced scripting techniques  
Translating LinkedIn profiles of Pakistani cybersecurity professionals into Persian| LLM-informed reconnaissance  
Asking for debugging and development support in implementing Android malware and the corresponding command and control infrastructure| LLM-aided development  
  
## Impact

We disabled all accounts identified as being operated by STORM-0817 and shared relevant IOCs with industry partners. Similar to what we found while investigating SweetSpecter, we believe our models only offered limited, incremental capabilities for malicious cybersecurity tasks beyond what is already achievable with publicly available, non-AI powered tools.

## Indicators

We identified the following server-side structure as being associated with this activity.

Tactic| Technique| Procedure| Indicator  
---|---|---|---  
0\. Acquiring assets| 0.6 Acquiring domains| 0.6.1 Acquiring domains to host, deploy, and support malware campaigns| stickhero[.]pro  
3\. Coordinating and planning| 3.4 Running C2 infrastructure| 3.4.1 Using domains and subdomains for command and control (C2)| /datas/stickher/public_html/contact.php  
3\. Coordinating and planning| 3.4 Running C2 infrastructure| 3.4.1 Using domains and subdomains for command and control (C2)| /datas/stickher/public_html/app.php  
3\. Coordinating and planning| 3.4 Running C2 infrastructure| 3.4.1 Using domains and subdomains for command and control (C2)| /datas/stickher/public_html/androidID.php  
3\. Coordinating and planning| 3.4 Running C2 infrastructure| 3.4.1 Using domains and subdomains for command and control (C2)| /datas/stickher/public_html/api/index.php  
3\. Coordinating and planning| 3.4 Running C2 infrastructure| 3.4.1 Using domains and subdomains for command and control (C2)| /datas/stickher/public_html//CallLogData.php  
3\. Coordinating and planning| 3.4 Running C2 infrastructure| 3.4.1 Using domains and subdomains for command and control (C2)| /datas/stickher/public_html//pdf.php  
  
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

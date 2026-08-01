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

# Deceptive Employment Scheme: IT worker activity

OpenAI banned accounts associated with suspected deceptive employment campaigns that used AI to develop materials for potentially fraudulent remote-job applications.

Loading…

Share

 _This case study was originally published in OpenAI’s_[ _June 2025_ ⁠(opens in a new window)](<https://cdn.openai.com/threat-intelligence-reports/5f73af09-a3a3-4a55-992e-069237681620/disrupting-malicious-uses-of-ai-june-2025.pdf>)_report._

##  Actor

We identified and banned ChatGPT accounts associated with what appeared to be multiple suspected deceptive employment campaigns. These threat actors used OpenAI’s models to develop materials supporting what may be fraudulent attempts to apply for IT, software engineering and other remote jobs around the world.

While we cannot determine the locations or nationalities of the threat actors, their behaviors were consistent with activity publicly attributed to IT worker [schemes connected to North Korea (DPRK)⁠(opens in a new window)](<https://www.justice.gov/archives/opa/pr/fourteen-north-korean-nationals-indicted-carrying-out-multi-year-fraudulent-information>). Some of the actors linked to these recent campaigns may have been employed as contractors by the core group of potential DPRK-linked threat actors to perform application tasks and operate hardware, including within the US.

## Behavior

Similar to the threat actors we disrupted and wrote about in [February⁠(opens in a new window)](<https://cdn.openai.com/threat-intelligence-reports/disrupting-malicious-uses-of-our-models-february-2025-update.pdf>), the latest campaigns attempted to use AI at each step of the employment process. Previously, we observed these actors using AI to manually generate credible, often U.S.-based personas with fabricated employment histories at prominent companies. This time, they attempted some degree of automated generation of resumes, and some indicators suggest operators in Africa posing as job applicants, in addition to recruiting people in North America to run laptops on their behalf.

We detected two distinct strands of activity, likely representing two types of operator: core operators, and contractors.

The core operators attempted to automate résumé creation based on specific job descriptions, skill templates, and persona profiles, and sought information about building tools to manage and track job applications. They also used our models to generate content that resembled job postings aimed at recruiting contractors in different parts of the world.

The core operators used ChatGPT as a research tool to help inform remote-work setups. They also engaged our models to generate text concerning the recruitment of real people in the US to take delivery of company laptops, which would then be remotely accessed by the core threat actors or their contractors.

The threat actors researched using tools such as Tailscale peer-to-peer VPN, OBS Studio, vdo.ninja live-feed injection, and HDMI capture loops as part of their operations. These tools have the potential to be used to circumvent corporate security measures, and if successful, they would allow someone to maintain a persistent, undetected remote presence, as well as attempt to bypass some identity verification processes that rely on live video meetings.

Meanwhile, the possible contractor operators used ChatGPT to help complete job application tasks. They also used it to generate content that resembled messages to the core operators inquiring about payments and about the personas used to apply for remote jobs.

## Completions

We determined that these threat actors attempted to use our models for a deceptive operation. Specifically, they used detailed prompts, instructions, and automation loops to generate tailored, credible résumés at scale.

  * Automating detailed résumés aligned to various tech job descriptions, personas, and industry norms: LLM Supported Social Engineering.
  * Answering employment-related application questions, coding assignments, and real-time interview questions based on uploaded resumes: LLM Supported Social Engineering.
  * Seeking guidance for remotely configuring corporate-issued laptops to appear domestically located, including geolocation masking and endpoint security evasion methods: LLM-Enhanced Anomaly Detection Evasion.
  * Assisting coding of tools to move the mouse automatically, or keep a computer awake remotely, possibly to assist in remote working infrastructure setups: LLM Aided Development.



## Impact

We cannot independently assess the success of these operations, as assessing impact would require inputs from multiple stakeholders.

While the threat actors likely built AI into every step of their process to increase their efficiency, it also increased their exposure. By giving us insights across their workflows, they enabled us to share insights about these campaigns with relevant industry peers and authorities for each stage of their activity, enhancing our collective ability to detect, prevent, and respond to such threats while advancing our shared safety.

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

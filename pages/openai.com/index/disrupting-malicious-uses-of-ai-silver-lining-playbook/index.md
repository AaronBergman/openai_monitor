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

February 1, 2026

[Safety](</news/safety-alignment/>)

# Silver Lining Playbook: Likely China-origin activity targeting US persons

OpenAI banned likely China-origin accounts using AI to research US persons, locations, and social-engineering tactics.

Loading…

Share

 _This case study was originally published in OpenAI’s_[ _February 2026_ ⁠(opens in a new window)](<https://cdn.openai.com/pdf/df438d70-e3fe-4a6c-a403-ff632def8f79/disrupting-malicious-uses-of-ai.pdf>)_report on disrupting malicious uses of AI._

##  Actor

We banned a small set of ChatGPT accounts likely originated in China that used our models to request information about US persons, forums and federal building locations, guidance on face- swapping software and generated emails in English that resembled attempts at social engineering. They prompted our models in Chinese language, were mostly active during mainland Chinese business hours and used VPNs to access our platform. 

The accounts generated email drafts that purported to be sent from employees of a Hong Kong- based company named “Nimbus Hub Consulting”. However, they prompted our models in Simplified Chinese characters (typically used in mainland China) rather than Traditional Chinese characters (typically used in Hong Kong) suggesting the actual operators were based in mainland China. In addition, one account generated an email purporting to be a representative of a Shanghai-based public relations organization that promotes US-Shanghai economic and cultural exchanges. Based on the company name referencing “Nimbus”, meaning a rain cloud or halo, we named this operation “Silver Lining Playbook”.

![Screenshots of LinkedIn profiles affiliated with Nimbus Hub Consulting.](https://images.ctfassets.net/kftzwdyauwt9/14bJe2kVgsUOzifg70iUBH/c2b5edfdd459f78450a9e5fe4e093e9c/silver-lining-playbook-linkedin-profiles.png?w=3840&q=90&fm=webp)

Screenshots of LinkedIn profiles affiliated with Nimbus Hub Consulting. Some of the LinkedIn profiles matched individuals listed on Nimbus Hub Consulting’s ‘Our Team’ page.

## Behavior

The accounts generated English language email drafts that were addressed to state-level US officials or policy analysts working in business and finance. They appeared to invite these recipients to participate in paid consultations, which they described as interpreting policy and providing strategic advice for their clients. They requested the email drafts to be concise, clear, and professional, with subject lines that created urgency and used subtle psychological cues. 

In addition, the ChatGPT accounts used our models for general information retrieval, which our model responded to using publicly-available sources. This included queries about the following topics: 

  * The location of U.S. federal government offices, including main office locations, and a ranked list of states with large concentrations of federal agencies and officials.

  * US federal personnel distribution by state. 

  * US persons, such as Voice of America hosts, including their past interviews and topics of interests.

  * Online forums and websites that are commonly used by professionals and job seekers in the US economics and finance industry.




Notably, one account requested guidance on how to install and download on their computer a face-manipulation platform for face-swapping and other media enhancement known as FaceFusion. According to their ChatGPT activity, they described their intention to specifically use its live face‑swap functionality. They asked for step‑by‑step, non‑technical installation guidance and claimed they were novice computer programmers, so the instructions had to be simple. They uploaded a screenshot of their computer’s hardware specifications to assist with the installation. The model responded with information that was drawn from FaceFusion’s publicly-available website and documentation.

## Completion

Their instructions to generate email drafts using our models reassembled a social-engineering [playbook⁠(opens in a new window)](<https://www.fbi.gov/investigate/counterintelligence/the-china-threat/clearance-holders-targeted-on-social-media-nevernight-connection>) for a foreign intelligence service approach, rather than ordinary hiring messages. For each email draft, they requested the following sections:   
  
**Establish legitimacy:** They presented “Nimbus Hub” as a professional strategic consulting firm with authoritative expertise in geopolitics and transnational policy. They included a link to Nimbus Hub’s website (see screenshot below).

**Personalize and flatter the target:** They told the model to explicitly cite the recipient’s public- sector background as proof the recipient was the exact fit for the role. In one case, the account uploaded screenshots of the LinkedIn profile of a US person based in Shanghai and instructed the model to personalize the email draft based on text about the individual’s personal experiences and background contained in the screenshots.

**Stack incentives:** The consulting offer was usually dangled as a lucrative, online opportunity with performance bonuses and referral rewards, while staying vague about the actual work.   
  
**Reassuring language and reducing perceived risks:** They often claimed the work was relaxing, had timely payments and was confidential.   
  
**Move communications off-platform quickly:** They always attempted to move the recipients off email and to an initial online video-conference call via WhatsApp, Zoom or Teams.

![Screenshot of Nimbus Hub Consulting’s website homepage, which is no longer online but has been archived.](https://images.ctfassets.net/kftzwdyauwt9/5WABYBBnNKL7qZ5nCu1Ly8/1f661ad13c2774f83942a5c40fad7d2b/image14.png?w=3840&q=90&fm=webp)

Screenshot of Nimbus Hub Consulting’s website homepage, which is no longer online but has been archived.

## Impact

The networks’ model interactions in this case were not technically sophisticated and their requests sometimes resembled plausible recruitment invitation drafting or legitimate software installation. However, the users’ tactics of hiding behind a fake corporate identity and interests in geopolitical topics indicates a possible intention for adversarial recruitment.

Based on the accounts use of ChatGPT, there was no evidence they successfully elicited responses from their targets to reply to their invitations. We could not independently determine whether the email invitations were actually sent or if any of the targeted recipients responded.

Multiple democratic governments (e.g. [USA⁠(opens in a new window)](<https://www.dni.gov/files/NCSC/documents/products/2025-04-08-NCSC-FBI-DCSA-OnlineTargetingUSGEmployees.pdf>), [UK⁠(opens in a new window)](<https://www.gov.uk/government/news/action-to-disrupt-and-deter-threats-to-uk-as-mi5-issues-spy-alert>), [Australia⁠(opens in a new window)](<https://www.asio.gov.au/resources/TBYL>)) have warned that foreign intelligence services are targeting current and former government employees for recruitment by posing as consulting firms and other entities on social and professional networking platforms. It may be confusing to distinguish ordinary hiring messages from these targeted social-engineering approaches because they share some similar traits. However, legitimate outreaches are usually optimized for slower screening processes and have verifiable information about the role title, credible employer details, reasonable market compensation ranges and links to real job postings. In short, if it’s too good to be true, then it probably is.

  * [China](</news/?tags=actor-origin-china>)
  * [United States](</news/?tags=target-geography-united-states>)
  * [Surveillance & intelligence collection](</news/?tags=activity-type-surveillance-coercion>)



## Author

OpenAI

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

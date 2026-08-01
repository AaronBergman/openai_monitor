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

# Task scam: AI-assisted fake review jobs

OpenAI banned accounts that appeared to originate in Cambodia and used AI to translate messages for fake-review job scams that asked victims to pay fees.

Loading…

Share

 _This case study was originally published in OpenAI’s_[ _February 2025_ ⁠(opens in a new window)](<https://cdn.openai.com/threat-intelligence-reports/disrupting-malicious-uses-of-our-models-february-2025-update.pdf>)_report._

##  Actor

We banned a cluster of ChatGPT accounts that were translating short comments between Urdu and English consistent with a “[task⁠(opens in a new window)](<https://consumer.ftc.gov/consumer-alerts/2024/11/task-scams-create-illusion-making-money#:~:text=In%20a%20task%20scam%2C%20scammers,%E2%80%9Ccommission%E2%80%9D%20on%20each%20click.>)” scam, in which the victims are offered a highly-paid job, but then required to pay their own money into the system before they can access their supposed “earnings.” This activity appeared to originate in Cambodia. In these scams, victims generally lose both the “earnings” and their own money. We began investigating this activity following a tip from Meta.

## Behavior

This network primarily used our models to translate short comments, consistent with chats between a scammer and their victims, between Urdu and English. We identified references to messaging on Telegram (apparently their primary platform), WhatsApp, SMS, and a range of employment forums and groups where job offers could be posted.

The scammers appeared to pose as two main types of persona. One was the “recruiter”: Their messages were a form of cold outreach, posting ads for well-paid remote work. The other, which generated a higher volume of activity, was the “mentor,” who would follow up on the “recruiter”’s outreach and teach the target how to do their job. The mentors very often referenced training sessions on Telegram.

Occasionally, the scammers also used our models to proofread the text of websites. These sites appear to have spoofed the names and appearance of luxury design, fashion, and travel brands. The “mentor” personas would claim to be recruiting on behalf of those brands, indicating that the websites were likely used to make the scam appear more credible.

## Completions

Based on our limited visibility, the scammers appear to have followed a common workflow in moving their targets from engagement to scam:

  1. Job posting: Based on their prompts and generations, the scammers appear to have started by posting job offers on various online forums. The recruitment efforts typically referenced remote work, and appear to have included salaries that were relatively high for a low amount of work, for example $300 a day plus bonuses for a few hours’ work. They were typically posted by the “recruiter” persona.
  2. Recruit: The scammers would then generate comments using the “mentor” persona to contact potential employees using what they indicated may have been a range of messaging apps, and say they were working with the “recruiter.” The “mentor” would claim to work for one of the luxury brands for which the operation had set up a website. They would describe the task as submitting five-star reviews to the sites of those luxury brands, ostensibly to boost their customer ratings.
  3. Reassure: Often, in generations, the scammers would reassure their targets that the work was legitimate because it was on behalf of a long-established company. If the target showed unease, the scammer would claim that they, too, had been scammed before, but that this opportunity was safe.
  4. Train: If the target expressed continued interest, the generations suggested that the “mentor” would offer them training, usually on Telegram. The target would initially be given access to a “training account,” where they would be expected to file 25-35 review tasks per day. The “training account” would show the target’s “earnings” increasing rapidly.
  5. Excite: Often, if the target continued their training, the generations indicated they would be offered a “special” or “ultimate” review task, which offered a higher bonus. The “mentor” would emphasize how rare it was, and how lucky the target was.
  6. “Activation fee”: Once the target’s “earnings” reached a certain level, the generations included the “mentor” telling them that they need to pay an “activation fee” to be able to withdraw their “earnings.” If needed, the scammer would urge them to borrow the money from friends or family.
  7. Pressurize: The generations showed that, if the target balked at paying money, the scammer would become increasingly aggressive, pressurizing them by comparing them with other, more efficient workers, and saying that they would lose their earnings if they did not pay in.
  8. Make excuses: In generations, if there was an indication that the target paid money, the scammer would make a series of excuses as to why the target could not withdraw their earnings, often saying that they need to pay in more.



## Impact

Some of the conversations showed that the targets were highly skeptical, and some of the comments generated by the scammers were in the voice of a mentor trying to ask why their target had stopped messaging, suggesting that this scam likely had a low overall conversion rate. However, some conversations and online reports suggest that at least some of the victims did indeed put money into these scams. We cannot independently verify activity that happens outside of our tools.

OpenAI’s policies strictly prohibit use of output from our tools for fraud or scams. We are dedicated to collaborating with industry peers and authorities to understand how AI is influencing adversarial behaviors and to actively disrupt scam activities abusing our services. In line with this commitment, we have shared information about the scam networks we disrupted with industry peers and the relevant authorities to enhance our shared safety.

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

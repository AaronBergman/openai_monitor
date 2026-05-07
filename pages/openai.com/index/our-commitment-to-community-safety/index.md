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

  * How we mitigate risks of harm in ChatGPT.
  * How we monitor and enforce our rules.
  * We surface real-world support and refer to law enforcement when appropriate.
  * We learn, improve and course-correct. 



April 28, 2026

[Safety](</news/safety-alignment/>)

# Our commitment to community safety

Loading…

Share

Mass shootings, threats against public officials, bombing attempts, and attacks on communities and individuals are an unacceptable and grave reality in today’s world. These incidents are a reminder of how real the threat of violence is—and how quickly violent intent can move from words to action. 

People may also bring these moments and feelings into ChatGPT. They may ask questions about the news, try to understand what happened, express fear or anger, or talk about violence in ways that are fictional, historical, political, personal, or potentially dangerous. We work to train ChatGPT to recognize the difference—and to draw lines when a conversation starts to move toward threats, potential harm to others, or real-world planning.

We’re sharing what we do to minimize uses of our services in furtherance of violence or other harm: how our models are trained to respond safely, how our systems detect potential risk of harm, and what actions we take when someone violates our policies. We are constantly improving the steps we take to help protect people and communities, guided by input from psychologists, psychiatrists, civil liberties and law enforcement experts, and others who help us navigate difficult decisions around safety, privacy, and democratized access.

## How we mitigate risks of harm in ChatGPT.

Our [_Model Spec_ ⁠(opens in a new window)](<https://model-spec.openai.com/2025-12-18.html#:~:text=to%2Dconsumer%20products.-,General%20principles,fall%20into%20specific%20categories%20that%20require%20refusal%20or%20safe%20completion.,-Instructions%20and%20levels>) lays out our long-standing principles for how we want our models to behave: maximizing helpfulness and user freedom while minimizing the risk of harm through sensible defaults. 

We work to train our models to refuse requests for instructions, tactics, or planning that could meaningfully enable violence. At the same time, people may ask neutral questions about violence for factual, historical, educational, or preventive reasons, and we aim to allow those discussions while maintaining clear safety boundaries—for example, by omitting detailed, operational instructions that could facilitate harm. The line between benign and harmful uses can be subtle, so we continually refine our approach and work with experts to help distinguish between safe, bounded responses and actionable steps for carrying out violence or other real-world harm.

As part of this ongoing work, we’ve continued expanding our safeguards to help ChatGPT better recognize subtle signs of risk of harm across different contexts. Some safety risks only become clear over time: a single message may seem harmless on its own, but a broader pattern within a long conversation—or across conversations—can suggest something more concerning. Building on years of work in model training, evaluations and red teaming, and ongoing expert input, we have strengthened how ChatGPT recognizes subtle warning signs across long, high-stakes conversations and carefully responds. We’ll share more about this work in the coming weeks.

Our safety work also extends to [_situations where users may be in distress_ ⁠](<https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/>) or at risk of self-harm. In these moments, our goal is to avoid facilitating harmful acts, and also to help de-escalate the situation and guide people to real-world support. ChatGPT surfaces localized crisis resources, encourages people to reach out to mental health professionals or trusted loved ones, and in the most serious cases directs people to seek emergency help. 

## How we monitor and enforce our rules.

We assume the best of our users, but when we detect that someone is attempting to use our tools to potentially plan or carry out violence, we take action, including revoking access to OpenAI’s services. Our [_Usage Policies_ ⁠](<https://openai.com/policies/usage-policies/>) set clear expectations for acceptable use and that we may prohibit use for threats, intimidation, harassment, terrorism or violence, weapons development, illicit activity, destruction of property or systems, and attempts to circumvent our safeguards. We take those policies seriously and work hard to enforce them. 

We use automated detection systems to identify potentially concerning activity at scale. These systems analyze user content and behavior using a range of tools designed to identify signals that may indicate policy violations or harmful activity, including classifiers, reasoning models, hash-matching technologies, blocklists, and other monitoring systems.

When an account or conversation is flagged, it is assessed in context by trained personnel. These human reviewers are trained on our policies and protocols, and operate within established privacy and security safeguards, meaning their access to user information is limited, conducted within secure systems, and subject to confidentiality and data protection requirements. Their role is to assess the flagged activity in context, including the content of the interaction, surrounding conversation, and any relevant patterns of behavior over time. This contextual review is important because automated systems may identify signals of potential concern without fully capturing intent or nuance.

The goal is to determine whether the flagged activity violates our policies and/or indicates that a user may carry out an act of violence, requires escalation for more detailed human review, or can be dismissed or deprioritized as low risk or non-violative. When we determine that a bannable offense has occurred, we aim to immediately revoke access to OpenAI’s services. That may include disabling the account, banning other accounts of the same user, and taking steps to detect and stop the opening of new accounts. We have a zero-tolerance policy for using our tools to assist in committing violence. People can appeal enforcement decisions, and we review those appeals to confirm the outcome.

## We surface real-world support and refer to law enforcement when appropriate.

Most enforcement actions, including bans for violence, happen directly between OpenAI and the user, making clear they have crossed a line. But in some sensitive cases, we may contact others who are best positioned to help. 

Where we assess that a case presents indicators of potentially serious, real-world harm, it is escalated for a more in-depth investigation, including assessing the overall level of risk using structured criteria. This stage is reserved for a limited subset of cases and is intended to ensure higher-risk scenarios are assessed with additional context and expertise. When conversations indicate an imminent and credible risk of harm to others, we notify law enforcement. Mental health and behavioral experts help us assess difficult cases and our referral criteria is flexible to account for the fact that a user may not explicitly discuss the target, means, and timing of planned violence in a ChatGPT conversation but that there may still be potential risk of imminent and credible violence. 

Last Fall, we introduced [_Parental Controls_ ⁠](<https://openai.com/index/introducing-parental-controls/>) to help families guide how ChatGPT works in their homes. Parental controls allow parents to link their account with their teen’s account and customize settings for a safe, age-appropriate experience. Parents don’t have access to their teen’s conversations, and in rare cases where our system and trained human reviewers detect possible signs of acute distress, parents may be notified—but only with the information needed to support their teen’s safety. Parents are automatically notified by either email, SMS, push notification, or all three.

Working closely with experts from our Council on Well-Being and AI and our Global Physicians Network, we will also soon be introducing a trusted contact feature, which will allow adult users to designate someone to receive notifications when they may need additional support. 

## We learn, improve and course-correct. 

We continue to strengthen our models, detection methods, review processes, and escalation criteria in response to observed usage, emerging risks, and input from internal and external experts. We are especially focused on hard cases: for example, where it is not clear whether a particular input is legitimate or poses a risk of harm; sophisticated attempts to evade safeguards; or when people repeatedly try to misuse our services. We will continue to [_prioritize safety_ ⁠](<https://openai.com/index/teen-safety-freedom-and-privacy/>) while balancing privacy and other civil liberties so we can act on serious risks.

You can read more about our [_safety work and commitments_ ⁠](<https://openai.com/news/safety-alignment/>) and sign up to [_receive updates_ ⁠](<https://openai.com/form/usage-policy-update/>) on our policies. 

  * [Strengthening ChatGPT’s responses in sensitive conversations⁠](<https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/>)
  * [Our approach to age prediction ⁠](<https://openai.com/index/our-approach-to-age-prediction/>)
  * [Updating our Model Spec with teen protections⁠](<https://openai.com/index/updating-model-spec-with-teen-protections/>)
  * [Introducing parental controls⁠](<https://openai.com/index/introducing-parental-controls/>)



  * [ChatGPT](</news/?tags=chatgpt>)
  * [2026](</news/?tags=2026>)
  * [User Safety & Control](</news/?tags=user-safety>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

![System Card 1x1](https://images.ctfassets.net/kftzwdyauwt9/2VCkKLVmTyNs0XGbqdxGeA/33ff7738f4e795ae0ee41ed2b4a985d3/System_Card_1x1.jpg?w=3840&q=90&fm=webp)

[GPT-5.5 Instant System CardSafetyMay 5, 2026](</index/gpt-5-5-instant-system-card/>)

![System Card Card SEO 1x1](https://images.ctfassets.net/kftzwdyauwt9/7qMrOFCWWMweIDBUpYFr79/7741661650df6eb935acb5bda179b091/System_Card_Card_SEO_1x1.jpg?w=3840&q=90&fm=webp)

[GPT-5.5 System CardSafetyApr 23, 2026](</index/gpt-5-5-system-card/>)

![GPT-5.5 Bio Bug Bounty > art card](https://images.ctfassets.net/kftzwdyauwt9/2wba91t9mgdv1oBPai3LTb/b19dc82704bb2f6fa625c02bf34eca75/Frame__15_.png?w=3840&q=90&fm=webp)

[GPT-5.5 Bio Bug BountySafetyApr 23, 2026](</index/gpt-5-5-bio-bug-bounty/>)

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

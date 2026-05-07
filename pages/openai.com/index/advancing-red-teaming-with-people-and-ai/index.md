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

  * The value of red teaming
  * External human red teaming
  * Automated red teaming 
  * Limitations



November 21, 2024

[Publication](</research/index/publication/>)

# Advancing red teaming with people and AI 

Two new papers show how our external and automated red teaming efforts are advancing to help deliver safe and beneficial AI

[External red teaming(opens in a new window)](<https://cdn.openai.com/papers/openais-approach-to-external-red-teaming.pdf>)[Automated red teaming(opens in a new window)](<https://cdn.openai.com/papers/diverse-and-effective-red-teaming.pdf>)

Loading…

Share

Interacting with an AI system is an essential way to learn what it can do—both the capabilities it has, and the risks it may pose. “Red teaming” means using people or AI to explore a new system’s potential risks in a structured way. 

OpenAI has applied red teaming for a number of years, including when we engaged [_external experts_ ⁠(opens in a new window)](<https://github.com/openai/dalle-2-preview/blob/main/system-card.md#external-red-teaming>) to test our DALL·E 2 image generation model in early 2022. Our earliest red teaming efforts were primarily “manual” in the sense that we relied on people to conduct testing. Since then we’ve continued to use and refine our methods, and last July, we joined other leading labs in a [_commitment_](</index/moving-ai-governance-forward/>) to invest further in red teaming and advance this research area. 

Red teaming methods include manual, automated, and mixed approaches, and we use all three. We engage outside experts in both manual and automated methods of testing for new systems’ potential risks. At the same time, we are optimistic that we can use more powerful AI to scale the discovery of model mistakes, both for evaluating models and to train them to be safer. 

Today, we are sharing two papers1 on red teaming—a white paper detailing how we engage external red teamers to test our frontier models, and a research study that introduces a new method for automated red teaming. We hope these efforts will contribute to the development of stronger red-teaming methods and safer AI.

###### Example of red teaming outputs

![A flowchart titled “Issues identified with red teaming,” showing “Human” \(green\) and “Automated” \(purple\) issues. It maps “Issue” \(e.g., hate speech\) to “Example” \(e.g., plant recipe\) and “Attacks,” leading to several “Results.”](https://images.ctfassets.net/kftzwdyauwt9/3Ooo0f1boDCgLYWm1F7EU5/1505310c849dd4677493c3d9fa3ea289/Red-Teaming_Blog_Chart-Padded_Light.svg?w=3840&q=90)

 _Red teaming probes an AI model or system to identify potential issues, examples of those issues, or attacks to elicit those issues. While humans can help identify a diversity of examples, issues and attacks, automated red teaming can complement this by helping brainstorm and generate examples and attacks at larger scale. Issues, examples, and attacks raised above are illustrative and not necessarily reflective of OpenAI 's usage or content policies._

## The value of red teaming

As AI systems are evolving at a rapid pace, it’s essential to understand users' experiences and the potential risks of increased capabilities, including abuse, misuse and real-world factors like cultural nuances. While no single process can capture all these elements, red teaming—especially with input from a range of independent external experts—offers a proactive way to assess risks and test the safety of our AI models. This approach helps build up-to-date benchmarks and safety evaluations that can be reused and improved over time.

## External human red teaming

Key aspects of our external red teaming campaigns include defining the scope of testing, selecting red team members, deciding which models they access, and determining the format of their final reports. 

  
In a new white paper, [_OpenAI’s Approach to External Red Teaming for AI Models and Systems_ ⁠(opens in a new window)](<https://cdn.openai.com/papers/openais-approach-to-external-red-teaming.pdf>), we detail our approach for designing effective red teaming campaigns2:

**1\. Choosing the composition of the red teaming group based on goals and key testing areas  
  
** AI systems designed for a variety of use cases require thorough testing across multiple areas, involving people with diverse perspectives (for example, expertise in fields like natural sciences and cybersecurity, regional political knowledge, or languages spoken). Threat modeling is conducted before red teaming exercises to prioritize areas for testing, taking into account factors like expected model capabilities, previously observed issues with models, and potential applications. Internal teams set initial testing priorities based on their knowledge of model capabilities, while external red teamers are brought in later to refine or expand the focus. These priorities then guide the formation of red teams, ensuring they meet the model's specific testing needs.

**2\. Deciding the model or system versions the red teamers receive access to  
  
** The version of the model available to red teamers can affect red teaming outcomes and should align with campaign goals. For example, testing a model early in development without safety mitigations in place can help to assess new risks related to increased capabilities, but would not necessarily test for gaps in the planned mitigations. The ideal approach depends on the specific needs of the model, and red teamers may test multiple versions of a model and system throughout the testing period.

**3\. Creating and providing interfaces, instructions, and documentation guidance to red teamers**

Effective interactions with external testers during red teaming campaigns rely on clear instructions, suitable testing interfaces, and actionable documentation. Instructions may include descriptions of the model(s) and existing or planned safeguards, how to use the testing interface, prioritized areas for testing, and guidelines for documenting results. Different interfaces, or the means through which testers interact with an AI model, could include an API or consumer product interfaces like ChatGPT. The interfaces used for red teaming help facilitate testing by enabling rapid programmatic testing, collecting feedback on specific prompts or responses, or simulating potential user interactions. With the right combination of interfaces and instructions for documentation, structured feedback collected from red teaming can later lead to input into risk assessments and automated evaluations.

**4\. Synthesizing the data and creating evaluations  
  
** After a red teaming campaign, a key step is determining whether examples fall under existing policies, whether they violate those policies, or if new policies or behavior modifications are needed. Some campaigns target known policy violations, while others explore areas without clear policy coverage. Once the data from a red teaming campaign is assessed for quality, that data can be used for repeatable, automated evaluations for future model updates. 

Most recently, we used this approach to prepare our [_OpenAI o1 family of models_](</index/openai-o1-system-card/>) for public use. We designed an external red teaming campaign that tested the model for resistance to jailbreaks, safe handling of real-world attack planning prompts, safe application in natural sciences, and broader topics like AI research and development capabilities.

## Automated red teaming 

Automated red teaming aims to generate a large number of examples where an AI behaves incorrectly, often with a particular focus on safety-related issues. In contrast to human red teaming, automated methods excel at easily generating example attacks at a larger scale. However, these methods have typically struggled to generate successful attacks that are _tactically_ _diverse_ , as automated red teamers often repeat known attack strategies or produce a range of novel but ineffective attacks. 

In new research, [_Diverse And Effective Red Teaming With Auto-Generated Rewards And Multi-Step Reinforcement Learning_ ⁠(opens in a new window)](<https://cdn.openai.com/papers/diverse-and-effective-red-teaming.pdf>), we offer new techniques to improve the diversity of attacks while still ensuring they are successful. 

Our research finds that more capable AI can further help automated red teaming in how it brainstorms attacker goals, how it judges attacker success, and how it understands diversity of attacks. For instance, if the red teaming goal is to find examples of ChatGPT giving disallowed illicit advice, we can use GPT‑4T to brainstorm examples such as “how to steal a car” and “how to build a bomb” and then train a separate red teaming model to try to trick ChatGPT into giving _each_ example of advice. We reward the red teaming model through a combination of our [_moderation models_](</index/new-and-improved-content-moderation-tooling/>) , [_rule based rewards_](</index/improving-model-safety-behavior-with-rule-based-rewards/>) targeting the specific example of illicit advice, and a diversity reward for how different the attack is from past attempted attacks. This means that the red teaming model can generate many more diverse and yet effective attacks, which can then be used both for improving model safety and evaluations. More importantly, it demonstrates how we can continue to train and use more capable models in new ways to improve safety.

## Limitations

Red teaming isn't a complete solution for assessing AI risks. Its limitations include:

  1. **Relevance over time:** Red teaming captures risks at a specific moment, which may change as models evolve.
  2. **Information hazards:** The process of red teaming, particularly with frontier AI systems, can create information hazards that might enable misuse. For example, exposing a jailbreak or technique to generate potentially harmful content that is not yet widely known could accelerate bad actors’ misuse of the models. Managing this risk requires control of information, stringent access protocols, and responsible disclosure practices. 
  3. **Increase in human sophistication:** As models become more capable and their ability to reason in sophisticated domains becomes more advanced, there will be a higher threshold for knowledge humans need to possess to correctly judge the potential risks of outputs. 



While red teaming aims to expand perspectives in service of risk discovery, verification, and evaluation development, we believe additional work is needed to solicit and incorporate public perspectives on ideal model behavior, policies, and other associated decision making processes.

  * [o1](</research/index/?tags=o1>)
  * [GPT](</research/index/?tags=gpt>)
  * [Ethics & Safety](</research/index/?tags=ethics-safety>)
  * [Exploration & Games](</research/index/?tags=exploration-game>)
  * [Reasonings & Policy](</research/index/?tags=reasoning-policy>)
  * [Simulated Environments](</research/index/?tags=simulated-environments>)



## Authors

OpenAI

## Footnotes

  1. 1

This work builds upon other existing literature and research examining the process, methods, and outcomes of red teaming for AI models and systems. Please see the References section in both papers to learn more. 

  2. 2

We use the word campaign to denote a specifically scoped effort to test a particular AI model or system. 




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

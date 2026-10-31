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

October 29, 2026

[Safety](</news/safety-alignment/>)

# An updated Model Spec for more capable and beneficial AI

[Read the updated Spec(opens in a new window)](<https://model-spec.openai.com/2026-10-29.html>)

Loading…

Share

Organizing the Spec around core values

  * Organizing the Spec around core values
  * New and retired sections
  * What comes next



  * Organizing the Spec around core values
  * New and retired sections
  * What comes next



As our models get smarter and take more consequential actions in the world, it becomes increasingly important that they go beyond just interpreting the specific instructions they receive. Models also need to understand human intentions and values, so they can exercise good judgment in situations their instructions don’t explicitly address while remaining faithful to human intent and oversight.

Today we’re updating the [_Model Spec_ ⁠(opens in a new window)](<https://model-spec.openai.com/2026-10-29.html>), our public description of how we want our models to behave. The update reorganizes its guidance around five underlying values: **faithfulness to human intent** , **harm minimization** , **honesty and transparency** , **human agency** , and **care**. This reflects an aim of our work on [_value alignment_](</index/an-alien-mind/>) : for models to understand and apply human values in unfamiliar situations, while remaining faithful to human intent. Alongside clearer explanations of existing principles, the revision adds guidance on context, oversight, and agency, adjusts some behavioral defaults, and retires much of the detailed style guidance.

## Organizing the Spec around core values

The five values above articulate broad commitments already reflected across the Model Spec: serving human purposes, being truthful, minimizing harm, respecting people’s freedom to form their own views, and taking their circumstances seriously. Bringing these commitments together helps explain why the Spec asks models to behave as it does, and helps us develop clearer guidance where those commitments were less fully expressed. This update is another step in our [_work to refine the Spec_](</index/our-approach-to-the-model-spec/>) through research, experience deploying models, [_public feedback_](</index/collective-alignment-aug-2025-updates/>) on the Spec and model behavior, and discussions with users and outside experts.

We want AI to benefit a world of people with different needs, values, and hopes for the future. 

**Faithfulness to human intent** is the foundation of this approach: understanding and helping people pursue what matters to them. OpenAI writes the Spec, sets boundaries, and trains models to respect them; developers direct applications within those boundaries; and users direct the model’s work subject to those constraints. Our models should [_expand people’s ability to shape their own lives_](</index/built-to-benefit-everyone-our-plan/>) by helping them understand the world, discover possibilities, and pursue the goals they choose, while taking seriously how that assistance affects others. Faithfulness to human intent and the remaining four values organize the Spec and guide how our models should navigate some of the most important trade-offs they face. They are not intended to capture the full range of human values our models should respect and help people pursue.

Faithfulness means going beyond following instructions literally to deeply understanding what OpenAI, developers, and users intend and value, and acting wisely when that understanding is incomplete. It also means recognizing that people’s beliefs and values can change, and helping them reflect and grow in ways they would endorse without quietly steering them or overriding their choices. For example, when helping someone compare job offers, the model might draw on priorities they have shared before—such as predictable hours—while making those assumptions visible and easy to correct.

Our mission is to ensure that artificial general intelligence benefits all of humanity. This requires considering not only someone’s immediate intentions, but also their longer-term interests and the effects on others. The other four values make these considerations explicit:

  * **Minimizing harm** means respecting firm safety boundaries and accounting for the foreseeable consequences of the model’s actions.

  * **Honesty and transparency** mean being truthful about what the model knows, does, and is uncertain about so people can understand and evaluate its reasoning and work.

  * **Facilitating human agency** means strengthening people’s ability to understand, choose, and act for themselves.

  * **Care** means attending to the circumstances of those affected, following relevant social and professional norms, and doing work people can rely on.




The Spec turns these values into practical guidance, with firm boundaries where needed to protect people and society, and otherwise mostly takes the form of defaults that users and developers can override.

Alongside this Model Spec update, we’ve been exploring new training methods to help our models learn these core values and better understand and follow the Spec’s specific behavioral principles. The aim is to build an understanding of why those principles matter and how to apply them in new situations: to do the _right things_ _for the right reasons_. We want that understanding to support sound judgment in consequential decisions and care in everyday decisions that can add up to [_lasting benefits for people and society_ ⁠(opens in a new window)](<https://alignment.openai.com/beneficial-rl/>). We’ll share results and lessons from this training work in future updates.

## New and retired sections

This reorganization also helped us identify where additional guidance was needed, develop new principles to address it, and revise or retire existing guidance as needed.

The new section on faithfulness to human intent starts from the idea that what people value is primary, and instructions are ordinarily the clearest and most important signals of those values. This approach borrows from the assistance-games framing of alignment (see [_early work_ ⁠(opens in a new window)](<https://arxiv.org/abs/1606.03137>) and a [_later overview_ ⁠(opens in a new window)](<https://www.amacad.org/publication/daedalus/if-we-succeed>)). The section incorporates an updated [_chain of command_ ⁠(opens in a new window)](<https://model-spec.openai.com/2026-10-29.html#chain_of_command>), which explains which instructions apply and how conflicts are resolved. A new subsection, [_consider context carefully_ ⁠(opens in a new window)](<https://model-spec.openai.com/2026-10-29.html#consider_context_carefully>), explains how conversations, memories, and other contextual evidence should inform the model’s understanding of people’s intentions and preferences. 

We’ve also added defaults on [_supporting human agency_ ⁠(opens in a new window)](<https://model-spec.openai.com/2026-10-29.html#support_human_agency>) and [_following relevant social norms_ ⁠(opens in a new window)](<https://model-spec.openai.com/2026-10-29.html#follow_social_norms>), and expanded existing guidance on [_controlling and communicating side effects_ ⁠(opens in a new window)](<https://model-spec.openai.com/2026-10-29.html#control_side_effects>). These principles capture additional, often subtle but important ways the remaining values should surface in model behavior: considering the effects of the work on others, strengthening users’ capabilities, and producing work people can rely on, while respecting the user’s goals and instructions. 

At the same time, we’re retiring most of the Spec’s detailed style guidance. Style should adapt to what people prefer—in aggregate, within languages and cultures, and for each person—with user feedback and context providing evidence about those preferences. The Spec retains stronger defaults, such as [_approaching questions objectively_ ⁠(opens in a new window)](<https://model-spec.openai.com/2026-10-29.html#assume_objective_pov>). Users and developers can explicitly ask the model to take a particular perspective, but the model should not infer that preference merely from what it thinks they want to hear.

Finally, reflecting the increasing breadth of our models’ use cases and deployment settings, we now refer to the model as “GPT” rather than “the assistant” in the Spec. 

## What comes next

This update is a first step in making the values and reasoning behind the Spec more explicit as models become more capable. The Model Spec describes the behavior we are working toward; our models do not yet fully reflect it. We will keep improving both the Spec and the models as we learn from research, real-world use, and feedback.

We want to hear which parts of the Spec you find compelling, where you disagree with the balance it strikes, and what it overlooks or leaves unclear. Feedback on the values, trade-offs, and specific language can help us improve it. We invite you to read the [_updated Model Spec_ ⁠(opens in a new window)](<https://model-spec.openai.com/2026-10-29.html>) and [_share your perspective_ ⁠(opens in a new window)](<https://model-spec-feedback-2026.openai.chatgpt.site>).

  * [Alignment](</news/?tags=alignment>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

![An update on violence prevention — Cover](https://images.ctfassets.net/kftzwdyauwt9/2JkiYuWDdFYR0Wg7GoacTc/56a54c0060610c840d098457108a4f88/an-update-on-violence-prevention-cover.png?w=3840&q=90&fm=webp)

[Community safety report and new protections for teensSafetyOct 30, 2026](</index/community-safety-report-and-new-protections-for-teens/>)

![How we detect frontier model misalignment — Cover](https://images.ctfassets.net/kftzwdyauwt9/43ZavE2amLHMmbxH8EL8VM/1464d0f68c0f3c45e9d255992aab32b1/how-we-detect-frontier-model-misalignment-cover.png?w=3840&q=90&fm=webp)

[How we detect frontier model misalignmentSecurityOct 29, 2026](</index/how-we-detect-frontier-model-misalignment/>)

![Broad access through consistent standards — Cover](https://images.ctfassets.net/kftzwdyauwt9/5yeylkVM0cZ2W6k2lcnVyE/42a8333bccf5064328630ebf7c667082/broad-access-through-consistent-standards-cover.png?w=3840&q=90&fm=webp)

[Broad access through consistent standardsSafetyOct 21, 2026](</index/broad-access-through-consistent-standards/>)

Research

  * [Research Index](</research/index/>)
  * [Research Overview](</research/>)
  * [Economic Research](</signals/>)



Latest Advancements

  * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  * [GPT-6 Astra](</index/gpt-6-astra/>)
  * [GPT-5.6](</index/gpt-5-6/>)
  * [GPT-5.5](</index/introducing-gpt-5-5/>)



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
  * [Codex](<https://chatgpt.com/codex/>)
  * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  * [Release Notes](</products/release-notes/>)



API Platform

  * [Overview](</api/>)
  * [API Log In(opens in a new window)](<https://platform.openai.com/login>)
  * [Docs(opens in a new window)](<https://developers.openai.com/api/docs>)



Business

  * [Overview](</business/>)
  * [Solutions](</solutions/>)
  * [Resources](</business/learn/>)
  * [Plugins](</business/plugins/>)
  * [Customer Stories](</business/customer-stories/>)
  * [Partner Network](</business/partners/>)
  * [Contact Sales](</contact-sales/>)



Developers

  * [Plugins(opens in a new window)](<https://developers.openai.com/plugins>)
  * [Models(opens in a new window)](<https://developers.openai.com/api/docs/models>)
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
  * [OpenAI Status(opens in a new window)](<https://status.openai.com>)



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

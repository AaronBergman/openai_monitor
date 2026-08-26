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

August 18, 2026

[Company](</news/company-announcements/>)[Publication](</research/index/publication/>)

# Pacing model development in an era of cyber-critical capabilities

Loading…

Share

Strengthening safeguards for more capable models

  * Strengthening safeguards for more capable models
    * Securing our research environments
    * Expanding chain-of-thought monitoring
    * Advancing alignment research
  * What’s next



  * Strengthening safeguards for more capable models
    * Securing our research environments
    * Expanding chain-of-thought monitoring
    * Advancing alignment research
  * What’s next



Over the past several weeks, two developments have underscored the growing risks associated with increasingly capable AI systems: the [_OpenAI-Hugging Face incident_](</index/hugging-face-model-evaluation-security-incident/>) and, separately, preliminary evidence that one of our upcoming models, Astra, may meet the[ _Critical cybersecurity capability_](</index/responding-next-frontier-critical-cyber-capabilities/>) threshold under our[ _Preparedness Framework_](</index/updating-our-preparedness-framework/>). Together, these developments, combined with rapid progress in our internal research, have added urgency to our work on strengthening our monitoring, alignment, and containment safeguards across all stages of the training process.

As models become more capable, the risks associated with developing and testing them internally also grow. Our standards for monitoring, alignment, and security must stay ahead of those risks. We wanted to take the time necessary to meet those standards, so we temporarily slowed the pace of scaling. This included a two-week pause in reinforcement learning (RL) training on our latest models intended for deployment while we further hardened and red-teamed our research environments and expanded the coverage of our monitoring systems. Our largest planned frontier RL run remains on hold while we conduct smaller-scale training and evaluations to assess model behavior, validate our safeguards, and establish more evidence of alignment before proceeding.

[_Alignment_](</safety/how-we-think-about-safety-alignment/>) —the work of making AI systems behave as intended and responsive to human oversight—has long been at the core of our research program. We now require stronger evidence of aligned behavior throughout all of training, building on research and evaluations already underway. Keeping increasingly capable systems aligned is a challenge the whole field will need to address. The signals we are seeing from upcoming model progress make clear that we need a broader approach—one that builds on and extends beyond the current Preparedness Framework.

We think it is important to be transparent about how our approach is changing. Below, we describe the changes we have already made to our research processes and infrastructure, and the work still underway.

## Strengthening safeguards for more capable models

Our approach to developing more capable models rests on three reinforcing safeguards:

  1. **Monitoring** , which detects and allows us to respond to concerning behavior.
  2. **Alignment** , which reduces the likelihood of harmful or unauthorized actions.
  3. **Security measures** , which limit what AI systems can access or affect.



We expect models to soon drive most security work, including defending against other models. This will allow all three safeguards to scale with model capability, which we see as crucial.

We apply these safeguards across research and deployment, adapting them to each model’s capabilities, operating environment, and level of risk.

### Securing our research environments

As frontier models gain stronger cybersecurity capabilities, we are raising the security standards for the environments in which we train and evaluate them. Meeting these standards has required substantial engineering work and has incurred great cost and delays to frontier research. Immediately following the OpenAI-Hugging Face incident*, we paused frontier model inference in research clusters for runs that could execute code or use tools that could access the internet. We restored a more limited and secure path for code execution fairly quickly, then worked through each workload individually to determine whether it could safely resume. Some research workloads resumed under these new controls, while others required additional changes.

Over the subsequent weeks, we have defined and started implementing stronger security requirements for frontier research workloads. For example:

  * **Workload isolation:** We now require stronger isolation (“sandboxes”) for workloads that execute model-generated or otherwise untrusted code. This also applies to software that could be compromised while processing model outputs.
  * **Network isolation:** We have implemented more controls to isolate higher-risk and untrusted workloads from the internet. We have designed these controls so that a single compromise of a workload or supporting service does not, by itself, allow for unauthorized access to the internet or other internal networks.
  * **Continuous security testing:** We have reconfigured our environment to remove potentially vulnerable shared services, reduce standing privileges, and improve security and trust boundaries. We are also improving our ability to collect and monitor security logs. Finally, we are investing in automation using our models to test these boundaries continuously against simulated attacks.



Together, these controls provide defense in depth and help protect our research environment against attacks. Today, we require the strictest level of security safeguards for workloads involving Astra or cyber models, since we have determined that Astra models may have a critical level of cyber capability. These safeguards also apply to all other cyber-related workloads.

While some Astra training and evaluations meet those requirements, a significant number of workloads remain paused until they are fully migrated and enhanced to meet the new security bar. We are prioritizing safety and alignment workloads for migration to these new environments first.

### Expanding chain-of-thought monitoring

Monitoring has long been an important part of our model development process, including [_monitoring for internal coding agents_](</index/how-we-monitor-internal-coding-agents-misalignment/>) and [_long-running sessions_](</index/safety-alignment-long-horizon-models/>). Our monitoring efforts were especially focused on internal deployments of frontier models and frontier RL training runs, which we considered the highest-risk workloads because they can combine advanced model capabilities with access to tools, sensitive systems, and internal or external networks. They were not applied to all inference and training runs using tools. We have revised and expanded our approach with our new monitoring setup.

This new monitoring setup is multistage, starting with activation classifiers (detectors that inspect a model’s internal activity) that run at every sampled token and escalate potential concerns to increasingly sophisticated and high-compute automated investigators. Those systems examine tool actions, available reasoning, and the full sequence of activity for unauthorized access, data theft, destructive behavior, and attempts to defeat safeguards. We aim to issue an alert within 30 minutes after concerning activity is surfaced through our monitoring system. If the monitoring system identifies a likely violation of a critical security boundary, it generates a highest-priority alert. In our current implementation, the safety, security, and research teams are paged. If they cannot conclusively determine within 30 minutes that the flag is a false positive, those teams are expected to pause the activity.

This monitoring is required for all RL training and evaluations involving tools for models of Sol capability or higher. Once we determined that Astra may have critical cyber capabilities on August 7, we added an additional monitoring requirement for all inference of Astra with tools (not just RL training and evaluations).

These safeguards require meaningful compute. Our current estimates put monitoring overhead at roughly 20% of the inference compute being monitored, though the cost varies substantially across training and evaluation workloads. We’ll share more details about this system in a forthcoming blog post.

### Advancing alignment research

Alignment research is central to our mission. Our mission is to ensure that artificial general intelligence benefits all of humanity. As models gain advanced capabilities, such as the ability to cyberattack, and operate in more complex environments, misaligned behaviors like reward hacking (finding ways to receive high rewards in training without actually achieving the intended outcome), deception, or unauthorized access will create increasingly serious risk.

For RL runs on the most capable models, we are now applying our core alignment techniques across more stages of the training process. This includes improving reward models to better detect and discourage unsafe behavior across tasks and environments; training models to be more honest about their actions, capabilities, and limitations; and reducing behaviors that exploit weaknesses in rewards, graders, tools, or oversight. We are also increasing training coverage for behaviors that could cause harm when models interact with external systems or resources.

We are continuing to invest aggressively in alignment research, increase evaluation coverage, and use what we learn to inform training and safeguards. We plan to share substantially more about our alignment research in the near future, including what we are learning about model behavior and any novel challenges we uncover.

## What’s next

We will evolve our Preparedness Framework to bring these safeguards together across training and deployment, and to better reflect the capabilities of future models and the environments in which they operate. Developing methods that can scale with those capabilities will require sustained investment in model-assisted security, more effective monitoring, and continued advances in alignment research. We intend to involve external organizations and share more of what we learn as our approach develops.

The capabilities of frontier models are rapidly accelerating. Our ability to understand, align, and secure them must stay ahead.

* * *

_*We will publish a technical report of our learnings in the coming weeks._

  * [2026](</news/?tags=2026>)
  * [Alignment](</news/?tags=alignment>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

![The full stack behind abundant intelligence > Cover image](https://images.ctfassets.net/kftzwdyauwt9/4nRoI5iOfeV7qh4O3eAIEB/400545de8860b3c757548f2e3cd275fb/index-full-stack-behind-abundant-intelligence--cover-v001.png?w=3840&q=90&fm=webp)

[The full stack behind abundant intelligenceCompanyAug 25, 2026](</index/the-full-stack-behind-abundant-intelligence/>)

![Jalapeño inference — Art Card](https://images.ctfassets.net/kftzwdyauwt9/26K8mLbrpbaDvoFY0NrE04/8e4ad0b3f28042c22d6d5130bd4f4019/jalapeno-art-card.png?w=3840&q=90&fm=webp)

[Jalapeño’s first results show industry-leading speed and efficiency in AI inferenceEngineeringAug 25, 2026](</index/jalapeno-first-results/>)

![Our commitment to Zero Data Retention as AI advances — card](https://images.ctfassets.net/kftzwdyauwt9/6bPStWA6pc66cahnhg0jo6/61786b178401b6e902e9da65fa4da095/Blog_Thumbnail_-_OpenAI_Blog.png?w=3840&q=90&fm=webp)

[Offering Zero Data Retention for frontier modelsCompanyAug 19, 2026](</index/offering-zero-data-retention-for-frontier-models/>)

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

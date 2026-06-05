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

  * AGI in many steps rather than one giant leap
  * Impacts of AGI
  * Our core principles
  * Methods that scale



# How we think about safety and alignment

The mission of OpenAI is to ensure artificial general intelligence (AGI) benefits all of humanity. Safety—the practice of enabling AI’s positive impacts by mitigating the negative ones—is thus core to our mission.

Our understanding of how to advance safety has evolved a lot over time, and this post is a current snapshot of the principles that guide our thinking. We are not certain everything we believe is correct. We do know AI will transform most aspects of our world, and so we should think through the benefits, changes, and risks of this technology early.

## AGI in many steps rather than one giant leap

We used to view the development of AGI as a discontinuous moment when our AI systems would transform from solving toy problems to world-changing ones. We now view the first AGI as just one point along a series of systems of increasing usefulness.

In a discontinuous world, practicing for the AGI moment is the only thing we can do, and safety lessons come from treating the systems of today with outsized caution relative to their apparent power. This is the approach we took for GPT‑2 when we initially didn’t release the model due to [_concerns about malicious applications_ ⁠](</index/better-language-models/>).

In the continuous world, the way to make the next system safe and beneficial is to learn from the current system. This is why we’ve adopted the principle of [_iterative deployment_ ⁠](<https://openai.com/index/language-model-safety-and-misuse/>), so that we can enrich our understanding of safety and misuse, give society time to adapt to changes, and put the benefits of AI into people’s hands. At present, we are navigating the new paradigm of [_chain-of-thought models_ ⁠](<https://openai.com/index/learning-to-reason-with-llms/>) \- we believe this technology will be extremely impactful going forward, and we want to study how to make it useful and safe by learning from its real-world usage. In the continuous world view, deployment aids rather than opposes safety.

These diverging views of the world lead to different interpretations of what is safe. For example, our release of ChatGPT was a Rorschach test for many in the field—depending on whether they expected AI progress to be discontinuous or continuous, they viewed it as either a detriment or learning opportunity towards AGI safety.

## Impacts of AGI

We are developing AGI because we believe in its potential to positively transform everyone’s lives. Almost any challenge facing humanity feels surmountable with a sufficiently capable AGI because intelligence has been responsible for most improvements for humanity, from literacy to machines to medicine.

Nevertheless, intelligence is a neutral term, and intelligence alone is not a guarantee for positive transformation. Achieving AGI’s potential includes working diligently to mitigate the potential harms of increasingly powerful AI systems, and developing and operating them in accordance with human values and with humans in control.

As AI becomes more powerful, the stakes grow higher. The exact way the post-AGI world will look is hard to predict—the world will likely be more different from today’s world than today’s is from the 1500s. But we expect the transformative impact of AGI to start within a few years. From today’s AI systems, we see three broad categories of failures:

  * **Human misuse** : We consider misuse to be when humans apply AI in ways that violate laws and democratic values. This includes suppression of free speech and thought, whether by political bias, censorship, surveillance, or personalized propaganda. It includes phishing attacks or scams. It also includes enabling malicious actors to cause harm at a new scale.
  * **Misaligned AI** : We consider misalignment failures to be when an AI’s behavior or actions are not in line with relevant human values, instructions, goals, or intent. For example an AI might take actions on behalf of its user that have unintended negative consequences, influence humans to take actions they would otherwise not, or undermine human control. The more power the AI has, the bigger potential consequences are.
  * **Societal disruption** : AI will bring rapid change, which can have unpredictable and possibly negative effects on the world or individuals, like increasing social tensions and inequality, or shifts in dominant values and societal norms. Access to AGI will determine economic success, which risks authoritarian regimes pulling ahead of democratic ones if they harness AGI more effectively.



Like with any new technology, there will be disruptive effects, some that are inseparable from progress, some that can be managed well, and some that may be unavoidable. Societies will have to find ways of democratically deciding about these trade-offs, and many solutions will require complex coordination and shared responsibility. Each failure mode carries risks that range from already present to speculative, and from affecting one person to painful setbacks for humanity to irrecoverable loss of human thriving.

We approach safety both by assessing current risks and anticipating future ones, mitigating each risk according to its impact and how much we can affect it today. We carefully balance capability development with proactive risk mitigation, with our [_Preparedness Framework_ ⁠(opens in a new window)](<https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf>) guiding hard tradeoffs.

## Our core principles

We don't know what the future will look like, and we have evolved our thinking already quite a bit over time. With this in mind, here are our core principles that currently guide our thinking and actions:

  * **Embracing uncertainty:**_We treat safety as a science, learning from iterative deployment rather than just theoretical principles._
  * **Defense in depth:**_We stack interventions to create safety through redundancy._
  * **Methods that scale:**_We seek out safety methods that become more effective as models become more capable._
  * **Human control** : _We work to develop AI that elevates humanity and promotes democratic ideals._
  * **Community effort:**_We view responsibility for advancing safety as a collective effort._



### Embracing uncertainty

 _We treat safety as a science, learning from iterative deployment rather than just theoretical principles._

We do not assume we can predict all future challenges in AI alignment solely from theoretical principles. Achieving safe AGI demands engaging with reality: beyond laboratory experiments, we must test systems in the real world and draw on the collective insight of everyone involved. Instead of working backward from hypothetical end states, we move forward taking incremental steps, while measuring and testing continuously. Because we conduct pre- and post-deployment assessments, we gain a deeper, empirical understanding of both capabilities and hazards as they emerge in real-world contexts. We do all of this while being cautious about assuming “alignment by default” from current training paradigms: insights drawn from earlier models or different training methods are useful but not definitive for future systems and training paradigms. Our approach demands hard work, careful decision-making, and continuous calibration of risks and benefits.

**Rigorous measurement**

Safety research requires science: standardizable measurement, open-minded experimentation, and testing. Being able to quantify risks effectively guides research direction and prioritization. We thus [_build_ ⁠](<https://openai.com/index/mle-bench/>) [_evaluations_ ⁠](<https://openai.com/index/introducing-swe-bench-verified/>) starting with measurement goals, often guided by a [_threat_ ⁠](<https://openai.com/index/building-an-early-warning-system-for-llm-aided-biological-threat-creation/>) model, and focus on capabilities that unlock potentially harmful behaviors. We iteratively expand and refine our evaluation suites to capture capability increases and evolving usage. We run these evaluations throughout model training and deployment processes to inform our training, launch, and mitigation plans.

**Proactive risk mitigation**

The best time to act is before risks fully materialize, initiating mitigation efforts as potential negative impacts—such as facilitation of malicious use-cases or the model deceiving its operator—begin to surface. While our [_Preparedness Framework_ ⁠(opens in a new window)](<https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf>)**** outlines how we do pre-deployment evaluations, we aim to advance mitigations early, even when risks have not yet fully developed, aren't currently causing harm, and are far from deployment. Even if we can’t observe these behaviors in the real world, we seek out opportunities for empirical observation, such as safely testing models in secure environments with restricted capabilities. As our systems become more powerful, they require additional safety measures. This proactive approach is how we understand and address issues before they escalate, and develop our safety techniques directly aligned with where capabilities are going.

**Iterative deployment**

It’s an advantage for safety that AI models have been growing in usefulness steadily over the years, making it possible for the world to experience incrementally better capabilities. This allows the world to engage with the technology as it evolves, helping society better understand and adapt to these systems while providing valuable feedback on their risks and benefits. Such iterative deployment helps us [_understand threats from real world use_ ⁠](<https://openai.com/index/disrupting-malicious-uses-of-ai-by-state-affiliated-threat-actors/>) and guides the research for the next generation of safety measures, systems, and practices.

In the future, we may see scenarios where the model risks become unacceptable even relative to benefits. We’ll work hard to figure out how to mitigate those risks so that the benefits of the model can be realized. Along the way, we’ll likely test them in secure, controlled settings. We may deploy into constrained environments, limit to trusted users, or release tools, systems, or technologies developed by the AI rather than the AI itself. These approaches will require ongoing innovation to balance the need for empirical understanding with the imperative to manage risk. For example, making increasingly capable models widely available by sharing their weights should include considering a reasonable range of ways a malicious party could feasibly modify the model, including by finetuning ([_see our 2024 statement on open model weights_ ⁠](<https://openai.com/global-affairs/openai-s-comment-to-the-ntia-on-open-model-weights/>)). We continue to develop the [Preparedness Framework⁠(opens in a new window)](<https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf>) to help us navigate and react to increasing risks. 

### Defense in depth

 _We stack interventions to create safety through redundancy._

It’s likely that no single intervention is the “solution” for safe and beneficial AI. Instead, we draw from the layered approaches in other safety-critical fields such as aerospace, nuclear power, and autonomous vehicles. This involves “layering” multiple defenses such that all of them would need to fail for a safety incident to occur.

First, in training our models for safety we apply multiple layers of support: [_teaching models to understand_ ⁠](</index/deliberative-alignment/>) and [_to adhere to core safety values_ ⁠](</index/improving-model-safety-behavior-with-rule-based-rewards/>), teaching them to follow user instructions and [_navigate conflicting instructions from different sources_ ⁠](</index/the-instruction-hierarchy/>), training them to be reliable even in the face of uncertainty, and making it robust to adversarial inputs. Our models are supported by complementary systemic defenses: [_continuous monitoring post-deployment_ ⁠](</index/a-holistic-approach-to-undesired-content-detection-in-the-real-world/>), [_open-source intelligence_ ⁠](</global-affairs/an-update-on-disrupting-deceptive-uses-of-ai/>) ([_OSINT_ ⁠(opens in a new window)](<https://en.wikipedia.org/wiki/Open-source_intelligence>)), and [_information security._ ⁠](</index/reimagining-secure-infrastructure-for-advanced-ai/>) Each safeguard has unique strengths and gaps, but by stacking multiple layers, we reduce the odds that an alignment failure or adversarial attack will slip through all defenses.

We test components individually as well as end-to-end. We establish safety protocols and principles for testing, including [_external red teaming_ ⁠](</index/red-teaming-network/>) and [_frontier risk assessments_ ⁠(opens in a new window)](<https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf>). We set clear deployment criteria, as outlined in our [_Preparedness Framework_ ⁠(opens in a new window)](<https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf>) and System Cards (see our System Cards for [_o1_ ⁠](</index/openai-o1-system-card/>), [_GPT‑4o_ ⁠](</index/gpt-4o-system-card/>), [_GPT‑4V(ision)_ ⁠(opens in a new window)](<https://cdn.openai.com/papers/GPTV_System_Card.pdf>), and [_GPT‑4_ ⁠(opens in a new window)](<https://cdn.openai.com/papers/gpt-4-system-card.pdf>)).

Importantly, we also leave room for evolution and iteration on our processes themselves. Our [Preparedness Framework⁠(opens in a new window)](<https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf>) has revision as a built-in principle to avoid ossifying as specific safety approaches become obsolete. 

![OpenAI safety diagram](https://images.ctfassets.net/kftzwdyauwt9/11cqEzkCP3m2xgaTNwj5q5/923c88040c8478f76b82645fdf48aee6/oai_safety_Diagram_Light.svg?w=3840&q=90)

## Methods that scale

 _We seek out safety methods that become more effective as models become more capable._

To align increasingly intelligent models, especially models that are more intelligent and powerful than humans, we must develop alignment methods that improve rather than break with increasing AI intelligence. In the past, we demonstrated that [_AI-written critiques_ ⁠](</index/critiques/>) [_augment humans’ ability_ ⁠](</index/finding-gpt4s-mistakes-with-gpt-4/>) to notice flaws, for example when training a next-generation model using RLHF. We also already [_use GPT‑4 for content policy development and moderation decisions_ ⁠](</index/using-gpt-4-for-content-moderation/>), and future AI might contribute to powerful safety measures such as formal verification which have been impractical for humans to implement at scale. Most recently, we have demonstrated that we can [_harness o1’s reasoning capabilities to improve its own alignment_ ⁠](</index/deliberative-alignment/>). We believe that increased intelligence can be harnessed to align superintelligence, but it’s not yet proven, and there’s a lot of evidence we will gather as we build more capable systems which could cause us to update our approach.

We are exploring ways to directly [_improve alignment by spending compute_ ⁠](</index/trading-inference-time-compute-for-adversarial-robustness/>), similar to how we improve intelligence. One way to do this is to directly optimize for robustness and reliability, which are critical to safe and aligned systems. Other ways could be maintaining a favorable balance between the strength of the training signal (e.g. reward models) and the model being trained, or using compute to improve our understanding of worst-case behaviors.

We have yet to fully understand, measure, and leverage the relationship between capabilities, safety, and alignment. Safety is often contextual, harder to measure, and thus harder to be optimized than capabilities such as solving math problems. As part of our research program, we aim to better understand how to optimize safety and capability under a unified objective, and how to leverage intelligence for alignment.

### Human control

 _We work to develop AI that elevates humanity and promotes democratic ideals._

Our approach to alignment centers humans. We aim to develop mechanisms that empower human stakeholders to express their intent clearly and [_supervise_ ⁠](</index/introducing-the-model-spec/>) AI systems effectively - even in complex situations, and as AI capabilities scale beyond human capabilities. Decisions about how AI behaves and what it is allowed to do should be determined by broad bounds set by society, and evolve with human values and contexts. AI development and deployment must have human control and empowerment at its core.

**Policy driven alignment**

We create transparent, auditable, and steerable models by integrating explicit policies and “case law” into our model training process. We facilitate transparency and democratic input by inviting public engagement in policy formation and incorporating feedback from various stakeholders. Our [_democratic inputs to AI grant_ ⁠](</index/democratic-inputs-to-ai-grant-program-update/>) was one example for exploring possible ways of democratic process to decide AI model behavior. Another example is our publishing of the [_Model Spec_ ⁠(opens in a new window)](<https://model-spec.openai.com/2025-02-12.html>), making explicit the tradeoffs and decisions that went into shaping it, and inviting public inputs for future versions. We are actively working on improving models’ ability to reason about [_human-written explicit policy_ ⁠](</index/deliberative-alignment/>) such as the Model Spec, to make sure that AI systems reliably follow directions.

**Alignment through human values, intent, and understanding**

Not all human values, preferences, and intents can be explicitly codified into policies or rules, because there is no _single_ moral or social norm. Many are nuanced, context-sensitive, and culture-dependent. Our research aims to bridge this gap by developing methods to encode these complex, often tacit elements into AI systems. This includes integrating human values, ethical principles, and common sense into our models, enabling them to not only follow explicit instructions but also respect the broader spirit of human intent. Grounding our models in these deeper principles helps them remain resilient to the imperfections of human feedback, preventing “reward hacking” and other exploitations of human error. While there often is no single right or wrong, we think that by teaching our models understanding in addition to compliance, we can develop tools to better adapt AI systems to diverse contexts, make informed decisions, and align with the moral and social norms of the communities they serve.

**Scalable oversight, active learning, verification, and Human-AI interfaces**

We focus on [_scalable oversight_ ⁠](</index/finding-gpt4s-mistakes-with-gpt-4/>) mechanisms that evolve alongside the increasing capabilities of AI systems. This includes [_novel human-AI interfaces_ ⁠](<https://openai.com/index/introducing-canvas/>) that empower individuals and institutions to interact with, control, visualize, verify, guide, and audit AI actions during development and post-deployment. We are exploring ways for AI systems to proactively identify areas of uncertainty, such as unclear risks, and seek clarification from human supervisors. Such systems can refine their understanding of human priorities and continually adjust their behavior to better align with evolving norms and contexts. Integrating scalable supervision mechanisms and active learning into human-AI interactions facilitates transparency and trust, ensuring that AI behaviors align with both individual expectations and institutional requirements as they evolve.

**Control in autonomous settings**

​​As AI systems increasingly operate beyond centralized infrastructures—residing on personal devices, embedded hardware, and forming networks of interacting agents— robust human oversight remains vital. Even when such systems can autonomously replicate, collaborate, or adapt their objectives, we must ensure that humans can meaningfully intervene and deactivate capabilities as needed. This involves for example designing mechanisms for remote monitoring, secure containment, and reliable fail-safes to preserve human authority.

### Community effort

 _We view responsibility for advancing safety as a collective effort._

Ensuring that AGI is safe and beneficial to everyone cannot be achieved by any single organization. It is a shared responsibility that depends on open collaboration across [_industry_ ⁠](</index/child-safety-adopting-sbd-principles/>), [_academia_ ⁠](</index/building-an-early-warning-system-for-llm-aided-biological-threat-creation/>), [_government_ ⁠](</index/openai-and-los-alamos-national-laboratory-work-together/>), and [_the public_ ⁠](</index/bug-bounty-program/>) at large.

OpenAI supports this principle by openly sharing safety-related insights, techniques and resources that can advance the entire field. We:

  * **Publish AI safety research** so that our methods and findings can contribute to the broader conversation and can be subject to external review, including peer review. 
  * **Provide resources to the field** , such as [_new_ ⁠](</index/introducing-swe-bench-verified/>) [_evaluation_ ⁠](</index/introducing-simpleqa/>) [_suites_ ⁠](</index/mle-bench/>) that can more reliably evaluate advancing capabilities and [_access to frontier methods_](</residency/>) and make use of artifacts the field produces, such as red teaming and evaluations.
  * **Fund research** that advances the field, in areas ranging from [_democratic inputs_ ⁠](</index/democratic-inputs-to-ai/>) into the design of AI systems to [_cybersecurity applications of AI_ ⁠](</index/openai-cybersecurity-grant-program/>).
  * **“Work in public” on the practical aspects of AI safety** , sharing our experiences building, testing, and delivering frontier AI at scale, so that the public, policymakers, and other practitioners can learn from our experience.
  * **Make our thinking on model behavior transparent and accountable** , through projects such as the [_Model Spec_ ⁠(opens in a new window)](<https://model-spec.openai.com/>).
  * **Support government expertise on AI safety and security,** including through our partnerships with the [_US AI Safety Institute_ ⁠(opens in a new window)](<https://www.nist.gov/news-events/news/2024/08/us-ai-safety-institute-signs-agreements-regarding-ai-safety-research>) and UK AI Security Institute to advance the science and practice of safety and capability evaluations.
  * [**_Propose policy initiatives_** ⁠](</global-affairs/openais-economic-blueprint/>)**** that include common sense rules of the road so that AI’s benefits can be maximized for everyone.
  * **Make**[**voluntary commitments** ⁠(opens in a new window)](<https://cdn.openai.com/global-affairs/paris-summit-update-on-voluntary-commitments-20250207.pdf>) such as publicly announced safety protocols and adherence to recognized industry standards that encourage us to follow best practices, even before new laws are in place. For instance, our [_Preparedness Framework_ ⁠(opens in a new window)](<https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf>) has become a leading model of how to address frontier risk, and helped inspire the recent [_Frontier AI Safety Commitments_ ⁠(opens in a new window)](<https://www.gov.uk/government/publications/frontier-ai-safety-commitments-ai-seoul-summit-2024/frontier-ai-safety-commitments-ai-seoul-summit-2024>) signed by 16 leading labs at a global summit.



We don’t know all the answers. We don’t even have all the questions. Because we don’t know, we are open to being wrong about our expectation on how progress will unfold and our approach to the challenges we see. We believe in a culture of healthy discussion and want feedback from people with different perspectives and attitudes on AI risk, especially those who may not agree with OpenAI’s current position.

Research

  * [Research Index](</research/index/>)
  * [Research Overview](</research/>)
  * [Economic Research](</signals/>)



Latest Advancements

  * [GPT-5.5](</index/introducing-gpt-5-5/>)
  * [GPT-5.4](</index/introducing-gpt-5-4/>)
  * [GPT-5.3 Instant](</index/gpt-5-3-instant/>)



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



API Platform

  * [Overview](</api/>)
  * [API Log In(opens in a new window)](<https://platform.openai.com/login>)
  * [Docs(opens in a new window)](<https://developers.openai.com/api/docs>)



Business

  * [Overview](</business/>)
  * [Solutions](</solutions/>)
  * [Resources](</business/learn/>)
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

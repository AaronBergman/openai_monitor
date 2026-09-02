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

September 1, 2026

[Safety](</news/safety-alignment/>)[Security](</news/security/>)

# Path to Astra: critical capabilities and frontier safeguards

Loading…

Share

Assessing Astra’s cybersecurity capabilities

  * Assessing Astra’s cybersecurity capabilities
  * Safeguards required for critical capabilities
  * Robustness against cyber abuse
  * Alignment & monitoring
  * What this will mean for users
  * Looking forward



  * Assessing Astra’s cybersecurity capabilities
  * Safeguards required for critical capabilities
  * Robustness against cyber abuse
  * Alignment & monitoring
  * What this will mean for users
  * Looking forward



Since our [_earlier assessment_](</index/responding-next-frontier-critical-cyber-capabilities/>) that Astra might reach a critical level of cybersecurity capability, we have gathered more evidence and run additional evaluations to assess the model’s capabilities. We now believe Astra meets the Critical cybersecurity capability threshold under our [_Preparedness Framework_](</index/updating-our-preparedness-framework/>) , meaning that with the right tools and access, it can find previously unknown security flaws and develop ways to exploit them across many well-protected systems without a person guiding each step. It is the first model we are designating at this level, and requires stronger safeguards during development and before release.

Over the past several weeks, we have delayed parts of Astra’s development and release while we strengthened and tested protections against cyber misuse and unauthorized model actions. Based on that work, we believe Astra’s safeguards sufficiently minimize the risk of severe harm for release under our Preparedness Framework.

While Astra was not involved in the [_Hugging Face incident_](</index/hugging-face-incident-and-the-road-ahead/>) , we have incorporated our [_learnings_ ⁠(opens in a new window)](<https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf>) from that incident into our safety approach. Based on retrospective testing, we believe our production safeguards at the time would have prevented the Hugging Face incident. We have since implemented even stronger safeguards for Astra, including training the model to more reliably refuse harmful cyber requests and respect safety restrictions, additional protections against misuse, and monitoring that can stop potentially unauthorized activity.

We plan to make Astra available soon, but access to its most advanced cybersecurity capabilities will be more limited. Advanced cybersecurity work will initially be available to a group of testers, with access through Daybreak Blue following to expand defensive use.

We will share more details about our safety, security and alignment testing and evaluations in the model’s system card at launch. Ahead of release, we want to provide an update on some of the work we have been doing to prepare to safely release a model with this level of cybersecurity capabilities—and be transparent about what risks remain.

## Assessing Astra’s cybersecurity capabilities

Under our [_Preparedness Framework_](</index/updating-our-preparedness-framework/>) , a model meets the Critical threshold if either of the following conditions is met:

  * The model can identify and develop functional zero-day exploits of all severity levels in many hardened real-world critical systems without human intervention.
  * The model can devise and execute end-to-end novel strategies for cyberattacks against hardened targets given only a high level desired goal.



Our preparedness evaluation of Astra combined automated public and private benchmarks with expert-driven assessments. Astra represents a significant increase in cybersecurity capabilities compared to GPT‑5.6 Sol: it is both significantly more token efficient and more capable at vulnerability identification and exploit development.

As one example, we ran Astra on ExploitBench where the model achieved a perfect score of 100% on the benchmark to evaluate the model’s ability to develop exploits from known vulnerabilities.

Due to contamination concerns, we then built an internal benchmark denoted “ExploitBench - Internal Port (June–August 2026)”, which contains 20 high-severity V8 vulnerabilities that were disclosed more recently _._ On this dataset, Astra achieves much higher arbitrary code-execution rates than GPT‑5.6 Sol using far fewer output tokens. During the evaluation, the model even discovered and used two zero-day vulnerabilities as part of an exploit chain. We are in the process of disclosing these two vulnerabilities to the maintainers.

_Astra results shown reflect capabilities with Daybreak Blue access, not the default production configuration._

In expert-led assessments against a hardened browser and operating system, Astra discovered previously unknown vulnerabilities and turned them into working exploit chains. It built a full browser-compromise chain that escaped the sandbox and executed commands on the host, when the browser opened an HTML file. The model also found multiple vulnerabilities in a hardened operating system and combined them into a local privilege-escalation chain from an unprivileged user to root. All together, our investigation has led us to conclude that Astra meets the critical threshold.

## Safeguards required for critical capabilities

For models with Astra’s level of cybersecurity capabilities, we need to cover two pathways to minimize risk for severe cyber harm, both during development and before deployment:

  * **Malicious actors using the model.** Our safeguards must robustly prevent malicious actors from using Astra to develop exploits for previously unknown flaws in hardened critical systems or to carry out end-to-end attacks against hardened targets.
  * **The model taking unauthorized, misaligned actions.** Even in the absence of a malicious user, a model with advanced cybersecurity capabilities could itself cause cyber harm if misaligned. In addition to having a very high standard for alignment for models with these capabilities, our safeguards must be able to rapidly detect and contain misaligned actions that could cause significant real-world harm as a second layer of defense.



Notably, the second pathway applies to _both_ internal development and external deployment. As we [_previously described_](</index/pacing-model-development-cyber-capabilities/>) , we paused certain frontier training (including certain training for Astra) for two weeks after the OpenAI-Hugging Face incident in order to harden our training infrastructure, including isolation and network controls, expanded monitoring, and strengthened alignment training and thresholds. We then continued smaller-scale work under stricter controls.

We held back certain larger reinforcement learning (RL) runs for future versions of Astra for longer, while we established higher bars for the safety and security of their training environment. On August 28th, we restarted the large frontier RL run that was previously paused after the new safety and security requirements were put in place. We are continuing to temporarily hold back some smaller experimental training runs.

Preparing Astra for release has also required stronger protections against cyber abuse and unauthorized actions. Below, we describe those safeguards and how we have tested them.

## Robustness against cyber abuse

Since deploying the first model we treated as High capability in cybersecurity in [_February_](</index/introducing-gpt-5-3-codex/>) , we have strengthened our cyber safeguards with each successive launch. Our overall safety approach layers post-trained model refusals, system level safety classifiers, as well as offline detection and threat disruption.

For [_GPT‑5.6_ ⁠(opens in a new window)](<https://deploymentsafety.openai.com/gpt-5-6>), we significantly improved the robustness of our system level stack, including by adding activation classifiers to detect cyberabuse and improving coverage over universal jailbreaks found through intensive automated red-teaming. Building upon these improvements, for Astra we have invested further into the model layer of our safeguard stack, as well as improving the ability of our safeguards to handle cross conversation context.

  * Leveraging new training techniques for model robustness, Astra more robustly refuses requests for disallowed cyber assistance. On our set of cyber jailbreak evaluations, Astra refuses 91.5% of requests (compared to 59% from GPT‑5.6 Sol).
  * For accounts assessed as higher risk, we apply a more conservative model-behavior boundary that refuses a broader range of potentially risky cyber assistance. For high risk users, we’ve [_expanded the context_](</index/chatgpt-recognize-context-in-sensitive-conversations/>) of our monitoring systems to be able to catch these kinds of cyber abuse.



We have also continued our program of rigorous testing, internal and external red-teaming, and remediation. In addition to regression testing to make sure all jailbreaks found from our previous testing periods remain covered, we are performing a new wave of red-teaming with our latest [_internal red-teaming attackers_](</index/unlocking-self-improvement-gpt-red/>). We are working with industry partners to define a common jailbreak rating system and will use our 24/7 rapid-response program to investigate and address new findings. We will share more details about our cyber safeguard testing in the Astra system card.

Helping defenders find and fix vulnerabilities remains a central pillar of our safety approach. At launch, we expect Astra’s safeguards to create more friction than we ultimately intend in order to protect against potential misuse. Access to Astra for advanced cybersecurity workflows will initially be available to a small group of alpha testers, with access through Daybreak Blue expanding afterward to support defensive use.

## Alignment & monitoring

We have also added additional layered protections to prevent the model from taking potentially misaligned actions:

  * **Model alignment:** In our evaluations, Astra was far more likely than GPT‑5.6 Sol to respect explicit safety and security restrictions and remain within its authorized scope, making it our most aligned model to date. We especially focused on the model’s respect for security and safety restrictions and propensity to stay within its authorized scope.
  * **Monitoring and control:** Paralleling our procedures internally, we are deploying Astra with additional chain-of-thought monitoring to rapidly detect and contain potentially misaligned actions.



Astra is a significant step forward in model alignment, and the culmination of several long-running alignment workstreams (ranging from pre-training interventions to more careful and consistent grading during reinforcement learning). In testing, we find that Astra is consistently more likely to respect explicit safety restrictions and warnings (such as auto-review) compared to GPT 5.6 Sol.

We also developed a test informed by the Hugging Face incident, in which agents running the cyber evaluation ExploitGym compromised a third party’s systems. We used the hardest tasks from that evaluation to create “honeypot” tests of whether a model would try to compromise surrounding security infrastructure instead of solving its assigned task. GPT‑5.6 Sol, without production safeguards, attempted to access those targets in 56% of tests simulating the benchmark environment where the model is instructed to develop exploits. Astra made no such attempts in these tests. These figures describe behavior under the test conditions without cyber safeguards, not normal production use.

_Left: In this new evaluation, we observe how models react to a rejection from auto-review. Each task is set in a knowledge-work environment, with the rollout beginning immediately after an auto-review denial. There are multiple ways then for the model to proceed: end the rollout, attempt to find a safer alternative, retry a similar command, or exploit a_[ _poor configuration_ ⁠(opens in a new window)](<https://learn.chatgpt.com/docs/agent-configuration/rules>)_to bypass auto-review entirely. Any pursuit of the latter two options would constitute a failure of this evaluation. Astra never attempted to circumvent auto-review.  
  
Right: In this evaluation, we check the tendency of a model to cheat (using “honeypots”) when faced with the most difficult or impossible tasks in the exploit gym evaluation. This was run in a simulated environment, with safeguards in observation-only mode, to evaluate the model’s behavior. While GPT‑5.6 Sol indicated higher likelihood for cheating in these scenarios, Astra did not attempt to use those shortcuts, and it was still able to legitimately solve some tasks._

Training models to be aligned is one layer of safety. We will share more detail about our alignment testing and results in the Astra system card.

We are also deploying misalignment monitoring in production for Astra-class models in order to detect and rapidly contain potential misalignment. These safeguards resemble our monitoring for internal deployments and involve a system of classifiers which check the model’s reasoning and actions for unauthorized behavior and automatically stop potentially unauthorized activity. These safeguards cannot replace good alignment of our models as capabilities increase, and our goal is for future models to be aligned well enough that these safeguards are never triggered.

## What this will mean for users

OpenAI is committed to ensuring that the benefits of AI are broadly accessible. Given the significant increase in Astra’s cybersecurity capabilities, we are being especially careful to make this deployment safe and secure. Extra safety checks can sometimes slow, pause, or stop legitimate work, including defensive cybersecurity.

The system may occasionally flag legitimate activity as potential cyber misuse or unauthorized behavior, leading to it inadvertently being slowed, paused, or stopped. This can include work that does not appear directly related to cybersecurity or tasks in which an agent is running for an extended period.

If the misalignment monitor pauses a task, users in ChatGPT or Codex may be asked to review the action before continuing. When using other surfaces like the API, the task will stop. We plan to keep calibrating these safeguards to reduce unnecessary interruptions and expand access to frontier capabilities through programs like Daybreak.

## Looking forward

We are entering a stage of AI development in which models can take on more consequential work, and failures of alignment and control can have more serious effects. Realizing the benefits of these systems will depend on our ability to align and control models as their capabilities grow.

That responsibility extends across training, evaluation, and deployment. It requires stronger evidence of aligned behavior, safeguards that keep pace with capability, and a willingness to slow down when those protections are not sufficient.

We will continue to test these systems, share what we learn, and be clear about what remains uncertain. The models that follow Astra will demand more of us. We will take the time and do the work needed to meet that responsibility.

  * [2026](</news/?tags=2026>)
  * [Framework](</news/?tags=framework>)
  * [Alignment](</news/?tags=alignment>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

[The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)

![Our commitment to Zero Data Retention as AI advances — card](https://images.ctfassets.net/kftzwdyauwt9/6bPStWA6pc66cahnhg0jo6/61786b178401b6e902e9da65fa4da095/Blog_Thumbnail_-_OpenAI_Blog.png?w=3840&q=90&fm=webp)

[Offering Zero Data Retention for frontier modelsCompanyAug 19, 2026](</index/offering-zero-data-retention-for-frontier-models/>)

![ChatGPT for Teens — square card](https://images.ctfassets.net/kftzwdyauwt9/5IP7e1KeD8zkZq6YUrKdKW/2325215681ea59d32dd09b3ea90f12c5/Art_Card-TEENS-1x13x.png?w=3840&q=90&fm=webp)

[Introducing ChatGPT for TeensProductAug 18, 2026](</index/chatgpt-for-teens/>)

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

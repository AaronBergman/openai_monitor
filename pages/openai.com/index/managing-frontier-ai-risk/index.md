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

# Managing frontier AI risk: From training to deployment

November 18, 2026 · Safety

Share

Defense in depth across the model lifecycle

  * Defense in depth across the model lifecycle

    * During research: contain models in sandboxed environments

    * Internal deployment: test alignment, closely monitor behavior

    * External deployment: protect against misuse and misalignment at scale

  * Incident Response and Disclosure

  * Related research and resources




  * Defense in depth across the model lifecycle

    * During research: contain models in sandboxed environments

    * Internal deployment: test alignment, closely monitor behavior

    * External deployment: protect against misuse and misalignment at scale

  * Incident Response and Disclosure

  * Related research and resources




The capabilities of frontier models are rapidly accelerating, and our ability to understand, align, and secure them must stay ahead. We are pacing the development and release of our models, including [_pausing_](</index/pacing-model-development-cyber-capabilities/>) [_internal training_ ⁠(opens in a new window)](<https://alignment.openai.com/misalignment-reports/an-agent-used-dns-to-reach-an-external-chatbot/>) or holding back models like GPT‑6.1 Astra when we need more time to meet our safety standards. We’ve introduced new processes such as [_safety cases_](</index/towards-safety-cases-for-frontier-ai-training/>) and require stronger evidence of aligned behavior throughout training. These requirements slow the pace of model releases, but they give us greater confidence to safely move forward.

Since the [_Hugging Face incident_ ⁠](<https://openai.com/index/hugging-face-incident-and-the-road-ahead/>) in July, we've strengthened safeguards and alignment requirements for how we train, test, and deploy models. This post explains how we evaluate and manage risk at each stage, from highly sandboxed training environments to the Codex deployment you use on your computer. We evaluate both models and safeguards at each stage, requiring a safety review to advance to the next stage. 

## Defense in depth across the model lifecycle

We use _defense in depth_ with multiple layers of protection that reduce dependence on any single safeguard. If one layer fails, others help prevent harm, limit consequences, or alert us so we can intervene.

We organize our protections around four layers:

Effective monitoring depends on **model monitorability** \- how reliably monitors can detect mistakes or unsafe behavior from a model’s reasoning and actions. For example, a model that verbalizes its intention to cheat in its chain-of-thought (CoT) is more monitorable than one that omits this information. We evaluate monitorability during training and before deployment, develop better [methods for measuring⁠(opens in a new window)](<https://alignment.openai.com/beyond-gmean-squared/>) it, and [study _what affects it_ ⁠(opens in a new window)](<https://alignment.openai.com/cot-monitorability-model-lifecycle/>).

The Hugging Face incident showed why we should not rely on sandboxing alone to contain highly capable models. We now monitor frontier models across most internal and external deployment settings, including all [_internal deployments that use tools_](</index/how-we-detect-frontier-model-misalignment/>).

The role of each layer changes across three stages of model development and deployment:

  * **Research:** We train, test, and use models in sandboxed environments.

  * **Internal deployment:** OpenAI employees use models for practical work.

  * **External deployment:** Models become available to people and organizations more broadly.




We rely on different layers at different stages. During training, when alignment is less certain, we depend more heavily on sandboxing and monitoring. As models gain broader access during deployment, alignment and system-level controls become increasingly important. At each stage, we evaluate whether the combined protections are sufficient for the model’s capabilities and access. Our determinations may be reviewed with our Safety Advisory Group (SAG) and overseen by the Safety and Security Committee (SSC) of the OpenAI Foundation’s Board of Directors. 

### During research: contain models in sandboxed environments

During the research phase, we evaluate models to gain confidence in their alignment properties. Because we cannot yet fully rely on alignment to prevent harm, we rely heavily on security and sandboxing to restrict what they can access and do.

Based on the current state of alignment research, monitoring systems, and the security of internet infrastructure, we believe the responsible approach is to conduct frontier model training with [_no live internet access_](</index/securing-our-frontier-model-training-environment/>). After the Hugging Face incident, we [_significantly restructured_](</index/securing-our-frontier-model-training-environment/>) our internal research systems to contain models using:

  * sandboxes that restrict the privileges of the model

  * virtual machines to further isolate the workload from the underlying computer

  * network and cloud perimeters that cut the entire cluster off from the internet 




We continuously red-team this system, having teams of our strongest models try to reach the live internet, escape security boundaries, or communicate with agents they are meant to be isolated from. This helps us test whether containment holds against the capabilities of the models it is intended to constrain.

As an additional layer of defense, we monitor all frontier inference to detect if the model has bypassed our security invariants. If our monitoring detects that the model has reached the internet, we [_page our security teams_](</index/how-we-detect-frontier-model-misalignment/>) and autopause the workload. 

Monitoring provides a critical backstop when containment fails. In a recent misalignment report, we shared that monitors[ _detected an internal research model exploiting a DNS misconfiguration_ ⁠(opens in a new window)](<https://alignment.openai.com/misalignment-reports/an-agent-used-dns-to-reach-an-external-chatbot/>) to gain limited internet access. We paused training and evaluation of our most capable models from September 20th to October 1st while we investigated and [_addressed the security gap_](</index/securing-our-frontier-model-training-environment/>).

To make interventions fast and reliable, we built [_Control Room_ ⁠](<https://openai.com/index/control-room/>), a central system that tracks research workloads and stops further model output within 35 seconds of receiving an instruction to halt a job. These controls are enforced directly in the inference infrastructure, so they do not depend on each research workload implementing its own shutdown mechanism. For frontier-model research workloads, they also stop model output if Control Room becomes unavailable.

Red-teaming and monitoring work together. We cannot guarantee that a sandbox is impenetrable, but red-teaming helps us assess how much effort a model would need to escape it. The more effort the model requires, the more the opportunity for monitors to detect and stop it.

We mandate strong security and monitoring controls at the research stage for a few reasons:

  * **Models are still being evaluated.** Some have not yet completed the safety training, alignment audits, and reviews required for public release.

  * **Frontier research settings can amplify risks.** Certain research tasks require more ambitious setups, making the model more persistent or capable than typically seen during external deployment (for example, a team of 10,000 agents was required to solve the [_Navier Stokes problem_](</index/navier-stokes-solution/>)).

  * **Training runs at scale with less direct human oversight.** Unlike a typical Codex session, our training workloads involve large numbers of model actions without a person following each interaction.




### Internal deployment: test alignment, closely monitor behavior

Before broad release, employees switch from sandboxed research use of [_frontier models to unsandboxed internal use_](</index/research-acceleration-view-inside-openai/>) , e.g. making the model accessible in ChatGPT to employees. This gives us a better understanding of how the models [_behave in practical settings_ ⁠(opens in a new window)](<https://alignment.openai.com/eval-production-behavior-gap/>), and informs deployment decisions. 

During this phase, we give the model access to the broader internet, our Slack, our codebase, and internal infrastructure. This is a significant change in risk, as the model’s actions now have a direct impact on the systems we use to build and run OpenAI. During internal deployment, we need to rely more on model alignment, system safeguards, and monitoring as opposed to security controls. 

Before a frontier model can be deployed outside of the sandbox, it must first go through alignment and [_monitorability testing_ ⁠(opens in a new window)](<https://alignment.openai.com/beyond-gmean-squared/>). We have a suite of alignment evaluations, which test both for specific alignment failure modes (such as circumventing safety and security restrictions) and broad measurements of propensity (such as resampling internal Codex trajectories and checking for misalignment). You can see more about our alignment and monitorability evaluations in the latest [_GPT‑6 Astra system card_ ⁠(opens in a new window)](<https://deploymentsafety.openai.com/gpt-6-astra>).

Mimicking our production setups, we add an additional layer of defense with system-level classifiers, which are designed to protect against frontier harms such as cyberabuse and bioweaponization. We also generally require [_Auto-Review_ ⁠(opens in a new window)](<https://alignment.openai.com/auto-review/>) for employees using Codex, which evaluates potentially risk actions and escalates them back to the user.

Finally, we monitor for misaligned behavior on every frontier inference during internal deployment. Since the model now has expanded privileges and access to internal information and systems, risks such as data exfiltration, or sending sensitive data to an unauthorized destination, become especially important to detect. Monitoring also helps us investigate [_new forms of misalignment_ ⁠(opens in a new window)](<https://alignment.openai.com/misalignment-reports/>).

### External deployment: protect against misuse and misalignment at scale

Public deployment exposes models to far more users, tasks, and environments, increasing both the scale and variety of risks. At this stage, we also need to protect against potentially malicious actors who purposefully direct the model to perform harm.

Before public release, models and system safeguards must meet our external deployment safety requirements. We assess them through:

  * **Performing a larger suite of alignment and safety evaluations.** For our frontier models, this includes performing new rounds of [_adaptive testing_ ⁠](<https://openai.com/index/unlocking-self-improvement-gpt-red/>) with our internal automated redteamers to stress-test the robustness of the model. We publish the results of our capability and safety evaluations in our [_system cards_ ⁠(opens in a new window)](<https://deploymentsafety.openai.com/gpt-6-astra>).

  * **For our most capable models, we also perform testing with third parties** to stress-test both our safeguards against misuse and the underlying alignment of our models.

  * **Examining monitoring flags from the internal deployment stage** to track any changes in the base model’s underlying alignment.




In addition to our “synchronous” safeguards (such as model safety training and system classifiers), for external deployments we also leverage offline enforcement and investigation. These teams use a combination of scaled agentic investigators and human review to detect and identify potential threat actors, ranging from cyberabuse, bioweaponization, [_distillation_ ⁠](<https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign/>), and misalignment from the model itself. Offline enforcement is especially helpful to gather information _across_ accounts in order to build a more holistic picture of a potential threat.

Trusted access programs, such as [_Daybreak_](</daybreak/>) and [_Rosalind_ ⁠](<https://openai.com/index/introducing-gpt-rosalind/>), offer another layer of security, and accelerate defenders and legitimate researchers while restricting access by potential attackers. 

## Incident Response and Disclosure 

When we notice a failure in one of our layers of safety, regardless of whether any harm actually occurred, we want to quickly investigate, triage, and if possible and appropriate, disclose the failure externally. Under our [_misalignment reporting_ ⁠](<https://openai.com/index/model-misalignment-reporting-framework/>) policy, any employee can flag an incident for public disclosure. These reports are investigated, and if there is a disagreement on whether they should be externally disclosed, the decision is escalated to our Safety Advisory Group (SAG). In addition to relying on employee reports, we proactively look for misalignment incidents so we can address them and share findings. 

You can see our misalignment reports [_here_ ⁠(opens in a new window)](<https://alignment.openai.com/misalignment-reports/>).

​

* * *

​

This work depends on both research progress and operational discipline: configuring controls correctly, testing how they interact, and responding decisively when they fail. A misconfigured network service or a failed automatic stop can undermine otherwise strong protections.

As models gain new capabilities, we will need to keep challenging the assumptions behind our safeguards and improving them where necessary. Lessons from research, internal use, and public deployment must inform how we train, evaluate, and deploy the next models.

We will continue sharing findings through system cards, incident reports, internal deployment [_risk reports_ ⁠(opens in a new window)](<https://cdn.openai.com/trust-and-transparency/oai_internal-use-catastrophic-risk-assessments_2026_2.pdf>), and [_external evaluations_ ⁠](<https://openai.com/index/priorities-principles-third-party-assessments/>) so that others can scrutinize our approach, including its limitations. When that evidence falls short of the bar we hold for safety, we will again pause training or withhold release until those requirements are met.

## Related research and resources

**Setting safety standards**

  * [ _**Pacing model development in an era of cyber-critical capabilities**_](</index/pacing-model-development-cyber-capabilities/>) — How we slowed frontier training while strengthening containment, expanding monitoring, and requiring stronger evidence of alignment.

  * [_**Towards safety cases for frontier AI training**_](</index/towards-safety-cases-for-frontier-ai-training/>) — Initial guidelines for evidence-based safety arguments covering technical safeguards, operational practices, and investigations of misalignment.

  * [_**Priorities and principles for effective third party assessments**_ ⁠](<https://openai.com/index/priorities-principles-third-party-assessments/>) — Our proposed approach to independent scrutiny of safety cases, safeguards, evaluations, and model behavior.

  * [_**Periodic Summary of Internal Use Catastrophic-Risk Assessments**_ ⁠(opens in a new window)](<https://cdn.openai.com/trust-and-transparency/oai_internal-use-catastrophic-risk-assessments_2026_2.pdf>) — Our public report covering June–September 2026 describes internal frontier-model deployments, their assessed risks, and changes to safeguards and governance.




**Defining and evaluating aligned behavior**

  * [ _**An updated Model Spec for more capable and beneficial AI**_ ⁠](<https://openai.com/index/updated-model-spec/>) — How we updated the Model Spec around five core values to guide models’ judgment, behavior, and respect for human oversight.

  * [_**Eval-production behavior gaps in agent safety and the role of eval-awareness**_ ⁠(opens in a new window)](<https://alignment.openai.com/eval-production-behavior-gap/>) — A study of differences between safety-evaluation results and production behavior, including how models’ interpretations of evaluation objectives affect performance.

  * [_**Beyond g-mean²: complementary metrics for monitorability**_ ⁠(opens in a new window)](<https://alignment.openai.com/beyond-gmean-squared/>) — New metrics for comparing monitorability and estimating residual risk in simulated systems where monitors reject model outputs.

  * [_**GPT‑6 Astra System Card**_ ⁠(opens in a new window)](<https://deploymentsafety.openai.com/gpt-6-astra>) — Detailed evaluations of Astra’s capabilities, safety, alignment, and monitorability, alongside its deployment safeguards and limitations.




**Containing models and improving safeguards**

  * [ _**Securing our frontier model training environment**_](</index/securing-our-frontier-model-training-environment/>) — How we strengthened isolation, built offline research environments, and used our strongest models to test containment boundaries.

  * [_**Training activation classifiers for safety and alignment**_ ⁠(opens in a new window)](<https://alignment.openai.com/training-activation-classifiers/>) — How classifiers use models’ internal activations to detect potentially harmful behavior and interrupt responses or tool calls.

  * [_**Auto-review of agent actions without synchronous human oversight**_ ⁠(opens in a new window)](<https://alignment.openai.com/auto-review/>) — How a separate review agent assesses actions that cross sandbox boundaries, helping coding agents work autonomously while blocking potentially harmful or unauthorized actions.

  * [_**GPT‑Red: Unlocking Self-Improvement for Robustness**_ ⁠](<https://openai.com/index/unlocking-self-improvement-gpt-red/>) — How we train automated red-teamers through self-play to discover vulnerabilities and improve models’ robustness against prompt injections.

  * [_**Control Room**_ ⁠](<https://openai.com/index/control-room/>) — How we track workloads across our research infrastructure and enforce rapid stops to model output when safety or security concerns require intervention.




**Incident response and disclosure**

  * [ _**How we detect frontier model misalignment**_](</index/how-we-detect-frontier-model-misalignment/>) — Our monitoring system combines activation probes, model-based review, automated investigation, and human response to detect and investigate concerning behavior.

  * [_**The Hugging Face incident and the road ahead**_ ⁠](<https://openai.com/index/hugging-face-incident-and-the-road-ahead/>) — Our findings from the Hugging Face incident and the changes it prompted across security, monitoring, and alignment.

  * [_**An agent used DNS to reach an external chatbot**_ ⁠(opens in a new window)](<https://alignment.openai.com/misalignment-reports/an-agent-used-dns-to-reach-an-external-chatbot/>) — How a research model bypassed internet restrictions through insufficient DNS filtering, how monitoring detected it, and the controls added afterward.

  * [_**Disrupting a coordinated model-distillation campaign**_ ⁠](<https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign/>) — How we investigated and disrupted attempts to extract protected model reasoning through account enforcement, technical controls, and partner coordination.

  * [_**Our framework for reporting model misalignment**_ ⁠](<https://openai.com/index/model-misalignment-reporting-framework/>) — Our process for tracking, investigating, and disclosing concerning model behavior, including cases whose causes or significance remain uncertain.

  * [_**Misalignment Reports and Notices**_ ⁠(opens in a new window)](<https://alignment.openai.com/misalignment-reports/>) — Our collection of disclosed incidents and notices showing how misalignment arises and where safeguards succeed or fail.




**Research progress and applications**

  * [ _**Research acceleration: The view inside OpenAI**_](</index/research-acceleration-view-inside-openai/>) — Early evidence of how coding agents are changing research inside OpenAI, including their growing use, increasingly complex tasks, and effects on experimentation.

  * [_**On the Navier–Stokes Millennium Prize Problem**_](</index/navier-stokes-solution/>) — A mathematical proof produced by an internal AI system, accompanied by a Lean formalization, illustrating the capabilities of large-scale research deployments.

  * [_**Daybreak**_](</daybreak/>) — Our cybersecurity program provides vetted defenders with advanced AI capabilities, security tools, and support to find vulnerabilities and strengthen defenses.

  * [_**Introducing GPT‑Rosalind for life sciences research**_ ⁠](<https://openai.com/index/introducing-gpt-rosalind/>) — A specialized model for biology, drug discovery, and translational medicine, available to eligible organizations through a trusted-access program.




  * [Alignment](</news/?tags=alignment>)
  * [Cybersecurity](</news/?tags=cybersecurity>)
  * [User Safety & Control](</news/?tags=user-safety>)
  * [2026](</news/?tags=2026>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

![Securing our frontier model training environment — Cover](https://images.ctfassets.net/kftzwdyauwt9/1YAlC4a6FgYc9r73SDH0Ef/bcd6bdf945006094fbc327ac46dee04d/new-approach-to-research-model-containment-cover.png?w=3840&q=90&fm=webp)

[Securing our frontier model training environmentSecurityOct 23, 2026](</index/securing-our-frontier-model-training-environment/>)

![How we detect frontier model misalignment — Cover](https://images.ctfassets.net/kftzwdyauwt9/43ZavE2amLHMmbxH8EL8VM/1464d0f68c0f3c45e9d255992aab32b1/how-we-detect-frontier-model-misalignment-cover.png?w=3840&q=90&fm=webp)

[How we detect frontier model misalignmentSecurityOct 29, 2026](</index/how-we-detect-frontier-model-misalignment/>)

![Our framework for reporting model misalignment — card image](https://images.ctfassets.net/kftzwdyauwt9/3mJz9GkBOjZvAMYPx8M1dj/2a9ac4b7e18b1c08feef5368c4fde2e2/model-misalignment-reporting-framework--cover-v002.png?w=3840&q=90&fm=webp)

[Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)

Research

  * [Research Index](</research/index/>)
  * [Research Overview](</research/>)
  * [Economic Research](</signals/>)



Latest Advancements

  * [GPT-6.2](<https://openai.com/index/introducing-gpt-6-2-astra-sol>)
  * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  * [GPT-6 Astra](</index/gpt-6-astra/>)
  * [GPT-5.6](</index/gpt-5-6/>)



Safety

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

![User intent and the Model Spec inform a model response in an expanded alignment layer above security, safeguards, and monitoring.](https://images.ctfassets.net/kftzwdyauwt9/6KPhYeZJEAA3TH4MqJsDKJ/65ad6cab0e4e4f2f77cfc6af16924c9d/model-alignment-expanded-layer-light.png?w=3840&q=90&fm=webp)

![An expanded security layer shows a sandbox within a virtual machine and network boundary restricting access to resources, between alignment, safeguards, and monitoring layers.](https://images.ctfassets.net/kftzwdyauwt9/K6ygWjrv1UiYhVWU7y2MZ/8c70a8a832989e6f44868f167f47fae1/security-sandboxing-expanded-layer-light.png?w=3840&q=90&fm=webp)

![An expanded safeguards layer routes a request through a safety classifier to allow or block, between alignment, security, and monitoring layers.](https://images.ctfassets.net/kftzwdyauwt9/2uRnqXKbQEqsGTWMeygmQJ/06686ab01254774a778abc76a54eab60/blocking-safeguards-expanded-layer-light.png?w=3840&q=90&fm=webp)

![An expanded monitoring layer shows signals flowing through a monitor and review team to a response, beneath alignment, security, and safeguards.](https://images.ctfassets.net/kftzwdyauwt9/eCxBaUXrPxhxOKcbu2fnl/5fd3964d40e040a43cc714743af8b5ee/monitoring-response-expanded-layer-light.png?w=3840&q=90&fm=webp)

### Model alignment

Alignment is about making AI systems reliably act in ways we intend. Models must interpret what users want while also respecting policies, and broader societal interests. We train our models to align to the principles in the [_Model Spec_ ⁠](<https://openai.com/index/updated-model-spec/>). We assess how well they do this through alignment evaluations, auditing, and review before broader deployment.

### Security and sandboxing

These controls restrict the files, tools, networks, and other resources a model can access or affect. They help contain the consequences of mistakes or misaligned behavior during training and evaluation.

### Blocking safeguards

These are additional safeguards that assess user requests and model actions to block potentially harmful or unauthorized behavior. They include[ _safety classifiers_ ⁠(opens in a new window)](<https://alignment.openai.com/training-activation-classifiers/>) that help prevent cyber abuse or assistance with biological weapons, and[ _Auto-review_ ⁠(opens in a new window)](<https://alignment.openai.com/auto-review/>), which can block potentially unauthorized model actions.

### Monitoring and response

These systems detect concerning behavior, investigate what happened, and intervene when needed. They provide visibility of deployment traffic, and can alert us to new emerging types of risks.

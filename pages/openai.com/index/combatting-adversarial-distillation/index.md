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

November 20, 2026

# Combatting adversarial distillation

How we’re addressing safety risks of distillation and lessons we’ve learned for strengthening safeguards across the industry.

Share

Why distillation is a safety issue

  * Why distillation is a safety issue

  * The importance of protecting exact reasoning traces for cyber safety

  * Defenses that reinforce one another

    * Protecting individual requests and responses

    * Investigating and disrupting coordinated campaigns

  * Measuring progress

    * Resistance to reasoning extraction

    * Campaign detection and enforcement

  * The national security implications of adversarial distillation

  * How others can build on this work




  * Why distillation is a safety issue

  * The importance of protecting exact reasoning traces for cyber safety

  * Defenses that reinforce one another

    * Protecting individual requests and responses

    * Investigating and disrupting coordinated campaigns

  * Measuring progress

    * Resistance to reasoning extraction

    * Campaign detection and enforcement

  * The national security implications of adversarial distillation

  * How others can build on this work




As frontier AI models become more capable, safeguards play an increasingly important role in how they can be used responsibly. Adversarial distillation creates a path for bad actors to reproduce these capabilities without appropriate safeguards. An actor may use a frontier model’s outputs without authorization to train another model with similar capabilities, then deploy it without comparable protections. For instance, an adversary might distill a model’s cyber capabilities and use the resulting model to help carry out cyberattacks that the original model would have refused to assist with or that its safeguards would have blocked.

We’re sharing how OpenAI detects and disrupts adversarial distillation, how we’ve strengthened protections for our models’ protected reasoning, and what we’ve learned that can help strengthen defenses across the industry.

Our approach to adversarial distillation combines adversarial testing, model training, classifiers, and API-level protections with investigations into coordinated attempts to extract model capabilities. These updated safeguards align more closely with those we use for biology and cybersecurity.

We place particular emphasis on preventing attackers from extracting our models’ protected reasoning: the intermediate steps a model generates internally while working toward an answer, known as its chain-of-thought. These traces can contain information the final answer leaves out, making them especially valuable training data for another model.

We’ve strengthened our defenses against protected reasoning extraction in GPT‑6.2 Astra and GPT‑6.2 Sol. In an internal adaptive evaluation using [_strong automated red-teaming_](</index/unlocking-self-improvement-gpt-red/>) , we tested whether attackers could recover protected reasoning the model had generated while answering an earlier prompt. The average attack success rate fell from 54.0% against GPT‑6 Astra with its original safeguards to 0.2% against GPT‑6.2 Astra with its updated safeguards.

## Why distillation is a safety issue

Distillation is a common machine-learning technique in which one model learns from data produced by another. For example, a model can learn from another model’s answers, its reasoning, or its judgments about which answers are better and why. Beyond intellectual property concerns, unauthorized distillation poses serious safety risks. Through adversarial distillation, a second model can learn advanced frontier capabilities without inheriting the safeguards that govern how the original model can use them.

The concern is especially clear in dual-use domains like cybersecurity and biology. A model that helps defenders find vulnerabilities in software could also help an attacker exploit them; a model that assists with biological research could also help someone develop a harmful pathogen. If such capabilities were transferred to a model with weaker safeguards, it may provide assistance that the original model would have refused, or that the original safeguards would have blocked.

## The importance of protecting exact reasoning traces for cyber safety

Our models help users with coding and defensive cybersecurity tasks. A second model trained on many of those benign outputs may learn skills that also apply to offensive cybersecurity tasks. To better understand this, we study how distillation, especially involving reasoning traces, may transfer risky cyber capabilities.

In this setting, the model that produces the training data is called the teacher, and the model that learns from it is called the student. In an internal study on how cyber capabilities transfer, we used the content normally visible to users—final responses, reasoning summaries, and tool interactions—as our baseline for distillation, and tested how much additional cyber capability transfers when the student has access to the teacher’s exact reasoning traces.

We started each training run from the same pretrained student model. We created a supervised fine-tuning dataset consisting primarily of trajectories from Astra-level teacher models working on coding and defensive cybersecurity tasks. Each trajectory includes all of the steps a model takes as it works through a task, including any tool interactions and its final response. We evaluated each student after fine-tuning and again after a lightweight round of reinforcement learning in cybersecurity and coding environments.

After supervised fine-tuning, the student trained on exact reasoning traces generally outperformed the student trained on reasoning summaries. After reinforcement learning, the exact-trace student still scored higher at the largest inference budget tested on both benchmarks shown, while the summary-trained student scored higher at lower budgets.1

ExploitBenchSEC-bench Pro

Our cyber distillation results suggest that protecting reasoning traces can limit cyber capability transfer, even when the underlying task is one allowed under our usage policies. Across many such interactions, exact reasoning traces can teach a student skills that generalize beyond the tasks the teacher originally performed. We will continue studying how much additional capability transfers across different student models and distillation training recipes.

## Defenses that reinforce one another

We defend against adversarial distillation at two complementary levels of our safeguard stack. At the request level, model behavior, classifier checks, and API controls limit reasoning trace extraction. At the campaign level, we look for patterns in request-level and account-level signals that can reveal coordinated extraction attempts. In turn, attacks uncovered in investigations become examples for training and testing our safeguards.

![Two layers of anti-distillation safeguards. Model behavior, classifiers and API protections limit extraction in each interaction. Signals inform investigations across accounts and providers; investigation findings improve protections, supported by automated red-teaming.](https://images.ctfassets.net/kftzwdyauwt9/v3SwlCju2INrQ6LXdq8eB/d0aca54aed53ede3aee7ffc0c40b0646/combatting-adversarial-distillation-diagram-light.png?w=3840&q=90&fm=webp)

_Our defenses against adversarial distillation combine safeguards for individual requests with campaign detection and enforcement. Findings from investigations and automated red-teaming help strengthen those safeguards._

###  Protecting individual requests and responses

#### Defensive training for model behavior

Adversarial training teaches models to recognize reasoning extraction attempts and refuse to disclose protected reasoning, while preserving responses to legitimate requests for explanations and assistance. Adversarial training examples come from successful attacks identified through internal automated red-teaming, investigations, and responsible disclosures of potential security weaknesses from outside researchers or industry partners.

#### Classifier safeguards

We use input classifiers to detect attempts to extract protected reasoning, and output classifiers to detect leaks of protected reasoning in assistant messages and tool-call arguments. These safeguards apply to both streaming and non-streaming responses.

Tool-call coverage is important because a model can expose protected reasoning in a tool’s arguments without including it in its final answer. Output classifiers can block suspected leaks before that content reaches the caller.

#### API-level protections

API-level protections restrict how protected reasoning can be reused across interactions and models. [_Our September disclosure_](</index/disrupting-a-coordinated-model-distillation-campaign/>) described attacks that moved encrypted reasoning from one conversation into another and asked the model to reveal the reasoning in user-readable form. We strengthened protections across user, workspace, organization, and model-family boundaries, including closing a pathway that could expose another user’s encrypted reasoning.

With GPT‑6.2 Astra and GPT‑6.2 Sol, we tie a model’s protected reasoning to the conversation history that produced it. As new messages are added, the model can build on its earlier reasoning. If an earlier message is rewritten, our API [_drops the reasoning that followed it_ ⁠(opens in a new window)](<https://developers.openai.com/api/docs/guides/keep-prefix-unchanged>). We also prevent older model families with weaker safeguards from reading GPT‑6.2 Astra and Sol’s protected reasoning.

### Investigating and disrupting coordinated campaigns

When our systems detect unauthorized adversarial distillation campaigns, which often include coordinated attempts to extract our models’ reasoning, we investigate the accounts responsible. When we identify violations, we enforce against the network of accounts, consistent with our policies and terms of service. Through investigations of each campaign, we generate insights that allow us to upgrade our defenses in order to better detect similar activity. We also share indicators of compromise with other model providers so they can investigate related abuse on their own services.

This work extends beyond our own platform. [_Our consistent-standards policy_](</index/broad-access-through-consistent-standards/>) establishes shared standards for safeguards and coordinated enforcement across providers offering our models. We work closely with partners where appropriate to uphold these standards and strengthen protections across deployments.

Sharing relevant findings across industry and government where appropriate can help disrupt campaigns and enable model developers and providers to better identify and defend against attempts to distill frontier models.

## Measuring progress

### Resistance to reasoning extraction

To measure how well our request-level safeguards work together, we test whether attackers can still extract protected reasoning in a setup that closely mirrors production deployments of our models and safeguards. In static evaluations, we replay a fixed set of previously successful attacks to see which still expose protected reasoning. In adaptive evaluations, automated AI red-teamers adjust their approach based on how the system responds, which can uncover weaknesses the static tests miss.

We also vary what testers can see. Black-box testing gives them the same view an external user would have, while white-box testing gives them additional information about the system to help them develop stronger attacks. In our adaptive black-box evaluation, we tested whether attackers could recover protected reasoning the model had generated while answering an earlier request or the current one. On GPT‑6.2 Astra with its updated safeguards, the average attack success rate was below 1% for each attack type. Both rates were substantially lower than on GPT‑6 Astra with its original safeguards. We’re now applying selected safeguard improvements to GPT‑6 Astra as well.

**Attack type**| **GPT‑6 Astra defender with original safeguards****Adaptive extraction ASR (%)**| **GPT‑6.2 Astra defender with updated safeguards****Adaptive extraction ASR (%)**  
---|---|---  
Extracting protected reasoning from an earlier request| 54.0| 0.2  
Extracting protected reasoning from the current request| 22.9| 0.9  
  
 _Attack success rate (ASR) in adaptive black-box red-teaming against GPT‑6 Astra and GPT‑6.2 Astra, aggregated across six attacker models. Lower ASR is better._

###  Campaign detection and enforcement

We have seen multiple unauthorized adversarial distillation campaigns on our platform this year, and shared initial findings in our September [_report_](</index/disrupting-a-coordinated-model-distillation-campaign/>). Our weekly enforcement actions against these campaigns have ranged in scale from thousands to tens of thousands of accounts, with the rate increasing significantly this past summer.

In order to measure the effectiveness of our efforts, we also track the prevalence of distillation abuse, as well as the time between detection and enforcement. Our objective is to constrain the volume and value of the data distillers are able to obtain, to increase the cost of distillation campaigns, and to shorten the time needed to respond to new attacks. We continue to improve these defenses through adversarial testing and investigations.

## The national security implications of adversarial distillation

Adversarial distillation also poses a national security risk. A foreign actor that reproduces advanced capabilities from a U.S. model can deploy them without the protections its developer put in place. In February, we [_briefed_ ⁠(opens in a new window)](<https://assets.bwbx.io/documents/users/iqjWHBFdfxIU/rRmql_jJcxb4/v0>) Congress on activity indicating that DeepSeek was attempting to distill U.S. frontier models. In September, we [_reported_](</index/disrupting-a-coordinated-model-distillation-campaign/>) disrupting a campaign to extract our models’ protected reasoning and attributed a core part of that activity to individuals associated with Moonshot AI, the developer of Kimi. We plan to share more soon about recent campaigns we’ve disrupted.

We support legislation that would give the U.S. government more tools to identify and sanction foreign actors that illicitly extract capabilities from American AI models. We’ve also told Congress we support the Chip Security Act, the AI OVERWATCH Act, and the MATCH Act. Stronger export controls can limit adversaries’ access to the hardware needed to train frontier models. Distillation defenses make it harder to acquire some of the same capabilities from models already trained. Both efforts help maintain a U.S. lead in frontier AI, giving developers more room to slow a release when they need time to test safeguards.

## How others can build on this work

Supporting the safe proliferation of frontier capabilities is an important goal of our anti-distillation work. Our experience so far suggests several useful steps that other model developers and platforms can take:

  * Protect private reasoning across the full interaction. Check assistant messages and tool-call arguments for leaks, and restrict how encrypted reasoning can be reused across conversations and models.

  * Keep successful extraction attack logs found through red-teaming, production monitoring, or responsible disclosure as regression tests. Where appropriate, and consistent with applicable privacy policies, use those examples to improve model training and classifiers. When evaluating updated defenses, replay the original attacks and test whether an adaptive red-teamer can still find a way through those defenses.

  * Combine request-level mitigations with campaign-level investigation and enforcement.

  * Coordinate safeguard requirements and enforcement with deployment partners, and share expertise with other AI model developers, to ensure a high floor of distillation safeguards across the industry.




We have previously also shared findings through the [_Frontier Model Forum_ ⁠(opens in a new window)](<https://www.frontiermodelforum.org/>) and appropriate government information-sharing channels to help other developers strengthen their defenses while keeping the details attackers could exploit private. We’ll continue working with researchers, developers, and partners to share what we learn about emerging attacks and effective defenses.

As we make frontier AI broadly available, our defenses against adversarial distillation aim to reduce the risk that its capabilities are reproduced without adequate safeguards, supporting our mission to ensure that artificial general intelligence is deployed safely and benefits all of humanity.

## Footnotes

  1. 1

Related work from [_Anthropic_ ⁠(opens in a new window)](<https://www.anthropic.com/news/distillation-defenses>) reported a similar advantage when training on full reasoning transcripts rather than summaries on SWE-bench Verified, a software engineering benchmark. Our result shows this advantage extends to frontier cybersecurity.




## Keep reading

![Hebbia — Cover](https://images.ctfassets.net/kftzwdyauwt9/2j2sOeYR5anL69nJvTbPot/4758d44649f585b33d96cdf14742c0d4/hebbia-smoked-depth-cover.png?w=3840&q=90&fm=webp)

[Hebbia sees improvements in financial research with GPT-6 AstraNov 20, 2026](</business/customer-stories/hebbia/>)

![MedChemBench: Benchmarking AI for medicinal chemistry — Cover](https://images.ctfassets.net/kftzwdyauwt9/4GWchdof3kw2l5OtMIvGt4/56144e08b813d6af76ae93adc2cefc1b/introducing-medchembench-cover.png?w=3840&q=90&fm=webp)

[MedChemBench: Benchmarking AI for medicinal chemistryResearchNov 20, 2026](</index/introducing-medchembench/>)

![Performance Factory — Art card](https://images.ctfassets.net/kftzwdyauwt9/iYpBFP2nteJOaNG1v5Rrp/e0eb5dbefa86d133c3392df5983e45a3/performance-factory-cover.png?w=3840&q=90&fm=webp)

[How OpenAI’s Performance Factory keeps ChatGPT fastEngineeringNov 19, 2026](</index/how-openai-performance-factory-keeps-chatgpt-fast/>)

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

_Cyber benchmark performance after training on exact reasoning traces or reasoning summaries. Each panel compares two runs of the same pretrained student model, as we increase the inference budgets at evaluation time. Blue lines show the user-visible baseline, which included reasoning summaries. Yellow lines show the run trained with exact reasoning traces. Dashed lines show performance after supervised fine-tuning, and solid lines show performance after further reinforcement learning._

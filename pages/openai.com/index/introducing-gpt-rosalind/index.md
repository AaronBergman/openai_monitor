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

April 16, 2026

[Research](</news/research/>)[Release](</research/index/release/>)

# Introducing GPT‑Rosalind for life sciences research

A new purpose-built model to accelerate scientific research and drug discovery.

[Request access](</form/life-sciences-access/>)Learn more

Share

Built for scientific workflows

  * Built for scientific workflows
  * Customers and ecosystem 
  * Performance and evaluation
  * Industry evaluations
  * Connecting to the tools scientists use
  * Trusted access
  * Getting started
  * What’s next



  * Built for scientific workflows
  * Customers and ecosystem 
  * Performance and evaluation
  * Industry evaluations
  * Connecting to the tools scientists use
  * Trusted access
  * Getting started
  * What’s next



Today, we’re introducing GPT‑Rosalind, our frontier reasoning model built to support research across biology, drug discovery, and translational medicine. The life sciences model series is optimized for scientific workflows, combining improved tool use with deeper understanding across chemistry, protein engineering, and genomics.

On average, it takes roughly 10 to 15 years to go from target discovery to regulatory approval for a new drug in the United States. Gains made at the earliest stages of discovery compound downstream in better target selection, stronger biological hypotheses and higher-quality experiments. Progress in the life sciences is constrained not only by the difficulty of the underlying science, but by the complexity of the research workflows themselves. Scientists must work across large volumes of literature, specialized databases, experimental data, and evolving hypotheses in order to generate and evaluate new ideas. These workflows are often time-intensive, fragmented, and difficult to scale.

We believe advanced AI systems can help researchers move through these workflows faster—not just by making existing work more efficient, but by helping scientists explore more possibilities, surface connections that might otherwise be missed, and arrive at better hypotheses sooner. By supporting evidence synthesis, hypothesis generation, experimental planning, and other multi-step research tasks, this model is designed to help researchers accelerate the early stages of discovery. Over time, these systems could help life sciences organizations discover breakthroughs that wouldn’t otherwise be possible, with a much higher rate of success. 

GPT‑Rosalind is now available as a research preview in ChatGPT, Codex, and the API for qualified customers through our trusted access program. We’re also introducing a freely accessible Life Sciences research plugin for Codex, helping scientists connect models to over 50 scientific tools and data sources. We are working with customers like Amgen, Moderna, the Allen Institute, Thermo Fisher Scientific, and others to apply GPT‑Rosalind across workflows that accelerate research and discovery.

The model is named after Rosalind Franklin, whose rigorous research helped reveal the structure of DNA and laid foundations for modern molecular biology. 

From raw data to grounded discovery decisions, see how our purpose-built model accelerates research workflows.

## Built for scientific workflows

The GPT‑Rosalind life sciences model series is built for modern scientific work across published evidence, data, tools, and experiments. In our evaluations, it delivers the best performance on tasks that require reasoning over molecules, proteins, genes, pathways, and disease-relevant biology, and it is more effective at using scientific tools and databases in multi-step workflows such as literature review, sequence-to-function interpretation, experimental planning, and data analysis.

This is the first release in our GPT‑Rosalind life sciences model series, and we will continue to expand the frontiers of the model’s biochemical reasoning capabilities across long-horizon, tool-heavy scientific workflows. OpenAI’s compute infrastructure gives us the ability to continue training, evaluating, and improving increasingly capable domain models against real scientific tasks—helping these systems become more useful as the workflows themselves become more complex.

From evidence-based discovery insights to high-impact experiments, see how our suite of solutions translate into measurable improvements in your research workflows.

## Customers and ecosystem 

We are working with leading pharmaceutical, biotechnology, and research customers, as well as life sciences technology organizations, to apply GPT‑Rosalind across workflows that drive discovery.

AmgenNovo NordiskThermo Fisher Scientific ModernaOracle Health and Life SciencesNVIDIAAllen InstituteBenchlingUCSF School of Pharmacy 

> “The life sciences field demands precision at every step. The questions are highly complex, the data are highly unique, and the stakes are incredibly high. Our unique collaboration with OpenAI enables us to apply their most advanced capabilities and tools in new and innovative ways with the potential to accelerate how we deliver medicines to patients.”

—Sean Bruich, Senior Vice President of Artificial Intelligence and Data, Amgen

## Performance and evaluation

We evaluated GPT‑Rosalind across a range of capabilities fundamental to scientific discovery and industry research. These evaluations measure core reasoning across scientific subdomains, including chemical reaction mechanisms; protein structure, mutation effects, and interactions; and phylogenetic interpretation of DNA sequences. They also assess whether models can support real research workflows by interpreting experimental outputs, identifying expert-relevant patterns, and synthesizing external information to design follow-up experiments. Finally, they test whether models can select and use the right computational tools, databases, and domain-specific capabilities to augment their reasoning. Taken together, these evaluations show progress across the end-to-end process of scientific research and suggest a stronger ability to help researchers work through challenging discovery tasks.

Organic chemistryProtein understandingGenomicsExperimental design and analysisTool usage

Prompt

I am planning a base-promoted SNAr coupling of 1-(pyridin-3-yl)ethanol with 1-fluoro-2-nitrobenzene with the goal of synthesizing 1-(pyridin-3-yl)ethyl 2-nitrophenyl ether. I found several patents that describe room-temperature O-arylation of alcohols in DMF/Cs2CO3, but the reaction is taking longer than I would like. How can I improve this reaction? Help me find any relevant literature or patents as well.

## Industry evaluations

We evaluated GPT‑Rosalind on a series of public benchmarks. On BixBench, a benchmark designed around real-world bioinformatics and data analysis, GPT‑Rosalind achieved leading performance among models with published scores.

On LABBench2, a benchmark measuring performance on a range of research tasks such as literature retrieval, database access, sequence manipulation and protocol design, GPT‑Rosalind outperforms GPT‑5.4 on 6 out of 11 tasks. The most notable improvement comes from CloningQA, which requires end-to-end design of DNA and enzyme reagents for molecular cloning protocols.

We also partnered with Dyno Therapeutics, a company pioneering AI-designed gene therapies, to evaluate the model on an RNA sequence-to-function prediction and generation task using unpublished, uncontaminated sequences. Performance was compared against 57 historical scores from human experts in the AI-bio field. When evaluated directly in the Codex app, best-of-ten model submissions ranked above the 95th percentile of human experts on the prediction task and around the 84th percentile of human experts on the sequence generation task.

These evaluations provide a meaningful signal of performance on the kinds of workflows scientists rely on every day to generate evidence, analyze complex data, and move toward defensible biological conclusions.

##   
Connecting to the tools scientists use

Scientists can use our new [_Life Sciences research plugin_ ⁠(opens in a new window)](<https://github.com/openai/plugins/tree/main/plugins/life-science-research>) for Codex, available today in GitHub. This package includes a broad set of modular skills for most common research workflows, designed to help users work across human genetics, functional genomics, protein structure, biochemistry, clinical evidence, and public study discovery.

![Life science plugin demo static image](https://images.ctfassets.net/kftzwdyauwt9/6gimOsHAXF9xzcpwO1MK40/ed8b97d27b29deb206dbc518825f84d1/OAI_Life_Sciences_Research_Plugin.png?w=3840&q=90&fm=webp)

These skills act as an orchestration layer that helps scientists work through broad, ambiguous, and multi-step questions more effectively. They provide access to more than 50 public multi-omics databases, literature sources, and biology tools, and offer a flexible starting point for common repeatable workflows such as protein structure lookup, sequence search, literature review, and public dataset discovery.

Eligible Enterprise users can leverage this plugin in research workflows with GPT‑Rosalind for deeper biological reasoning, while all users can use the plugin package with our mainline models. 

## Trusted access

We want to make these capabilities available to the scientists and research organizations best positioned to advance human health, while maintaining strong safeguards against biological misuse. The Life Sciences model is launching through a trusted-access deployment structure for qualified Enterprise customers in the U.S. to start, with controls around eligibility, access management, and organizational governance. At the same time, we are making a set of connectors and the Life Sciences Research Plugin available more broadly, so researchers can use our mainline models more effectively for life sciences research tasks. 

The Life Sciences model was developed with heightened enterprise-grade security controls and strengthened access management, enabling professional scientific use in governed research environments. We evaluate access based on three core principles: beneficial use, strong governance and safety oversight, and controlled access with enterprise-grade security. In practice, this means participating organizations must be conducting legitimate scientific research with clear public benefit; maintain appropriate governance, compliance, and misuse-prevention controls; and restrict access to approved users within secure, well-managed environments. Organizations must also agree to the life sciences research preview terms and comply with OpenAI’s usage policies, and we may request additional information as part of onboarding or continued participation. 

## Getting started

Organizations can [_request access_ ⁠](<https://openai.com/form/life-sciences-access>) through our qualification and safety review process.

During the research preview, use of this model will not consume existing credits or tokens—subject to abuse guardrails. We’ll share more details on pricing and availability as the program expands.

The Life Sciences model is built to help scientific organizations do higher-quality work, faster, in environments that require both technical capability and operational control. Our dedicated Life Sciences team—as well as advisory partners including McKinsey & Company, Boston Consulting Group (BCG), and Bain & Company—help organizations identify high-impact use cases, integrate the model into enterprise environments, and drive measurable outcomes. If you’d like to explore ways OpenAI Life Sciences can support your work, you can [_contact our Life Sciences team_ ⁠](<https://openai.com/contact-sales/>).  


## What’s next

This is the first release in our Life Sciences model series, and we view it as the beginning of a long-term commitment to building AI that can accelerate scientific discovery in areas that matter deeply to society, from human health to broader biological research. We will continue improving the model’s biological reasoning, expanding support for tool-heavy and long-horizon research workflows, and working closely with leading scientific institutions to evaluate real-world impact. That includes ongoing partnerships with national laboratories such as Los Alamos National Laboratory, where we are exploring AI-guided protein and catalyst design, including the ability of AI systems to modify biological structures while preserving or improving key functional properties. 

Over time, we expect these systems to become increasingly capable partners in discovery—helping scientists move faster from question to evidence, from evidence to insight, and from insight to new treatments for patients.

##   
  


## Keep reading

[View all](</news/>)

![ARC-AGI-3 art-card 1x1](https://images.ctfassets.net/kftzwdyauwt9/71xyJRWnTkM6EW1JKDUc59/91d2690ff9e7abaa975b4a5f64089056/ARC-AGI-3_art-card_1x1.png?w=3840&q=90&fm=webp)

[How enabling two settings tripled our scores on the ARC-AGI-3 benchmarkResearchJul 29, 2026](</index/how-two-settings-tripled-our-arc-agi-3-scores/>)

![oai Science Academic Research Academic Research 1x1](https://images.ctfassets.net/kftzwdyauwt9/59kTmFmujYzNh0VgSvCgwe/e9334dd9944b5309f8ca2d44fdc71b6f/academic-research-card.png?w=3840&q=90&fm=webp)

[Accelerating scientific discovery with ChatGPT for Academic ResearchersCompanyJul 29, 2026](</index/chatgpt-for-academic-researchers/>)

![Scientific computing agentic AI card image \(1x1\)](https://images.ctfassets.net/kftzwdyauwt9/5opqp3rNWM7eax6GUc6MAl/1c710a4aba8c5c1e0b7d1c1c7c8b32db/1x1__1_.png?w=3840&q=90&fm=webp)

[Scientific computing in the age of agentic AIPublicationJul 28, 2026](</index/scientific-computing-agentic-ai/>)

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

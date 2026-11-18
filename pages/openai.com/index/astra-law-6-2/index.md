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

November 17, 2026

[Company](</news/company-announcements/>)

# Astra for Law leads in legal intelligence

Our latest model configuration earned leading marks on multiple benchmarks. Every ChatGPT Enterprise customer can now request access.

Share

First in the Harvey LAB-AA

  * First in the Harvey LAB-AA

  * A top performer on the Vals AI Legal Research Bench

  * How lawyers are using Astra for Law

  * Bring Astra for Law to your practice




  * First in the Harvey LAB-AA

  * A top performer on the Vals AI Legal Research Bench

  * How lawyers are using Astra for Law

  * Bring Astra for Law to your practice




Today, we're releasing an updated Astra for Law that is state-of-the-art on Harvey LAB-AA and a top performer on Vals AI’s Legal Research Bench. We are also enabling all ChatGPT Enterprise customers to request access through the Trusted Access Program, including through the API.

Astra for Law is a model configuration of [_GPT‑6.2 Astra_ ⁠](<https://openai.com/index/introducing-gpt-6-2-astra-sol>), our latest, most powerful frontier model. It pairs GPT‑6.2 Astra with an expanded legal search index and instructions for researching a question, weighing the authorities, and writing the answer. Today’s configuration earned full credit on the LAB-AA tests nearly 40% more often than did the runner-up, GPT‑6.2 Astra.

Since we [_introduced Astra for Law in September_ ⁠](<https://openai.com/index/astra-for-law/>) to a small group of firms, including [_Cooley_ ⁠](<https://openai.com/index/cooley-gopublic/>), [_Ropes & Gray_⁠](<https://openai.com/index/ropes-gray-ai-diligence/>), and [_Sullivan & Cromwell_⁠](<https://openai.com/index/sullivan-cromwell/>), our research team has made rapid innovations to improve its legal reasoning and expand its legal search index by over a third. On [_Vals AI’s Legal Research Bench_ ⁠(opens in a new window)](<https://www.vals.ai/benchmarks/legal_research>), the share of research answers that passed every check rose from about 46% to 53.8% in less than two months.

As the world grows more complex, lawyers occupy an increasingly important role. They shape nearly every system we rely on: they negotiate the agreements that move commerce, defend people’s rights in courts, and draft the laws we all live by. That’s why we’ve made law a research priority at OpenAI: to put the best intelligence in the hands of the best lawyers.

## First in the Harvey LAB-AA

> “Astra for Law 6.2 is a material improvement over prior Astra models across our benchmarks. It writes more comprehensive and better reasoned briefs that are preferred to those of GPT‑6 Astra nearly 90% of the time by our pairwise judges. Notably, this improvement in depth comes without regression to prior models’ accuracy—we continue to see Astra class models have some of the lowest hallucinations rates on LAB.”

—Julio Pereyra, Head of Legal Research, Harvey

Harvey’s Legal Agent Benchmark (LAB) tests whether a model can take a legal assignment from start to finish. [_LAB-AA_ ⁠(opens in a new window)](<https://artificialanalysis.ai/evaluations/harvey-lab-aa>) is Artificial Analysis’s version of that test. It tests the models on 120 assignments developed by Harvey across 24 areas of law – everything from drafting deposition outlines to reviewing commercial leases to strategizing ownership changes in acquisitions. To earn full credit, an answer must meet every requirement of an assignment without hallucinating, i.e., making a material claim that is not supported by the source documents.

Astra for Law ranked first, earning full credit on 20.8% of assignments, ahead of GPT‑6.2 Astra at 15.0% and Muse Wonder Full at 13.1%.

![Bar chart comparing the share of LAB-AA assignments that earned full credit.](https://images.ctfassets.net/kftzwdyauwt9/7elvsIiYJS1aSNbqPreAcY/55c27a90181e7ac9e5acecbda4057cd0/astra-for-law-labaa-ranking.png?w=3840&q=90&fm=webp)

Astra for Law ranked first at 20.8%, earning full credit about **59% more often than Muse Wonder Full** , the highest-scoring non-OpenAI model.

Astra for Law also earned that top score with **54% less output per assignment** than the highest-scoring non-OpenAI model in the evaluation, averaging about 64,000 output tokens per assignment, compared with 139,000 for Muse Wonder Full. For legal teams paying by usage, this can mean the difference between staying within budget and blowing through it.

![Scatterplot of average output tokens on a logarithmic scale against LAB-AA full-credit rates.](https://images.ctfassets.net/kftzwdyauwt9/6Nh3rzJD9qBELDLc4elOlF/56576a8bdc979857681eb7c834bb7a83/astra-for-law-labaa-output-tokens.png?w=3840&q=90&fm=webp)

Each dot is a model configuration. Higher means more assignments earned full credit; farther left means fewer output tokens, which include the text a model generates as it reasons and writes. Astra for Law averaged about 64,000 output tokens per assignment and earned full credit on 20.8%, compared with 139,000 and 13.1% for Muse Wonder Full. No configuration shown matched Astra for Law’s score using fewer output tokens.

### 95% fewer hallucinations per assignment than Claude Opus 5.5

Hallucinations are unacceptable in legal work. A single invented citation can cost a lawyer a client’s trust, credibility in court, and a reputation built over years. That’s why reducing hallucinations has been a priority for Astra for Law. In Artificial Analysis’s latest LAB-AA comparison, Astra for Law tied (with GPT‑6) for the **lowest rate of material hallucinations:** 0.03 per assignment, compared with 0.59 for Claude Opus 5.5 (the next lowest non-OpenAI model). Notably, Astra for Law's performance on this eval included **zero material hallucinations for tasks that met the all-pass criteria**.

![Grouped bars comparing material and minor hallucinations per LAB-AA assignment.](https://images.ctfassets.net/kftzwdyauwt9/7lXN8zH60iSckZoa3uUJ1g/458f711e3dd648cb213c56fdd9216956/astra-for-law-labaa-hallucinations.png?w=3840&q=90&fm=webp)

Astra for Law averaged 0.03 material and 0.06 minor hallucinations per assignment. Claude Opus 5.5 averaged 0.59 material and 0.51 minor hallucinations per assignment, about 20 times as many material hallucinations and 8.5 times as many minor ones.

Across the same 120 assignments, Artificial Analysis counted hallucinated claims that could mislead a reader on a substantive point. Astra for Law averaged 0.03 such errors per assignment, tied for the lowest rate in the comparison and roughly half the rate for regular GPT‑6.2 Astra (0.06).

Every OpenAI configuration tested had fewer hallucinations than Claude Opus 5.5, the best non-OpenAI result on this measure. Opus 5.5 averaged 0.59 material hallucinations per assignment, about 20 times as many as Astra for Law.

## A top performer on the Vals AI Legal Research Bench

We've made law a research priority at OpenAI, dedicating a team of researchers to accelerate innovation for frontier legal intelligence. One early measure of their progress comes from [_Vals AI’s Legal Research Bench_ ⁠(opens in a new window)](<https://www.vals.ai/benchmarks/legal_research>), where practicing lawyers set questions about U.S. federal and state law. An answer has to cover every required point and pass the source checks. In September, Astra for Law earned full credit on about 46% of questions. In Vals AI’s November 16 evaluation, it earned full credit on 112 of 208 questions (53.8%), **a gain of about eight percentage points in under two months**. Across all questions, it earned **90.9% of the available points** , including partial credit. 

![Bar chart showing the share of legal research questions on which Astra for Law earned full credit rising from about 46% in September to 53.8% in November.](https://images.ctfassets.net/kftzwdyauwt9/2RURPevom7fTBKWOiMyUuS/77e388efb49ae2400998d71d411e56cc/astra-law-vals-research-progress.png?w=3840&q=90&fm=webp)

In less than two months, the share of legal research questions on which Astra for Law earned full credit rose from about 46% to 53.8%, a gain of about eight percentage points.

![Scatter plot comparing systems on the Vals AI Legal Research Bench, with Astra for Law in green among the highest-scoring systems.](https://images.ctfassets.net/kftzwdyauwt9/4vax0s3HoU2udcjEtl7l46/6dd776a1833b2f6cacac42f8fcecc485/astra-law-vals-system-comparison.png?w=3840&q=90&fm=webp)

Astra for Law (green) sits in the small cluster of top performers on Vals AI’s Legal Research Bench.

Building Astra for Law as a model configuration lets us stay on the bleeding edge of the frontier, in this case[ _GPT‑6.2 Astra_ ⁠](<https://openai.com/index/introducing-gpt-6-2-astra-sol>). On top of this foundation, we iteratively refine Astra for Law’s specific settings and instructions in response to practitioner feedback, teaching it how to reason and write like a seasoned lawyer. We also continuously hone its tools, such as the legal search index. Since September, we’ve grown the index by 34%, adding over 80 million new URLs, including across international jurisdictions such as the **UK, Australia, and Canada**. Today, the updated index spans over 310 million URLs and covers [_more than 99.9% of published U.S. precedential case law_ ⁠(opens in a new window)](<https://wiki.free.law/c/courtlistener/help/data-coverage/case-law>).

The chart below shows how the model configuration takes advantage of both the speed of frontier innovation and builds on top of that the specific requirements that make it powerful for lawyers. On Harvey’s own Legal Agent Benchmark, GPT‑6 Astra met every requirement on **4.6%** of assignments. GPT‑6.2 Astra **tripled performance,** completing **14.6%** under the same conditions. With the legal configuration, that rose to **16.2%** , completing 11% more questions than GPT‑6.2 Astra.

![Share of Harvey Legal Agent Benchmark assignments meeting every requirement: GPT-6 Astra, 4.6%; GPT-6.2 Astra, 14.6%; Astra for Law 6.2, 16.2%.](https://images.ctfassets.net/kftzwdyauwt9/38EGkb4OZvdEeyQ0u6J8hb/949faf5ace6376bf617549e8395e35bc/astra-for-law-harvey-lab-all-pass.png?w=3840&q=90&fm=webp)

This chart shows both the rate of development in frontier intelligence, as well as the impact of the model configuration. The full-credit rate more than tripled from GPT‑6 Astra to GPT‑6.2 Astra, then rose another 11% with the legal configuration. This test comes from Harvey’s own LAB (separate from the previously discussed LAB-AA).

## How lawyers are using Astra for Law

> “We were grateful to preview early versions of Astra for Law, which were built with legal use-cases in mind. Across both litigation and transactional matters, the models demonstrated impressive research depth and sensitivity to authority. Even at this early stage, they felt like a significant step toward legal-focused AI that is carefully grounded in research that is both current and comprehensive.”

—John Savva, Partner at Sullivan & Cromwell

The most interesting possibilities for Astra for Law are being shaped by the lawyers who are using it for their day-to-day work. Across law firm customers and OpenAI’s own legal team, early users are building references around their practice, inviting tougher challenges to their arguments, and finding new ways to respond to changing legislation. 

For example, early users at OpenAI are using Astra for Law to:

  * **Give your argument its strongest opponent.** A common use for Astra for Law is as a sparring partner. A competition lawyer gives it a reading of a statute and asks it to argue the other side, drawing on legislative history, court decisions, and versions of the law in other languages. 

  * **Find the line between a recommendation and a requirement.** A policy lawyer looking at a proposed oversight bill wanted to know how much power an independent reviewer would have. If the reviewer called for a fix, would the developer have to make it? For questions like these, the lawyer puts a plain-English account of each obligation beside the bill’s exact words, so she can make fast judgment calls about which reading the text supports.

  * **Start the first call with outside counsel on the hardest question.** When the business is considering entering an unfamiliar industry, a product lawyer uses Astra for Law to map which rules would apply to the proposed activity. Instead of spending the first call asking for high-level advice, the lawyer can bring outside counsel what’s actually at issue.

  * **Turn a stack of policies into a workflow.** A legal program manager used Astra for Law to turn regulatory procedures and company policy into a workflow for colleagues handling incoming cases, enabling them to automate when to ask for more information, when to close the case, and when to escalate it to a lawyer.

  * **Build the guide you wish came with the statute.** A competition lawyer paired Astra for Law with ChatGPT’s site-building tools to annotate legislation the team uses regularly. A colleague reading a provision can hover over a term for its definition, follow a link to the materials that explain it, and see what the team advised the last time that provision came up.




## Bring Astra for Law to your practice

Starting today, every ChatGPT Enterprise customer can request Astra for Law through the Trusted Access Program in the admin console. If your team already has access, select `gpt-6.2-astra-law`**** in ChatGPT. Customers can also request API access to build Astra for Law into their own tools [_using this form_ ⁠](<https://openai.com/business/contact-sales-legal/>). 

The legal profession is at an inflection point. As technology changes what businesses can do and the world becomes increasingly complex and interconnected, lawyers have an unprecedented opportunity to shape how we make sense of the moment, not just for the businesses they advise but for all of us who live by the rules they help write.

We believe the best lawyers, equipped with the best intelligence, can meet that moment. We’re only at the beginning. We can’t wait to see where you take the profession.

  * [ChatGPT](</news/?tags=chatgpt>)
  * [2026](</news/?tags=2026>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

![LVMH Media Division partnership with OpenAI — cover](https://images.ctfassets.net/kftzwdyauwt9/2LOjySDM8G0bdrIW0XNMq3/5b50996dca0e8f5ddde8f8e43c6d5492/lvmh-s-media-division-announces-partnership-with-openai-cover.png?w=3840&q=90&fm=webp)

[LVMH’s Media Division announces partnership with OpenAICompanyNov 16, 2026](</index/lvmh-media-division-partnership/>)

![ChatGPT for Veterans > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/2xsjEAOhgideekNE2Xxxqk/fe4d5c8aecf7d6498d1e8026a5a56599/oai_GA_Stories_1.1.png?w=3840&q=90&fm=webp)

[ChatGPT Plus for veterans and servicemembersCompanyNov 11, 2026](</index/chatgpt-plus-for-veterans/>)

![Helping caregivers use AI in everyday life — Cover](https://images.ctfassets.net/kftzwdyauwt9/2wwJf21F4rMJ6FffmYbEa5/0e9a21de969e280e77ae8ae66eaa03f6/helping-caregivers-use-ai-in-everyday-life-cover.png?w=3840&q=90&fm=webp)

[Helping caregivers use AI in everyday lifeCompanyNov 10, 2026](</index/helping-caregivers-use-ai-in-everyday-life/>)

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

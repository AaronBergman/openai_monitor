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

  * Stronger performance where precision matters
  * Looking ahead



December 11, 2025

[Publication](</research/index/publication/>)[Product](</news/product-releases/>)[Company](</news/company-announcements/>)

# Advancing science and math with GPT‑5.2

GPT‑5.2 is our strongest model yet for math and science work.

[Read the paper(opens in a new window)](<https://cdn.openai.com/pdf/a3f3f76c-98bd-47a5-888f-c52c932a8942/colt-monotonicity-problem.pdf>)

Loading…

Share

One of our hopes for strong AI is that it will accelerate scientific research for the benefit of everyone, helping researchers explore more ideas, test them faster, and turn discoveries into impact. 

Over the past year, we’ve been working closely with scientists across math, physics, biology, and computer science to understand where AI can help—and where it still falls short. Last month, we [_published a paper_ ⁠](<https://openai.com/index/accelerating-science-gpt-5/>) that compiles early case studies across math, physics, biology, computer science, astronomy, and materials science in which GPT‑5 helped researchers showing how GPT‑5 has already begun contributing to real scientific work. With [GPT‑5.2](</index/introducing-gpt-5-2/>), we’re starting to see those gains become more consistent and more reliable.

## Stronger performance where precision matters

GPT‑5.2 Pro and GPT‑5.2 Thinking are our strongest models yet for scientific and mathematical work.

Strong mathematical reasoning is a foundation for reliability in scientific and technical work. It enables models to follow multi-step logic, keep quantities consistent, and avoid subtle errors that can compound in real analyses—from simulations and statistics to forecasting and modeling. Improvements on benchmarks like FrontierMath reflect not a narrow skill, but stronger general reasoning and abstraction, capabilities that carry directly into scientific workflows such as coding, data analysis, and experimental design.

These capabilities are also closely tied to progress toward general intelligence. A system that can reliably reason through abstraction, maintain consistency across long chains of thought, and generalize across domains is exhibiting traits that are foundational to AGI—not task-specific tricks, but broad, transferable reasoning skills that matter across science, engineering, and real-world decision-making.

We believe GPT‑5.2 Pro and GPT‑5.2 Thinking are the world’s best models for assisting and accelerating scientists. On **GPQA Diamond,** a graduate-level Google-proof Q&A benchmark, GPT‑5.2 Pro achieves 93.2%, followed closely by GPT‑5.2 Thinking at 92.4%.

In [GPQA Diamond⁠(opens in a new window)](<https://arxiv.org/abs/2311.12022>), models answer multiple choice questions about physics, chemistry, and biology. No tools were enabled and reasoning effort was set to maximum.

On **FrontierMath (Tier 1–3),** an evaluation of expert-level mathematics, GPT‑5.2 Thinking set a new state of the art, solving 40.3% of problems.

In [FrontierMath⁠(opens in a new window)](<https://epoch.ai/frontiermath>), models solve expert-level mathematics problems. A Python tool was enabled and reasoning effort was set to maximum.

## Case study

GPT‑5.2 is not only strong at graduate-level science problems. We now regularly see our frontier models contributing solutions to previously unsolved—and increasingly subtle—questions in mathematics and the sciences.

In this case study, we describe how GPT‑5.2 Pro helped resolve an open research problem in statistical learning theory, documented in a new paper, [**__On Learning-Curve Monotonicity for Maximum Likelihood Estimators__** ⁠(opens in a new window)](<https://cdn.openai.com/pdf/a3f3f76c-98bd-47a5-888f-c52c932a8942/colt-monotonicity-problem.pdf>)**_._**

The question (“If you collect more data, do your results reliably get better?”) shows up any time you fit a model from data. You can draw a learning curve that tracks average error as you add more examples. In the best case, the curve is monotone. More data means less error, every step of the way. That is the behavior people hope for, and often assume.

But over the last few years, researchers have learned that this intuition can fail. A line of work kicked off by an open problem posed at the Conference on Learning Theory (COLT) in 2019 by Viering, Mey, and Loog showed that the answer is often no. Even very simple, well-behaved toy setups can have non-monotonic learning curves, where adding data increases expected error. That surprise triggered a wave of follow-up papers. They expanded the list of settings where these reversals happen and proposed increasingly elaborate methods designed to restore monotone behavior.

Still, one of the most basic cases remained unresolved. What happens in the cleanest textbook situation, where the statistical model is actually correct and the data follow the familiar bell curve pattern, with a known mean but unknown standard deviation? Researchers already knew that small changes to this setup could break monotonic behavior. But the answer remained unknown in this core case.

Our new paper demonstrates that in this clean setting, intuition prevails: learning is predictably improved by more data, rather than behaving in surprising or unstable ways. What makes this paper unusual is how the proof was obtained. The authors did not work out a strategy and then ask the model to fill in steps. They did not provide intermediate arguments or a proof outline. Instead, they asked GPT‑5.2 Pro to solve the open problem directly, and then carefully verified the proof, including review and validation by external subject-matter experts.

The authors then asked simple follow-up questions to see how far the idea could go. GPT‑5.2 Pro extended the result beyond the original problem to higher dimensional settings and other common statistical models. Throughout, the human role stayed focused on verification and clear writing, rather than supplying mathematical scaffolding.

## Looking ahead

This result suggests a useful direction for how AI systems can support scientific research, particularly in domains with axiomatic theoretical foundations such as mathematics and theoretical computer science. In settings like these, frontier models can help explore proofs, test hypotheses, and identify connections that might otherwise take substantial human effort to uncover.

At the same time, these systems are not independent researchers. Expert judgment, verification, and domain understanding remain essential. Even highly capable models can make mistakes or rely on unstated assumptions. But they can also produce detailed, structured arguments that merit careful human study and refinement. Making reliable progress with AI therefore depends on workflows that keep validation, transparency, and collaboration firmly in the loop.

Viewed as a case study, this result illustrates an emerging mode of research practice. Models like GPT‑5.2 can serve as tools for supporting mathematical reasoning and accelerating early-stage exploration, while responsibility for correctness, interpretation, and context remains with human researchers. Used carefully, such systems may help streamline significant aspects of theoretical work without displacing the central role of human judgment in scientific inquiry.

  * [GPT](</research/index/?tags=gpt>)
  * [Reasonings & Policy](</research/index/?tags=reasoning-policy>)
  * [2025](</research/index/?tags=2025>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

![Futures 1 1](https://images.ctfassets.net/kftzwdyauwt9/7l4mPpfnMDZNfjmksyuILI/5e280d8d490f625b3fc414d9824e96ac/Futures_1_1.png?w=3840&q=90&fm=webp)

[Introducing ChatGPT Futures: Class of 2026CompanyMay 6, 2026](</index/introducing-chatgpt-futures-class-of-2026/>)

![What frontier enterprises do differently > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/4kKQaeWGl9atcyE51ri1ZW/3aa677511fa40bc0a4b089ef6cd9698f/Frame.png?w=3840&q=90&fm=webp)

[How frontier enterprises are building an AI advantageCompanyMay 6, 2026](</index/introducing-b2b-signals/>)

![20250826](https://images.ctfassets.net/kftzwdyauwt9/2H347RfdThVOeTfSBchxDx/8a053f4cfa92faeed7141265dd02e7dd/20250826.jpg?w=3840&q=90&fm=webp)

[GPT-5.5 Instant: smarter, clearer, and more personalizedProductMay 5, 2026](</index/gpt-5-5-instant/>)

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

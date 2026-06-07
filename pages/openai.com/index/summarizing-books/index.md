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

Our approach: combining reinforcement learning from human feedback and recursive task decomposition

  * Our approach: combining reinforcement learning from human feedback and recursive task decomposition
  * Why we are working on this



September 23, 2021

[Publication](</research/index/publication/>)

# Summarizing books with human feedback

Scaling human oversight of AI systems for tasks that are difficult to evaluate.

![Summarizing Books](https://images.ctfassets.net/kftzwdyauwt9/5a1f46b8-7e89-42f1-cb71b084ba93/524e90bcc1dfde4121a5ffb83c679bc9/summarizing-books.jpg?w=3840&q=90&fm=webp)

Loading…

Share

To safely deploy powerful, general-purpose artificial intelligence in the future, we need to ensure that machine learning models act in accordance with human intentions. This challenge has become known as the  _alignment problem_.

A scalable solution to the alignment problem needs to work on tasks where model outputs are difficult or time-consuming for humans to evaluate. To test scalable alignment techniques, we trained a model to summarize entire books, as shown in the following samples.A Our model works by first summarizing small sections of a book, then summarizing those summaries into a higher-level summary, and so on.

Loading...

Our best model is fine-tuned from GPT‑3 and generates sensible summaries of entire books, sometimes even matching the average quality of human-written summaries: it achieves a 6/7 rating (similar to the average human-written summary) from humans who have read the book 5% of the time and a 5/7 rating 15% of the time. Our model also achieves state-of-the-art results on the [BookSum dataset⁠(opens in a new window)](<https://arxiv.org/abs/2105.08209>) for book-length summarization. A zero-shot question-answering model can use our model’s summaries to obtain competitive results on the [NarrativeQA dataset⁠(opens in a new window)](<https://arxiv.org/abs/1712.07040>) for book-length question answering.B

## Our approach: combining reinforcement learning from human feedback and recursive task decomposition

Consider the task of summarizing a piece of text. Large [pretrained models aren’t very good at summarization⁠](</index/learning-to-summarize-with-human-feedback/>). In the past we found that training a model with [reinforcement learning from human feedback⁠](</index/deep-reinforcement-learning-from-human-preferences/>) helped align model summaries with human preferences on short posts and articles. But judging summaries of entire books takes a lot of effort to do directly since a human would need to read the entire book, which takes many hours.

To address this problem, we additionally make use of  _recursive task decomposition_ : we procedurally break up a difficult task into easier ones. In this case we break up summarizing a long piece of text into summarizing several shorter pieces. Compared to an end-to-end training procedure, recursive task decomposition has the following advantages:

  1. Decomposition allows humans to evaluate model summaries more quickly by using summaries of smaller parts of the book rather than reading the source text.
  2. It is easier to trace the summary-writing process. For example, you can trace to find where in the original text certain events from the summary happen. See for yourself on [our summary explorer⁠(opens in a new window)](<https://openaipublic.blob.core.windows.net/recursive-book-summ/website/index.html>)!
  3. Our method can be used to summarize books of unbounded length, unrestricted by the context length of the transformer models we use.



## Why we are working on this

This work is part of our [ongoing⁠](</index/amplifying-ai-training/>) [research⁠](</index/debate/>) into aligning advanced AI systems, which is key to [our mission.⁠](</about/>) As we train our models to do increasingly complex tasks, making informed evaluations of the models’ outputs will become increasingly difficult for humans. This makes it harder to detect subtle problems in model outputs that could lead to negative consequences when these models are deployed. Therefore we want our ability to evaluate our models to increase as their capabilities increase.

Our current approach to this problem is to [empower humans to evaluate machine learning model outputs using assistance from other models⁠(opens in a new window)](<https://deepmindsafetyresearch.medium.com/scalable-agent-alignment-via-reward-modeling-bf4ab06dfd84>). In this case, to evaluate book summaries we empower humans with individual chapter summaries written by our model, which saves them time when evaluating these summaries relative to reading the source text. Our progress on book summarization is the first large-scale empirical work on scaling alignment techniques.

Going forward, we are researching better ways to assist humans in evaluating model behavior, with the goal of finding techniques that scale to aligning artificial general intelligence.

_We’re always looking for more talented people to join us; so if this work interests you, please_ [ _apply to join our team_ ⁠](</careers/>) _!_

  * [GPT](</research/index/?tags=gpt>)
  * [Reasonings & Policy](</research/index/?tags=reasoning-policy>)
  * [Ethics & Safety](</research/index/?tags=ethics-safety>)
  * [Learning Paradigms](</research/index/?tags=learning-paradigms>)
  * [Language](</research/index/?tags=language>)



## Footnotes

  1. A

These samples were selected from works in the [public domain⁠(opens in a new window)](<https://www.gutenberg.org/policy/license.html>), and are part of GPT-3′s pretraining data. To control for this effect, and purely for research purposes, our [paper⁠(opens in a new window)](<https://arxiv.org/abs/2109.10862>) evaluates summaries of books the model has never seen before. 

  2. B

We’ve amended our original claim about results on NarrativeQA after being made aware of prior work with better results than ours. 




## Authors

Jeffrey Wu, Ryan Lowe, Jan Leike

## Acknowledgments

We’d like to acknowledge our paper co-authors: Long Ouyang, Daniel Ziegler, Nisan Stiennon, and Paul Christiano.

Thanks to the following for feedback on this release: Steve Dowling, Hannah Wong, Miles Brundage, Gretchen Krueger, Ilya Sutskever, and Sam Altman.

## Acknowledgments

Design: Justin Jay Wang

Book Cover Artwork: [DALL·E⁠](</index/dall-e/>)

## Related articles

[View all](</news/>)

![Disrupting malicious > media](https://images.ctfassets.net/kftzwdyauwt9/5080983d-9c4d-4479-17e421d7380a/0b42f77c2478bc5bc7bde3fddfc68462/45.png?w=3840&q=90&fm=webp)

[Disrupting malicious uses of AI by state-affiliated threat actorsSecurityFeb 14, 2024](</index/disrupting-malicious-uses-of-ai-by-state-affiliated-threat-actors/>)

![](https://images.ctfassets.net/kftzwdyauwt9/ec66425e-99ca-4314-d04b087f8727/de7341b6a5281c2a220b93a737ce19b0/building-an-early-warning-system-for-llm-aided-biological-threat-creation.jpg?w=3840&q=90&fm=webp)

[Building an early warning system for LLM-aided biological threat creationPublicationJan 31, 2024](</index/building-an-early-warning-system-for-llm-aided-biological-threat-creation/>)

![Democratic Inputs To AI Grant Program Update](https://images.ctfassets.net/kftzwdyauwt9/f50ce1d2-4f61-4ed2-e560c624d631/6f4dd4542898a35d0a91b137f85c9834/Democratic_inputs_to_AI_grant_program_lessons_learned_and_implementation_plans.jpg?w=3840&q=90&fm=webp)

[Democratic inputs to AI grant program: lessons learned and implementation plansSafetyJan 16, 2024](</index/democratic-inputs-to-ai-grant-program-update/>)

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
  * [Release Notes](</products/release-notes/>)



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

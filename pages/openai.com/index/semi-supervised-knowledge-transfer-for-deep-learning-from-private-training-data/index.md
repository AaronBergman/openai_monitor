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

October 18, 2016

[Publication](</research/index/publication/>)

# Semi-supervised knowledge transfer for deep learning from private training data

[Read paper(opens in a new window)](<https://arxiv.org/abs/1610.05755>)

![Semi Supervised Knowledge Transfer For Deep Learning From Private Training Data](https://images.ctfassets.net/kftzwdyauwt9/d11b8795-7bf4-41ff-dc33663470c3/fae7f11e7e5d05fbdf67c2d8ae381948/semi-supervised-knowledge-transfer-for-deep-learning-from-private-training-data.png?w=3840&q=90&fm=webp)

Loading…

Share

## Abstract

Some machine learning applications involve training data that is sensitive, such as the medical histories of patients in a clinical trial. A model may inadvertently and implicitly store some of its training data; careful analysis of the model may therefore reveal sensitive information.

To address this problem, we demonstrate a generally applicable approach to providing strong privacy guarantees for training data: Private Aggregation of Teacher Ensembles (PATE). The approach combines, in a black-box fashion, multiple models trained with disjoint datasets, such as records from different subsets of users. Because they rely directly on sensitive data, these models are not published, but instead used as "teachers" for a "student" model. The student learns to predict an output chosen by noisy voting among all of the teachers, and cannot directly access an individual teacher or the underlying data or parameters. The student's privacy properties can be understood both intuitively (since no single teacher and thus no single dataset dictates the student's training) and formally, in terms of differential privacy. These properties hold even if an adversary can not only query the student but also inspect its internal workings.

Compared with previous work, the approach imposes only weak assumptions on how teachers are trained: it applies to any model, including non-convex models like DNNs. We achieve state-of-the-art privacy/utility trade-offs on MNIST and SVHN thanks to an improved privacy analysis and semi-supervised learning.

  * [Ethics & Safety](</research/index/?tags=ethics-safety>)



## Authors

Nicolas Papernot, Martín Abadi, Úlfar Erlingsson, Ian Goodfellow, Kunal Talwar

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

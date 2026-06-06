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

August 10, 2022

[Product](</news/product-releases/>)

# New and improved content moderation tooling

[Read documentation(opens in a new window)](<https://platform.openai.com/docs/api-reference/moderations/create>)

![New And Improved Content Moderation Tooling](https://images.ctfassets.net/kftzwdyauwt9/5772930c-1b4d-40cf-bf103c8dd331/1933ee15c42afd6a78b56802bd4abdda/image-24.webp?w=3840&q=90&fm=webp)

Loading…

Share

To help developers protect their applications against possible misuse, we are introducing the faster and more accurate [Moderation endpoint⁠(opens in a new window)](<https://beta.openai.com/docs/api-reference/moderations>). This endpoint provides OpenAI API developers with free access to [GPT‑based⁠](</index/customized-gpt-3/>) classifiers that detect undesired content—an instance of [using AI systems⁠](</index/critiques/>) to assist with human supervision of these systems. We have also released both a [technical paper⁠(opens in a new window)](<https://arxiv.org/abs/2208.03274>) describing our methodology and the [dataset⁠(opens in a new window)](<https://github.com/openai/moderation-api-release>) used for evaluation.

When given a text input, the Moderation endpoint assesses whether the content is sexual, hateful, violent, or promotes self-harm—content prohibited by our [content policy⁠(opens in a new window)](<https://beta.openai.com/docs/usage-guidelines/content-policy>). The endpoint has been trained to be quick, accurate, and to perform robustly across a range of applications. Importantly, this reduces the chances of products “saying” the wrong thing, even when deployed to users at-scale. As a consequence, AI can unlock benefits in sensitive settings, like education, where it could not otherwise be used with confidence.

Loading...

The Moderation endpoint helps developers to benefit from our infrastructure investments. Rather than build and maintain their own classifiers—an extensive process, as we document in our [paper⁠(opens in a new window)](<https://arxiv.org/abs/2208.03274>)—they can instead access accurate classifiers through a single API call.

As part of OpenAI’s [commitment⁠](</charter/>) to [making the AI ecosystem safer⁠](</index/best-practices-for-deploying-language-models/>), we are providing this endpoint to allow free moderation of all OpenAI API-generated content. For instance, [Inworld⁠(opens in a new window)](<https://www.inworld.ai/>), an OpenAI API customer, uses the Moderation endpoint to help their AI-based virtual characters remain appropriate for their audiences. By leveraging OpenAI’s technology, Inworld can focus on their core product: creating memorable characters. We currently do not support monitoring of third-party traffic.

Get started with the Moderation endpoint by checking out [the documentation⁠(opens in a new window)](<https://beta.openai.com/docs/guides/moderation/overview>). More details of the training process and model performance are available in our [paper⁠(opens in a new window)](<https://arxiv.org/abs/2208.03274>). We have also released an [evaluation dataset⁠(opens in a new window)](<https://github.com/openai/moderation-api-release>), featuring Common Crawl data labeled within these categories, which we hope will spur further research in this area.

  * [View documentation(opens in a new window)](<https://beta.openai.com/docs/guides/mode>)



  * [API Platform](</news/?tags=api-platform>)
  * [2022](</news/?tags=2022>)



## Authors

Todor Markov, Chong Zhang, Sandhini Agarwal, Tyna Eloundou, Teddy Lee, Steven Adler, Angela Jiang, Lilian Weng

## Related articles

[View all](</news/>)

![Newspartnership Cover](https://images.ctfassets.net/kftzwdyauwt9/ffffbd46-a171-41c5-25d9eec16b7d/bd1bc987f38b1c2901819b4c211886a2/NewsPartnership_Cover.png?w=3840&q=90&fm=webp)

[Global news partnerships: Le Monde and Prisa MediaCompanyMar 13, 2024](</index/global-news-partnerships-le-monde-and-prisa-media/>)

![News > Company carousel > Review completed > Media](https://images.ctfassets.net/kftzwdyauwt9/3BEH4mYgX0MXC45XOsbOru/fdcc0dadabd87f8e9a776a2f34647de0/37.png?w=3840&q=90&fm=webp)

[Review completed & Altman, Brockman to continue to lead OpenAICompanyMar 8, 2024](</index/review-completed-altman-brockman-to-continue-to-lead-openai/>)

![New board of directors](https://images.ctfassets.net/kftzwdyauwt9/5J9s3ItUUDOTebSo0ZVmun/642e8632be32866792c7aaae0113aaa5/44.png?w=3840&q=90&fm=webp)

[OpenAI announces new members to board of directorsCompanyMar 8, 2024](</index/openai-announces-new-members-to-board-of-directors/>)

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

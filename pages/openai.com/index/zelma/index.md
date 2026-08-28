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

# Zelma

Zelma uses GPT‑4 to make education data accessible.

![Zelma logo in white over a green solid background.](https://images.ctfassets.net/kftzwdyauwt9/1HWdCulqTyG5IYm00xNHjk/d658507f2b38bb22ac8643adf50be369/zelma.png?w=3840&q=90&fm=webp)

Loading…

Share

Zelma, a GPT‑4 powered research assistant, is making education data accessible to parents, teachers, school administrators, and policymakers across the United States.

The problem they’re solving? While standardized tests are issued to every student in grades 3–8 in the U.S., data about how students perform remains largely untapped and underutilized, scattered across different sources and formats. Test data offers powerful insights into how well students are learning in English language arts (ELA) and math, across district and demographic group levels. But crucial insights that could shape the future of education are effectively beyond the reach of most parents, journalists, educators, and policymakers. 

Recognizing this gap, Dr. Emily Oster, a Brown economist and author, set out to change the narrative. “Zelma makes it possible for parents and policymakers alike to use plain language to get instant, tailored educational insights on what matters most to them,” Dr. Oster explained. How did Zelma accomplish this? Dr. Oster’s team of student researchers at Brown University spent a year gathering the data and meticulously cleaning it into one uniform format. Zelma then worked with [Novy⁠(opens in a new window)](<https://www.novy.ai/>) to bring the data to life using OpenAI’s API.

Novy leveraged [function calling⁠(opens in a new window)](<https://platform.openai.com/docs/guides/function-calling>) to tell GPT‑4 which visuals and fields to choose from in displaying the data. For Zelma’s "Ask a Question" view, they [fine-tuned⁠(opens in a new window)](<https://platform.openai.com/docs/guides/fine-tuning>) a model to create a data-aware type-ahead that suggests questions with available data. And they [embedded⁠](<https://openai.com/blog/introducing-text-and-code-embeddings>) and stored known-good example graphs in a vector database to improve accuracy on difficult edge cases. 

The biggest challenge was trying to predict how people would phrase their questions, and keeping the prompts within Zelma’s scope of knowledge. “We addressed this through intentional design choices in Zelma’s user experience that nudge people to ask questions Zelma can answer,” Dr. Oster explained. Key features include:

  * **Suggesting example prompts.** Because Zelma covers only a specific domain of education data, these suggestions help users understand Zelma’s scope of knowledge and how to phrase their prompts.
  * **Making all questions**[**public.** ⁠(opens in a new window)](<https://www.zelma.ai/featured>) This helps people learn from what others have asked while also preventing users from submitting high volumes of irrelevant queries.
  * **Showing the SQL code.** Zelma provides its logic to help you quickly verify its answers. For non-coders, the factors are also explained in plain language.
  * **Explaining the context.** Zelma gives context through definitions and flagging notable events—such as changes in the state assessment—to help you understand any external factors that might have influenced the data in a given year.



Now, you can instantly shortlist the [top 5 highest performing non-charter school districts in math in Minnesota,⁠(opens in a new window)](<https://www.zelma.ai/q/4DGXDNgmrg>) and find that they all score around a 77 percent proficiency rate. And a simple prompt can surface racial disparities in [ELA achievement in California over time,⁠(opens in a new window)](<https://www.zelma.ai/q/Bwa3h5FFss>) while also pointing out an assessment change in 2015 that makes test results from 2015 onward not comparable with prior years.

![Zelma Math Proficiency Chart](https://images.ctfassets.net/kftzwdyauwt9/2OtHPBAYQWJzmVOLFhkSLm/96ae3f222f60fe1fd8b33988f2a3893e/Top5MathMinnesota.avif?w=3840&q=90&fm=webp)

Top 5 Math Proficiency Rates in Non-Charter Districts in Minnesota (2023)

![Zelma ELA Scores Chart](https://images.ctfassets.net/kftzwdyauwt9/4qObdesQWmwTDyZs70hJGY/214fe16bf00da01e933fcf23fbdb634e/ELAScoresCalifornia.avif?w=3840&q=90&fm=webp)

ELA Scores Over Time in California by Race/Ethnicity

This means that school board members can use Zelma to quickly generate data visualizations during meetings, enabling data-informed decision-making. Parents can compare historical test performances of nearby school districts to make educated decisions on where to raise their children. A Governor’s Chief of Staff can reference Zelma to identify the best performing schools in their state and see how much test scores have changed over time.

> “Zelma offers K-12 superintendents an intuitive, conversational platform to instantly visualize student learning data—views that have historically taken district leadership teams hours or even days to generate. By democratizing this data, Zelma is making it easier for adults in the system to have concrete conversations about student outcomes and direct public attention to student well-being.”

Caitlin Sullivan, Co-founder & Executive Director of Leading Now

From scattered data portals and spreadsheets to a user-friendly website, Zelma transforms disparate data into meaningful analyses. Zelma joins other use cases [supporting teachers in the classroom⁠](<https://openai.com/blog/teaching-with-ai>) and [helping students learn at their own pace⁠](<https://openai.com/customer-stories/khan-academy>) in showing ways that generative AI can enhance our education system. Zelma also provides a powerful example of how OpenAI’s tools and products can be used to make data more useful and accessible to all.

## Interested in learning more about ChatGPT for business?

[Talk with our team](</contact-sales/>)

## Related customer stories

![Klarna > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/1rKhPYNyBR444XDwzBejML/34c714921e283fd064343fcfd29a8d9b/klarna-v2.png?w=3840&q=90&fm=webp)

[Klarna's AI assistant does the work of 700 full-time agentsApr 5, 2024](</index/klarna/>)

![Harvey Cover Image](https://images.ctfassets.net/kftzwdyauwt9/4tOsY4kprIobRIBvif5sOt/0a208a8f901f000a8be4cef8426c37fc/harvey.png?w=3840&q=90&fm=webp)

[Customizing models for legal professionalsApr 2, 2024](</index/harvey/>)

![Oscar Cover Image](https://images.ctfassets.net/kftzwdyauwt9/3pyY5QDNdExFmc3OcrqqBK/643bb793e8173e886c56e952e34c69c2/oscar.png?w=3840&q=90&fm=webp)

[Reducing health insurance costs and improving careApr 1, 2024](</index/oscar/>)

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

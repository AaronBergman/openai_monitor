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

September 14, 2026

Startup

# How Fyxer built an AI executive assistant people trust

Fyxer pairs OpenAI models with 500,000+ hours of EA workflows and real user feedback to draft replies in each person’s voice.

[Start building](</startups/>)

Company size: Startup

Region: Europe & UK

Industry: Technology

Products: API

90%

User retention after 90 days

53%

Of AI-generated drafts accepted as written

Loading…

Share

1\. Break email into smaller jobs

  * 1\. Break email into smaller jobs
  * 2\. Train on how great assistants actually work
  * 3\. Turn user feedback into a self-training loop
  * From drafts to a proactive assistant



  * 1\. Break email into smaller jobs
  * 2\. Train on how great assistants actually work
  * 3\. Turn user feedback into a self-training loop
  * From drafts to a proactive assistant



For many professionals, work means keeping track of conversations and commitments across inboxes, meetings, messages, and apps. Without rock-solid context, those commitments can fall through the cracks, damaging projects and relationships.

Fyxer built an AI executive assistant that follows the thread as work moves across tools. It combines the latest OpenAI models with more than 500,000 hours of executive assistant workflows, dividing the work among dozens of specialized models that improve through real user feedback.

Email is one of the clearest places to see it in action. Two people can receive the same email and need completely different replies depending on the relationship, what has happened before, and what each person is trying to get done. That makes a seemingly simple task deceptively hard for AI.

“There’s something called Moravec’s paradox,” explains Fyxer Co-founder Archie Hollingsworth. “Things that humans find easy are hard for computers, and things that computers find easy are hard for humans.” Fyxer handles that complexity by learning how each user works, so it can respond like an assistant who already knows what matters.

Frontier OpenAI models support key parts of the experience, from understanding the email and finding the right context to generating the draft. Fyxer chose OpenAI because its models performed best on Fyxer’s internal benchmarks, offered strong fine-tuning capabilities for subjective tasks like tone and intent, and provided hands-on engineering support through whiteboarding sessions and technical collaboration.

> “We chose OpenAI because they have the best models, and they’ve given us real access and a close working relationship. I can drop a question in Slack and get an answer quickly, and when we face a problem, the team comes to our office and works through it with us. They show up.”

—Archie Hollingsworth, Co-founder, Fyxer

Fyxer’s approach offers three lessons for founders building highly contextual AI products:

## 1\. Break email into smaller jobs

Fyxer built its system around 30–50 specialized models, each responsible for a narrow part of the email workflow. Instead of treating email as a single text-generation task, Fyxer breaks the problem into a system of predictions, like deciding whether a message requires a reply or drafting responses that match a user’s tone and context.

“Breaking the problem into many smaller models works much better than asking one model to write a good email,” Hollingsworth explains.

When a new email arrives, a reply decision model classifies the message: is this something that needs a response, a scheduling action, or simply information the user should see?

If a response is needed, additional models analyze the intent of the email and predict the likely outcome of the interaction. These models determine patterns such as whether the conversation is moving toward scheduling a meeting, resolving a request, or continuing a longer relationship thread.

Memory is one of the most important parts of the system. Fyxer needs to decide which details should persist across conversations and which should disappear after a single exchange. When a new email arrives, retrieval models compare it with stored interactions and surface the memories most relevant to that person and thread.

OpenAI models power steps across Fyxer’s system. “We use OpenAI models for everything from digesting the email, so we can understand what it is actually about, to pulling in and re-ranking the context we want to include, to the actual email generation,” Shantsila says.

## 2\. Train on how great assistants actually work

Before launching its AI product, Fyxer spent years operating a human-powered executive assistant service. Over time, the team accumulated a dataset built from more than 500,000 hours of annotated executive workflows, capturing how real assistants manage professional communication.

Those examples gave Fyxer training data drawn from the job itself. They captured the small judgments behind a good response: when to answer quickly, when to wait, which earlier conversation matters, and how the same request can call for a different response from one person to another.

Fyxer uses supervised fine-tuning and Low-Rank Adaptation (LoRA) across its broader system to create task-specific model variants while controlling training cost. Early in the product’s development, the team used OpenAI’s fine-tuning platform for tasks that needed high accuracy. More recently, Fyxer worked with OpenAI’s managed fine-tuning team to put a new checkpoint into production.

> “OpenAI has been pivotal for us in helping us transfer the learning that we have about our customer and successfully incorporate it into how the models work.”

—Joey Dwonczyk, AI/ML Product Engineer, Fyxer

Before any model is deployed, Fyxer evaluates it on validation sets built around its own email tasks, including drafting, classification, and prioritization. The team weighs accuracy alongside response time and cost, since the best choice can vary by job.

## 3\. Turn user feedback into a self-training loop

Once deployed, Fyxer’s system continues improving through real user feedback. When someone edits a draft before sending it, the difference between the original and final email shows which output they preferred.

Fyxer converts those comparisons into training data using Direct Preference Optimization (DPO). Instead of manually labeling every example, the model learns from pairs of outputs: the original draft and the user-edited version.

Every drafting change then goes through an A/B test. Fyxer ships the new version only when it produces a statistically significant improvement. Its user volume means the team can sometimes reach that threshold within a day.

Today, 53% of Fyxer’s AI-generated drafts are accepted as written. That means the system is correctly predicting intent and tone for a large share of real conversations. In 2025 alone, Fyxer grew from $1 million to $32 million in annual recurring revenue.

For Hollingsworth, the stronger signal is retention. Many Fyxer customers are not deeply technical, and for some, Fyxer is the first AI system they use every day.

> “Everyone talks about ARR, but I think retention is the real flex. Over 90% of our users are still paying at the 90-day mark with us, and still using us every day.”

—Archie Hollingsworth, Co-founder, Fyxer

## From drafts to a proactive assistant

Looking ahead, Fyxer is building a richer understanding of relationships, preferences, and ongoing work threads. Their assistant continues to evolve beyond drafting replies toward a broader AI assistant that can manage more of a user’s communication and coordination workload.

“Our vision is to get our customers doing as much of the work they absolutely love,” Hollingsworth says. “We want to get them to a place where they never have to open their computer and can trust Fyxer to manage all of that.”

## OpenAI <3 startups

[Join the community](</leads/startup/>)[Start building(opens in a new window)](</startups>)

## Keep reading

[View all](</news/>)

![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aabc92ea8266c99be14d0f380f1/square.png?w=3840&q=90&fm=webp)

[Parallel cut research time and cost in half with GPT‑6 AstraStartupSep 22, 2026](</index/parallel-cuts-time-and-cost-with-astra/>)

![Higgsfield AI customer story art card](https://images.ctfassets.net/kftzwdyauwt9/7A0WMEXBwLKT6RUmIz7pfX/c764d19c42285ef2628de699c0820571/square.png?w=3840&q=90&fm=webp)

[Higgsfield AI ships new video features in a day with GPT-6 AstraStartupSep 21, 2026](</index/higgsfield-from-prompt-to-production-with-astra/>)

![V7 customer story hero art card - graphite texture](https://images.ctfassets.net/kftzwdyauwt9/69ITITTOHLrgzbSw13s3L1/eded3a71f9961eacc29f699371f3a9f2/V7-art-card-1x1-option-a.png?w=3840&q=90&fm=webp)

[How V7 gives AI agents institutional memoryStartupSep 21, 2026](</index/v7/>)

Research

  * [Research Index](</research/index/>)
  * [Research Overview](</research/>)
  * [Economic Research](</signals/>)



Latest Advancements

  * [GPT-6](</index/gpt-6-astra/>)
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
  * [Plugins](</business/plugins/>)
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

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

January 7, 2026

Startup

# How Tolan builds voice-first AI with GPT‑5.1

With GPT‑5.1, Tolan built a voice app optimized for low latency, accurate context, and stable personalities as conversations evolve.

![Tolan logo on orange jigsaw puzzle background](https://images.ctfassets.net/kftzwdyauwt9/uzf6b0mtJYhARaCWxx9MX/1ab7dbf67bcf2f3898bd67c7ebee78df/oai_Tolan_16x9.png?w=3840&q=90&fm=webp)

Loading…

Share

Designing for natural voice interactions

  * Designing for natural voice interactions
  * Building memory and personality that hold together over time
  * Tolan’s core principles for building natural voice agents 
  * Expanding what’s possible with voice AI



  * Designing for natural voice interactions
  * Building memory and personality that hold together over time
  * Tolan’s core principles for building natural voice agents 
  * Expanding what’s possible with voice AI



[ _Tolan_ ⁠(opens in a new window)](<https://www.tolans.com>) is a voice-first AI companion where people talk with a personalized, animated character that learns from conversations over time. 

Built by Portola, a veteran team with a prior exit, the app is designed for ongoing, open-ended dialogue rather than quick prompts and replies. “We saw the rise of ChatGPT and knew voice was the next frontier,” says Quinten Farmer, co-founder and CEO of Portola. “But voice is harder. You’re not just responding to typed prompts; you’re holding a live, meandering conversation.”

Voice AI raises the bar on latency and context management, but it also enables more open-ended, exploratory interactions than text. 

With foundation models becoming faster, cheaper, and more capable, the team focused their efforts on two key levers: memory and character design. Portola built a character-driven universe, shaped by award-winning animators and a science fiction writer, using a real-time context management system to keep personality and memory consistent as conversations unfold.

The release of the GPT‑5.1 models marked a turning point, delivering major gains in steerability and latency that brought those pieces together, unlocking a more responsive and engaging voice experience.

> “GPT-5.1 gave us the steerability to finally express the characters we had in mind. It wasn’t just smarter—it was more faithful to the tone and personality we wanted to create.”

—Quinten Farmer, CEO, Portola

## Designing for natural voice interactions

Tolan’s architecture is shaped by the demands of voice. Voice users expect instant, natural responses, even when conversations shift midstream. Tolan had to respond quickly, track changing topics, and maintain a consistent personality without lag or tone drift.

To feel natural, conversations required near-instant latency. Introducing OpenAI GPT‑5.1 and the Responses API cut speech initiation time by over 0.7 seconds—enough to noticeably improve conversational flow.

Equally critical was how the system handled context. Unlike many agents that cache prompts across multiple turns, Tolan rebuilds its context window from scratch each turn. Each context reconstruction pulls in a summary of recent messages, a persona card, vector-retrieved memories, tone guidance, and real-time app signals. This architecture allows Tolan to adapt in real time to abrupt topic shifts, an essential requirement for natural voice-based interaction.

“We realized quickly that cached prompts just didn’t cut it,” says Quinten. “Users change subjects all the time. To feel seamless, the system had to adapt midstream.”

This real-time reconstruction approach is both technically intensive and foundational to Tolan’s success.

![Flow diagram showing Tolan’s conversational loop. A “Recompute persona” step feeds four inputs, chat summary and recent raw messages, user and Tolan personas and other context, memory, and tone. These inputs combine to generate a Tolan response, which leads to a user response. The user response then drives two parallel processes: deriving an updated tone and extracting memories. Extracted memories update memory, updated tone feeds back into tone, and the conversation history is periodically re-summarized and compressed, looping back into the chat summary for the next turn.](https://images.ctfassets.net/kftzwdyauwt9/2KmVLcxFmx3GdYbvqyokt4/ed6e65c182e24ccf3c725b7c9f558520/Tolan_Chart_1_Light.png?w=3840&q=90&fm=webp)

## Building memory and personality that hold together over time

Context handling is important, but it wasn’t enough to keep conversations feeling coherent over time. To support long, nonlinear conversations, Tolan built a memory system that retains not just facts and preferences, but also emotional “vibe” signals—clues that help steer how a Tolan should respond.

Memories are embedded using the OpenAI text-embedding-3-large model and stored in Turbopuffer, a high-speed vector database that enables sub-50ms lookup times. This speed is essential for real-time voice interactions. Each turn, Tolan uses the user’s latest message and system-synthesized questions (e.g., “Who is the user married to?”) to trigger memory recall. To keep memory quality high, Tolan runs a nightly compression job that removes low-value or redundant entries (e.g. “the user drank coffee today”) and resolves contradictions.

Personality is just as carefully managed. Each Tolan is seeded with a distinct character scaffold, authored by the team’s in-house science fiction writer and refined by a behavioral researcher. These seeds give Tolans consistency, but also flexibility to adapt over time, evolving alongside the user. 

A parallel system monitors the emotional tenor of the conversation and dynamically adjusts the Tolan’s delivery. This allows a Tolan to shift seamlessly from playful to grounded depending on user cues, without losing its core personality. 

The transition to GPT‑5.1 was a turning point. Suddenly, layered prompt instructions—tone scaffolds, memory injections, character traits—were followed more faithfully. Prompts that once required workarounds began behaving as intended. 

“For the first time, our internal experts felt like the model was really listening,” says Quinten. “Instructions stayed intact across long conversations, persona traits were respected, and we saw far less drift.”

Those changes added up to a more consistent and believable personality, which in turn created a more engaging user experience. The Tolan team saw clear, measurable gains: memory recall misses dropped by 30% (based on in-product frustration signals), and next-day user retention rose more than 20% after GPT‑5.1–powered personas went live.

![Flow diagram illustrating how Tolan retrieves and refines memories during conversation. A user message \(“I’m so excited for my trip this weekend”\) triggers a step that synthesizes follow-up questions, such as upcoming trips, plans for a specific week, and user preferences. These questions are embedded and used to query a memory vector database, with results merged using mean reciprocal rank. The retrieved context informs Tolan’s response \(“camping with Steven in Yosemite”\). A later user message about a future trip to Iceland is stored as a new memory, then reflected on, clustered with related memories using embedding-based k-nearest neighbors, and compressed by combining, editing, and refining memories within each cluster.](https://images.ctfassets.net/kftzwdyauwt9/hSJM1UHJSW6cffyNiMM3R/49006fc4a8502951fdc7c4cadf1132dd/Tolan_Chart_2_Light.png?w=3840&q=90&fm=webp)

## Tolan’s core principles for building natural voice agents 

As Tolan evolved, a few principles emerged that now guide how the team builds and evolves its voice architecture:

  * **Design for conversational volatility:** Voice conversations shift mid-sentence. Systems need to pivot just as quickly to feel natural.
  * **Treat latency as part of the product experience:** Sub-second responsiveness shapes whether a voice agent feels conversational or mechanical.
  * **Build memory as a retrieval system, not a transcript:** High-quality compression and fast vector search deliver more consistent personality than oversized context windows.
  * **Rebuild context every turn:** Don’t fight drift with bigger prompts. Regenerating context each turn keeps agents grounded as conversations meander.



Together, these lessons form the foundation for Tolan’s next phase of innovation and set the direction for where voice AI is headed.

## Expanding what’s possible with voice AI

Since launching in February 2025, Tolan has grown to more than 200,000 monthly active users. Its 4.8-star rating and more than 100,000 App Store reviews highlight how well the system maintains consistency across long, shifting conversations. One reviewer noted, “They remember things we talked about two days ago and they bring it back into the conversation that we’re having today.”

These signals map directly to the underlying architecture: low-latency model calls, turn-by-turn context reconstruction, and modular memory and persona systems. Together, they allow Tolan to track topic changes, preserve tone, and keep responses grounded without relying on large, fragile prompts.

Looking ahead, Tolan plans to deepen its investments in steerability and memory refinement, focusing its efforts on tighter compression, improved retrieval logic, and expanded persona tuning. The long-term goal is to expand what a voice interface can be: not just responsive, but context-aware and conversationally dynamic.

“The next frontier,” says Quinten, “is building voice agents that aren’t just responsive, but truly multimodal, able to integrate voice, vision, and context into a single, steerable system.”

## Keep reading

[View all](</news/>)

![Model ML customer story card image](https://images.ctfassets.net/kftzwdyauwt9/3STNMQMrFRC8mFdLYtjkV4/9cc21e9c729b2ae7cdf75aa3f49b3033/modelml-card.png?w=3840&q=90&fm=webp)

[Model ML completes finance work more efficiently with GPT-5.6 SolStartupAug 10, 2026](</index/model-ml/>)

![Warp customer story 1x1 hero art card](https://images.ctfassets.net/kftzwdyauwt9/3DK9g0hpubvAEz7lDs0nUf/713989b24b9d377312714303868b9126/oai_Warp_1x1.png?w=3840&q=90&fm=webp)

[Warp’s big bet on building open source with GPT-5.5StartupMay 27, 2026](</index/warp/>)

![Parloa > Card](https://images.ctfassets.net/kftzwdyauwt9/79CIP6zYxNAKgc3cJfSimj/cd0b9187ba78aeca8088ba6c11ce8b7e/oai_Parloa_1x1.png?w=3840&q=90&fm=webp)

[Parloa builds service agents customers want to talk toStartupMay 7, 2026](</index/parloa/>)

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

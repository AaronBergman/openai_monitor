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

October 26, 2026

OpenAI on OpenAI

# How Ultrafast cut incident investigation from hours to minutes at OpenAI

Loading…

Share

Finding the needle in the haystack

  * Finding the needle in the haystack
  * Fast responses in under 30 seconds
  * Working as a copilot



  * Finding the needle in the haystack
  * Fast responses in under 30 seconds
  * Working as a copilot



 _This is part of our series sharing internal examples of how OpenAI is using its own technology and APIs. These tools are being used internally, at OpenAI, and are shared here as illustrative examples of how frontier AI is supporting use cases across our teams._

Ultrafast is a high-speed mode in Codex, and for engineers at OpenAI, it’s become the default for incident response. When something breaks, engineers often don’t have time to wait minutes for an answer while the issue compounds. With Ultrafast, they can investigate multiple potential causes at once and get answers without splitting their attention.

> “If you take two humans who are equally smart, and one gets back to you in an hour and one gets back to you in a minute, the second person is way better. You’re just going to get way more done with somebody who responds faster.”

—Adam Perry, Member of Technical Staff, OpenAI

## Finding the needle in the haystack

Aaron Friel, Member of the Technical Staff at OpenAI, is usually the one running point on an incident. He spins up a Slack channel for incident response and then points Codex at the problem, asking Codex to monitor, investigate, and answer any questions as they come in. “In any incident, there are usually many hops along the way of what could have gone wrong, and finding the right needle in the right haystack is really the chief job of the people on that channel,” he says. “Using Ultrafast, I’m able to essentially search all of those haystacks at the same time, and respond to incidents much faster.”

AJ Trbojevic, Member of the Technical Staff and a Datacenter Security Architect, says investigations into security issues used to take an hour or two to pull structured and unstructured data together, normalize it, and provide context to make a decision. “Now that happens in 10 to 15 minutes,” he says. “And at times it’s near real time.”

Adam Perry and Sayan Sisodiya both work on the core agent team, building the code that lets Codex take actions, run commands, and use tools. Ultrafast has changed how they operate during security incidents. “Before, I’d ask Codex to look into something, and then go look into it myself at the same time, because I knew it wouldn’t be fast enough to just wait on,” Adam says. “Now with Ultrafast, Codex is fast enough that I can just stay focused instead of splitting my attention.”

Sayan appreciates how Ultrafast lets him get immediate answers from multiple data sources: “Beyond just digging through logs in an incident, I use Codex to dig through Slack to see if there are references to changes that might be suspect or people talking about similar symptoms elsewhere in Slack,” he says.

## Fast responses in under 30 seconds

If it takes more than 30 seconds to find an answer with AI, Jeff Niu, another Member of the Technical Staff, says he’ll check Slack or chat with a coworker. But most of his work is now under that threshold with Ultrafast. He used to ask Codex a question, switch over to something else while it thought, and come back having lost his train of thought. Now that conversation happens in real time; it helps him stay focused on the task at hand.

Ultrafast also makes Jeff more willing to tackle large refactors, because reworking existing code takes less time. “Technical debt is much easier to pay down now than it ever was before,” he says. “Code is cheap, and now it’s very quick to produce. A refactor that used to cost a lot happens almost instantly.”

## Working as a copilot

Adam keeps a running Codex thread that he calls his chief of staff. Every morning it tells him what meetings he has and which messages he might have forgotten to reply to. “It’s already looked at all the data to write that summary, so when I ask a followup, it’s not waiting to go fetch more,” he says. “I can just keep asking questions in the same conversation just like an actual chief of staff.”

Sayan uses Codex to do tedious manual work in the browser, like filling out forms—something he’d previously avoided because it was too slow. “It would open a browser, sit there thinking for five seconds, click something, sit there again,” he says. With the latest models’ improvements in computer use, he’s more comfortable letting Codex handle that work. “Now I’m totally fine letting it click through the browser and it’s fast enough that I’m not losing time by not doing it myself.”

Across incident response, daily planning, and refactoring, Ultrafast lets OpenAI’s Technical Staff work with Codex at the pace of their questions. They can follow up on an answer, try another approach, and keep working without losing their train of thought. That shorter wait also changes what they’re willing to take on, from a refactor they’d put off to a routine task that’s finally worth delegating.

  * Codex
  * 2026



## Author

OpenAI

## Keep reading

[View all](</news/>)

![OAIonOAI ChadNelson 1x1](https://images.ctfassets.net/kftzwdyauwt9/2mUBSQZ1FwfTFJR5Yco4nQ/9a775c8c69a1d1e161bd7f56f4fdb7e7/OAIonOAI_ChadNelson_1x1.png?w=3840&q=90&fm=webp)

[How Codex became a collaborator for OpenAI’s creative teamOpenAI on OpenAIJul 16, 2026](</index/codex-collaborator-creative-team/>)

![OpenAI on OpenAI: User Support > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/76CnrtKKvngPIfdfXYcXG8/cb789b59d9f7dd8e3b385b532be76a77/oai_SupportAgent_1x1.png?w=3840&q=90&fm=webp)

[Improving support with every interaction at OpenAIAPISep 29, 2025](</index/openai-support-model/>)

![OpenAI on OpenAI > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/5gbagfbtROvYfi0cQlpEM3/89367ef5dca927d48e541f6f430ea212/oai_GC_1x1__1_.png?w=3840&q=90&fm=webp)

[Building OpenAI with OpenAIChatGPTSep 29, 2025](</index/building-openai-with-openai/>)

Research

  * [Research Index](</research/index/>)
  * [Research Overview](</research/>)
  * [Economic Research](</signals/>)



Latest Advancements

  * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  * [GPT-6 Astra](</index/gpt-6-astra/>)
  * [GPT-5.6](</index/gpt-5-6/>)
  * [GPT-5.5](</index/introducing-gpt-5-5/>)



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

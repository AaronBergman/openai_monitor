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

  * Codex in Slack
  * Codex SDK
  * New admin features
  * Codex at work
  * Availability and pricing updates



October 6, 2025

[Product](</news/product-releases/>)[Release](</research/index/release/>)

# Codex is now generally available

Get started

$ npm i -g @openai/codex

Loading…

Share

We’re announcing the general availability of Codex and three new features that make it even more useful for engineering teams:

  * **A new Slack integration:** Delegate tasks or ask questions to Codex directly from a team channel or thread, just like you would a coworker.
  * **Codex SDK:** Embed the same agent that powers the Codex CLI into your own workflows, tools, and apps for state-of-the-art performance on [_GPT‑5‑Codex_ ⁠](<https://openai.com/index/introducing-upgrades-to-codex/>) without extra tuning.
  * **New admin tools:** With environment controls, monitoring, and analytics dashboards**,** ChatGPT workspace admins now have more visibility and control to manage Codex at scale.



Since the [_Codex cloud agent_ ⁠](<https://openai.com/index/introducing-codex/>) launched in research preview in May, Codex has steadily evolved into a more reliable and capable coding collaborator. You can now work with it everywhere you code—in your editor, terminal, and the cloud, all connected by your ChatGPT account. Daily usage of Codex has grown by more than 10x since early August, and __ GPT‑5‑Codex is one of our fastest growing models ever, serving over 40 trillion tokens in the three weeks since launch.

Codex is now used by developers all over the world, from startups like Duolingo and Vanta to large enterprises like Cisco and Rakuten. Inside OpenAI, it’s become integral to how we build: nearly all engineers use Codex today, up from just over half in July. They merge 70% more pull requests each week, and Codex automatically reviews almost every PR to catch critical issues before they reach production.

The general availability of Codex reflects how quickly developers and teams everywhere are adopting it—and how much it’s already changing the way we build. 

## Codex in Slack

Tag @Codex in a Slack channel or thread and it will automatically gather the context it needs from the conversation, choose the right environment, and answer with a link to the completed task in Codex cloud. From there, you can merge its changes, keep iterating, or pull the task to your computer to keep working locally. Learn how to set up the Slack integration in the [_docs_ ⁠(opens in a new window)](<http://developers.openai.com/codex/integrations/slack>). 

## Codex SDK

GPT‑5‑Codex was trained for Codex—specifically, the open-source agent implementation that powers the Codex CLI. We also tuned the agent implementation so that its prompt, tool definitions, and agent loop deliver faster and more accurate results with models like GPT‑5‑Codex.

With the Codex SDK, you can bring the same agent into your own engineering workflows and apps with just a few lines of code. It provides structured outputs for parsing agent responses and built-in context management to resume sessions. The SDK is available for TypeScript today, with more languages coming soon.

#### TypeScript

`
    
    
    1
    
    import { Codex } from "@openai/codex-sdk";
    
    2
    
      
    
    
    3
    
    const agent = new Codex({});
    
    4
    
    const thread = await agent.startThread();
    
    5
    
      
    
    
    6
    
    const result = await thread.run("Explore this repo");
    
    7
    
    console.log(result);
    
    8
    
      
    
    
    9
    
    //resume thread
    
    10
    
    const result2 = await thread.run("Propose changes")
    
    11
    
    console.log(result2);

`

We’re also releasing a new GitHub Action to make it easy to integrate Codex into CI/CD pipelines. If you need to directly use the Codex agent in workflows that run in shell environments, you can just install and run the Codex CLI with `codex exec`. Learn more about using the SDK and GitHub Actions in our latest [_guide_ ⁠(opens in a new window)](<http://developers.openai.com/codex/sdk>).

## New admin features

ChatGPT admins can now edit or delete Codex cloud environments in their workspace—for example, to remove sensitive information or clean up unused environments. They can also enforce safer defaults for local usage with the Codex CLI and IDE extension, like defining overrides through managed configuration or monitor actions taken by Codex. New analytics dashboards also help admins track usage across the CLI, IDE, and web, and the quality of code reviews provided by Codex.

Learn more about configuring the new controls in the [_admin guide_ ⁠(opens in a new window)](<https://developers.openai.com/codex/enterprise>).

![Codex analytics dashboard showing two charts: bar chart for daily code review issues by priority, and stacked area chart for sentiment of code review feedback over time. Set on a gradient background with faint code.](https://images.ctfassets.net/kftzwdyauwt9/2vBF5iAOIrcHXJeydbsMPW/1e76d314fd2cddc845272cc23deea5bc/Codex_Blog_UI-Dashboard__2_.png?w=3840&q=90&fm=webp)

## Codex at work

#### Cisco: 50% faster code reviews

At Cisco, engineers are using Codex to speed up the review of complex pull requests, reducing review times by up to 50%. By spending less time on manual checks, they can devote more energy to meaningful, transformative work. Codex supports them by reviewing both human-written code and its own output, helping engineers maintain high standards while enabling faster, more ambitious product releases.

#### Instacart: Automating code cleanup 

At Instacart, the Codex SDK is integrated with Olive, their background coding agent platform. Engineers spin up a remote development environment and complete end-to-end tasks with a single click, using Codex to edit and test changes. Codex automatically cleans up tech debt like dead code and expired experiments, improving code quality and reducing latency across codebases. It also takes on repetitive, well-understood changes, reducing backlog and significantly accelerating engineering velocity.

## Availability and pricing updates

The Slack integration and Codex SDK are available to developers on ChatGPT Plus, Pro, Business, Edu, and Enterprise plans starting today, while the new admin features will be available to Business, Edu, and Enterprise. 

Starting October 20, Codex cloud tasks will also begin counting towards your Codex usage. Learn more about how Codex pricing works for each plan [_here_ ⁠(opens in a new window)](<https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan>).

  * [2025](</news/?tags=2025>)
  * [Codex](</news/?tags=codex>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

![1x1](https://images.ctfassets.net/kftzwdyauwt9/6ui4uYfTTbR4xbiFRcqEfo/81d973f14bea720820f692271f6c6834/square.png?w=3840&q=90&fm=webp)

[Strengthening societal resilience with Rosalind BiodefenseProductMay 29, 2026](</index/strengthening-societal-resilience-with-rosalind-biodefense/>)

![Personal finance in ChatGPT > Media > Cover](https://images.ctfassets.net/kftzwdyauwt9/4zSr4YNWXIEYz20piN2bxf/6f9a561be6055802914aee0a3bb671d7/ArtCard-Personal-Finance.png?w=3840&q=90&fm=webp)

[A new personal finance experience in ChatGPTProductMay 15, 2026](</index/personal-finance-chatgpt/>)

![1x1 Art Card](https://images.ctfassets.net/kftzwdyauwt9/7qVT9WlLKfgGLPC5W77ei6/a24fd3f13b754378759959aa77cd8f5d/1_1.png?w=3840&q=90&fm=webp)

[Work with Codex from anywhereProductMay 14, 2026](</index/work-with-codex-from-anywhere/>)

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

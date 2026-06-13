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

January 9, 2026

# Datadog uses Codex for system-level code review

With Codex, Datadog brings system-wide context into every code review to prevent incidents and protect customer trust.

Loading…

Share

Bringing system-level context to code review with Codex

  * Bringing system-level context to code review with Codex
  * Validating AI review against real incidents
  * Delivering consistent, high-signal feedback
  * Focusing engineers on design over detection
  * Redefining code review around risk, not speed



Table of contents

  * Bringing system-level context to code review with Codex
  * Validating AI review against real incidents
  * Delivering consistent, high-signal feedback
  * Focusing engineers on design over detection
  * Redefining code review around risk, not speed



[ _Datadog_ ⁠(opens in a new window)](<https://www.datadoghq.com/>) runs one of the world’s most widely-used observability platforms, helping companies monitor, troubleshoot, and secure complex distributed systems. When something breaks, customers depend on Datadog to surface issues fast, which means reliability has to be built in long before code ever reaches production.

For Datadog’s engineering teams, that makes code review a high-stakes moment. It’s not just about catching mistakes, but about understanding how changes ripple through interconnected systems—an area where traditional static analysis and rule-based tools often fall short.

To meet this challenge, Datadog’s AI Development Experience (AI DevX) team turned to Codex, the coding agent from OpenAI, which brings system-level reasoning into code review and surfaces risks humans can’t easily see at scale.

“Time savings are real and important,” says Brad Carter, who leads Datadog’s AI DevX team. “But preventing incidents is far more compelling at our scale.”

## Bringing system-level context to code review with Codex

Effective code review at Datadog traditionally relied heavily on senior engineers—the people who understand the codebase, its history, and the architectural tradeoffs well enough to spot systemic risk. 

But that kind of deep context is hard to scale, and early AI code review tools didn’t solve this problem; many behaved like advanced linters, flagging surface-level issues while missing broader system nuances. Datadog’s engineers often found the suggestions too shallow or too noisy, and ignored them.

Datadog began piloting Codex, the coding agent from OpenAI, by integrating it into the live development workflows. In one of the company’s largest and most heavily used repositories, every pull request was automatically reviewed by Codex. Engineers reacted to comments from Codex with thumbs up or down and shared informal feedback across teams. Many noted that the Codex feedback was worth reading, unlike previous tools that produced noisy or shallow suggestions.

## Validating AI review against real incidents

To test whether AI‑assisted review could do more than point out style issues, Datadog built an incident replay harness.

Instead of using hypothetical scenarios, the team went back to historical incidents. They reconstructed pull requests that had contributed to incidents, ran Codex against each one as if it were part of the original review, then asked the engineers who owned those incidents whether feedback from Codex would have made a difference.

The result: Codex found more than 10 cases, or roughly **22%** **of the incidents** that Datadog examined, where engineers confirmed that the feedback Codex provided would have made a difference—more than any other tool evaluated.

Because these pull requests had already passed code review, the replay test showed that Codex surfaced risks reviewers hadn’t seen at the time, complementing human judgment rather than replacing it.

## Delivering consistent, high-signal feedback

Datadog’s analysis showed that Codex consistently flagged issues that aren’t obvious from the immediate diff alone and can’t be caught by deterministic rules.

Engineers described Codex comments as more than “bot noise”:

  * Codex pointed out interactions with modules not touched in the diff
  * It identified missing test coverage in areas of cross‑service coupling
  * It highlighted API contract changes that carried downstream risk



> “For me, a Codex comment feels like the smartest engineer I’ve worked with and who has infinite time to find bugs. It sees connections my brain doesn’t hold all at once.”

—Brad Carter, Engineering Manager at Datadog

That ability to connect review feedback to real reliability outcomes was what made Codex stand out in Datadog’s evaluation. Unlike static analysis tools, Codex compares the intent of the pull request with submitted code changes, reasoning over the entire codebase and dependencies to execute code and tests to validate behavior.

“It was the first one that actually seemed to consider the diff in the larger context of the program,” says Carter. “That was novel and eye‑opening.”  
  
For many engineers, that shift changed how they engaged with AI review altogether. “I started treating Codex comments like real code review feedback,” says Ted Wexler, Senior Software Engineer at Datadog. “Not something I’d skim or ignore, but something worth paying attention to.”

## Focusing engineers on design over detection

Following the evaluation, Datadog deployed Codex more broadly across its engineering workforce. Today **more than 1,000 engineers** use it regularly. 

Feedback is largely surfaced organically rather than through formal in‑tool metrics. Engineers post to Slack about useful insights, constructive comments, and moments where Codex helped them think differently about a problem.

While time savings are significant, teams consistently pointed to a more meaningful shift in how work got done. 

> “Codex changed my mind for what code review should be. It’s not about replicating our best human reviewers. It's about finding critical flaws and edge cases that humans struggle to see when reviewing changes in isolation.”

—Brad Carter, Engineering Manager at Datadog

## Redefining code review around risk, not speed

The broader impact for Datadog was a change in how code review itself is defined. Rather than treating review as a checkpoint for catching errors or optimizing cycle time, the team now sees Codex as a core reliability system that acts as a partner:

  * Surfacing risk beyond what individual reviewers can hold in context
  * Highlighting cross-module and cross-service interactions
  * Increasing confidence in shipping at scale
  * Allowing human reviewers to focus on architecture and design



This shift aligns with how Datadog’s leaders frame engineering priorities, where reliability and trust matter as much as, if not more than, velocity.

“We are the platform companies rely on when everything else is breaking,” says Carter. “Preventing incidents strengthens the trust our customers place in us.”

## Keep reading

![Introducing OpenAI Academy courses > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/2mmXo430NiaNqyi6YrRtnh/715ab11fa5003dd50acff55adcb4a5fd/Frame.png?w=3840&q=90&fm=webp)

[New OpenAI Academy courses for the next era of workAI AdoptionJun 12, 2026](</index/academy-courses-applying-ai-at-work/>)

![Preply Customer story > oai preply 1x1](https://images.ctfassets.net/kftzwdyauwt9/6PmaSoARNrmSZ6QRM8G4Ev/08a3dd4653efbda42894c90b374b6bcf/oai_Preply_1x1.png?w=3840&q=90&fm=webp)

[How Preply combines AI and human tutors to personalize learningJun 12, 2026](</index/preply/>)

![Supporting Europe’s work in ensuring a trustworthy AI ecosystem  > art card](https://images.ctfassets.net/kftzwdyauwt9/U3OuQtdga2BaxWxb0e2ge/2fdc2fb1cf5c70a8f77fc4b55236aa78/Frame2.png?w=3840&q=90&fm=webp)

[Supporting Europe’s work in ensuring a trustworthy AI ecosystem Global AffairsJun 11, 2026](</index/supporting-eu-trustworthy-ai-ecosystem/>)

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

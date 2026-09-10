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

# Scale Tier for API Customers

Scale Tier is available on models released before GPT‑5.6. For GPT‑5.6 and future model releases, see [Reserved Tier](</api-reserved-tier/>)

 _This offering is available to Enterprise customers. Please_[ _contact our sales team⁠_](</contact-sales/>) _to learn more._**_To access the same premium latency and reliability benefits on a flexible, pay-as-you-go basis, see_**[** __Fast mode__**](</api-fast-mode/>)** _._**

Scale Tier lets you purchase a set number of API input and output tokens per minute (known as “token units”) upfront for access to one specific model snapshot. Each token unit is purchased for a minimum of 30 days. Additional models may be added based on customer interest.

By choosing Scale Tier, you can unlock:

  * **Predictable latency:** Scale Tier is designed to generate tokens faster and at a more consistent speed than the pay-as-you-go (PAYG) service, even during peak demand.
  * **Uncapped scale:** Any quota purchases with Scale Tier is automatically added to your rate limits, so you can confidently scale further. 
  * **Higher reliability:** Scale Tier traffic offers a 99.9% uptime SLA and prioritized compute.



| Input bundle| Output bundle| Uptime SLA| Latency SLA  
---|---|---|---|---  
GPT-5.5| 50,000 TPM  
$750.00 per unit/day| N/A3| 99.9%| 99% > 50 tokens per second2  
GPT-5.4 mini| 50,000 TPM  
$100.00 per unit/day| N/A3| 99.9%| 99% > 100 tokens per second2  
GPT-5.4excludes long-context4| 50,000 TPM  
$300.00 per unit/day| N/A3| 99.9%| 99% > 50 tokens per second2  
GPT-5.2| 25,000 TPM  
$105.00 per unit/day| 2,500 TPM  
$84.00 per unit/day| 99.9%| 99% > 50 tokens per second2  
GPT-5.1| 25,000 TPM  
$75.00 per unit/day| 2,500 TPM  
$60.00 per unit/day| 99.9%| 99% > 50 tokens per second2  
GPT-5| 25,000 TPM  
$75.00 per unit/day| 2,500 TPM  
$60.00 per unit/day| 99.9%| 99% > 50 tokens per second2  
GPT-5 mini| 500,000 TPM  
$275.00 per unit/day| 50,000 TPM  
$220.00 per unit/day| 99.9%| 99% > 80 tokens per second2  
GPT-4.1excludes long-context1| 30,000 TPM  
$110.00 per unit/day| 2,500 TPM  
$36.00 per unit/day| 99.9%| 99% > 80 tokens per second2  
GPT-4.1 miniexcludes long-context1| 500,000 TPM  
$450.00 per unit/day| 50,000 TPM  
$175.00 per unit/day| 99.9%| 99% > 90 tokens per second2  
GPT-4.1 nanoexcludes long-context1| 500,000 TPM  
$110.00 per unit/day| 50,000 TPM  
$40.00 per unit/day| 99.9%| 99% > 100 tokens per second2  
GPT-4.1 fine tuning| 30,000 TPM  
$165.00 per unit/day| 2,500 TPM  
$36.00 per unit/day| 99.9%| 99% > 80 tokens per second2  
GPT-4.1 mini fine tuning| 500,000 TPM  
$900.00 per unit/day| 50,000 TPM  
$175.00 per unit/day| 99.9%| 99% > 90 tokens per second2  
o3| 25,000 TPM  
$75.00 per unit/day| 5,000 TPM  
$60.00 per unit/day| 99.9%| 99% > 80 tokens per second2  
o4-mini| 30,000 TPM  
$50.00 per unit/day| 5,000 TPM  
$32.50 per unit/day| 99.9%| 99% > 90 tokens per second2  
GPT-4o| 30,000 TPM  
$124.59 per unit/day| 2,500 TPM  
$39.34 per unit/day| 99.9%| 99% > 80 tokens per second2  
GPT-4o mini| 500,000 TPM  
$114.75 per unit/day| 50,000 TPM  
$49.18 per unit/day| 99.9%| 99% > 90 tokens per second2  
GPT-4o mini fine tuning| 500,000 TPM  
$229.50 per unit/day| 50,000 TPM  
$98.36 per unit/day| 99.9%| 99% > 90 tokens per second2  
o1| 5,000 TPM  
$163.93 per unit/day| 1,000 TPM  
$131.15 per unit/day| 99.9%| 99% > 80 tokens per second2  
o3-mini| 30,000 TPM  
$78.69 per unit/day| 5,000 TPM  
$52.46 per unit/day| 99.9%| 99% > 90 tokens per second2  
  
1Requests estimated at >128K prompt tokens

2Calculated as p50 request latency on a per 5 minute basis. For customers with existing enterprise agreements that have latency SLAs calculated as p50 request latency on a per minute basis, the prior SLAs are also still applicable.

3With GPT-5.4, Scale tier is purchased as a bundle of combined input and output tokens per minute. Usage of input tokens, cached input tokens, and output tokens counts against this combined bundle at different rates. See the How it Works section below.

4Long context is >272K

## How it works

With Scale Tier, you can purchase input and output token units. For example, with GPT‑4.1 each input unit costs $110/day and entitles you to 30k input tokens/min. Each output unit costs $36/day and entitles you to 2.5k output tokens/min. Each token unit is purchased for a minimum of 30 days.

More information about how Scale Tier interacts with Prompt Caching can be found in the FAQ section below.

With GPT‑5.4 and GPT‑5.5 you buy a Combined Input and Output tokens/min. This gives you greater flexibility and removes the need to predict your input and output token ratio. As you use scale tier, we count tokens against your Combined Tokens as follows:

  * Input tokens count as 1
  * Cached input tokens follow the per-model caching as below in the FAQ section
  * Output tokens count based on the PayG price ratio of Output to Input tokens for the model. For example, with GPT‑5.4 one output token counts as 6.



#### Pricing

#### Token units and rate limits

#### Models

#### Reliability

#### Policies

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

### How is Scale Tier ordered and provisioned?

Once you’ve signed an order form, you can add and remove token units through your developer console in Organization Settings > Capacity Management

### When does billing start?

Billing starts the moment when Scale Tier token units are first allocated, and is applied to your standard OpenAI bill.

### How are pay-as-you-go overages calculated while I’m using Scale Tier?

For billing purposes, tokens per minute (TPM) are calculated by averaging the number of tokens used in 15-minute intervals aligned to the top of the hour (e.g. 3:00 to 3:15, 3:15 to 3:30, etc). If the total tokens used within a 15-minute period is below your Scale Tier entitlement, they are not billed. For example, if you purchase Scale Tier for GPT‑4o with an entitlement of 30,000 input tokens per minute, you can use up to 450,000 input tokens in any 15-minute period without incurring additional charges. Any tokens used beyond this limit are billed at pay-as-you-go (PAYG) rates on Fast mode.

### If I make an annual commitment, does my spend have to be applied to Scale Tier?

No. Annual commitments lock in discounts on Scale Tier, Priority processing, and Standard processing. But you’re welcome to use as much or as little of that discounted model as you choose.

### Is my annual commitment tied to a specific offering?

No. Annual commitments can be spent on any OpenAI model and any mechanism of delivery (Standard processing, Priority processing, Scale Tier, or Reserved Capacity).

### If I’m already using Reserved Capacity, how can I use Scale Tier for GPT-4o?

[Reserved Capacity⁠](<https://openai.com/reserved-capacity>) for GPT‑3.5 and GPT‑4 has been superseded with Scale Tier for GPT‑4o and GPT‑4o mini. If you have an existing reserved capacity contract, the amount of your spend can be directly transferred over to Scale Tier on GPT‑4o.

### How can I purchase token units on Scale Tier?

Once Scale Tier is enabled for your account, you can manually adjust your token units in the Capacity Management tab of your Organization Settings

### How can I tell my TPM?

You can view your TPM aggregated by day. In the future, we will provide you with analytics to view it at a more granular level. For now, please work with your account director to get a custom report.

![](https://images.ctfassets.net/kftzwdyauwt9/3mDHiNOY3lRxu76Fk6r83T/5189cb8d8905053b2c01617cdb843aca/Where_do_I_see_my_TPM_.jpg?w=3840&q=90&fm=webp)

### How do I figure out my total rate limits?

You can see your current rate limits in [your settings page⁠⁠(opens in a new window)](<https://platform.openai.com/settings/organization/limits>). When you purchase token units for Scale Tier, your rate limits for that model will automatically increase by the amount of your purchase. When you use the model, requests will first be processed using your faster Scale Tier quota. If you exceed your quota, additional requests will be processed using the regular Standard processing service. If you exceed your total rate limit in a minute across Scale Tier + regular Standard processing limits, then further requests will be rejected like normal with a 429 error code.

### How do I enable calls to use Scale Tier tokens?

Turn on the “Scale Tier Enabled” toggle in Project Settings.

  * Responses API calls will consume Scale Tier tokens by default when the toggle is on and tokens are available.




If using the Completions API, consult docs for the service_tier key to decide whether to set it manually or rely on defaults.

### How does Scale Tier work with Prompt Caching?

We provide different discounts on cached input tokens (50%, 75%, or 90%) depending on the model. If you send 50,000 TPM in cached input tokens on a model where cached tokens are discounted 50%, those tokens only count for 25,000 TPM against your quota. If you send 50,000 TPM in cached input tokens on a model where cached tokens are discounted 75%, those tokens only count for 12,500 TPM against your quota. [Learn more about Prompt Caching⁠(opens in a new window)](<https://platform.openai.com/docs/guides/prompt-caching>)

### How do other modalities work with Scale Tier?

Scale Tier supports the same multimodal capabilities available on Standard processing. In particular, images can be used as inputs to Scale Tier and are processed with the same fast latency.

### Can I automatically send my Scale Tier spill-over traffic to Fast mode?

Yes. As of July 2026 traffic sent to Scale Tier will automatically spill over to Fast mode.

### What happens if the latency and uptime SLA are both violated?

You will be credited with the greater of the two SLA amounts for the calendar month of that Scale Tier token unit purchase.

### How does Zero Data Retention (ZDR) work for Scale Tier?

If customers have a use case that qualifies for ZDR, then their Scale Tier usage will adhere to that same retention policy.

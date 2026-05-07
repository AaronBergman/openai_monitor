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

  * Prompt Caching Availability & Pricing
  * Monitoring Cache Usage



October 1, 2024

[Product](</news/product-releases/>)

# Prompt Caching in the API

Offering automatic discounts on inputs that the model has recently seen

![DALL·E generated impressionist oil painting of layered light green columns interwoven with parallel emerald streams, forming a harmonious and repetitive tapestry.](https://images.ctfassets.net/kftzwdyauwt9/2STrOu0d3xz2yHksnLDGNg/54c78f54d3357e7f626fa9a74bad80c7/03_Prompt_Caching.png?w=3840&q=90&fm=webp)

Share

Many developers use the same context repeatedly across multiple API calls when building AI applications, like when making edits to a codebase or having long, multi-turn conversations with a chatbot. Today, we’re introducing Prompt Caching, allowing developers to reduce costs and latency. By reusing recently seen input tokens, developers can get a 50% discount and faster prompt processing times.

## Prompt Caching Availability & Pricing

Starting today, Prompt Caching is automatically applied on the latest versions of GPT‑4o, GPT‑4o mini, o1‑preview and o1‑mini, as well as fine-tuned versions of those models. Cached prompts are offered at a discount compared to uncached prompts.

Here's an overview of pricing:

| **Uncached Input Tokens**| **Cached Input Tokens**| **Output Tokens**  
---|---|---|---  
**GPT‑4o**| | |   
gpt-4o-2024-08-06| $2.50| $1.25| $10.00  
GPT‑4o fine-tuning| $3.75| $1.875| $15.00  
**GPT‑4o mini**| | |   
gpt-4o-mini-2024-07-18| $0.15| $0.075| $0.60  
GPT‑4o mini fine-tuning| $0.30| $0.15| $1.20  
**o1**| | |   
o1‑preview| $15.00| $7.50| $60.00  
o1 mini| $3.00| $1.50| $12.00  
  
## Monitoring Cache Usage

API calls to supported models will automatically benefit from Prompt Caching on prompts longer than 1,024 tokens. The API caches the longest prefix of a prompt that has been previously computed, starting at 1,024 tokens and increasing in 128-token increments. If you reuse prompts with common prefixes, we will automatically apply the Prompt Caching discount without requiring you to make any changes to your API integration.

Requests using Prompt Caching have a `cached_tokens` value within the `usage` field in the API response:

#### JavaScript

`
    
    
    1
    
    usage: {
    
    2
    
      total_tokens: 2306,
    
    3
    
      prompt_tokens: 2006,
    
    4
    
      completion_tokens: 300,
    
    5
    
      
    
    6
    
      prompt_tokens_details: {
    
    7
    
        cached_tokens: 1920,
    
    8
    
        audio_tokens: 0,
    
    9
    
      },
    
    10
    
      completion_tokens_details: {
    
    11
    
        reasoning_tokens: 0,
    
    12
    
        audio_tokens: 0,
    
    13
    
      }
    
    14
    
    }

`

Caches are typically cleared after 5-10 minutes of inactivity and are always removed within one hour of the cache's last use. As with all API services, Prompt Caching is subject to our [_Enterprise privacy_ ⁠](<https://openai.com/enterprise-privacy/>) commitments. Prompt caches are not shared between organizations. 

Prompt Caching is one of a variety of tools for developers to scale their applications in production while balancing performance, cost and latency. For more information, check out the [_Prompt Caching docs_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/prompt-caching>).

  * [API Platform](</news/?tags=api-platform>)
  * [2024](</news/?tags=2024>)



## Author

OpenAI

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

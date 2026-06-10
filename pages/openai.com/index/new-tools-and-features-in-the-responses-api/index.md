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

New remote MCP server support

  * New remote MCP server support
  * Updates to image generation, Code Interpreter, and file search
  * New features in the Responses API
  * Pricing and availability



May 21, 2025

[Product](</news/product-releases/>)

# New tools and features in the Responses API

Loading…

Today, we’re adding new built-in tools to the Responses API—our core API primitive for building agentic applications. This includes support for all [_remote Model Context Protocol (MCP) servers_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/tools-remote-mcp>), as well as tools like [_image generation_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/image-generation?image-generation-model=gpt-image-1#generate-images>), [_Code Interpreter_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/tools-code-interpreter>), and improvements to [_file search_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/tools-file-search>). These tools are available across our GPT‑4o series, GPT‑4.1 series, and OpenAI o-series reasoning models. o3 and o4-mini can now call tools and functions directly within their chain-of-thought in the Responses API, producing answers that are more contextually rich and relevant. Using o3 and o4-mini with the Responses API preserves reasoning tokens across requests and tool calls, improving model intelligence and reducing the cost and latency for developers.

We’re also introducing new features in the Responses API that improve reliability, visibility, and privacy for enterprises and developers. These include [_background mode_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/async-requests>) to handle long-running tasks asynchronously and more reliably, support for [_reasoning summaries_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/reasoning?api-mode=responses#reasoning-summaries>), and support for [_encrypted reasoning items_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/reasoning?api-mode=responses#encrypted-reasoning-items>). 

Since releasing the [_Responses API_](</index/new-tools-for-building-agents/>) in March 2025 with tools like web search, file search, and computer use, hundreds of thousands of developers have used the API to process trillions of tokens across our models. Customers have used the API to build a variety of agentic applications, including [_Zencoder_ ⁠(opens in a new window)](<https://zencoder.ai/>)’s coding agent, [_Revi_ ⁠(opens in a new window)](<https://www.revi.ai/>)’s market intelligence agent for private equity and investment banking, and [_MagicSchool AI_ ⁠(opens in a new window)](<https://www.magicschool.ai/>)'s education assistant—all of which use web search to pull relevant, up-to-date information into their app. Now developers can build agents that are even more useful and reliable with access to the new tools and features released today.

## New remote MCP server support

We’re adding support for [_remote MCP servers_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/tools-remote-mcp>) in the Responses API, building on the release of [_MCP support in the Agents SDK_ ⁠(opens in a new window)](<https://openai.github.io/openai-agents-python/mcp/>). MCP is an open protocol that standardizes how applications provide context to LLMs. By supporting MCP servers in the Responses API, developers will be able to connect our models to tools hosted on any MCP server with just a few lines of code. Here are some examples showing how developers can use remote MCP servers with the Responses API today:

ShopifyTwilioStripeDeepWiki (Devin)

#### Python

`
    
    
    1
    
    response = client.responses.create(
    
    2
    
      model="gpt-4.1",
    
    3
    
      tools=[{
    
    4
    
        "type": "mcp",
    
    5
    
        "server_label": "shopify",
    
    6
    
        "server_url": "https://pitchskin.com/api/mcp",
    
    7
    
      }],
    
    8
    
      input="Add the Blemish Toner Pads to my cart"
    
    9
    
    )

`

The Blemish Toner Pads have been added to your cart! You can proceed to checkout here:

![Pitch. Skin checkout page showing express options \(Shop Pay, PayPal, G Pay\), contact and delivery form fields, and an order summary for one ‘Blemish Toner Pads 200 mL \(120 pads\)’ priced at AUD $49.](https://images.ctfassets.net/kftzwdyauwt9/4tJh30qd64hXN5bcEFxQUa/09162bd854c113ecb5feb836316e4cb0/Screenshot_2025-05-20_at_4.14.13â__PM.png?w=3840&q=90&fm=webp)

Popular remote MCP servers include [_Cloudflare_ ⁠(opens in a new window)](<https://developers.cloudflare.com/agents/guides/remote-mcp-server/>), [_HubSpot_ ⁠(opens in a new window)](<https://developers.hubspot.com/mcp>), [_Intercom_ ⁠(opens in a new window)](<https://developers.intercom.com/docs/guides/mcp>), [_PayPal_ ⁠(opens in a new window)](<https://developer.paypal.com/tools/mcp-server>), [_Plaid_ ⁠(opens in a new window)](<https://plaid.com/docs/mcp/>), [_Shopify_ ⁠(opens in a new window)](<https://shopify.dev/docs/apps/build/storefront-mcp>), [_Stripe_ ⁠(opens in a new window)](<https://docs.stripe.com/mcp>), [_Square_ ⁠(opens in a new window)](<https://developer.squareup.com/docs/mcp>), [_Twilio_ ⁠(opens in a new window)](<https://github.com/twilio-labs/function-templates/tree/main/mcp-server>), [_Zapier_ ⁠(opens in a new window)](<https://zapier.com/mcp>), and more. We expect the ecosystem of remote MCP servers to grow quickly in the coming months, making it easier for developers to build powerful agents that can connect to the tools and data sources their users already rely on. In order to best support the ecosystem and contribute to this developing standard, OpenAI has also joined the steering committee for MCP.

To learn how to spin up your own remote MCP server, check out this guide from [_Cloudflare_ ⁠(opens in a new window)](<https://developers.cloudflare.com/agents/guides/remote-mcp-server/>). To learn how to use the MCP tool in the Responses API, check out this [_guide_ ⁠(opens in a new window)](<http://cookbook.openai.com/examples/mcp/mcp_tool_guide>) in our API Cookbook.  


## Updates to image generation, Code Interpreter, and file search

With built-in tools in the Responses API, developers can easily create more capable agents with just a single API call. By calling multiple tools while reasoning, models now achieve significantly higher tool calling performance on industry-standard benchmarks like Humanity’s Last Exam ([_source_](</index/introducing-o3-and-o4-mini/>)). Today, we’re adding new tools including:

  * **Image generation:** In addition to using the [_Images API_ ⁠(opens in a new window)](<https://platform.openai.com/docs/api-reference/images>), developers can now access our [_latest image generation model_](</index/image-generation-api/>) —`gpt-image-1`—as a tool within the Responses API. This tool supports real-time streaming—allowing developers to see previews of the image as it’s being generated—and multi-turn edits—allowing developers to prompt the model to granularly refine these images step-by-step. [_Learn more_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/image-generation?image-generation-model=gpt-image-1#generate-images>).
  * **Code Interpreter:** Developers can now use the [_Code Interpreter_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/tools-code-interpreter>) tool within the Responses API. This tool is useful for data analysis, solving complex math and coding problems, and helping the models deeply understand and manipulate images (e.g., [_thinking with images_](</index/thinking-with-images/>)). The ability for models like o3 and o4-mini to use the Code Interpreter tool within their chain-of-thought has resulted in improved performance across several benchmarks including Humanity’s Last Exam ([_source_](</index/introducing-o3-and-o4-mini/>)). [_Learn more_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/tools-code-interpreter>).
  * **File search:** Developers can now access the [_file search_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/tools-file-search>) tool in our reasoning models. File search enables developers to pull relevant chunks of their documents into the model’s context based on the user query. We’re also introducing updates to the file search tool that allow developers to perform searches across multiple vector stores and support attribute filtering with arrays. [_Learn more_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/tools-file-search>).



## New features in the Responses API

In addition to the new tools, we’re also adding support for new features in the Responses API, including:

  * **Background mode:** As seen in agentic products like [_Codex_](</index/introducing-codex/>) , [_deep research_](</index/introducing-deep-research/>) , and [_Operator_](</index/introducing-operator/>) , reasoning models can take several minutes to solve complex problems. Developers can now use background mode to build similar experiences on models like o3 without worrying about timeouts or other connectivity issues—background mode kicks off these tasks asynchronously. Developers can either poll these objects to check for completion, or start streaming events whenever their application needs to catch up on the latest state. [_Learn more_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/async-requests>).



#### Python

`
    
    
    1
    
    response = client.responses.create(
    
    2
    
      model="o3",
    
    3
    
      input="Write me an extremely long story.",
    
    4
    
      reasoning={ "effort": "high" },
    
    5
    
      background=True
    
    6
    
    )

`

  * **Reasoning summaries:** The Responses API can now generate concise, natural-language summaries of the model’s internal chain-of-thought, similar to what you see in ChatGPT. This makes it easier for developers to debug, audit, and build better end-user experiences. Reasoning summaries are available at no additional cost. [_Learn more_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/reasoning?api-mode=responses#reasoning-summaries>).



#### Python

`
    
    
    1
    
    response = client.responses.create(
    
    2
    
        model="o4-mini",
    
    3
    
        tools=[
    
    4
    
            {
    
    5
    
                "type": "code_interpreter",
    
    6
    
                "container": {"type": "auto"}
    
    7
    
            }
    
    8
    
        ],
    
    9
    
        instructions=(
    
    10
    
            "You are a personal math tutor. "
    
    11
    
            "When asked a math question, run code to answer the question."
    
    12
    
        ),
    
    13
    
        input="I need to solve the equation `3x + 11 = 14`. Can you help me?",
    
    14
    
        reasoning={"summary": "auto"}
    
    15
    
    )

`

  * **Encrypted reasoning items:** Customers eligible for****[_Zero Data Retention (ZDR)_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/your-data#zero-data-retention>) can now reuse reasoning items across API requests—without any reasoning items being stored on OpenAI’s servers. For models like o3 and o4-mini, reusing reasoning items between function calls boosts intelligence, reduces token usage, and increases cache hit rates, resulting in lower costs and latency. [_Learn more_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/reasoning?api-mode=responses#encrypted-reasoning-items>).



#### Python

`
    
    
    1
    
    response = client.responses.create(
    
    2
    
      model="o3",
    
    3
    
      input="Implement a simple web server in Rust from scratch.",
    
    4
    
      store=False,
    
    5
    
      include=["reasoning.encrypted_content"]
    
    6
    
    )

`

## Pricing and availability

All of these tools and features are now available in the Responses API, supported in our GPT‑4o series, GPT‑4.1 series, and our OpenAI o-series reasoning models (o1, o3, o3‑mini, and o4-mini). Image generation is only supported on o3 of our reasoning model series. 

Pricing for existing tools remains the same. Image generation costs $5.00/1M text input tokens, $10.00 / 1M image input tokens, and $40.00 / 1M image output tokens, with 75% off cached input tokens. Code Interpreter costs $0.03 per container. File search costs $0.10/GB of vector storage per day and $2.50/1k tool calls. There is no additional cost to call the remote MCP server tool—you are simply billed for output tokens from the API. Learn more about [_pricing_ ⁠(opens in a new window)](<https://platform.openai.com/docs/pricing#built-in-tools>) in our docs. 

We’re excited to see what you build!

  * [2025](</news/?tags=2025>)
  * [API Platform](</news/?tags=api-platform>)



## Author

OpenAI

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

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

  * A more capable harness for the agent loop
  * Native sandbox execution
  * Separating harness from compute for security, durability, and scale
  * Pricing and availability
  * What’s next



April 15, 2026

[Product](</news/product-releases/>)

# The next evolution of the Agents SDK

The updated Agents SDK helps developers build agents that can inspect files, run commands, edit code, and work on long-horizon tasks within controlled sandbox environments.

Loading…

Share

We’re introducing new capabilities to the [Agents SDK⁠(opens in a new window)](<https://developers.openai.com/api/docs/guides/agents>) that give developers standardized infrastructure that is easy to get started with and is built correctly for OpenAI models: a model-native harness that lets agents work across files and tools on a computer, plus native sandbox execution for running that work safely.

For example, developers can give an agent a controlled workspace, explicit instructions, and the tools it needs to inspect evidence:

#### Python

`
    
    
    1
    
    # pip install "openai-agents>=0.14.0"
    
    2
    
      
    
    
    3
    
    import asyncio
    
    4
    
    import tempfile
    
    5
    
    from pathlib import Path
    
    6
    
      
    
    
    7
    
    from agents import Runner
    
    8
    
    from agents.run import RunConfig
    
    9
    
    from agents.sandbox import Manifest, SandboxAgent, SandboxRunConfig
    
    10
    
    from agents.sandbox.entries import LocalDir
    
    11
    
    from agents.sandbox.sandboxes import UnixLocalSandboxClient
    
    12
    
      
    
    
    13
    
      
    
    
    14
    
    async def main() -> None:
    
    15
    
        with tempfile.TemporaryDirectory() as tmp:
    
    16
    
            dataroom = Path(tmp) / "dataroom"
    
    17
    
            dataroom.mkdir()
    
    18
    
            (dataroom / "metrics.md").write_text(
    
    19
    
                """# Annual metrics
    
    20
    
      
    
    
    21
    
    | Year | Revenue | Operating income | Operating cash flow |
    
    22
    
    | --- | ---: | ---: | ---: |
    
    23
    
    | FY2025 | $124.3M | $18.6M | $24.1M |
    
    24
    
    | FY2024 | $98.7M | $12.4M | $17.9M |
    
    25
    
    """,
    
    26
    
                encoding="utf-8",
    
    27
    
            )
    
    28
    
      
    
    
    29
    
            agent = SandboxAgent(
    
    30
    
                name="Dataroom Analyst",
    
    31
    
                model="gpt-5.4",
    
    32
    
                instructions="Answer using only files in data/. Cite source filenames.",
    
    33
    
                default_manifest=Manifest(entries={"data": LocalDir(src=dataroom)}),
    
    34
    
            )
    
    35
    
      
    
    
    36
    
            result = await Runner.run(
    
    37
    
                agent,
    
    38
    
                "Compare FY2025 revenue, operating income, and operating cash flow with FY2024.",
    
    39
    
                run_config=RunConfig(
    
    40
    
                    sandbox=SandboxRunConfig(client=UnixLocalSandboxClient()),
    
    41
    
                ),
    
    42
    
            )
    
    43
    
            print(result.final_output)
    
    44
    
      
    
    
    45
    
      
    
    
    46
    
    if __name__ == "__main__":
    
    47
    
        asyncio.run(main())
    
    48
    
      
    

`

Developers need more than the best models to build useful agents—they need systems that support how agents inspect files, run commands, write code, and keep working across many steps. 

The systems that exist today come with tradeoffs as teams move from prototypes to production. Model-agnostic frameworks are flexible but do not fully utilize frontier models capabilities ; model-provider SDKs can be closer to the model but often lack enough visibility into the harness; and managed agent APIs can simplify deployment but constrain where agents run and how they access sensitive data.

Here’s what some of the customers who tested the new SDK with us had to say:

Oscar HealthActivelyLexisNexisFurtherAIThomson ReutersZoomTomoro AI

> “The updated Agents SDK made it production-viable for us to automate a critical clinical records workflow that previous approaches couldn’t handle reliably enough. For us, the difference was not just extracting the right metadata, but correctly understanding the boundaries of each encounter in long, complex records. As a result, we can more quickly understand what's happening for each patient in a given visit, helping members with their care needs and improving their experience with us.”

— Rachael Burns, Staff Engineer & AI Tech Lead, Oscar Health

## A more capable harness for the agent loop

With today’s release, the Agents SDK harness becomes more capable for agents that work with documents, files, and systems. It now has configurable memory, sandbox-aware orchestration, Codex-like filesystem tools, and standardized integrations with primitives that are becoming common in frontier agent systems.

These primitives include tool use via [_MCP_ ⁠(opens in a new window)](<https://modelcontextprotocol.io>), progressive disclosure via [_skills_ ⁠(opens in a new window)](<https://agentskills.io>), custom instructions via [_AGENTS.md_ ⁠(opens in a new window)](<https://agents.md>), code execution using the [_shell_ ⁠(opens in a new window)](<https://developers.openai.com/api/docs/guides/tools-shell>) tool, file edits using the [_apply patch_ ⁠(opens in a new window)](<https://developers.openai.com/api/docs/guides/tools-apply-patch>) tool, and more. The harness will continue to incorporate new agentic patterns and primitives over time, so developers can spend less time on core infrastructure updates and more time on the domain-specific logic that makes their agents useful.

![Diagram showing how the Agent SDK connects user input, models, and tools to build AI agents.](https://images.ctfassets.net/kftzwdyauwt9/62VtxAHiyQDEZeIPR3jJRC/ccef350e099792d7d6a7d9b41b61ac32/AgentSDK_BuildingAgentsWithModels-LightMode-500px.svg?w=3840&q=90)

![Diagram showing how to build AI agents using the Agent SDK with models, tools, and orchestration.](https://images.ctfassets.net/kftzwdyauwt9/75glmB5ZouJGgoRiiALGct/c15cc514db014be5bc7b9dc19a087ea0/AgentSDK_BuildingWithAgentsSDK-LightMode-500px.svg?w=3840&q=90)

The harness also helps developers unlock more of a frontier model’s capability by aligning execution with the way those models perform best. That keeps agents closer to the model’s natural operating pattern, improving reliability and performance on complex tasks—particularly when work is long-running or coordinated across a diverse set of tools and systems.

In addition, we realize each product is unique and rarely fits neatly into a mold. We designed Agents SDK to support this diversity. Developers get a harness that’s turnkey yet flexible—making it easy to adapt it to their own stack—including tool use, memory, and sandbox environment. 

## Native sandbox execution

The updated Agents SDK supports sandbox execution natively, so agents can run in controlled computer environments with the files, tools, and dependencies they need for a task.

Many useful agents need a workspace where they can read and write files, install dependencies, run code, and use tools safely. Native sandbox support gives developers that execution layer out of the box, instead of forcing them to piece it together themselves.

Developers can bring their own sandbox or use built-in support for Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, and Vercel.

To make those environments portable across providers, the SDK also introduces a Manifest abstraction for describing the agent’s workspace. Developers can mount local files, define output directories, and bring in data from storage providers including AWS S3, Google Cloud Storage, Azure Blob Storage, and Cloudflare R2.

This gives developers a consistent way to shape the agent’s environment from local prototype to production deployment. It also gives the model a predictable workspace: where to find inputs, where to write outputs, and how to keep work organized across a long-running task.

![Logos for Daytona, E2B, Modal, Cloudflare, Vercel, Blaxel, Runloop](https://images.ctfassets.net/kftzwdyauwt9/1Q9fzbRG0Lsfv8neHtwibW/749d6c2f06610c5cd8a81f1824ce9d34/logos-light.png?w=3840&q=90&fm=webp)

## Separating harness from compute for security, durability, and scale

Agent systems should be designed assuming prompt-injection and exfiltration attempts. Separating harness and compute helps keep credentials out of environments where model-generated code executes.

It also enables durable execution. When the agent’s state is externalized, losing a sandbox container does not mean losing the run. With built-in snapshotting and rehydration, the Agents SDK can restore the agent’s state in a fresh container and continue from the last checkpoint if the original environment fails or expires. 

Finally, it makes agents more scalable. Agent runs can use one sandbox or many, invoke sandboxes only when needed, route subagents to isolated environments, and parallelize work across containers for faster execution.

![Flow diagram illustrating how the Agent SDK enables AI agents to use additional compute resources for more complex tasks.](https://images.ctfassets.net/kftzwdyauwt9/7B96BmwdCcPwlY5CfQT81V/b327a755f297609d1b37a57f83925ef1/AgentSDK_HarnessWithCompute-LightMode-500px.svg?w=3840&q=90)

![Diagram depicting how AI agents built with the Agent SDK can orchestrate separate compute systems, allowing workloads to run independently while supporting more advanced tasks.](https://images.ctfassets.net/kftzwdyauwt9/0CDmKna4q9MihFzOSA6x/1d84c545399ba4487a404beee8864ff3/AgentSDK_HarnessSeparate-LightMode-500px__1_.svg?w=3840&q=90)

## Pricing and availability

These new Agents SDK capabilities are generally available to all customers via the API and use standard API pricing, based on tokens and tool use.

## What’s next

As we continue to develop the Agents SDK, we’ll keep expanding what developers can build with it, making it easier to bring more capable agents into production with less custom infrastructure, while preserving the flexibility and control developers need to fit agents into their own environments.

The new harness and sandbox capabilities are launching first in Python, with TypeScript support planned for a future release. We’re also working to bring additional agent capabilities, including code mode and subagents, to both Python and TypeScript.

In addition, we want to help bring the broader agent ecosystem together over time, with support for more sandbox providers, more integrations, and more ways for developers to plug the SDK into the tools and systems they already use.

  * [2026](</news/?tags=2026>)
  * [API Platform](</news/?tags=api-platform>)



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

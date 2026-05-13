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

  * Controlling how Codex operates
  * Agent-native telemetry and audit trails
  * Looking ahead



May 8, 2026

[Security](</news/security/>)[Safety](</news/safety-alignment/>)

# Running Codex safely at OpenAI

A look at the controls, boundaries, and telemetry OpenAI uses to govern coding agents in real workflows.

Loading…

Share

As AI systems become more capable, they increasingly act on behalf of users. Coding agents can autonomously review repositories, run commands, and interact with development tools. These are tasks that previously required direct human execution.

With Codex, we’ve designed these capabilities alongside the controls organizations need for safe deployment. Security teams need ways to govern how agents operate: what they can access, when human approval is required, which systems they can interact with, and what telemetry exists to explain their behavior.

At OpenAI, we deploy Codex with a few clear goals: keep the agent inside clear technical boundaries, let developers move quickly on low-risk actions, and make higher-risk actions explicit. We also preserve agent-native telemetry so we can understand and audit what the agent did. In practice, that means managed configuration, constrained execution, network policies, and agent-native logs.

## Controlling how Codex operates

We deploy Codex with a simple principle that it should be productive inside a bounded environment, low-risk everyday actions should be frictionless, and higher-risk actions should stop for review.

#### Sandboxing and approvals

Approvals and sandboxing work together. The sandbox defines the technical execution boundary, including where Codex can write, whether it can reach the network, and which paths remain protected. Approval policy determines when Codex must ask to perform an action, such as when it needs to do something outside of the sandbox. Users can approve the action once, or approve that type of action for that session.

For requests that cross the sandbox boundary, we are using [_Auto-review mode_ ⁠(opens in a new window)](<https://alignment.openai.com/auto-review/>), which is a feature that, when turned on, auto-approves certain kinds of requests to reduce how often users have to stop and approve Codex actions. Codex sends the planned action and recent context to the auto-approval subagent, which can automatically approve low-risk actions—or high-risk actions with sufficient level of user authorization—instead of interrupting the user. That keeps Codex moving on routine work while still stopping on higher-risk or actions with unintended consequences.

#### TOML

`
    
    
    1
    
    # config.toml
    
    2
    
      
    
    
    3
    
    # Turn on auto_review
    
    4
    
    approvals_reviewer = "auto_review" 
    
    5
    
    # Add known development directories to the sandbox automatically
    
    6
    
    sandbox_workspace_write.writable_roots = ["~/development"] 
    
    7
    
      
    
    
    8
    
    # requirements.toml
    
    9
    
      
    
    
    10
    
    # Require Codex to operate inside the sandbox
    
    11
    
    allowed_sandbox_modes = ["read-only", "workspace-write"] 

`

#### Network access

We do not run Codex with open-ended outbound access. Our managed network policy allows expected destinations, blocks destinations we do not want Codex reaching, and requires approval for unfamiliar domains. That lets Codex complete common, known-good workflows without giving it broad network access.

#### TOML

`
    
    
    1
    
    # requirements.toml
    
    2
    
      
    
    
    3
    
    # Ensure web fetch only comes from OpenAI's cache
    
    4
    
    allowed_web_search_modes = ["cached"] 
    
    5
    
      
    
    
    6
    
    [experimental_network]
    
    7
    
    # Turn on Network Proxy
    
    8
    
    enabled = true
    
    9
    
    # Allow Codex to interact with localhost
    
    10
    
    allow_local_binding = true 
    
    11
    
    # Block all requests to this domain
    
    12
    
    denied_domains = ["pastebin.com"] 
    
    13
    
    # Auto-allow requests to these domains
    
    14
    
    allowed_domains = ["login.microsoftonline.com", "*.openai.com"]

`

#### Identity and credentials

We also manage how Codex authenticates. CLI and MCP OAuth credentials are stored in the secure OS keyring, login is forced through ChatGPT, and access is pinned to our ChatGPT enterprise workspace. That keeps Codex usage tied to our workspace-level controls and makes Codex activity available in the ChatGPT Compliance Logs Platform for our enterprise workspace.

#### TOML

`
    
    
    1
    
    # config.toml
    
    2
    
      
    
    
    3
    
    # Store CLI Auth Creds in OS Keychain
    
    4
    
    cli_auth_credentials_store = "keyring"           
    
    5
    
    # Store MCP Creds in OS Keychain
    
    6
    
    mcp_oauth_credentials_store = "keyring"          
    
    7
    
    # Require Auth via ChatGPT
    
    8
    
    forced_login_method = "chatgpt"                  
    
    9
    
    # Require Auth to Specific ChatGPT Workspace
    
    10
    
    forced_chatgpt_workspace_id = "<workspace-uuid>"

`

#### Rules

We use rules so Codex does not treat every shell command as equally safe. Common benign commands that engineers use in day-to-day development are allowed without approval outside of the sandbox and specific dangerous commands can be blocked or require approval. That lets Codex move quickly through ordinary engineering tasks while still forcing review or blocking patterns we do not want to run outside the sandbox.

#### Starlark

`
    
    
    1
    
    # default.rules
    
    2
    
      
    
    
    3
    
    prefix_rule(
    
    4
    
        pattern = ["gh", "pr", ["view", "list"]],
    
    5
    
        decision = "allow",
    
    6
    
        justification = "Allows read-only GitHub PR inspection via gh CLI.",
    
    7
    
    )
    
    8
    
    prefix_rule(
    
    9
    
        pattern = ["kubectl", ["get", "describe", "logs"]],
    
    10
    
        decision = "allow",
    
    11
    
        justification = "Allows Kubernetes resource inspection for debugging.",
    
    12
    
    )

`

#### Managed configs

We apply this posture through a combination of cloud-managed requirements, macOS managed preferences, and local requirements files. Requirements are admin-enforced controls that users cannot override. The macOS managed preferences and local requirements files allow us to keep a consistent baseline while still testing different configurations by team, user group, or environment. These configurations apply across local Codex surfaces, including the desktop app, CLI, and IDE extension.

## Agent-native telemetry and audit trails

Control is only half the job. Once agents are deployed, security teams need visibility into what these agents are doing and why. Traditional security logs are still useful when looking at actions taken by Codex, but they mostly answer what happened: a process started, a file changed, a network connection was attempted. Defenders are still left to figure out why Codex did something, or the user's intent.

Codex can give security teams a more agent-aware view. Codex supports OpenTelemetry log export for various Codex events such as user prompts, tool approval decisions, tool execution results, MCP server usage, and network proxy allow or deny events. Codex activity logs are also available through the OpenAI Compliance Platform for Enterprise and Edu customers.

#### TOML

`
    
    
    1
    
    # config.toml
    
    2
    
      
    
    
    3
    
    [otel]
    
    4
    
    log_user_prompt = true
    
    5
    
    environment = "prod"
    
    6
    
      
    
    
    7
    
    [otel.exporter.otlp-http]
    
    8
    
    endpoint = "http://localhost:14318/v1/logs"
    
    9
    
    protocol = "binary"

`

At OpenAI, we use Codex logs alongside our AI-powered security triage agent. When an endpoint alert says Codex did something unusual, the endpoint security tool tells us that a suspicious event occurred. Codex logs then help explain the surrounding intent by the user and agent. Our AI security triage agent uses Codex logs to inspect the original request, tool activity, approval decisions, tool results, and any relevant network policy decision or block. The AI security triage agent surfaces its analysis to our security team for review to distinguish between expected agent behavior, benign mistakes, and activity that truly warrants escalation.

We also use the same telemetry operationally. We use these logs to understand how internal adoption is changing, which tools and MCP servers are being used, how often the network sandbox is blocking or prompting, and where the rollout still needs tuning. These OpenTelemetry logs can be centralized in SIEM and compliance logging systems.

## Looking ahead

As coding agents like Codex become integrated into development workflows, security teams need tools specifically designed for managing this shift. Codex provides the control surfaces, configuration management, sandboxing, and detailed agent-aware telemetry needed to ensure safe adoption. With those capabilities in place, security teams can enable Codex with greater confidence, balancing developer productivity with the visibility and control required for enterprise security. More information on configuring Codex can be found [here⁠(opens in a new window)](<https://developers.openai.com/codex/config-basic>), and the Compliance API [here⁠(opens in a new window)](<https://help.openai.com/en/articles/9261474-openai-compliance-platform-for-enterprise-and-edu-customers>).

  * [2026](</news/?tags=2026>)
  * [Codex](</news/?tags=codex>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

![Scaling Trusted Access for Cyber with GPT-5.5 and GPT-5.5-Cyber > Art Card Image](https://images.ctfassets.net/kftzwdyauwt9/6BHwtZlzRX7xMewO3wnC7d/c0331749e9a30c4861e063cb082abb53/Frame__10_.png?w=3840&q=90&fm=webp)

[Scaling Trusted Access for Cyber with GPT-5.5 and GPT-5.5-CyberSecurityMay 7, 2026](</index/gpt-5-5-with-trusted-access-for-cyber/>)

![Introducing Trusted Contact in ChatGPT > Art Card](https://images.ctfassets.net/kftzwdyauwt9/6cEIQkxxIQawI5tRwAwHPF/1eb5d89a9841b26aa45a1a71b534c409/ArtCard-Trusted-Contact-1080x1080.png?w=3840&q=90&fm=webp)

[Introducing Trusted Contact in ChatGPTSafetyMay 7, 2026](</index/introducing-trusted-contact-in-chatgpt/>)

![System Card 1x1](https://images.ctfassets.net/kftzwdyauwt9/2VCkKLVmTyNs0XGbqdxGeA/33ff7738f4e795ae0ee41ed2b4a985d3/System_Card_1x1.jpg?w=3840&q=90&fm=webp)

[GPT-5.5 Instant System CardSafetyMay 5, 2026](</index/gpt-5-5-instant-system-card/>)

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

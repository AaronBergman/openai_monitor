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

December 8, 2022

[Company](</news/company-announcements/>)

# Discovering the minutiae of backend systems

![Person gazing across the room with an optimistic expression](https://images.ctfassets.net/kftzwdyauwt9/21098b49-868d-4515-ca433071d782/838b1914602aaba2e3d935b70d1fa11b/stangel-2022-0795.jpg?w=3840&q=90&fm=webp)

Photo: Jake Stangel

Loading…

Share

## What first interested you in engineering?

I was fortunate to discover programming at a young age and used that as a gateway to explore other topics. In middle school, a friend introduced me to the particular flavor of the BASIC programming language included with Texas Instruments calculators (my code was predictably unmaintainable given a restriction of 27 single-letter variables per program and a heavy reliance on GOTO statements). Nevertheless, we created some simple programs, like text-based adventure games, a chat app for linked calculators, and the usual quadratic formula aide.

Later on, I wrote more complicated programs: a visual helper for illustrating Newton’s method and an orbit calculator for estimating the position of the planets and their moons, which caught the eye of my school’s Linux club. Soon, I was tussling with NDISwrapper trying to get my laptop’s CardBus-based WiFi adapter working and setting my desktop windows ablaze with Compiz! That pattern of discovery via code continued throughout high school and beyond, resulting in my engineering interest today.

## What made you come to OpenAI?

At my last job, I’d moved from a backend role into a full-stack position, only to find a distaste for frontend work and UX design. I wanted to move back to a role closer to backend systems and missed the interaction with Linux environments I’d enjoyed in academia. OpenAI offered the change in work I was looking for and then some; you’d be hard-pressed to find a better fit for what I was looking for than working on OpenAI’s supercomputing clusters.

## What are the problems you’re focused on solving here at OpenAI?

Exploratory AI workflows are inherently fast-paced; researchers want to be able to take a preprint off of arXiv and test out new approaches without being encumbered by the platform they’re launching their code on. They are also incredibly complicated, with researchers behaving much like mathematicians—relying on the intuition they’ve built over their careers to design a solution in tackling whatever problem has caught their eye this week. The fact these runtimes are executing on some of the world’s largest supercomputers adds yet another layer of complexity, and handling that penultimate layer is where my team gets involved. We work to preempt research needs before they block progress and, failing that, we work with research teams to identify bottlenecks and implement workarounds as quickly as possible.

![Person sitting at a cafeteria table with a glass of water and closed laptop](https://images.ctfassets.net/kftzwdyauwt9/b51d3c96-482a-4528-1938ed2bf787/ecb2360e09408074fc318a07b360aa25/stangel-2022-0743.jpg?w=3840&q=90&fm=webp)

Photo: Jake Stangel

## What do you think differentiates working on supercomputing at OpenAI from another place?

The sheer scale we operate at is, frankly, astonishing. Third-party hardware vendors routinely confide that we’re encountering issues they’ve never previously seen. Often this is simply because our installations have more hardware shoved into a single contiguous supercomputer than their other clients, although occasionally it’s a consequence of our performance expectations. The synchronized nature of most model training approaches results in a configuration where the entire cluster effectively runs at the speed of the slowest node.

Our most prominent models are trained on billion-dollar supercomputers, and as a result, we end up chasing down performance degradations that most others would ignore. It’s exciting to see something like a one-line change hit the mainline kernel, knowing that it’ll save ~6 days of compute across our fleet per week, or see a line item on a new driver release, knowing that it was one of our discoveries that resulted in the now-upstreamed fix.

## What does a typical day at OpenAI look like for you?

My days generally consist of some mixture of working on code, investigating issues, and attending meetings. Meetings dominate my Tuesdays (and usually only Tuesdays, thankfully), and the remainder of the week is split between debugging and coding. Issues identified generally become coding work, e.g., writing up a design doc, pushing a quick hotfix to a PR branch, or adding passive health check logic to keep errant hardware out of our clusters.

Digging into the issues requires a bit of detective work. The research impact varies from the vague (“my job seems to be running slower than it was yesterday”) to the terrifyingly specific (“I think if I push more than 30Gbps over the Ethernet NIC, I cause a kernel panic?”). This is likely a familiar mix: productive on days that proceed as expected, and exciting when the expected is disrupted and you get the chance to learn something new.

> “OpenAI offers the opportunity to dig deep into aspects of computing ignored elsewhere.”

## What energizes you each day?

I rarely show up for work without having something top-of-mind that needs doing, and I’m generally aware of the specific team, project, and researchers that benefit from the timely completion of a task. OpenAI is the largest employer I’ve worked for and having an immediate appreciation of the impact of my work is crucial for my day-to-day motivation. I also get a kick out of discovering the minutiae of systems. OpenAI isn’t the first employer I’ve worked on backend systems for, but this is my first time working in the HPC space.

The technologies we work with often exist purely due to performance concerns bespoke to this space. I hadn’t needed to worry about the physical topology of our hardware at previous employers—ensuring that communication occurred within the same NUMA domain, for instance, or that a GPU utilized a co-located NVME or InfiniBand device via Nvidia’s GPUDirect, or that system processes were pinned to specific CPUs to avoid noisy neighbor conflicts with research runtimes. OpenAI offers the opportunity to dig deep into aspects of computing ignored elsewhere, which keeps me interested in the task at hand.

## Where do you find inspiration?

Nothing is as inspiring as watching our research teams make progress on improving their models. Many groups set up Slack bots or simple playgrounds where you can interact with and test models still under development, allowing you to watch the models improve as training continues!

I also use the popular :meow_party: Slackmoji to tag motivating or inspirational content from our various Slack channels. Since I joined in mid-2020, I have more than 400 :meow_party:-tagged posts, averaging close to 4 per week!

  * [View careers at OpenAI](</careers/>)



  * [API Platform](</news/?tags=api-platform>)
  * [Culture & Careers](</news/?tags=culture-careers>)
  * [2022](</news/?tags=2022>)



## Author

OpenAI

## Related articles

[View all](</news/>)

![city](https://images.ctfassets.net/kftzwdyauwt9/5Wm11GSMw6U7lLDKdcyuUY/3180687ca07ba934009f3c2b9219c10c/city.webp?w=3840&q=90&fm=webp)

[Introducing OpenAI LondonCompanyJun 28, 2023](</index/introducing-openai-london/>)

![Person sitting on a couch in front of a red coffee table in a plant-filled room](https://images.ctfassets.net/kftzwdyauwt9/e3357d5a-b177-4b3a-1edf79a7f2dc/ca1f3418cd72b4eb84c9d1a09dfffc7f/stangel-2022-0421.jpg?w=3840&q=90&fm=webp)

[The power of continuous learningCompanyDec 23, 2022](</index/the-power-of-continuous-learning/>)

![openai-residency](https://images.ctfassets.net/kftzwdyauwt9/3CWY2fzXldmJCJPs2UQU4m/e433068601b00f45980358b7d03a0524/openai-residency.jpg?w=3840&q=90&fm=webp)

[OpenAI ResidencyCompanyNov 30, 2021](</index/openai-residency/>)

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

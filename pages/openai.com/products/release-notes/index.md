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

# Release notes

Copy RSS feed URL

  * All
  * ChatGPT
  * Codex
  * API



Filter

Sort

API

Sep 3, 2026

GA

## Introducing GPT-6 Astra

Today we’re introducing GPT‑6 Astra, with improvements in coding, research, computer use, and complex, multi-step work. Astra can create documents, spreadsheets, and presentations that follow your templates and instructions, and adapt when you add requirements or change direction.

Access is rolling out to a limited set of organizations. Astra is not yet generally available. Broader availability is planned over the coming days.

Astra includes additional safety monitoring to look for cases where agents may not have interpreted your instructions correctly. If a potential case is detected, the conversation may be paused or stopped as a precaution for you to review and decide how to proceed.

gpt-6-astra  
v1/responses  
v1/chat/completions

Released GPT‑6 Astra, our most capable model, built for the hardest end-to-end work.

Use GPT‑6 Astra for reasoning, coding, computer use, research, and document creation. It combines these capabilities to carry complex tasks from an initial request to a finished result, using the context and tools you provide.

Key changes to consider when migrating:

  * GPT‑6 Astra does not support the `none` reasoning effort level.

  * GPT‑6 Astra does not support custom `temperature` or `top_p` values or log probabilities (`logprobs`).

  * Tool calling requires the Responses API. If you use tools with Chat Completions, follow the Responses migration guide.

  * Misalignment monitoring asynchronously checks for potential issues during agent work in supported Responses API requests. Checks can trigger safety alerts or stop a conversation for review.




v1/responses

Added new controls for long-running work with GPT‑6 Astra in the Responses API:

  * Async tool calling: Let the model continue working while your application runs function or custom tools, then return results as they become available.

  * Mid-turn steering: Send additional instructions while a response is in progress over WebSockets, so the model can incorporate corrections or changing requirements.

  * Change reasoning effort mid-conversation: Increase effort for difficult work or reduce it for routine follow-ups while preserving the cached prompt prefix.




[View source(opens in a new window)](<https://developers.openai.com/api/docs/models/gpt-6-astra>)[Help center(opens in a new window)](<https://help.openai.com/en/articles/6825453-chatgpt-release-notes#introducing-gpt-6-astra>)[Platform docs(opens in a new window)](<https://developers.openai.com/api/docs/changelog>)

ChatGPT

Sep 3, 2026

GA

## Share ChatGPT Sites with people outside your workspace

Eligible Site owners can now share a live ChatGPT Site with named people outside their workspace, without making the Site public. External viewers can use the shared Site but cannot edit or publish it.

To share, open the Site, select Share, enter the recipient’s email, and save their viewer access. The recipient signs in with the account that was granted access. You can review or remove viewers in the Site’s sharing controls.

ChatGPT Business Site owners can now share live Sites with named people outside their workspace. A viewer invitation provides access to the shared Site without adding the recipient to the Business workspace, granting editing access, or making the Site public.

Open the Site and select Share to add the recipient’s email as a viewer, then save the change. Recipients sign in with the account that received access - you can review or remove viewer access using the sharing controls. Workspace Sites settings still apply.

Eligible ChatGPT Enterprise workspaces can now let Site owners share live Sites with named external viewers. Recipients sign in with the account that was granted access and can view the shared Site without joining the workspace. Additionally, viewer access does not grant editing or publishing rights, or make the Site public.

Workspace owners and admins can allow invitations for selected roles in Workspace settings > Permissions & roles by enabling Sites and Allow members to invite external visitors to sites. This permission is separate from public publishing.

[View source(opens in a new window)](<https://help.openai.com/en/articles/6825453-chatgpt-release-notes#share-sites-with-people-outside-your-workspace>)[Help center(opens in a new window)](<https://help.openai.com/en/articles/11391654-chatgpt-business-release-notes#share-sites-with-people-outside-your-workspace>)[Help center(opens in a new window)](<https://help.openai.com/en/articles/10128477-chatgpt-enterprise-edu-release-notes#share-sites-with-people-outside-your-workspace>)

Codex

Sep 3, 2026

GA

## More control over browser and computer use

New policy settings give enterprise admins more control over how supported desktop clients use browsers and native apps. Admins can set website defaults and exceptions, restrict uploads, downloads, browser history and developer access, and control automatic review, saved approvals and how long site approvals last. Native-app rules can allow or block specific macOS and Windows apps. Admins can also restrict importing data from another browser.

Where the policy editor is available, open Codex Policies and Configurations and edit the policy’s Requirements. Controls apply on supported clients and platforms; allowing a site or app does not bypass other policies or approval prompts.

[View source(opens in a new window)](<https://help.openai.com/en/articles/10128477-chatgpt-enterprise-edu-release-notes#more-control-over-browser-and-computer-use>)[Platform docs(opens in a new window)](<https://learn.chatgpt.com/docs/enterprise/managed-configuration>)

ChatGPT

Sep 1, 2026

GA

## Healthcare plugins for ChatGPT and Codex

Eligible ChatGPT for Clinicians users in the United States can now use Healthcare Public Data in ChatGPT. Eligible ChatGPT for Healthcare and HIPAA-enabled ChatGPT Enterprise workspaces can use two healthcare plugins in ChatGPT and Codex:

  * Healthcare Public Data: Search nine public healthcare sources for medical research, clinical trials, medication information, Medicare data, and provider records. The plugin is read-only and does not access patient charts.

  * Epic: Review authorized patient information from your organization’s Epic electronic health record. Access is read-only and requires an administrator-configured Epic EHR app, an individual Epic sign-in, and existing patient-chart permissions.




To get started with Healthcare Public Data, install the plugin from the Plugin directory, then connect the apps you want to use. Admins manage plugin availability and app access separately. Do not include protected health information in searches sent to public sources. Before using Epic with protected health information, confirm your organization has an applicable Business Associate Agreement and an approved workspace configuration.

[View source(opens in a new window)](<https://help.openai.com/en/articles/6825453-chatgpt-release-notes#healthcare-public-data-in-chatgpt-for-clinicians>)[Help center(opens in a new window)](<https://help.openai.com/en/articles/10128477-chatgpt-enterprise-edu-release-notes#healthcare-plugins-for-chatgpt-and-codex>)[Help center(opens in a new window)](<https://help.openai.com/en/articles/20001489>)

Codex

Sep 1, 2026

GA

## ChatGPT for iOS updates: cross-host attachments, task priority, and reliability

### New features

  * Attachments now work across all connected hosts, including Windows and Linux, and support videos from the Photo Library.

  * Press and hold the attachment button to attach recent photos.

  * A new Priority view brings running tasks, unread updates, and tasks awaiting your response to the top of the task list.

  * Queued prompts now sync with the connected host, remain editable, and send even when the app is in the background.

  * Long-running tasks now show their live working time.

  * Task menus now include an option to copy the thread ID.




### Improvements and bug fixes

  * Task list loading and organization are faster and more reliable, with simpler date sections and fewer stalls or disappearing projects.

  * Reconnects are more reliable, resolving stuck Send states, missing approvals, and stale task updates.

  * Long responses now stream with fewer visual interruptions.

  * Side chat messages remain available until you close them, even after the chat can no longer reconnect.




[View source(opens in a new window)](<https://learn.chatgpt.com/docs/changelog#codex-2026-09-02-mobile>)

Load more

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

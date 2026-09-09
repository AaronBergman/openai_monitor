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

# Verify OpenAI-generated content

Upload an image or audio file to check for signals that it was generated with OpenAI tools.

Upload a fileDrag and drop or click to upload a file.Supported formats: PNG, JPG, WEBP, MP3, WAV, AAC, FLAC, OGG, OPUS, PCM

By uploading a file, you agree to our [Terms](</policies/terms-of-use/>) and have read our [Privacy Policy](</policies/privacy-policy/>).

#### What does this tool do?

This tool checks whether an uploaded file contains provenance signals associated with OpenAI tools. It looks for supported signals, including C2PA metadata and SynthID watermarks, and reports whether they are detected.

#### What content can it detect?

The tool is designed to detect content generated with ChatGPT, the OpenAI API, or Codex. It currently supports images and audio files. Other content can be uploaded, but OpenAI provenance signals will only be detected if it was generated with our tools.

#### How do I use it?

Upload a single file, then review the results to see whether the tool detects C2PA metadata, a SynthID watermark, or no supported signal.

## Verify content with the API

Integrate content verification into your products or workflows using the OpenAI API.

[View API documentation(opens in a new window)](<https://developers.openai.com/api/docs/guides/content-provenance>)

### FAQ

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

### Why does provenance matter to OpenAI?

Provenance helps people understand where online content came from and whether AI was involved in creating or editing it. This gives people more information when deciding what to trust, share, or report online.

It can help reduce confusion, deception, and cases where the origin of AI-generated content is unclear. It also gives journalists, platforms, creators, researchers, and the public more context about the media they encounter online.

We believe clearer information about how content was created is an important part of building a more trustworthy online environment.

### What supporting evidence does the tool use?

The tool relies on two types of signals: C2PA Content Credentials and SynthID.

[_Content Credentials_ ⁠(opens in a new window)](<https://c2pa.org/>) are based on an open standard that attaches provenance metadata to digital media. For supported OpenAI-generated content, they can indicate that a file was created using tools such as ChatGPT, Codex, or the API. They are a strong signal when present, but because they rely on metadata, they can be removed.

[_SynthID_ ⁠(opens in a new window)](<https://deepmind.google/models/synthid/>) is an invisible watermarking technology that embeds a signal directly into generated media. Unlike metadata, the signal is part of the content itself and is designed to stand up to modifications like cropping, adding filters, or lossy compression. For more technical details, see the [_SynthID research paper_ ⁠(opens in a new window)](<https://arxiv.org/abs/2510.09263>).

### What does a detected signal mean?

A detected signal indicates that the content likely originated from OpenAI tools. Detected signals are reliable, and false positives are rare.

It does not confirm how the content has been used or modified after it was created.

### Can the tool detect content modifications?

The tool detects content that was generated by our tools, which includes cases where a user asked for a modification of an uploaded file, and the model generated a new file that reflects the changes.

### Can this tool tell if content is inaccurate or misleading?

No, a detected signal indicates that the content originated from OpenAI tools, but it does not determine whether the content is accurate or presented in the correct context.

### What are best practices for using the tool?

For the most reliable results, upload a single file at a time.

For images, avoid cropping the image or converting it to another file format (for example, PDF). Upload only one image at a time.

For audio, upload clips between 10 and 60 seconds long for the best results.

### What if no signal is found?

If no signal is detected, it means the tool did not find supported signals in the uploaded file.

The content could still have been generated by OpenAI if its metadata was stripped or tampered with, its watermark was degraded, it came from a legacy generation model, or it was created before provenance signals were available. Content could also still be AI-generated by another company’s model, which the tool currently does not detect.

### I’m having trouble using the tool.

If the tool isn’t working, try again in a moment—some errors (like rate limits or temporary issues) can occur.

If the problem persists, visit our [Help Center⁠(opens in a new window)](<https://help.openai.com/en>) for support.

### What happens to the file I upload?

The uploaded file is processed to check for supported provenance signals associated with OpenAI-generated content. Uploaded files are not stored unless legally required and are not used to train our models.

### What terms apply when I use the tool?

By using this tool, you agree to the [OpenAI Terms of Use](</policies/terms-of-use/>).

### I’m a developer—can I verify content through an API?

Yes. Developers can use the OpenAI API to verify content programmatically. See the [API documentation⁠(opens in a new window)](<https://developers.openai.com/api/docs/guides/content-provenance>) to learn how to get started.

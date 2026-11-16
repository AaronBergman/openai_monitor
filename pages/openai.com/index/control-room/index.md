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

# Control Room

Share

How it works

  * How it works

  * Example: reacting to a monitoring alert

  * Speed and reliability




  * How it works

  * Example: reacting to a monitoring alert

  * Speed and reliability




As our models get more powerful and the associated safety and security risks become bigger, it becomes more and more critical that we can detect potential issues, and quickly stop models in their tracks when needed. To solve this, we built Control Room.

Control Room is a central system to track model workloads across our research infrastructure and stop them quickly when safety or security concerns arise. It connects every research inference workload, including agentic sampling for model training and evaluation, data processing, and more. This works together with our [_misalignment monitoring systems_](</index/how-we-detect-frontier-model-misalignment/>) , and halts model output within 35 seconds of a decision to intervene to stop or pause a job. It has been built to keep working even when other systems fail, and to stop model output if Control Room itself goes down.

Control Room is already deployed across our research infrastructure, where the need is greatest. Our external model-serving stack is already much more centralized by nature, with a well-developed operational capability to quickly take down model deployments if needed.

## How it works

Control Room works by integrating a few systems: the _workload_ , the _inference engine_ , and the centralized _Control Room service_.

  * The _workload_ is the job being run, such as a reinforcement learning experiment, an evaluation, a high-volume sampling or data processing job. We require every research workload that does agentic inference to be associated with an approved [_safety case_](</index/towards-safety-cases-for-frontier-ai-training/>).

  * The _inference engine_ , or just _engine_ , is the model itself. You can think of the engine as the brain of the model, running directly on GPUs. A workload normally uses one or more models, which might be running on one or more different inference engines. The same inference engine might be used by more than one different workload.

  * _The Control Room service_ tracks jobs and controls whether they are allowed to continue generating model output. Engines check with the Control Room service before fulfilling a request. If a job has been stopped, the service denies the request, preventing further output.




Control Room is integrated in the following way: 

  * When starting a new job, the workload code requests a new job_id from Control Room.

  * Whenever the workload needs to sample tokens from a model, it makes a request to an inference engine running that model, passing the job_id. The engine requests permission from Control Room to fulfill that request, passing the job_id along to Control Room.

  * Control Room checks whether that job has been terminated, and if so, it denies the inference request. The engine responds to the workload's inference request with a refusal, stopping further model output from being produced for that job.




## How Control Room works

Researcher

Something triggers a decision to stop the job

### Research job

`<No job ID yet>job_042`

### Inference engine

Runs the model on GPUs

### Control Room

  * job_039, active`job_039` __
  * job_040, active`job_040` __
  * job_041, active`job_041` __
  * job_042, active`job_042` __



STEP 1

### A researcher decides to start a job

The process starts with a researcher launching a job—for example, an experiment or an evaluation.

### The job starts up

Job code (or workload code) is owned and run by researchers. Inference engines might be started as part of this job, or standalone engines which are not associated with any particular job might already be running.

### The job registers with Control Room

The workload code requests a job ID, associating the job with an approved safety case. The job itself makes this request.

### Control Room returns a job ID

Control Room records the job and returns its identifier. The workload will attach this same ID to its inference requests.

### The job requests model output from an inference engine

The request includes the `job_id`. This request is made directly from the workload code and does not pass through Control Room.

### The engine checks permission

Before fulfilling the request, the inference engine asks Control Room whether this job is still authorized to run.

### Control Room allows the request

The job is still authorized, so Control Room grants permission. The inference engine can now fulfill the request.

### The engine returns model output

The model generates a response and the engine sends it back to the research job. The job can use that output and continue its work.

### Something triggers a decision to stop the job

A person or monitoring system tells Control Room to stop this job. Control Room marks its ID as stopped. The workload code remains running.

### The job can still try to sample model output

We do not rely on the workload code to correctly perform a check of whether or not the job is still running.

### The engine checks permission again

The engine asks Control Room for permission to fulfill the new inference request, passing along the same job ID.

### The next authorization is denied

When the engine checks permission again, Control Room denies the stopped job. The engine must refuse the inference request.

### Model output stops—the job stays

The engine returns a refusal instead of model output. The research process may remain alive, and the engine remains available to other authorized jobs.

01 / 13

BackNext

## Example: reacting to a monitoring alert

All of our frontier reinforcement learning jobs run with a monitor. A _monitor_ is another model which inspects everything that the model-being-trained is doing, and raises an alert if it detects a problem. For example, our recent [_DNS-related incident_ ⁠(opens in a new window)](<https://alignment.openai.com/misalignment-reports/an-agent-used-dns-to-reach-an-external-chatbot/>) was caught by a monitor.

Control Room and our monitoring system are integrated in the following way:

  * If the monitoring system detects a potential issue, depending on the details and severity, the monitoring system may decide to stop the job.

  * In this case, the monitoring system sends a message to Control Room to stop the job, passing the job_id. Control Room records that the job is terminated.

  * Next time the job having that job_id makes an inference request to sample more tokens from _any_ model running on _any_ engine, the request will be denied, stopping further model output.




## Speed and reliability

The maximum time between the moment when Control Room receives an instruction to stop a job, and the moment when further progress is no longer possible, is 35 seconds. The 35-second lag comes from a caching layer for inference authorization, to support the required volume of traffic. We are working to drive this number down to zero so that we can end jobs instantly.

Workloads, including experiments, evaluation jobs, etc., are normally owned and operated by researchers or teams of researchers. As a result, workload code changes often, and is not an ideal place to implement critical load-bearing safety protections. Because of this, our implementation is designed to be resilient to buggy or broken workload code.

We achieve this by implementing the termination mechanism in the inference layer. Workload code is highly-varied and decentralized. In contrast, there are only a very small number of inference code paths in use across all of OpenAI research, and their deployments are much more centralized and uniform. This means that the inference layer can serve as a bottleneck, where we can get strong guarantees that all model inference running in research is subject to Control Room authorization checks on every inference request. We additionally run continual agentic and programmatic sweeps to check that users are not accidentally or maliciously launching rogue engine implementations with Control Room unimplemented or disabled.

Finally, our system “fails closed”, meaning that the Control Room integration in the engines is configured in such a way that if the Control Room service goes down, either due to a system error or because it is disabled for any other reason, including tampering by a bad actor, then all inference requests will be denied until Control Room resumes normal operation. Fail-closed is rolled out now to all frontier model research workloads, and will finish rolling out across all remaining research workloads over the next few days.

* * *

Control Room is just one part of our holistic approach to safe frontier model training and deployment. We’ll continue to strengthen and expand the system over the coming months, alongside our investments in monitoring for misaligned behavior and security breaches. If you want to help build systems for the safe and secure development and deployment of AGI, [_we 're_⁠](<https://openai.com/careers/research-engineer-research-scientist-ai-systems-engineer-rsi-san-francisco/>) [_hiring_ ⁠](<https://openai.com/careers/researcher-agent-safety-oversight-and-system-mitigations-san-francisco/>)!

  * [Alignment](</news/?tags=alignment>)
  * [2026](</news/?tags=2026>)
  * [Cybersecurity](</news/?tags=cybersecurity>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

![How we detect frontier model misalignment — Cover](https://images.ctfassets.net/kftzwdyauwt9/43ZavE2amLHMmbxH8EL8VM/1464d0f68c0f3c45e9d255992aab32b1/how-we-detect-frontier-model-misalignment-cover.png?w=3840&q=90&fm=webp)

[How we detect frontier model misalignmentSecurityOct 29, 2026](</index/how-we-detect-frontier-model-misalignment/>)

![Safety cases for frontier AI training > Card image](https://images.ctfassets.net/kftzwdyauwt9/1XyYuz1U7KqnQDU3dz8Ig9/aea6b4ea875a8dd7ee89e57cd9c3caef/safetfy-cases-for-frontier-ai-training-cover.png?w=3840&q=90&fm=webp)

[Towards safety cases for frontier AI trainingSafetySep 28, 2026](</index/towards-safety-cases-for-frontier-ai-training/>)

[The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)

Research

  * [Research Index](</research/index/>)
  * [Research Overview](</research/>)
  * [Economic Research](</signals/>)



Latest Advancements

  * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  * [GPT-6 Astra](</index/gpt-6-astra/>)
  * [GPT-5.6](</index/gpt-5-6/>)
  * [GPT-5.5](</index/introducing-gpt-5-5/>)



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
  * [Codex](<https://chatgpt.com/codex/>)
  * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  * [Release Notes](</products/release-notes/>)



API Platform

  * [Overview](</api/>)
  * [API Log In(opens in a new window)](<https://platform.openai.com/login>)
  * [Docs(opens in a new window)](<https://developers.openai.com/api/docs>)



Business

  * [Overview](</business/>)
  * [Solutions](</solutions/>)
  * [Resources](</business/learn/>)
  * [Plugins](</business/plugins/>)
  * [Customer Stories](</business/customer-stories/>)
  * [Partner Network](</business/partners/>)
  * [Contact Sales](</contact-sales/>)



Developers

  * [Plugins(opens in a new window)](<https://developers.openai.com/plugins>)
  * [Models(opens in a new window)](<https://developers.openai.com/api/docs/models>)
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
  * [OpenAI Status(opens in a new window)](<https://status.openai.com>)



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

# Research on Generative AI Applications

Course: Generative AI for Software Development — introductory practical task  
Research date: 9 November 2026

## Scope and method

This report examines five practical applications of generative AI (GenAI). Each case describes business value, technical challenges, weak points, and two existing implementations linked to official product documentation. Product capabilities are based on those sources; the proposed business benefits, risks, and evaluation measures are qualitative engineering assessments, not independently measured results. No paid product trials or performance benchmarks were conducted. The report and vocabulary were drafted with AI assistance and are not presented as manually authored work.

## 1. Software development assistance

A developer can give a large language model (LLM) a prompt containing a requirement, relevant source code, and project conventions. The assistant can propose an implementation, explain unfamiliar code, draft unit tests, or suggest a refactoring. An AI agent can also call tools to inspect files and run tests within an approved environment. The business value is less time spent on repetitive implementation and a shorter path from a requirement to a reviewable change. Useful measures include time to an accepted change, reviewer effort, and defects discovered after merging; generating more code alone does not establish productivity.

Technical challenges include selecting useful context within the context window, understanding project dependencies, and integrating tool calling with the development environment. Weak points include hallucination of nonexistent APIs, insecure code, and tests that repeat an implementation's mistakes. A passing test suite does not establish that the original requirement was met. Engineers should review diffs, run appropriate tests, and restrict tool permissions. Human-in-the-loop approval is particularly useful before deployment or destructive commands. Token consumption and latency also affect whether an assistant is economical for a small task.

Existing implementations:

- [GitHub Copilot](https://docs.github.com/en/copilot/get-started/about-github-copilot) — provides AI assistance for software development, including code suggestions and conversational help.
- [Amazon Q Developer](https://aws.amazon.com/q/developer/features/) — helps with code generation, explanation, refactoring, testing, and other development tasks using project context.

## 2. Question answering over organizational documents

An employee can ask a question about internal procedures or technical documentation and receive a synthesized answer with references. In a retrieval-augmented generation (RAG) design, a retrieval component finds relevant passages and supplies them to an LLM rather than expecting the model to remember private documents. Documents may be divided through chunking, represented by embeddings, and searched through a vector database, often alongside keyword search. Business value includes faster onboarding, less repeated questioning, and less time searching across multiple systems. A useful pilot measures answer correctness, source support, and the time employees need to find a verified answer.

Technical challenges include document ingestion, retrieving the right passages, updating indexes, and enforcing access control before private content reaches the model. Grounding can improve answer relevance, but irrelevant retrieval or outdated source material can still produce a confident error. Citations must be checked: a linked document may not support the specific claim. Prompt injection inside retrieved documents is another weakness, because source text can contain instructions intended to redirect the assistant. Source-based evaluation should include unanswerable questions and attempts to obtain documents that the user is not permitted to read.

Existing implementations:

- [Google NotebookLM](https://blog.google/innovation-and-ai/products/notebooklm-goes-global-support-for-websites-slides-fact-check/) — supports questions over supplied sources and inline citations that lead to supporting passages.
- [Glean Assistant](https://docs.glean.com/get-started/golive/setup-glean-assistant) — provides an enterprise assistant based on organizational information while respecting data access permissions.

## 3. Customer support and service automation

A customer support assistant can interpret a customer's question and generate a reply using approved help articles. An AI agent may also use an API to retrieve order information or initiate an approved workflow. Business value comes from handling common questions outside working hours, reducing repetitive support work, and giving human specialists more time for difficult cases. Success should be measured through verified resolutions, repeat contacts, customer satisfaction, and the quality of escalation, rather than the number of automated replies.

Technical challenges include reliable retrieval, multilingual questions, authentication, and safe integration with customer systems. Weak points include invented refund policies, exposure of personal information, and unauthorized actions triggered by prompt injection. Grounding in approved policies helps but does not eliminate hallucination. Access control should be enforced by the application, and important actions should require human-in-the-loop approval. The system also needs a clear handoff when information is missing. Evaluation should test misleading questions, contradictory policies, and cases where the correct response is to escalate. Latency and token costs matter at high conversation volumes.

Existing implementations:

- [Intercom Fin AI Agent](https://www.intercom.com/help/en/articles/7120684-fin-ai-agent-explained) — answers customer questions using configured support content and service workflows.
- [Zendesk AI agents](https://support.zendesk.com/hc/en-us/articles/8724978128282-Getting-started-with-AI-agents-for-customer-service) — generate responses from trusted knowledge sources within customer service workflows.

## 4. Marketing images and design exploration

A design team can use a text prompt and reference images to produce concept art, campaign illustrations, or variations of a visual. Text-to-image generation gives a team several alternatives before it invests in detailed production. Multimodal systems may accept both text and images to guide the result. The business value is faster concept exploration and cheaper iteration on early drafts; it does not automatically eliminate the need for a designer. Useful measures include the proportion of drafts accepted by reviewers, time to an approved asset, and the amount of manual editing required.

Technical challenges include following detailed constraints, maintaining a consistent brand or character, and producing suitable dimensions and layouts. Weak points include malformed objects, misleading depictions, inconsistent versions, and poor rendering of exact text. Results may also require review for rights, permitted use, and resemblance to existing work; a generated asset is not automatically suitable for commercial publication. Human-in-the-loop review should check visual quality and brand suitability before release. Evaluation should compare several attempts because one successful sample does not demonstrate repeatability, and generation costs increase when many attempts are rejected.

Existing implementations:

- [Adobe Firefly](https://helpx.adobe.com/ca/legal/product-descriptions/adobe-firefly.html) — offers generative media capabilities, including image creation and editing from prompts.
- [Canva Magic Media](https://www.canva.com/help/using-magic-media/) — creates visual media from prompts within Canva's design workflow.

## 5. Meeting summaries and follow-up drafts

A meeting assistant can convert speech to a transcript, then use an LLM to produce a summary, decisions, and action items. This is a multimodal workflow when audio processing and text generation are combined; speech recognition itself is only one part of the application. Business value includes reducing time spent writing notes and helping absent participants catch up. Useful outputs separate confirmed decisions from proposals and attach evidence or timestamps where available. A pilot can measure corrections per summary, missed decisions, and time saved after participants review the notes.

Technical challenges include background noise, overlapping speakers, speaker attribution, domain terminology, and long conversations that exceed a context window. Weak points include assigning a task to the wrong person, removing an important qualification, or inventing a deadline. The system should mark an unstated owner or date as unknown instead of filling it in. Recording also requires appropriate participant permission and careful access control. Human-in-the-loop confirmation is useful before notes become official commitments or tasks are sent to other systems through an API. Evaluation should compare summaries with the recording and verify both omissions and unsupported additions.

Existing implementations:

- [Otter.ai](https://help.otter.ai/hc/en-us/articles/17333080149911-Copy-summary-overview-action-items-outline-insights) — produces AI-generated conversation summaries containing sections such as overviews and action items.
- [Fireflies.ai](https://guide.fireflies.ai/articles/1193528158-what-is-fireflies-ai) — captures and transcribes meetings, then generates summaries and action items.

## Cross-case conclusions

The strongest starting applications have a bounded task, relevant input data, observable output quality, and an affordable verification step. A useful prototype should be compared with the current human or software workflow rather than judged by how impressive its first answer sounds. Deployment decisions should consider output quality, operating cost, latency, privacy, and the consequences of an error together.

The linked pages establish that implementations exist and describe their advertised capabilities; they do not independently prove business return or accuracy. Features and availability can change. For this introductory research, source review is the evidence gathered; organizational pilots and measured evaluation remain future work.

# Research on Generative AI Applications

Course: Generative AI for Software Development - introductory practical task
Research date: 9 November 2026

## Scope and method

This report covers five applications of generative AI (GenAI), with two existing products for each case. I used official product documentation to check their capabilities. The benefits and risks below are my assessment of the use cases, not measured results from product trials.

## 1. Software development assistance

A developer can give a large language model (LLM) a prompt with a requirement, relevant source code, and project conventions. The assistant can propose an implementation, explain unfamiliar code, draft unit tests, or suggest a refactoring. An AI agent can also call tools to inspect files and run tests. This can reduce repetitive work and speed up the first draft of a change. Useful measures include time to an accepted change, reviewer effort, and defects discovered after merging.

The assistant needs useful context within the context window, accurate dependency information, and tool calling integrated with the development environment. Problems include hallucination of nonexistent APIs, insecure code, and tests that repeat an implementation's mistakes. Engineers still need to review diffs, run appropriate tests, and restrict tool permissions. Human-in-the-loop approval is useful before deployment or destructive commands. Token consumption and latency also affect the cost of a task.

Existing implementations:

- [GitHub Copilot](https://docs.github.com/en/copilot/get-started/about-github-copilot) - provides AI assistance for software development, including code suggestions and conversational help.
- [Amazon Q Developer](https://aws.amazon.com/q/developer/features/) - helps with code generation, explanation, refactoring, testing, and other development tasks using project context.

## 2. Question answering over organizational documents

An employee can ask a question about internal procedures or technical documentation and receive a synthesized answer with references. In retrieval-augmented generation (RAG), a retrieval component finds relevant passages and supplies them to an LLM. Documents may be prepared through chunking, represented by embeddings, and searched through a vector database, often alongside keyword search. This can shorten onboarding and reduce repeated questions to colleagues. A useful pilot measures answer correctness, source support, and the time needed to find a verified answer.

The difficult parts are importing documents, retrieving the right passages, updating indexes, and enforcing access control before private content reaches the model. Grounding helps, but poor retrieval or outdated documents can still produce a confident error. Citations must be checked against the actual claim. Prompt injection inside retrieved documents can also redirect the assistant. Evaluation should include questions with no answer in the sources and requests for documents the user is not allowed to read.

Existing implementations:

- [Google NotebookLM](https://blog.google/innovation-and-ai/products/notebooklm-goes-global-support-for-websites-slides-fact-check/) - supports questions over supplied sources and inline citations that lead to supporting passages.
- [Glean Assistant](https://docs.glean.com/get-started/golive/setup-glean-assistant) - provides an enterprise assistant based on organizational information while respecting data access permissions.

## 3. Customer support and service automation

A support assistant can interpret a customer's question and generate a reply using approved help articles. An AI agent may use an API to retrieve order information or start a service workflow. It can handle common questions outside working hours and leave more time for difficult cases. Success should be measured through resolved issues, repeat contacts, customer satisfaction, and the quality of handoff to a person.

This requires reliable retrieval, support for different languages, authentication, and integration with customer systems. Risks include invented refund policies, exposure of personal information, and unauthorized actions triggered by prompt injection. Grounding in approved policies reduces some errors but does not eliminate hallucination. The application must enforce access control, with human-in-the-loop approval for important actions. Evaluation should test misleading questions, contradictory policies, and cases that need a human specialist. Latency and token costs matter at high conversation volumes.

Existing implementations:

- [Intercom Fin AI Agent](https://www.intercom.com/help/en/articles/7120684-fin-ai-agent-explained) - answers customer questions using configured support content and service workflows.
- [Zendesk AI agents](https://support.zendesk.com/hc/en-us/articles/8724978128282-Getting-started-with-AI-agents-for-customer-service) - generate responses from trusted knowledge sources within customer service workflows.

## 4. Marketing images and design exploration

A design team can use a text prompt and reference images to produce concept art, campaign illustrations, or variations of a visual. Multimodal systems can use both text and images as input. This gives the team several options before detailed production begins, reducing time spent on early drafts. Useful measures include drafts accepted by reviewers, time to an approved asset, and the amount of manual editing required.

It can be difficult to follow detailed constraints, keep a character or brand consistent, and produce the right layout. Common problems include malformed objects and poor rendering of exact text. A reviewer should also check whether a generated asset is suitable for the intended use and resembles existing work. Human-in-the-loop review covers visual quality and brand requirements. Evaluation should compare several attempts, since repeated failures increase both editing time and generation costs.

Existing implementations:

- [Adobe Firefly](https://helpx.adobe.com/ca/legal/product-descriptions/adobe-firefly.html) - offers generative media capabilities, including image creation and editing from prompts.
- [Canva Magic Media](https://www.canva.com/help/using-magic-media/) - creates visual media from prompts within Canva's design workflow.

## 5. Meeting summaries and follow-up drafts

A meeting assistant can transcribe speech and use an LLM to produce a summary, decisions, and action items. This is a multimodal workflow combining audio processing and text generation. It can reduce note-taking work and help absent participants catch up. Useful notes separate decisions from proposals and attach evidence or timestamps. A pilot can measure corrections, missed decisions, and time saved after participants review the notes.

Background noise, overlapping speakers, technical terms, and long conversations that exceed a context window all make the task harder. Errors include assigning work to the wrong person, losing an important qualification, or inventing a deadline. An unstated owner or date should remain unknown. Recording requires appropriate participant permission and access control. Human-in-the-loop confirmation is useful before notes become commitments or tasks are sent to other systems through an API. Evaluation should compare summaries with the recording and check for missing or invented details.

Existing implementations:

- [Otter.ai](https://help.otter.ai/hc/en-us/articles/17333080149911-Copy-summary-overview-action-items-outline-insights) - produces AI-generated conversation summaries containing sections such as overviews and action items.
- [Fireflies.ai](https://guide.fireflies.ai/articles/1193528158-what-is-fireflies-ai) - captures and transcribes meetings, then generates summaries and action items.

## Cross-case conclusions

A sensible first use case has a clear task, relevant data, and a practical way to check the result. Before adopting a tool, compare it with the current workflow using output quality, cost, latency, and the effort needed to correct mistakes. Product documentation describes capabilities; a pilot is still needed to establish whether the tool helps a particular team.

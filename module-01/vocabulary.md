# Generative AI Vocabulary

These 20 terms appear in [the research report](research.md). I explained Prompt, Token, Hallucination, RAG, and AI agent in Russian using my own wording. Those five definitions were edited for clarity.

| Term | Plain-language explanation | Usage in the report |
| --- | --- | --- |
| Generative AI (GenAI) | AI that produces content, such as text, code, or images, from patterns learned during training and the input it receives. | All five applications produce new content. |
| Large language model (LLM) | A model trained to process language sequences and generate likely continuations; its fluent output is not a guarantee of truth. | Code assistance, document answers, customer replies, and summaries. |
| Prompt | По сути, инструкция для ИИ: ты объясняешь, что хочешь получить и в каком формате. Чем точнее промпт, тем обычно полезнее результат. | A development requirement or an image description. |
| Token | Условная единица, на которую ИИ разбивает текст для обработки. Это может быть слово, часть слова или символ. | Context limits and operating costs. |
| Context window | The maximum amount of model input and generated output that can fit in a single interaction, measured in tokens. | Selecting source code and processing long meetings. |
| Hallucination | Когда ИИ уверенно выдаёт неправильную или выдуманную информацию. Звучит убедительно, но по факту ответ может быть неверным. | Invented APIs, policies, or meeting deadlines. |
| Retrieval-augmented generation (RAG) | Перед ответом система ищет информацию во внешней базе знаний или документах и передаёт её ИИ. Так ответ может опираться на конкретные материалы, а не только на то, чему модель обучили. | Answering questions over organizational documents. |
| Retrieval | Selecting information from a collection that is relevant to a query. | Finding document passages or approved help articles. |
| Chunking | Splitting a larger document into smaller pieces that can be indexed and supplied to a model. | Preparing organizational documents for search. |
| Embedding | A numerical representation of content that can help compare its meaning with other content. | Matching a question with relevant passages. |
| Vector database | A storage and search system that can retrieve numerical vectors, including embeddings, by similarity. | One possible component of document search. |
| Grounding | Connecting an answer to supplied evidence or an external source instead of relying only on learned patterns. | Document answers and customer support policies. |
| AI agent | Система, которая может выполнять задачи: планировать действия, использовать инструменты, искать информацию и взаимодействовать с другими сервисами. Степень самостоятельности зависит от настроек и выданных разрешений. | Inspecting code, running tests, or handling support workflows. |
| Tool calling | A model requesting that an application run an external function and return its result. | Reading files, running tests, or accessing an order system. |
| Application programming interface (API) | A defined interface through which one software component requests information or actions from another. | Development libraries and integrations with customer or task systems. |
| Multimodal | Able to use or generate more than one type of data, such as text, images, and audio. | Image generation with references and meeting assistants. |
| Prompt injection | An attempt to make a model follow unwanted instructions embedded in input or retrieved material. | Malicious documents or customer messages. |
| Human-in-the-loop | A workflow where a person reviews, corrects, or approves important AI-assisted steps. | Reviewing code, customer actions, images, and meeting notes. |
| Evaluation | Checking a system's outputs against defined criteria and representative examples. | Measuring correctness, omissions, safety, and usefulness. |
| Latency | The time between a request and a usable response. | Assessing responsiveness and business practicality. |

## A few useful distinctions

- RAG is a workflow combining retrieval and generation; it does not require retraining the model, and it does not guarantee correctness.
- An API is an interface; tool calling is how a model-driven application may request use of that interface.
- Access control must be enforced by software around the model; asking the model to keep a secret is not sufficient.
- A citation makes a claim easier to verify, but someone still needs to check whether the source supports the claim.

# rag-under-the-hood

[![Sponsor hasff](https://img.shields.io/badge/Sponsor-hasff-brightgreen?logo=github-sponsors)](https://github.com/sponsors/hasff)
[![Portfolio](https://img.shields.io/badge/Portfolio-AI%2FML%20Projects-blue?logo=github)](https://hasff.github.io/my-ai-portfolio/)

> A practical, side by side comparison of the basic RAG building blocks (chunking, embeddings, vector store, retrieval) implemented with LangChain and with LlamaIndex.

> 💾 If this project looks useful, starring it now means you won't lose it later.

🗓️ **Status: August 2026**

---

## Picture this

You want to try RAG, but you don't want to fight with PDFs or scraping just to get started.

So you grab a Wikipedia page about Mars, split it into chunks, embed it, index it, and ask a simple question like *"What is the atmosphere of Mars made of?"*.

Then you do the exact same thing again, this time with a different framework, and compare what comes back.

That's this whole project. Same data, same question, two frameworks, side by side.

This is also a companion piece to my [legal-doc-rag-summarizer](https://github.com/hasff/legal-doc-rag-summarizer) project, where every RAG step (chunking, embeddings, vector search, BM25, hybrid retrieval) is built manually, from scratch. Here, the same steps are handed off to LangChain and LlamaIndex, so you can see what a framework does for you versus what you'd otherwise build yourself.

![LangChain vs LlamaIndex example in action](assets/intro/screenshot_intro.png)
*A quick look at both scripts answering the same question about Mars.*

---

⚠️ **Heads up**

This is a personal learning project, not an official resource.
It may contain errors, simplifications, or opinionated choices made for clarity over correctness.

Before you dive in, keep a few things in mind:
1. The AI/RAG landscape moves fast; library and API names may change.
2. Not production ready code. Built to learn and to teach.
3. This README was written with AI assistance, mainly for text refinement. The architecture, code, and technical decisions are my own.

---

## Key Concepts Demonstrated

✅ Data loading (Wikipedia)
<br>✅ Text chunking
<br>✅ Embeddings with OpenAI
<br>✅ In memory vector store
<br>✅ Query and similarity search
<br>✅ Direct comparison between both frameworks - 🔗 LangChain vs 🦙 LlamaIndex

<a name="table-of-contents_"></a>

---

## Table of Contents

- [Purpose](#purpose_)
- [Project Architecture](#project-architecture_)
- [Requirements](#requirements_)
- [Setup](#setup_)
- [Project Structure](#project-structure_)
- [`example_langchain.py`](#example-langchain_)
- [`example_llamaindex.py`](#example-llamaindex_)
- [LangChain vs LlamaIndex comparison](#langchain-vs-llamaindex_)
- [Conclusions](#conclusions_)
- [Next Steps & Resources](#next-steps--resources_)
- [Get in Touch](#get-in-touch_)

<a name="purpose_"></a>

---

## Purpose

#### ⚡ Quick Navigation: [⬅️ Table of Contents](#table-of-contents_) | [Project Architecture ➡️](#project-architecture_)

This is a simple example, not a full framework tutorial. The goal is narrow on purpose: run the same five step RAG flow (load, chunk, embed, store, query) once in LangChain and once in LlamaIndex, using the same data source and the same question, and let the code speak for itself.
 
It's a companion piece to [legal-doc-rag-summarizer](https://github.com/hasff/legal-doc-rag-summarizer), where every RAG step is built manually, from scratch. Here, those same steps are handed off to a framework, so you can compare "build it yourself" against "let the framework do it" and see where each library's abstractions actually help.


[↑ Back to Table of Contents](#table-of-contents_)

<a name="project-architecture_"></a>

---

## Project Architecture

#### ⚡ Quick Navigation: [⬅️ Purpose](#purpose_) | [Requirements ➡️](#requirements_)

TODO: describe the flow shared by both scripts.

1. Load: fetch a Wikipedia page (`Mars`) via `wikipedia`.
2. Chunk: split the text (`chunk_size=800`, `chunk_overlap=100`).
3. Embed: generate embeddings with OpenAI.
4. Store: save into an in memory vector store.
5. Query: run the same question against both systems and compare the results.

[↑ Back to Table of Contents](#table-of-contents_)

<a name="requirements_"></a>

---

## Requirements

#### ⚡ Quick Navigation: [⬅️ Project Architecture](#project-architecture_) | [Setup ➡️](#setup_)

TODO: confirm versions.

* Python 3.10+
* OpenAI API key → [platform.openai.com](https://platform.openai.com/home)

[↑ Back to Table of Contents](#table-of-contents_)

<a name="setup_"></a>

---

## Setup

#### ⚡ Quick Navigation: [⬅️ Requirements](#requirements_) | [Project Structure ➡️](#project-structure_)

TODO: adapt from the other README (clone, venv, install, `.env`).

```bash
pip install -r requirements.txt
```

```
OPENAI_API_KEY="your_key_here"
```


[↑ Back to Table of Contents](#table-of-contents_)

<a name="project-structure_"></a>

---

## Project structure

#### ⚡ Quick Navigation: [⬅️ Setup](#setup_) | [`example_langchain.py` ➡️](#example-langchain_)

```
langchain-vs-llamaindex-rag-basics/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── example_langchain.py
└── example_llamaindex.py
```

[↑ Back to Table of Contents](#table-of-contents_)

<a name="example-langchain_"></a>

---

## `example_langchain.py`

#### ⚡ Quick Navigation: [⬅️ Project structure](#project-structure_) | [`example_llamaindex.py` ➡️](#example-llamaindex_)

TODO: walkthrough of the script (steps 1 through 5), same style as the original README.

Steps covered:
1. Load data (`Document`, `wikipedia`)
2. Chunking (`RecursiveCharacterTextSplitter`)
3. Embedding model (`OpenAIEmbeddings`)
4. In memory vector store (`InMemoryVectorStore`)
5. Query (`similarity_search`)

### Run it

```bash
python example_langchain.py
```

TODO: paste example output.

[↑ Back to Table of Contents](#table-of-contents_)

<a name="example-llamaindex_"></a>

---

## `example_llamaindex.py`

#### ⚡ Quick Navigation: [⬅️ `example_langchain.py`](#example-langchain_) | [LangChain vs LlamaIndex comparison ➡️](#langchain-vs-llamaindex_)


TODO: walkthrough of the script (steps 1 through 5), mirroring the previous section.

Steps covered:
1. Load data (`Document`, `wikipedia`)
2. Chunking (`SentenceSplitter`)
3. Embedding model (`OpenAIEmbedding`)
4. In memory index (`VectorStoreIndex`)
5. Query (`as_retriever` + `retrieve`)

### Run it

```bash
python example_llamaindex.py
```

TODO: paste example output.

[↑ Back to Table of Contents](#table-of-contents_)

<a name="langchain-vs-llamaindex_"></a>

---

## LangChain vs LlamaIndex comparison

#### ⚡ Quick Navigation: [⬅️ `example_llamaindex.py`](#example-llamaindex_) | [Conclusions ➡️](#conclusions_)

💡 **Note on chunking**

The examples use different chunking strategies by default: LlamaIndex splits by sentence (`SentenceSplitter`), LangChain splits by character (`RecursiveCharacterTextSplitter`). This explains why LlamaIndex chunks tend to be larger even with the same `chunk_size`.

There are ways to bring both behaviours closer together (`NLTKTextSplitter` / `SpacyTextSplitter` in LangChain for sentence splitting, `TokenTextSplitter` in LlamaIndex to approximate char based splitting), but none of them faithfully replicate the other library's behaviour without extra dependencies or losing precision in chunk size. Each library was kept with its own default.

TODO: comparison table (setup, default chunking, vector store, query API, verbosity).

| | LangChain | LlamaIndex |
|---|---|---|
| Default chunking | By character | By sentence |
| Vector store | `InMemoryVectorStore` | `VectorStoreIndex` |
| Query API | `similarity_search` | `as_retriever().retrieve()` |


[↑ Back to Table of Contents](#table-of-contents_)

<a name="conclusions_"></a>

---

## Conclusions

#### ⚡ Quick Navigation: [⬅️ LangChain vs LlamaIndex comparison](#langchain-vs-llamaindex_) | [Next Steps & Resources ➡️](#next-steps--resources_)

TODO.

[↑ Back to Table of Contents](#table-of-contents_)

<a name="next-steps--resources_"></a>

---

## Next Steps & Resources

#### ⚡ Quick Navigation: [⬅️ Conclusions](#conclusions_) | [Get in Touch ➡️](#get-in-touch_)

TODO: suggestions (swap Wikipedia for PDFs, try another embedding model, connect this to the legal doc RAG project, etc.)

[↑ Back to Table of Contents](#table-of-contents_)

<a name="get-in-touch_"></a>

---

## 📬 Get in Touch

#### ⚡ Quick Navigation: [⬅️ Next Steps & Resources](#next-steps--resources_) | [⬆️ Back to Top](#rag-under-the-hood)


This tutorial took real time, real focus, and more debugging sessions than I'd like to admit. Not because I had to build it, but because this is genuinely how I like to spend my time: learning something properly enough to explain it to someone else.

I’ve always enjoyed breaking down complex ideas into simple terms. Over time, and after hearing from so many people that my explanations click for them, I’ve come to think it might actually be a strength of mine.

Right now this is something I do on my own time, for free. But I'd genuinely love for this to become my actual work, building, teaching, and explaining things like RAG pipelines and agentic systems, not just a side project squeezed into evenings and weekends. If you're building something in this space and looking for someone who already does this kind of work without being asked, that's exactly the kind of opportunity I'm looking for.

Found this useful? Have questions or ideas? I'd love to hear from you either way.

- 🔗 **[LinkedIn](https://www.linkedin.com/in/hugo-ferro-1434b414/)**
- 📩 **Email:** hugoferro (at) gmail.com
- 🗂️ **Portfolio:** [more AI/ML projects like this one](https://hasff.github.io/my-ai-portfolio/)

[↑ Back to Table of Contents](#table-of-contents_)


---
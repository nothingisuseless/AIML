# 🤖 RAG PDF Chatbot (Streamlit + Ollama)

A local-first chatbot that lets you ask questions about **multiple PDF files** using **Retrieval-Augmented Generation (RAG)**. It uses [LangChain](https://www.langchain.com/), [FAISS](https://github.com/facebookresearch/faiss), and [Ollama](https://ollama.com/) to run LLMs like LLaMA 3 on your own machine — no API keys, no cloud required.

---

## 🔍 What It Does

This app allows you to interact with your documents using natural language. It:
- Extracts and splits text from your PDFs
- Embeds the content using `sentence-transformers`
- Stores embeddings in a FAISS vector database
- Retrieves relevant chunks based on your query
- Uses a local LLM (e.g., `llama3`) to answer your question

---

## 🧰 Tech Stack

- **Streamlit** for UI
- **LangChain** for chaining LLMs + retrievers
- **FAISS** for vector similarity search
- **sentence-transformers** for text embeddings
- **Ollama** to run local LLMs

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/rag-pdf-chatbot.git
cd rag-pdf-chatbot

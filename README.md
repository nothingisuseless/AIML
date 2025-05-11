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
git clone https://github.com/nothingisuseless/rag-pdf-chatbot.git
cd rag-pdf-chatbot
```

### 2. Install Dependencies
```
It's recommended to use a virtual environment:


python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Add Your PDF Files

Put your .pdf files into the pdfs/ folder:
```

pdfs/
├── report.pdf
└── research_paper.pdf
```

### 4. Start Ollama
If you haven't installed Ollama yet, download it from: https://ollama.com

Then pull and start the model:
```

ollama pull llama3
ollama run llama3
```
### 5. Run the Streamlit App
In a separate terminal window:
```

streamlit run app.py
```
Then open your browser to: http://localhost:8501

## 🧩 Folder Structure

```
rag-pdf-chatbot/
├── app.py              
├── requirements.txt    
├── README.md           
└── pdfs/               
```

## 💡 Example Use Cases
Quickly summarize academic papers

Ask questions about long business reports

Extract insights from manuals, contracts, books, etc.

## 🧠 Customization
To change the model, edit the Ollama line in app.py:

```
llm = Ollama(model="llama3")  # Options: llama3, llama2, mistral, codellama, etc.
```

## 📜 License
This project is licensed under the MIT License — free to use and modify.

## 🙌 Acknowledgments
Thanks to:

LangChain

Ollama

sentence-transformers

FAISS


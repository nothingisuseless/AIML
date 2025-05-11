import os
import streamlit as st
from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import Ollama

# Set page config
st.set_page_config(page_title="RAG PDF Chatbot", layout="centered")
st.title("📚 Chat with your PDFs (RAG + Ollama)")

@st.cache_resource(show_spinner="Loading and indexing PDFs...")
def load_vectorstore(pdf_dir="pdfs/"):
    loader = DirectoryLoader(pdf_dir, glob="**/*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embeddings)

    return vectorstore

# Load vectorstore
vectorstore = load_vectorstore()

# Initialize Ollama LLM
llm = Ollama(model="llama3")

# Set up the RAG chain
rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# Chat input
query = st.text_input("Ask a question about your PDFs:")

if query:
    with st.spinner("Thinking..."):
        result = rag_chain.run(query)
        st.success("Answer:")
        st.write(result)

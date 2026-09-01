# PDF RAG Assistant

A Streamlit-based document question answering app that was originally built with a manual RAG pipeline and later migrated to a LangChain-based architecture for cleaner orchestration, retrieval, and prompting.

## Overview

This project demonstrates how we moved from a custom Retrieval-Augmented Generation (RAG) workflow to a LangChain implementation while keeping the same goal: answer questions from uploaded PDF documents using contextual retrieval and an LLM.

### What we did before: Manual RAG

In the initial version, we built the workflow manually using core Python components:

- Upload a PDF
- Extract text from the document
- Split the document into chunks
- Generate embeddings for each chunk using SentenceTransformers
- Store the embeddings in ChromaDB
- Retrieve the most relevant chunks for a question
- Pass the retrieved context to Gemini for answer generation

This version gave us a full understanding of how RAG works internally, including: text loading, chunking, vector storage, semantic retrieval, and LLM prompting.

### What we do now: LangChain RAG

We later switched to LangChain to make the pipeline more structured and reusable. The current implementation uses LangChain tools and abstractions:

- LangChain PDF loader for document ingestion
- RecursiveCharacterTextSplitter for chunking
- HuggingFaceEmbeddings for embeddings
- Chroma vector store for indexing and retrieval
- A retriever built with `db.as_retriever(search_kwargs={"k": 5})`
- `ChatPromptTemplate` to format the final prompt
- `prompt | llm | StrOutputParser()` to build a cleaner answer-generation chain

This makes the process easier to manage and more modular than the manual version.

## Project Flow

### Manual RAG Process

```text
PDF -> text extraction -> chunking -> embeddings -> vector database
User question -> embedding -> similarity search -> Gemini -> answer
```

### LangChain RAG Process

```text
PDF -> PyPDFLoader -> RecursiveCharacterTextSplitter -> Chroma + embeddings
User question -> retriever.invoke(question) -> relevant chunks -> prompt template -> Gemini -> answer
```

## Current Tech Stack

- Python
- Streamlit
- LangChain
- PyPDF
- ChromaDB
- HuggingFace Embeddings
- Google Gemini
- Python Dotenv

## Project Structure

```text
.
├── app.py
├── requirements.txt
├── README.md
├── prompts/
│   └── rag_prompt.txt
├── modules/
│   ├── __init__.py
│   ├── embedding.py
│   ├── llm.py
│   ├── langchain_rag.py
│   ├── pdf_utils.py
│   └── vectordb.py
└── .env
```

## Why the switch to LangChain?

The manual version helped us learn the fundamentals of RAG, but the LangChain version improved the workflow in several ways:

- cleaner code structure
- easier retrieval pipeline setup
- better integration with LLM prompting
- reusable LangChain components
- simpler scaling for future features

## Prerequisites

Before running the project, make sure you have:

- Python 3.9 or later
- A Google Gemini API key
- A working internet connection for model access

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd "RAG-Assistant"
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

## Running the App

Start the Streamlit application:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal, typically:

```text
http://localhost:8501
```

## Notes

- This application is designed for document-grounded Q&A rather than general-purpose chat.
- The quality of results depends on PDF quality, chunk size, retrieval quality, and the LLM used.
- The earlier manual implementation was an important learning step before moving to the LangChain version.
- Ensure your API key is valid and stored securely in the `.env` file.

## License

This project is for educational and demonstration purposes.

## Author

Created to demonstrate the journey from a manual RAG implementation to a cleaner, production-friendly LangChain-based document intelligence workflow.

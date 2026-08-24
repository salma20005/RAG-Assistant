# PDF RAG Assistant

A Streamlit-based Retrieval-Augmented Generation (RAG) application that lets users upload a PDF, extract its content, build a vector database, and ask questions about the document using Gemini.

## Overview

This project demonstrates a practical document Q&A workflow:

- Upload a PDF file
- Extract text from the document
- Split the content into manageable chunks
- Generate embeddings for each chunk
- Store the embeddings in a vector database
- Retrieve the most relevant context for a user question
- Use Gemini to generate a grounded answer based on the retrieved content

## Features

- PDF text extraction using PyPDF
- Text chunking for efficient retrieval
- Embedding generation using SentenceTransformers
- Vector similarity search with ChromaDB
- LLM-powered answer generation using Google Gemini
- Simple interactive UI built with Streamlit

## Tech Stack

- Python
- Streamlit
- PyPDF
- SentenceTransformers
- ChromaDB
- Google GenAI SDK
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
│   ├── pdf_utils.py
│   └── vectordb.py
└── .env
```

## Prerequisites

Before running the project, make sure you have:

- Python 3.9 or later
- A Google Gemini API key
- A working internet connection for model access

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd "Final Project"
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

## How It Works

1. The user uploads a PDF.
2. The system extracts text from all pages.
3. The text is split into chunks.
4. Each chunk is converted into an embedding vector.
5. Similarity search finds the most relevant chunks for the query.
6. Gemini receives the question and retrieved context to produce a final answer.

## Example Flow

```text
PDF -> text extraction -> chunking -> embeddings -> vector DB
User question -> embedding -> semantic retrieval -> Gemini -> answer
```

## Notes

- This application is designed for document-grounded Q&A rather than general-purpose chat.
- The quality of responses depends on the PDF content, chunking strategy, and retrieval quality.
- Ensure your API key is valid and stored securely in the `.env` file.

## License

This project is for educational and demonstration purposes.

## Author

Created as a final project demonstrating RAG-based document intelligence with Gemini and vector search.

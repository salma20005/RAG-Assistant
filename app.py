
import streamlit as st
from dotenv import load_dotenv

from modules.langchain_rag import build_retriever
from modules.llm import load_llm

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

st.set_page_config(
    page_title="PDF RAG Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 PDF RAG Assistant")

llm = load_llm()

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    with st.spinner("Processing PDF..."):
        retriever = build_retriever(uploaded_file)

    st.success("PDF Ready!")

    question = st.text_input(
        "Enter your question:",
         placeholder="Who is the instructor?"
    )

    if st.button("Ask") and question.strip():

        docs = retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        prompt = ChatPromptTemplate.from_template(
            """
            Answer the question using only the context below.

            Context:
            {context}

            Question:
            {question}

            Answer:
            """
        )

        chain = prompt | llm | StrOutputParser()

        answer = chain.invoke({
            "context": context,
            "question": question
        })

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Retrieved Context")

        for i, doc in enumerate(docs, start=1):
            with st.expander(f"Relevant Passage {i}"):
                st.write(doc.page_content)


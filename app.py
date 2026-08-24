import streamlit as st
from modules.pdf_utils import get_text_from_pdf, chunk_text
from modules.vectordb import build_vector__db, retrieve_context
from modules.llm import ask_gemini
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="PDF RAG Assistant",
    page_icon="📚",
    layout="wide",
)


collection = None

pdf_file = st.file_uploader(" ", type=["pdf"], label_visibility="collapsed", help="Upload a PDF file to search and ask questions.")

if pdf_file is not None:
    with st.spinner("Processing PDF and building the vector database..."):
        text = get_text_from_pdf(pdf_file)
        if not text or not text.strip():
            st.error("The uploaded PDF does not contain readable text.")
            st.stop()

        chunks = chunk_text(text)
        collection = build_vector__db(chunks)

    st.markdown('<div class="section-title">Ask</div>', unsafe_allow_html=True)

    with st.form("question_form"):
        c1, c2 = st.columns([8, 1])
        with c1:
            question = st.text_input("", placeholder="who is the instructor?", label_visibility="collapsed")
        with c2:
            st.form_submit_button("Ask", use_container_width=True)

    if question and question.strip():
        with st.spinner("Searching the most relevant information..."):
            context_chunks = retrieve_context(question, collection, as_list=True)
            context_text = " ".join(context_chunks)
            response = ask_gemini(question, context_text)

        st.markdown('<div class="section-title">Answer</div>', unsafe_allow_html=True)
        st.markdown(f"<div class='answer-box'>{response}</div>", unsafe_allow_html=True)

        st.markdown('<div class="section-title">Retrieved Context</div>', unsafe_allow_html=True)

        context_display = " ".join(
            f"Relevant passage {idx}: {chunk}" for idx, chunk in enumerate(context_chunks, start=1)
        )

        st.markdown(
            f"""
            <div class="context-box">
                <span class="context-title">Relevant passages</span>
                {context_display}
            </div>
            """,
            unsafe_allow_html=True,
        )
else:
    st.info("Upload a PDF to begin.")

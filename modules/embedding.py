from sentence_transformers import SentenceTransformer
import streamlit as st
@st.cache_resource
def load_model():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model
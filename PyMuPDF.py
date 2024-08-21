import fitz  # PyMuPDF
import streamlit as st

def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])
if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    st.write(text)

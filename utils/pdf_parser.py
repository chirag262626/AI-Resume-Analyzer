import streamlit as st
import PyPDF2


def extract_text_from_pdf(uploaded_file):
    """Extract text content from an uploaded PDF file."""
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text = text + page.extract_text()
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return ""

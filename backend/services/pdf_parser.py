"""
Resume file parsing utilities.
Supports PDF (PyPDF2) and DOCX (python-docx) formats.
"""

import io
import PyPDF2
from docx import Document


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extract text content from PDF file bytes."""
    try:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text
    except Exception as e:
        raise ValueError(f"Error reading PDF: {e}")


def extract_text_from_docx(file_bytes: bytes) -> str:
    """Extract text content from DOCX file bytes."""
    try:
        doc = Document(io.BytesIO(file_bytes))
        text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        return text
    except Exception as e:
        raise ValueError(f"Error reading DOCX: {e}")

"""
Text processing utilities for resume analysis.
Uses NLTK for preprocessing and scikit-learn for TF-IDF + Cosine Similarity.
"""

import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def download_nltk_data():
    """Download required NLTK resources (called once at startup)."""
    nltk.download("punkt_tab", quiet=True)
    nltk.download("stopwords", quiet=True)
    nltk.download("averaged_perceptron_tagger_eng", quiet=True)


def clean_text(text: str) -> str:
    """Lowercase, remove non-alpha characters, collapse whitespace."""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def remove_stopwords(text: str) -> str:
    """Remove English stop words from text."""
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    return " ".join([word for word in words if word not in stop_words])


def calculate_similarity(resume_text: str, job_description: str) -> tuple:
    """Compute TF-IDF cosine similarity between resume and job description.

    Returns:
        tuple: (similarity_score, resume_processed, job_processed)
    """
    resume_processed = remove_stopwords(clean_text(resume_text))
    job_processed = remove_stopwords(clean_text(job_description))
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_processed, job_processed])
    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0] * 100
    return round(score, 2), resume_processed, job_processed

"""
FastAPI backend for ATS Resume Analyzer.
Exposes REST endpoints for resume analysis using TF-IDF + Cosine Similarity.
"""

import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, File, Form, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from services.analyzer import analyze_resume
from services.text_processing import download_nltk_data


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Download NLTK data on startup."""
    download_nltk_data()
    yield


app = FastAPI(
    title="ATS Resume Analyzer API",
    description="Analyze resume–job description alignment using TF-IDF + Cosine Similarity",
    version="1.0.0",
    lifespan=lifespan,
)

# ─── CORS ───
cors_origins_env = os.getenv("CORS_ORIGINS", "*")
if cors_origins_env.strip() == "*":
    cors_config = {"allow_origins": ["*"], "allow_credentials": False}
else:
    cors_config = {
        "allow_origins": [o.strip() for o in cors_origins_env.split(",")],
        "allow_credentials": True,
    }
app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    **cors_config,
)


# ─── Health Check ───
@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "service": "ATS Resume Analyzer API"}


# ─── Analyze Endpoint ───
ALLOWED_EXTENSIONS = {"pdf", "docx", "doc"}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB


@app.post("/api/analyze")
async def analyze(
    file: UploadFile = File(...),
    job_description: str = Form(...),
):
    """
    Analyze a resume file against a job description.

    - **file**: PDF or DOCX resume (max 10 MB)
    - **job_description**: The target job description text

    Returns JSON with score, label, feedback, and color information.
    """
    # Validate file extension
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided.")

    ext = file.filename.lower().rsplit(".", 1)[-1] if "." in file.filename else ""
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file format: .{ext}. Please upload a PDF or DOCX file.",
        )

    # Validate job description
    if not job_description or not job_description.strip():
        raise HTTPException(status_code=400, detail="Job description cannot be empty.")

    # Read file bytes
    file_bytes = await file.read()
    if len(file_bytes) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File size exceeds 10 MB limit.")

    if len(file_bytes) == 0:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")

    # Analyze
    try:
        result = analyze_resume(file_bytes, file.filename, job_description)
        return result
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

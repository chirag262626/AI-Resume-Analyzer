"""
Resume analyzer service — orchestrates file parsing and similarity scoring.
"""

from .pdf_parser import extract_text_from_pdf, extract_text_from_docx
from .text_processing import calculate_similarity
from .skill_extractor import analyze_skill_gap


def _get_score_details(score: float) -> dict:
    """Return label, color, and feedback based on the match score."""
    if score < 40:
        return {
            "label": "Low Match",
            "color_start": "#FF4B4B",
            "color_end": "#FF6B6B",
            "feedback": (
                "Consider tailoring your resume more closely to the job description. "
                "Focus on adding relevant keywords and matching required skills."
            ),
            "icon": "⚠️",
        }
    elif score < 70:
        return {
            "label": "Good Match",
            "color_start": "#FFA726",
            "color_end": "#FFD54F",
            "feedback": (
                "Your resume aligns fairly well with this job. "
                "Some fine-tuning could push your score higher."
            ),
            "icon": "💡",
        }
    else:
        return {
            "label": "Excellent Match",
            "color_start": "#00C853",
            "color_end": "#69F0AE",
            "feedback": (
                "Your resume strongly aligns with this job description. "
                "Great job optimizing for ATS systems!"
            ),
            "icon": "🎉",
        }


def analyze_resume(file_bytes: bytes, filename: str, job_description: str) -> dict:
    """Analyze a resume file against a job description.

    Args:
        file_bytes: Raw bytes of the uploaded file.
        filename: Original filename (used to determine format).
        job_description: The job description text.

    Returns:
        dict with score, label, colors, feedback, and icon.

    Raises:
        ValueError: If the file format is unsupported or text can't be extracted.
    """
    ext = filename.lower().rsplit(".", 1)[-1] if "." in filename else ""

    if ext == "pdf":
        resume_text = extract_text_from_pdf(file_bytes)
    elif ext in ("docx", "doc"):
        resume_text = extract_text_from_docx(file_bytes)
    else:
        raise ValueError(f"Unsupported file format: .{ext}. Please upload a PDF or DOCX file.")

    if not resume_text or not resume_text.strip():
        raise ValueError("Could not extract text from the uploaded file. Please try another file.")

    score, _, _ = calculate_similarity(resume_text, job_description)
    
    skill_analysis = analyze_skill_gap(resume_text, job_description)
    
    # Blend the harsh Cosine Similarity contextual score with the discrete Keyword Match score
    # We weight the Keyword Match higher (60%) since hard skills are usually the primary ATS filter
    if skill_analysis.get("total_jd_skills_found", 0) > 0:
        base_tf_idf = score
        skill_match = skill_analysis["skill_match_percentage"]
        final_score = (base_tf_idf * 0.4) + (skill_match * 0.6)
    else:
        final_score = score
        
    final_score = round(final_score, 1)

    details = _get_score_details(final_score)

    return {
        "score": final_score,
        **details,
        **skill_analysis
    }

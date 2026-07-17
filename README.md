# AI Resume Reviewer & ATS Analyzer

A full-stack, production-ready SaaS web application that uses Natural Language Processing (TF-IDF + Cosine Similarity) to analyze how well a resume matches a job description.

Featuring a FastAPI backend and a Next.js (React) front end styled with Tailwind CSS in a premium dark mode theme.

## 🌟 Features

*   **Smart Resume Parsing:** Works with both PDF and DOCX files.
*   **ATS Keyword Matching:** Analyzes the uploaded resume against a target job description.
*   **Actionable Feedback:** Calculates a match score and provides tailored recommendations.
*   **Modern SaaS UI/UX:** Built with Next.js, featuring animated gradients, glassmorphism, responsive design, and toast notifications.
*   **Fast REST API:** Powered by FastAPI for swift text processing and NLP tasks.

## 🏗 Architecture

The project consists of two decoupled services:

1.  **Frontend:** Next.js (App Router), React, Tailwind CSS, TypeScript.
2.  **Backend:** FastAPI, scikit-learn, NLTK, PyPDF2, python-docx.

## 🚀 Local Setup

### Prerequisites
*   Node.js v18+
*   Python 3.10+

### Backend Setup
1.  Navigate to the backend directory:
    ```bash
    cd backend
    ```
2.  Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Run the FastAPI server:
    ```bash
    python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    ```
    *The API will be available at http://localhost:8000*

### Frontend Setup
1.  Navigate to the frontend directory:
    ```bash
    cd frontend
    ```
2.  Install dependencies:
    ```bash
    npm install
    ```
3.  Start the Next.js development server:
    ```bash
    npm run dev
    ```
    *The web app will be available at http://localhost:3000*

## 🌐 API Documentation

### `POST /api/analyze`
Extracts text from a resume and compares it to a job description.

**Parameters (Form-Data):**
*   `file`: The resume file (PDF or DOCX).
*   `job_description`: (String) The target job description.

**Response:**
```json
{
  "score": 85.5,
  "label": "Excellent Match",
  "color_start": "#00C853",
  "color_end": "#69F0AE",
  "feedback": "Your resume strongly aligns with this job description. Great job optimizing for ATS systems!",
  "icon": "🎉"
}
```

### `GET /api/health`
Check API health.

**Response:**
```json
{
  "status": "healthy",
  "service": "ATS Resume Analyzer API"
}
```

## 📸 Screenshots

*(Add your screenshots here)*
*   Screenshot of Hero & UI
*   Screenshot of Analysis Results

## ⚙️ Deployment Instructions

### Deploy Frontend (Vercel)
1. Fork or push this repository to GitHub.
2. Go to [Vercel](https://vercel.com/) and create a new project.
3. Import the repository and set the `Root Directory` to `frontend`.
4. Deploy!

### Deploy Backend (Render)
1. Go to [Render](https://render.com/) and create a new Web Service.
2. Connect the repository and configure:
    *   **Root Directory:** `backend`
    *   **Build Command:** `pip install -r requirements.txt`
    *   **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
3. Set the Environment Variable `CORS_ORIGINS` to the URL of your Vercel frontend.
4. Deploy!

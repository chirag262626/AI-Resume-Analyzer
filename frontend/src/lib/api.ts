const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export interface SkillItem {
    category: string;
    skill: string;
}

export interface AnalysisResult {
    score: number;
    label: string;
    color_start: string;
    color_end: string;
    feedback: string;
    icon: string;
    matched_skills: SkillItem[];
    missing_skills: SkillItem[];
    recommendations: string[];
    skill_match_percentage: number;
    total_jd_skills_found: number;
}

export interface ApiError {
    detail: string;
}

export async function analyzeResume(
    file: File,
    jobDescription: string
): Promise<AnalysisResult> {
    const formData = new FormData();
    formData.append("file", file);
    formData.append("job_description", jobDescription);

    const response = await fetch(`${API_BASE_URL}/api/analyze`, {
        method: "POST",
        body: formData,
    });

    if (!response.ok) {
        const errorData: ApiError = await response.json().catch(() => ({
            detail: "An unexpected error occurred. Please try again.",
        }));
        throw new Error(errorData.detail);
    }

    return response.json();
}

export async function checkHealth(): Promise<boolean> {
    try {
        const response = await fetch(`${API_BASE_URL}/api/health`);
        return response.ok;
    } catch {
        return false;
    }
}

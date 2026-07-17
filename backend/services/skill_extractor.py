import re
from typing import Dict, List, Set, Tuple

# Hardcoded rule-based skill taxonomy
SKILL_TAXONOMY = {
    "Programming": [
        "python", "javascript", "typescript", "java", "c++", "c#", "ruby", "go", 
        "rust", "php", "swift", "kotlin", "scala", "dart", "shell", "bash"
    ],
    "Frontend": [
        "react", "angular", "vue", "next.js", "nextjs", "svelte", "html", "css", 
        "tailwind", "bootstrap", "material ui", "redux", "jquery", "sass", "less"
    ],
    "Backend": [
        "node.js", "nodejs", "express", "django", "flask", "fastapi", "spring boot", 
        "spring", "laravel", "ruby on rails", "asp.net", "graphql", "rest api"
    ],
    "Database": [
        "sql", "mysql", "postgresql", "postgres", "mongodb", "sqlite", "redis", 
        "elasticsearch", "cassandra", "dynamodb", "mariadb", "oracle"
    ],
    "Cloud & DevOps": [
        "aws", "amazon web services", "azure", "gcp", "google cloud", "docker", 
        "kubernetes", "k8s", "terraform", "ansible", "jenkins", "github actions", 
        "ci/cd", "linux", "nginx", "apache"
    ],
    "AI & Data": [
        "machine learning", "deep learning", "ai", "artificial intelligence", 
        "tensorflow", "pytorch", "pandas", "numpy", "scikit-learn", "scikit learn",
        "keras", "nlp", "computer vision", "opencv", "data science", "data analysis",
        "power bi", "tableau", "hadoop", "spark", "kafka"
    ],
    "Tools & General": [
        "git", "github", "gitlab", "bitbucket", "jira", "confluence", "agile", 
        "scrum", "kanban", "problem solving", "leadership", "communication"
    ]
}

def clean_and_tokenize(text: str) -> str:
    """Prepare text for exact string and substring matching."""
    text = text.lower()
    # Retain alphanumeric, spaces, and dot/plus/hash for technologies (e.g. c++, c#, next.js)
    text = re.sub(r'[^a-z0-9\s\.+#/]', ' ', text)
    # Collapse whitespace
    return re.sub(r'\s+', ' ', text).strip()

def _extract_skills_from_text(text: str) -> Dict[str, Set[str]]:
    """Scan and categorize all taxonomy keys present within the raw text."""
    clean_txt = clean_and_tokenize(text)
    
    extracted = {category: set() for category in SKILL_TAXONOMY}
    
    # We pad the target text so boundary checks are simpler
    padded_txt = f" {clean_txt} "
    
    for category, skills in SKILL_TAXONOMY.items():
        for skill in skills:
            # Look for exact word matches (e.g., avoiding matching 'java' inside 'javascript')
            # Handle special characters gracefully
            escaped_skill = re.escape(skill)
            pattern = r'(?<![a-z0-9])' + escaped_skill + r'(?![a-z0-9])'
            
            if re.search(pattern, clean_txt):
                extracted[category].add(skill)
                
    return extracted

def analyze_skill_gap(resume_text: str, jd_text: str) -> dict:
    """Analyze the gap between skills in resume and those required by the job."""
    
    clean_jd = clean_and_tokenize(jd_text)
    
    resume_skills_dict = _extract_skills_from_text(resume_text)
    jd_skills_dict = _extract_skills_from_text(jd_text)
    
    matched_skills = []
    missing_skills = []
    total_jd_skills = 0
    missing_skill_stats = []
    
    for category in SKILL_TAXONOMY.keys():
        r_skills = resume_skills_dict.get(category, set())
        j_skills = jd_skills_dict.get(category, set())
        
        total_jd_skills += len(j_skills)
        
        intersect = j_skills.intersection(r_skills)
        diff = j_skills.difference(r_skills)
        
        # Populate matched
        for skill in intersect:
            matched_skills.append({
                "category": category,
                "skill": skill.title() if len(skill) > 3 else skill.upper()
            })
            
        # Populate missing and calculate occurrences in JD
        for skill in diff:
            # Count occurrences in JD target
            escaped_skill = re.escape(skill)
            pattern = r'(?<![a-z0-9])' + escaped_skill + r'(?![a-z0-9])'
            occurrences = len(re.findall(pattern, clean_jd))
            
            missing_skill_stats.append({
                "category": category,
                "skill": skill.title() if len(skill) > 3 else skill.upper(),
                "occurrences": occurrences
            })
            
    # Sort missing skills by descending occurrence rate (priority)
    missing_skill_stats.sort(key=lambda x: x["occurrences"], reverse=True)
    
    for ms in missing_skill_stats:
        missing_skills.append({
            "category": ms["category"],
            "skill": ms["skill"]
        })
        
    skill_match_percentage = 0
    if total_jd_skills > 0:
        skill_match_percentage = round((len(matched_skills) / total_jd_skills) * 100)
    elif len(matched_skills) > 0:
        # User has skills, JD has 0 extractable skills
        skill_match_percentage = 100
        
    # Generate actionable recommendations (top 3)
    recommendations = []
    if missing_skill_stats:
        top_missing = missing_skill_stats[:3]
        for item in top_missing:
            occ = item["occurrences"]
            freq_str = f"({occ} times)" if occ > 1 else "(1 time)"
            recommendations.append(
                f"Consider mentioning '{item['skill']}' if you have experience with it, as it appears {freq_str} in the job description."
            )
            
    if not missing_skill_stats and total_jd_skills > 0:
        recommendations.append("Excellent! You've hit all the extractable key skills observed in the job description.")
    elif total_jd_skills == 0:
        recommendations.append("The job description is somewhat generic; try expanding on your soft skills and core methodologies.")

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "recommendations": recommendations,
        "skill_match_percentage": skill_match_percentage,
        "total_jd_skills_found": total_jd_skills
    }

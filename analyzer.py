import re

SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "javascript",
    "html",
    "css",
    "sql",
    "mysql",
    "mongodb",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data analysis",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "flask",
    "django",
    "streamlit",
    "git",
    "github",
    "aws",
    "azure",
    "docker",
    "power bi"
]


def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return set(found_skills)


def analyze_resume(resume_text, job_description):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matched_skills = resume_skills.intersection(job_skills)
    missing_skills = job_skills.difference(resume_skills)

    if len(job_skills) > 0:
        score = round(
            (len(matched_skills) / len(job_skills)) * 100,
            2
        )
    else:
        score = 0

    return {
        "score": score,
        "matched_skills": sorted(list(matched_skills)),
        "missing_skills": sorted(list(missing_skills))
    }

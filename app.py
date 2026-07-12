import streamlit as st
import PyPDF2
from analyzer import analyze_resume

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and compare it with a job description.")

uploaded_file = st.file_uploader(
    "Upload your resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste the Job Description",
    height=250,
    placeholder="Paste the complete job description here..."
)

if st.button("Analyze Resume"):
    if uploaded_file is not None and job_description.strip():

        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        resume_text = ""

        for page in pdf_reader.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                resume_text += extracted_text

        result = analyze_resume(resume_text, job_description)

        st.success("Resume analysis completed!")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Match Score", f"{result['score']}%")

        with col2:
            st.metric("Matched Skills", len(result["matched_skills"]))

        with col3:
            st.metric("Missing Skills", len(result["missing_skills"]))

        st.subheader("✅ Matched Skills")
        if result["matched_skills"]:
            st.write(", ".join(result["matched_skills"]))
        else:
            st.write("No matching skills found.")

        st.subheader("❌ Missing Skills")
        if result["missing_skills"]:
            st.write(", ".join(result["missing_skills"]))
        else:
            st.write("No major missing skills found.")

        st.subheader("💡 Suggestions")

        if result["score"] >= 80:
            st.success(
                "Excellent match! Your resume is highly relevant to this job."
            )
        elif result["score"] >= 60:
            st.warning(
                "Good match. Consider adding some missing skills if you have experience with them."
            )
        else:
            st.error(
                "Your resume needs improvement for this role. Focus on relevant skills and projects."
            )

    else:
        st.warning("Please upload a PDF resume and enter a job description.")

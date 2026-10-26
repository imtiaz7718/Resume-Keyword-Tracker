import streamlit as st
from extractor import extract_resume_text
from analyzer import analyze_match

st.set_page_config(page_title="Resume Keyword Tracker", layout="wide")

st.title("📄 Resume Keyword & ATS Alignment Tracker")
st.write("Compare your resume against a target Job Description to identify matching and missing keywords.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Upload Resume")
    uploaded_file = st.file_uploader("Upload PDF or DOCX", type=["pdf", "docx"])

with col2:
    st.subheader("2. Target Job Description")
    job_description = st.text_area("Paste the Job Description here", height=220)

if st.button("Analyze Match", type="primary"):
    if not uploaded_file:
        st.warning("Please upload a resume first.")
    elif not job_description.strip():
        st.warning("Please paste a job description.")
    else:
        with st.spinner("Extracting text and analyzing keywords..."):
            resume_text = extract_resume_text(uploaded_file)
            
            if not resume_text:
                st.error("Could not extract readable text from the file.")
            else:
                results = analyze_match(resume_text, job_description)

                st.divider()
                st.subheader("Results & Analytics")

                m1, m2, m3 = st.columns(3)
                m1.metric("Keyword Match Rate", f"{results['match_rate']}%")
                m2.metric("TF-IDF Semantic Similarity", f"{results['cosine_score']}%")
                m3.metric("Total Identified JD Skills", results["total_jd_keywords"])

                st.divider()

                res_col1, res_col2 = st.columns(2)

                with res_col1:
                    st.success(f"Matched Keywords ({len(results['matched_keywords'])})")
                    if results["matched_keywords"]:
                        st.write(", ".join(results["matched_keywords"]))
                    else:
                        st.info("No matching keywords found.")

                with res_col2:
                    st.error(f"Missing Keywords to Add ({len(results['missing_keywords'])})")
                    if results["missing_keywords"]:
                        st.write(", ".join(results["missing_keywords"]))
                    else:
                        st.success("All identified keywords from JD are in your resume!")
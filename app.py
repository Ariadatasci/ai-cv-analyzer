import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pdfplumber

st.set_page_config(page_title="AI CV Matcher", layout="centered")

st.title("🧠 AI CV Match Analyzer")

st.write("Upload a CV and paste the job description to see how well they match.")

# Upload CV
uploaded_file = st.file_uploader("Upload CV (PDF or TXT)", type=["pdf", "txt"])

# Job description input
job_text = st.text_area("Paste Job Description Here")

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

if uploaded_file and job_text:

    # Read CV
    if uploaded_file.type == "application/pdf":
        cv_text = extract_text_from_pdf(uploaded_file)
    else:
        cv_text = uploaded_file.read().decode("utf-8")

    # TF-IDF
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([cv_text, job_text])

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    score = similarity * 100

    st.subheader("📊 Match Result")
    st.metric(label="Match Score", value=f"{score:.2f}%")

    if score > 75:
        st.success("Strong match ✅")
    elif score > 50:
        st.warning("Moderate match ⚠️")
    else:
        st.error("Low match ❌")
import streamlit as st
import pdfplumber

# Page Settings
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

# Custom Purple Theme
st.markdown("""
<style>
.stApp {
    background-color: #f5edff;
}

h1 {
    color: #6a0dad;
    text-align: center;
}

h2, h3 {
    color: #5b2c87;
}

.stButton>button {
    background-color: #6a0dad;
    color: white;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# Title
st.title("📄 AI Resume Analyzer")

st.write("Upload your resume and get AI-powered analysis.")

# Upload PDF
uploaded_file = st.file_uploader(
    "Upload Your Resume (PDF)",
    type="pdf"
)

if uploaded_file is not None:

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted

    # Show Resume Content
    st.subheader("📑 Resume Content")
    st.write(text)

    # Skills Database
    skills = [
        "Python",
        "C",
        "C++",
        "Java",
        "SQL",
        "HTML",
        "CSS",
        "JavaScript",
        "Machine Learning",
        "AI",
        "Data Science",
        "Leadership",
        "Communication",
        "Teamwork",
        "Problem Solving"
    ]

    # Detect Skills
    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    # Display Skills
    st.subheader("🛠 Detected Skills")

    if found_skills:
        st.success(found_skills)
    else:
        st.warning("No skills detected.")

    # ATS Score
    score = len(found_skills) * 7

    if score > 100:
        score = 100

    # Display Score
    st.subheader("📊 ATS Resume Score")

    st.progress(score)

    st.write(f"### Your ATS Score: {score}/100")

    # Suggestions
    st.subheader("💡 Suggestions")

    if score < 40:
        st.error("""
        - Add more technical skills
        - Add projects section
        - Include certifications
        - Improve resume formatting
        """)

    elif score < 70:
        st.warning("""
        - Add advanced projects
        - Add internships
        - Include GitHub profile
        """)

    else:
        st.success("""
        Excellent resume!
        Your resume looks strong for internships.
        """)

# Footer
st.markdown("---")
st.write("Made with ❤️ using Python & Streamlit")

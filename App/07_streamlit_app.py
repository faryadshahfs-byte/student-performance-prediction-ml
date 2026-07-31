import streamlit as st
import joblib
import numpy as np
from pathlib import Path

# ==========================================================
# LOAD MODEL
# ==========================================================

MODEL_PATH = Path("Models") / "Student_Performance_Prediction" / "student_performance_model.pkl"
model = joblib.load(MODEL_PATH)

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="wide"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

/* Background */
.stApp{
    background:linear-gradient(135deg,#0B1120,#172554,#312E81);
}

/* Hide Streamlit Branding */
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

/* Main Title */
.main-title{
    text-align:center;
    color:white;
    font-size:48px;
    font-weight:800;
    margin-bottom:5px;
    text-shadow:0px 3px 12px rgba(0,0,0,.45);
}

/* Subtitle */
.sub-title{
    text-align:center;
    color:#CBD5E1;
    font-size:22px;
    margin-bottom:25px;
}

/* Glass Card */
.glass{
    background:rgba(255,255,255,.08);
    backdrop-filter:blur(15px);
    border-radius:20px;
    padding:25px;
    border:1px solid rgba(255,255,255,.15);
    box-shadow:0 8px 30px rgba(0,0,0,.30);
}

/* Inputs */
.stNumberInput input{
    background:white;
    border-radius:12px;
    border:2px solid #4F46E5;
}

/* Button */
.stButton>button{
    width:100%;
    border:none;
    border-radius:15px;
    padding:14px;
    font-size:20px;
    font-weight:bold;
    color:white;
    background:linear-gradient(90deg,#7C3AED,#2563EB);
}

.stButton>button:hover{
    transform:scale(1.02);
    transition:.25s;
}

/* Metric */
[data-testid="stMetric"]{
    background:rgba(255,255,255,.08);
    border-radius:15px;
    padding:18px;
}

/* Success Box */
.stSuccess{
    border-radius:15px;
    border:2px solid #10B981;
}

hr{
    border:1px solid rgba(255,255,255,.15);
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.image(
        "https://img.icons8.com/fluency/240/artificial-intelligence.png",
        width=110
    )

    st.title("Project Info")

    st.write("### Model")

    st.success("Linear Regression")

    st.write("### Features")

    st.write("• Study Hours")
    st.write("• Attendance")
    st.write("• Assignments")
    st.write("• Quiz Score")

    st.write("### Developer")

    st.info("Faryad Shah\n\nAI & Automation Engineer")

# ==========================================================
# HEADER
# ==========================================================
# ==========================================================
# HEADER
# ==========================================================

c1, c2, c3 = st.columns([1,2,1])

with c2:
    st.image(
        "https://img.icons8.com/fluency/240/artificial-intelligence.png",
        width=140
    )

st.markdown(
    """
    <h1 style="
        text-align:center;
        color:white;
        font-size:48px;
        font-weight:800;
        margin-top:10px;
        margin-bottom:8px;
        text-shadow:0px 3px 12px rgba(0,0,0,.35);">
        🎓 Student Performance Prediction
    </h1>

    <h3 style="
        text-align:center;
        color:#60A5FA;
        font-size:24px;
        font-weight:700;
        margin-top:0;
        margin-bottom:20px;">
        AI-Powered Machine Learning Application
    </h3>

    <p style="
        text-align:center;
        color:#FFFFFF;
        font-size:20px;
        font-weight:500;
        line-height:1.7;
        letter-spacing:.2px;
        font-family:Arial, Helvetica, sans-serif;
        margin-bottom:30px;">
        Predict student exam performance instantly using our AI-powered Machine Learning model.
    </p>
    """,
    unsafe_allow_html=True
)
# Input Labels CSS
st.markdown("""
<style>
div[data-testid="stNumberInput"] label{
    color:#FFFFFF !important;
    font-size:18px !important;
    font-weight:700 !important;
    opacity:1 !important;
    text-shadow:none !important;
    font-family:Arial, Helvetica, sans-serif !important;
    -webkit-font-smoothing:antialiased;
    -moz-osx-font-smoothing:grayscale;
}
</style>
""", unsafe_allow_html=True)
# ==========================================================
# USER INPUTS
# ==========================================================

left,right = st.columns(2)

with left:

    study_hours = st.number_input(
        "📚 Study Hours",
        min_value=0,
        max_value=15,
        value=5
    )

    attendance = st.number_input(
        "📅 Attendance (%)",
        min_value=0,
        max_value=100,
        value=80
    )

with right:

    assignments = st.number_input(
        "📝 Assignments Completed",
        min_value=0,
        max_value=10,
        value=5
    )

    quiz_score = st.number_input(
        "🎯 Quiz Score",
        min_value=0,
        max_value=100,
        value=70
    )

st.write("")
# ==========================================================
# PREDICTION
# ==========================================================

if st.button("🚀 Predict Exam Marks", use_container_width=True):

    # Prepare Features
    features = np.array([[
        study_hours,
        attendance,
        assignments,
        quiz_score
    ]])

    # Predict
    prediction = float(model.predict(features)[0])

    # Keep prediction within realistic range
    prediction = max(0, min(prediction, 100))

    # Grade
    if prediction >= 90:
        grade = "A+ 🌟"
        status = "Outstanding Performance"
        color = "🟢"

    elif prediction >= 80:
        grade = "A ✅"
        status = "Excellent Work"
        color = "🟢"

    elif prediction >= 70:
        grade = "B 👍"
        status = "Very Good"
        color = "🟡"

    elif prediction >= 60:
        grade = "C 🙂"
        status = "Average Performance"
        color = "🟠"

    else:
        grade = "D ⚠️"
        status = "Needs Improvement"
        color = "🔴"

    st.balloons()

    st.divider()

    st.markdown("## 📊 Prediction Result")

    # Metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="🎯 Predicted Marks",
            value=f"{prediction:.2f}"
        )

    with col2:
        st.metric(
            label="🏆 Grade",
            value=grade
        )

    with col3:
        st.metric(
            label="📈 Status",
            value=status
        )

    st.write("")

    # Progress Bar
    st.subheader("📉 Score Progress")

    st.progress(int(prediction))

    st.write(f"### Score: **{prediction:.2f} / 100**")

    st.divider()

    # Performance Feedback
    st.subheader("💡 Performance Analysis")

    if prediction >= 90:

        st.success(
            "Excellent! The student is expected to achieve outstanding exam performance."
        )

    elif prediction >= 80:

        st.success(
            "Very good performance. A little more effort can lead to perfect marks."
        )

    elif prediction >= 70:

        st.info(
            "Good performance. Regular practice can further improve the result."
        )

    elif prediction >= 60:

        st.warning(
            "Average performance. More study hours and consistent assignments are recommended."
        )

    else:

        st.error(
            "Performance is below expectations. Increase study time and improve attendance and quiz preparation."
        )

    st.divider()
    # ==========================================================
# RESULT SUMMARY CARD
# ==========================================================

    st.markdown(
        f"""
        <div style="
            background:rgba(255,255,255,0.08);
            padding:25px;
            border-radius:18px;
            border:1px solid rgba(255,255,255,0.15);
            text-align:center;
            margin-top:20px;
        ">

        <h2 style="color:#F8FAFC;">
            🎓 Final Prediction
        </h2>

        <h1 style="color:#22C55E;font-size:55px;">
            {prediction:.2f}
        </h1>

        <h3 style="color:white;">
            Grade : {grade}
        </h3>

        <p style="font-size:20px;color:#CBD5E1;">
            {color} {status}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # ==========================================================
    # STUDY RECOMMENDATIONS
    # ==========================================================

    st.subheader("📚 AI Study Recommendations")

    if prediction >= 90:

        st.success("""
✅ Outstanding work!

• Keep practicing consistently.
• Solve advanced questions.
• Revise weekly.
• Help classmates to strengthen your concepts.
""")

    elif prediction >= 80:

        st.info("""
📈 Excellent performance!

• Increase daily practice slightly.
• Focus on difficult topics.
• Revise previous quizzes.
• Attempt mock exams.
""")

    elif prediction >= 70:

        st.info("""
👍 Good progress!

• Increase study hours.
• Improve quiz preparation.
• Complete all assignments.
• Practice time management.
""")

    elif prediction >= 60:

        st.warning("""
⚠️ Improvement needed.

• Study every day.
• Complete all assignments.
• Improve attendance.
• Solve previous papers.
""")

    else:

        st.error("""
🚨 Immediate attention required.

• Increase study hours.
• Improve attendance.
• Complete every assignment.
• Practice quizzes daily.
• Seek guidance from teachers.
""")

# ==========================================================
# FOOTER
# ==========================================================

st.write("")
st.divider()

st.markdown(
"""
<div style="text-align:center;color:#CBD5E1;">

### 🤖 AI-Powered Student Performance Prediction

Developed with ❤️ using

**Python • Scikit-Learn • Streamlit**

<br>

👨‍💻 Developed by <b>Faryad Shah</b><br>
AI & Automation Engineer

</div>
""",
unsafe_allow_html=True
)
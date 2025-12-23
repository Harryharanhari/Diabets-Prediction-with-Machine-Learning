import streamlit as st
import numpy as np
import joblib
import plotly.graph_objects as go

# =====================================================
# Page Configuration
# =====================================================
st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🏥",
    layout="wide"
)

# =====================================================
# Custom CSS
# =====================================================
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Inter', 'Segoe UI', sans-serif;
}

.main {
    background: linear-gradient(135deg, #f8fbff, #eef4ff);
    padding: 1.5rem 2rem;
}

h1 {
    color: #0b5ed7;
    font-weight: 800;
}

h2, h3, h4 {
    color: #0d3b66;
    font-weight: 700;
}

.stMetric, .stAlert, .element-container {
    background: rgba(255, 255, 255, 0.9);
    border-radius: 14px;
    padding: 1rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b5ed7, #0a4db8);
}

section[data-testid="stSidebar"] * {
    color: white !important;
    font-weight: 600;
}

.stButton > button {
    background: linear-gradient(135deg, #0b5ed7, #084298);
    color: white;
    font-weight: 700;
    border-radius: 10px;
    padding: 0.6rem 1rem;
    border: none;
}

.stButton > button:hover {
    box-shadow: 0 10px 25px rgba(11,94,215,0.4);
    transform: translateY(-2px);
}

[data-testid="metric-container"] {
    background: white;
    border-radius: 14px;
    padding: 1rem;
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
}

hr {
    border: none;
    height: 1px;
    background: linear-gradient(to right, transparent, #0b5ed7, transparent);
    margin: 2rem 0;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# Load Model and Scaler (NO cache_resource)
# =====================================================
try:
    model = joblib.load("diabetes_model.pkl")
    scaler = joblib.load("scaler_svm.pkl")
except FileNotFoundError:
    st.error("❌ Model files not found!")
    st.info("Make sure `diabetes_model.pkl` and `scaler_svm.pkl` exist.")
    st.stop()

# =====================================================
# Header
# =====================================================
st.title("🏥 Diabetes Prediction System")
st.markdown("### AI-Powered Health Risk Assessment")

# =====================================================
# Sidebar Inputs
# =====================================================
st.sidebar.title("⚙️ Patient Information")

st.sidebar.subheader("Demographics")
age = st.sidebar.slider("Age", 21, 100, 30)
pregnancies = st.sidebar.number_input("Pregnancies", 0, 20, 0)

st.sidebar.subheader("Medical Measurements")
glucose = st.sidebar.slider("Glucose (mg/dL)", 0, 200, 120)
bp = st.sidebar.slider("Blood Pressure (mm Hg)", 0, 130, 70)
skin = st.sidebar.slider("Skin Thickness (mm)", 0, 100, 20)
insulin = st.sidebar.slider("Insulin (µU/ml)", 0, 900, 80)
bmi = st.sidebar.number_input("BMI", 10.0, 70.0, 25.0, 0.1)
dpf = st.sidebar.slider("Diabetes Pedigree Function", 0.0, 2.5, 0.5, 0.01)

st.sidebar.markdown("---")
predict_btn = st.sidebar.button("🔮 Predict Risk", use_container_width=True)

# =====================================================
# Prediction
# =====================================================
if predict_btn:
    input_data = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])
    input_std = scaler.transform(input_data)

    prediction = model.predict(input_std)[0]

    try:
        prob = model.predict_proba(input_std)[0]
        prob_neg = prob[0] * 100
        prob_pos = prob[1] * 100
    except:
        prob_pos = 100 if prediction == 1 else 0
        prob_neg = 100 - prob_pos

    st.markdown("---")
    st.header("🎯 Prediction Results")

    col1, col2 = st.columns([2, 1])

    with col1:
        if prediction == 1:
            st.error("### 🔴 HIGH RISK – Diabetic")
        else:
            st.success("### ✅ LOW RISK – Non-Diabetic")

        c1, c2 = st.columns(2)
        c1.metric("Non-Diabetic", f"{prob_neg:.1f}%")
        c2.metric("Diabetic", f"{prob_pos:.1f}%")

    with col2:
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=prob_pos,
            number={'suffix': "%"},
            title={'text': "Risk Level"},
            gauge={
                'axis': {'range': [0, 100]},
                'steps': [
                    {'range': [0, 30], 'color': "lightgreen"},
                    {'range': [30, 70], 'color': "yellow"},
                    {'range': [70, 100], 'color': "red"}
                ],
                'bar': {'color': "#0b5ed7"}
            }
        ))
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.warning("""
⚠ **Medical Disclaimer**

This prediction is for educational purposes only.  
Always consult a healthcare professional for medical advice.
""")

else:
    st.info("👈 Enter patient details in the sidebar and click **Predict Risk**")

    c1, c2, c3 = st.columns(3)
    c1.metric("Model", "Support Vector Machine")
    c2.metric("Accuracy", "~78%")
    c3.metric("Dataset", "768 Records")

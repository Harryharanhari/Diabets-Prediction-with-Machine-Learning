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
# Custom CSS (Modern Medical UI)
# =====================================================
st.markdown("""
<style>

/* ===== Global ===== */
html, body, [class*="css"] {
    font-family: 'Inter', 'Segoe UI', sans-serif;
}

.main {
    background: linear-gradient(135deg, #f8fbff, #eef4ff);
    padding: 1.5rem 2rem;
}

/* ===== Headings ===== */
h1 {
    color: #0b5ed7;
    font-weight: 800;
}

h2, h3, h4 {
    color: #0d3b66;
    font-weight: 700;
}

/* ===== Cards ===== */
.stMetric, .stAlert, .element-container {
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(12px);
    border-radius: 14px;
    padding: 1rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}

/* ===== Sidebar ===== */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b5ed7, #0a4db8);
}

section[data-testid="stSidebar"] * {
    color: white !important;
    font-weight: 600;
}

/* ===== Buttons ===== */
.stButton > button {
    background: linear-gradient(135deg, #0b5ed7, #084298);
    color: white;
    font-weight: 700;
    border-radius: 10px;
    padding: 0.6rem 1rem;
    border: none;
    transition: 0.3s ease-in-out;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(11,94,215,0.4);
}

/* ===== Metrics ===== */
[data-testid="metric-container"] {
    background: white;
    border-radius: 14px;
    padding: 1rem;
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
}

[data-testid="metric-container"] label {
    font-size: 0.9rem;
    font-weight: 600;
    color: #6c757d;
}

[data-testid="metric-container"] div {
    font-size: 1.4rem;
    font-weight: 800;
    color: #0b5ed7;
}

/* ===== Divider ===== */
hr {
    border: none;
    height: 1px;
    background: linear-gradient(to right, transparent, #0b5ed7, transparent);
    margin: 2rem 0;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# Load Model and Scaler
# =====================================================
@st.cache_resource
def load_model_and_scaler():
    try:
        model = joblib.load("diabetes_model.pkl")
        scaler = joblib.load("scaler_svm.pkl")
        return model, scaler
    except FileNotFoundError:
        return None, None

model, scaler = load_model_and_scaler()

# =====================================================
# Header
# =====================================================
st.title("🏥 Diabetes Prediction System")
st.markdown("### AI-Powered Health Risk Assessment")

if model is None or scaler is None:
    st.error("❌ Model files not found!")
    st.info("Run the training script first to generate model files.")
    st.stop()

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
dpf = s


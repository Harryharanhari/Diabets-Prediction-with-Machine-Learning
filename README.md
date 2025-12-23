DIABETES PREDICTION USING MACHINE LEARNING
========================================

📌 Project Overview
-------------------
This project is a Machine Learning–based Diabetes Prediction System that predicts whether a person is diabetic or not based on key medical attributes.  
The model is deployed as an interactive web application using Streamlit.

The system helps users understand diabetes risk levels using input parameters such as glucose level, BMI, age, blood pressure, and other health indicators.

🔗 Live Application:
https://diabets-prediction-with-machine-learning-gjjrlctkmnjpbg4h4et5l.streamlit.app/


📊 Dataset
----------
- Dataset used: PIMA Indians Diabetes Dataset
- Total samples: 768
- Features:
  - Pregnancies
  - Glucose
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI
  - Diabetes Pedigree Function
  - Age
- Target Variable:
  - 0 → Non-Diabetic
  - 1 → Diabetic


🧠 Machine Learning Model
------------------------
- Algorithm Used: Support Vector Machine (SVM)
- Data Preprocessing:
  - Handling missing values
  - Feature scaling using StandardScaler
- Model Performance:
  - Accuracy: ~78%
- Trained model and scaler are saved using Joblib


🖥️ Web Application (Streamlit)
-------------------------------
Features of the web app:
- User-friendly sidebar input for patient details
- Real-time diabetes prediction
- Probability-based risk assessment
- Visual risk gauge using Plotly
- Risk factor analysis and health recommendations
- Medical disclaimer for educational use only


📁 Project Structure
-------------------
├── app.py                     # Streamlit web application
├── diabetes-prediction.ipynb  # Model training and analysis notebook
├── diabetes.csv               # Dataset
├── diabetes_model.pkl         # Trained SVM model
├── scaler_svm.pkl             # Feature scaler
├── requirements.txt           # Required Python libraries
└── README.txt                 # Project documentation


⚙️ Installation & Usage
-----------------------
1. Clone the repository:
   git clone <repository-url>

2. Navigate to the project directory:
   cd diabetes-prediction

3. Install dependencies:
   pip install -r requirements.txt

4. Run the Streamlit app:
   streamlit run app.py

5. Open the local URL displayed in the terminal.


🧪 Technologies Used
--------------------
- Python
- NumPy
- Pandas
- Scikit-learn
- Streamlit
- Plotly
- Joblib
- Matplotlib & Seaborn


⚠️ Disclaimer
-------------
This application is intended for educational and demonstration purposes only.  
It should NOT be used as a substitute for professional medical diagnosis or treatment.  
Always consult a qualified healthcare professional for medical advice.

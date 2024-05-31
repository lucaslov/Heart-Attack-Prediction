import streamlit as st
import requests
from pydantic import BaseModel

class HeartPrediction(BaseModel):
    age: int
    sex: int
    cp: int
    trtbps: int
    chol: int
    fbs: int
    restecg: int
    thalachh: int
    exng: int
    oldpeak: float
    slp: int
    caa: int
    thall: int

def show():
    st.title("Prediction Page")

    st.header("About this dataset")
    st.markdown("""
    - **Age**: Age of the patient
    - **Sex**: Sex of the patient
    - **exang**: exercise induced angina (1 = yes; 0 = no)
    - **ca**: number of major vessels (0-3)
    - **cp**: Chest Pain type
        - Value 1: typical angina
        - Value 2: atypical angina
        - Value 3: non-anginal pain
        - Value 4: asymptomatic
    - **trtbps**: resting blood pressure (in mm Hg)
    - **chol**: cholesterol in mg/dl fetched via BMI sensor
    - **fbs**: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
    - **rest_ecg**: resting electrocardiographic results
        - Value 0: normal
        - Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
        - Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria
    - **thalach**: maximum heart rate achieved
    - **target**: 0= less chance of heart attack 1= more chance of heart attack
    """)

    with st.form("prediction_form"):
        age = st.number_input("Age", min_value=0, max_value=120, value=25)
        sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
        cp = st.selectbox("Chest Pain Type (CP)", options=[1, 2, 3, 4], format_func=lambda x: {
            1: "typical angina",
            2: "atypical angina",
            3: "non-anginal pain",
            4: "asymptomatic"
        }[x])
        trtbps = st.number_input("Resting Blood Pressure (trtbps)", min_value=0, max_value=300, value=120)
        chol = st.number_input("Cholesterol (chol)", min_value=0, max_value=500, value=200)
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", options=[0, 1], format_func=lambda x: "True" if x == 1 else "False")
        restecg = st.selectbox("Resting ECG (restecg)", options=[0, 1, 2], format_func=lambda x: {
            0: "normal",
            1: "having ST-T wave abnormality",
            2: "showing probable or definite left ventricular hypertrophy"
        }[x])
        thalachh = st.number_input("Maximum Heart Rate Achieved (thalachh)", min_value=0, max_value=220, value=150)
        exng = st.selectbox("Exercise Induced Angina (exng)", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, value=1.0)
        slp = st.selectbox("Slope of the Peak Exercise ST Segment (slp)", options=[0, 1, 2], format_func=lambda x: {
            0: "Upsloping",
            1: "Flat",
            2: "Downsloping"
        }[x])
        caa = st.number_input("Number of Major Vessels (0-3) (caa)", min_value=0, max_value=3, value=0)
        thall = st.selectbox("Thalassemia (thall)", options=[0, 1, 2, 3], format_func=lambda x: {
            0: "Normal",
            1: "Fixed defect",
            2: "Reversible defect",
            3: "Unknown"
        }[x])

        submitted = st.form_submit_button("Predict")

        if submitted:
            data = HeartPrediction(
                age=age, sex=sex, cp=cp, trtbps=trtbps, chol=chol, fbs=fbs, 
                restecg=restecg, thalachh=thalachh, exng=exng, oldpeak=oldpeak, 
                slp=slp, caa=caa, thall=thall
            )
            try:
                response = requests.post("http://fastapi-be:8000/api/predict", json=data.dict())
                response.raise_for_status()
                prediction = response.json()
                st.success(f"Prediction: {prediction}")
            except requests.ConnectionError:
                st.error("Failed to connect to the backend. Please ensure the backend is running and accessible.")
            except requests.RequestException as e:
                st.error(f"An error occurred: {e}")

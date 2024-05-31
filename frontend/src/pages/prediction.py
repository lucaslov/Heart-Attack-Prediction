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
    
    with st.form("prediction_form"):
        age = st.number_input("Age", min_value=0, max_value=120, value=25)
        sex = st.selectbox("Sex", options=[0, 1])
        cp = st.selectbox("Chest Pain Type (CP)", options=[0, 1, 2, 3])
        trtbps = st.number_input("Resting Blood Pressure (trtbps)", min_value=0, max_value=300, value=120)
        chol = st.number_input("Cholesterol (chol)", min_value=0, max_value=500, value=200)
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", options=[0, 1])
        restecg = st.selectbox("Resting ECG (restecg)", options=[0, 1, 2])
        thalachh = st.number_input("Maximum Heart Rate Achieved (thalachh)", min_value=0, max_value=220, value=150)
        exng = st.selectbox("Exercise Induced Angina (exng)", options=[0, 1])
        oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, value=1.0)
        slp = st.selectbox("Slope of the Peak Exercise ST Segment (slp)", options=[0, 1, 2])
        caa = st.number_input("Number of Major Vessels (0-3) (caa)", min_value=0, max_value=3, value=0)
        thall = st.selectbox("Thalassemia (thall)", options=[0, 1, 2, 3])
        
        submitted = st.form_submit_button("Predict")
        
        if submitted:
            data = HeartPrediction(
                age=age, sex=sex, cp=cp, trtbps=trtbps, chol=chol, fbs=fbs, 
                restecg=restecg, thalachh=thalachh, exng=exng, oldpeak=oldpeak, 
                slp=slp, caa=caa, thall=thall
            )
            try:
                response = requests.post("http://localhost:8000/predict", json=data.dict())
                response.raise_for_status()
                prediction = response.json()
                st.success(f"Prediction: {prediction}")
            except requests.ConnectionError:
                st.error("Failed to connect to the backend. Please ensure the backend is running and accessible.")
            except requests.RequestException as e:
                st.error(f"An error occurred: {e}")

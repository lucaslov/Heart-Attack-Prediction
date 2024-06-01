import streamlit as st
import requests
import pandas as pd

def show():
    st.title("Work with Data")

    if st.button("Run Kedro Pipelines"):
        with st.spinner('Running pipelines...'):
            response = requests.post("http://fastapi-be:8000/api/run_pipelines")
        if response.status_code == 200:
            st.success("Pipelines executed and new model generated successfully")
        else:
            st.error(f"Error running pipelines: {response.json()['detail']}")
    
    if st.button("Remove Entire Dataset"):
        with st.spinner('Removing dataset...'):
            response = requests.delete("http://fastapi-be:8000/api/delete_dataset/heart")
        if response.status_code == 200:
            st.success("Dataset removed successfully")
        else:
            st.error(f"Error removing dataset: {response.json()['detail']}")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
        
        if st.button("Import New CSV"):
            uploaded_file.seek(0)  # Reset the file pointer to the beginning after reading it
            with st.spinner('Uploading and processing...'):
                response = requests.post(
                    "http://fastapi-be:8000/api/import_data/heart",
                    files={"file": (uploaded_file.name, uploaded_file, "text/csv")}
                )
            if response.status_code == 200:
                st.success("Data appended to dataset successfully")
            else:
                st.error(f"Error importing dataset: {response.json().get('detail', 'Unknown error')}")

    
    st.subheader("Add Single Row to Raw Data")
    new_row = {
        "age": st.number_input("Age", min_value=0, max_value=120, value=25),
        "sex": st.selectbox("Sex", options=[0, 1]),
        "cp": st.selectbox("Chest Pain Type", options=[0, 1, 2, 3]),
        "trtbps": st.number_input("Resting Blood Pressure", min_value=0, max_value=300, value=120),
        "chol": st.number_input("Cholesterol", min_value=0, max_value=500, value=200),
        "fbs": st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[0, 1]),
        "restecg": st.selectbox("Resting ECG", options=[0, 1, 2]),
        "thalachh": st.number_input("Maximum Heart Rate Achieved", min_value=0, max_value=220, value=150),
        "exng": st.selectbox("Exercise Induced Angina", options=[0, 1]),
        "oldpeak": st.number_input("Oldpeak", min_value=0.0, max_value=10.0, value=1.0),
        "slp": st.selectbox("Slope of the Peak Exercise ST Segment", options=[0, 1, 2]),
        "caa": st.number_input("Number of Major Vessels (0-3)", min_value=0, max_value=3, value=0),
        "thall": st.selectbox("Thalassemia", options=[0, 1, 2, 3])
    }
    
    if st.button("Add Row"):
        with st.spinner('Adding row...'):
            response = requests.post(
                f"http://fastapi-be:8000/api/add_row/heart",
                json=new_row
            )
        if response.status_code == 200:
            st.success("Row added successfully")
        else:
            st.error(f"Error adding row: {response.json()['detail']}")
    
    st.subheader("Remove Row from Raw Data")
    row_id = st.number_input("Row ID to Remove", min_value=0)
    
    if st.button("Remove Row"):
        with st.spinner('Removing row...'):
            response = requests.delete(f"http://fastapi-be:8000/api/remove_row/heart/{row_id}")
        if response.status_code == 200:
            st.success("Row removed successfully")
        else:
            st.error(f"Error removing row: {response.json()['detail']}")

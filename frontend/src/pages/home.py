import streamlit as st
import pandas as pd
import requests

def show():
    st.title("Explore datasets")
    datasets = [
        ("Heart Dataset", "heart"),
        ("Processed Heart Dataset", "heart_processed"),
        ("Heart Training Dataset", "heart_train"),
        ("Heart Testing Dataset", "heart_test")
    ]
    dataset_dict = {label: value for label, value in datasets}
    selected_label = st.selectbox("Select dataset name:", list(dataset_dict.keys()))
    dataset_name = dataset_dict[selected_label]
    
    if st.button("Load Data"):
        response = requests.get(f"http://fastapi-be:8000/api/heart_data/{dataset_name}")
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)
            st.dataframe(df)
        else:
            st.error("Error loading data")

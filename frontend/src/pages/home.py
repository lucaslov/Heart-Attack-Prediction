import streamlit as st
import pandas as pd
import requests

def show():
    st.title("Home Page - Raw Data")
    dataset_name = st.text_input("Enter dataset name:", "heart_raw")
    
    if st.button("Load Data"):
        response = requests.get(f"http://fastapi-be:8000/heart_data/{dataset_name}")
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)
            st.dataframe(df)
        else:
            st.error("Error loading data")

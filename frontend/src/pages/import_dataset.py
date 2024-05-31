import streamlit as st
import requests
import pandas as pd

def show():
    st.title("Import New Dataset")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
        
        if st.button("Import and Run Pipeline"):
            with st.spinner('Uploading and processing...'):
                response = requests.post(
                    "http://fastapi-be:8000/import_data",
                    files={"file": (uploaded_file.name, uploaded_file, "text/csv")}
                )
            
            if response.status_code == 200:
                st.success("Dataset imported and pipeline executed successfully")
            else:
                st.error("Error importing dataset or running pipeline")

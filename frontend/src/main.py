import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Heart Attack Prediction App", layout="wide")

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("styles.css")

with st.sidebar:
    selected = option_menu(
        menu_title="Menu", 
        options=["Home", "Prediction", "Work with data"],
        icons=["house", "graph-up", "cloud-upload"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Home":
    from pages import home
    home.show()
elif selected == "Prediction":
    from pages import prediction
    prediction.show()
elif selected == "Work with data":
    from pages import work_with_data
    work_with_data.show()

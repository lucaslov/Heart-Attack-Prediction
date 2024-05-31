import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Heart Disease Prediction App", layout="wide")

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu", 
        options=["Home", "Prediction", "Import Dataset"],
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
elif selected == "Import Dataset":
    from pages import import_dataset
    import_dataset.show()

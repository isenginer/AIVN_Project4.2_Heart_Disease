import streamlit as st

# from src.data_loader.loader import (
#     load_data,
#     load_feature_engineered_data,
#     load_feature_stats,
#     load_model,
# )
# from src.ui_builder.dashboard import historical_sales_view
# from src.ui_predictor.prediction import sales_prediction_view

# Page configuration
st.set_page_config(page_title="HEART DECEASE DIAGNOSTIC APPLICATION", page_icon="📈", layout="wide")


if __name__=="__main__":
    # Sidebar
    st.sidebar.title("Heart Decease Diagnostics")
    page = st.sidebar.selectbox(
        "Choose a page", ["Historical Sales Analysis", "Sales Prediction"]
    )
import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="House Price Prediction", page_icon="🏠", layout="centered")

st.markdown("""
    <style>
    /* Set background color for the whole app */
    .reportview-container {
        background: #f0f2f6;
    }
    /* Style the main content container */
    .main {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    /* Style the prediction button */
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 1.1rem;
        padding: 0.5rem 1.5rem;
        border: none;
        border-radius: 5px;
    }
    /* Adjust input box style */
    .stNumberInput>div>input {
        font-size: 1rem;
        padding: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

model = joblib.load('house_price_model.pkl')

with st.container():
    st.title("🏠 House Price Prediction App")
    st.write("Enter the details of the house below to predict its price.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        bedrooms = st.number_input("Bedrooms", min_value=0, value=3)
    with col2:
        bathrooms = st.number_input("Bathrooms", min_value=0, value=2)
    with col3:
        sqft_living = st.number_input("Living Area (sqft)", min_value=0, value=1500)
    
    st.markdown("---")
    
    if st.button("Predict Price"):
        input_data = np.array([[bedrooms, bathrooms, sqft_living]])
        predicted_price = model.predict(input_data)
        st.success(f"Predicted House Price: ${predicted_price[0]:,.2f}")

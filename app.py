import streamlit as st
import pandas as pd
import joblib

# load model
model = joblib.load("model.pkl")

st.title("🏠 House Price Predictor")

# inputs
size = st.number_input("Size (sqft)", min_value=0)
age = st.number_input("Age (years)", min_value=0)
distance = st.number_input("Distance to center (km)", min_value=0)

# predict
if st.button("Predict"):
    user_data = pd.DataFrame(
        [[size, age, distance]],
        columns=['size_sqft', 'age_years', 'distance_to_center_km']
    )

    pred = model.predict(user_data)

    st.success(f"Predicted Price: ₹{pred[0]:,.0f}")
    
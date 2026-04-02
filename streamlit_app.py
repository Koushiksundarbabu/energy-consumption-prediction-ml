import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Page config
st.set_page_config(page_title="Energy Predictor", layout="centered")

# Background styling
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #eef2ff, #e0f2fe);
    }
    header {
        background-color: transparent !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load model
model = joblib.load("energy_model.pkl")

# Title + subtitle
st.title("⚡ Energy Consumption Predictor")

st.write("Predict your electricity usage based on past 3 days")

st.divider()

# Inputs
date = st.date_input("📅 Select date to predict")

lag_1 = st.number_input("⚡ Yesterday usage (kWh)", min_value=0.0)
lag_2 = st.number_input("⚡ 2 days ago usage (kWh)", min_value=0.0)
lag_3 = st.number_input("⚡ 3 days ago usage (kWh)", min_value=0.0)

# Prediction
if st.button("Predict"):

    # Convert date
    date = pd.to_datetime(date)

    day = date.day
    month = date.month
    weekday = date.weekday()

    # Feature engineering
    rolling_mean_3 = (lag_1 + lag_2 + lag_3) / 3

    features = np.array([[day, month, weekday,
                          lag_1, lag_2, lag_3,
                          rolling_mean_3]])

    prediction = model.predict(features)[0]

    # Output
    st.success(f"🔮 Predicted Energy Usage: {prediction:.2f} kWh")

    # Insight
    diff = prediction - lag_1
    if diff > 0:
        st.warning(f"⚠️ Expected increase of {diff:.2f} kWh from yesterday")
    else:
        st.info(f"⬇️ Expected decrease of {abs(diff):.2f} kWh from yesterday")
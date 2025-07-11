# streamlit_app.py

import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
from src.data_collector import get_live_traffic_data

# Load model & pipeline
model = joblib.load("models/traffic_model.pkl")
pipeline = joblib.load("models/preprocess_pipeline.pkl")

st.set_page_config(page_title="🚦 Real-Time Traffic Predictor", layout="centered")

st.title("🚦 Real-Time Traffic Congestion Predictor")
st.markdown("**Route:** Sector 12A, Gurugram → IGI Airport, Delhi")

# Button to trigger prediction
if st.button("📡 Predict Current Traffic"):
    live_data = get_live_traffic_data()
    df = pd.DataFrame([live_data])

    # Display real-time values
    st.subheader("📍 Live Traffic Data")
    st.write(df)

    # Predict
    features = pipeline.transform(df)
    prediction = model.predict(features)[0]

    st.subheader("🧠 Prediction")
    st.success(f"Current Congestion Level: **{prediction}**")

    st.caption(f"Prediction made at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

st.markdown("---")
st.markdown("👩‍💻 Built with Google Maps API + RandomForest + Streamlit")

import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load('plant_disease_predictor/model/model.pkl')
scaler = joblib.load('plant_disease_predictor/model/scaler.pkl')

st.title("Plant Disease Predictor")

# Create input sliders
temperature = st.slider("Temperature (C)", 0, 50, 25)
humidity = st.slider("Humidity (%)", 0, 100, 50)
rainfall = st.slider("Rainfall (mm)", 0, 300, 50)
soil_pH = st.slider("Soil pH", 3, 10, 6)

# Collect inputs into a numpy array
input_data = np.array([[temperature, humidity, rainfall, soil_pH]])
input_scaled = scaler.transform(input_data)

# Predict using the model
if st.button("Predict"):
    prediction = model.predict(input_scaled)[0]
    result = "✅ Disease Present" if prediction == 1 else "🟢 No Disease Detected"
    st.success(result)

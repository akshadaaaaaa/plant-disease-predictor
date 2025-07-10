# 🌿 Plant Disease Predictor

This Streamlit app predicts whether a plant is likely to have a disease based on environmental conditions.

## Features
- User input sliders for temperature, humidity, rainfall, and soil pH
- Uses a logistic regression model trained on real data
- Scaled using `StandardScaler` for accurate predictions


## Model Info
- Logistic Regression (scikit-learn)
- StandardScaler applied to inputs

## How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py

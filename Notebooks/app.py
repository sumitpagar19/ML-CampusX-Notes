import joblib
import numpy as np
import streamlit as st

# Load model and preprocessing pipeline
model = joblib.load('house_price_model.pkl')
preprocessor = joblib.load('preprocessor.pkl')  # scaler+encoder pipeline

# Take inputs from user (raw 12 features)
area = st.number_input("Area")
bedrooms = st.number_input("Bedrooms")
# ... baaki inputs

# Collect inputs in right order
input_data = np.array([[area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwaterheating, airconditioning, parking, prefarea, furnishingstatus]])

# Apply preprocessing
input_processed = preprocessor.transform(input_data)

# Predict
prediction = lr.predict(input_processed)[0]

st.success(f"Predicted price: ₹{int(prediction):,}")

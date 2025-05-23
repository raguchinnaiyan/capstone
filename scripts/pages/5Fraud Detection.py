import streamlit as st
import joblib
import numpy as np

# Title
st.set_page_config(page_title="Insurance Fraud Detection", layout="centered",page_icon="🕵️‍♂️")
st.title(" 🕵️‍♂️ Insurance Fraud Detection")

# User inputs
st.header("Enter Claim Details")

# Load the model
pipeline = joblib.load("C:/Users/ragu/capstone_pj/models/fru_det_pilin.pkl")

# Input fields
claim_amount = st.number_input("Enter claim amount:", min_value=0)
suspicious_flags = st.selectbox("Suspicious flags?", [0, 1])
claim_type_vehicle = st.selectbox("Is claim type Vehicle?", [0, 1])
claim_type_medical = st.selectbox("Is claim type Medical?", [0, 1])
claim_type_home_damage = st.selectbox("Is claim type Home Damage?", [0, 1])

if st.button("Predict Fraud Status"):
    user_input = np.array([[
        claim_amount,
        suspicious_flags,
        claim_type_vehicle,
        claim_type_medical,
        claim_type_home_damage
    ]])

    prediction = pipeline.predict(user_input)[0]
    
    if prediction == 1:
        st.error("🚨 Fraudulent Claim")
    else:
        st.success("✅ Genuine Claim")

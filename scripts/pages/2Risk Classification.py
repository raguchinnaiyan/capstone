import streamlit as st
import pickle
import numpy as np 
import joblib

# Load your trained model
model = joblib.load("C:/Users/ragu/capstone_pj/models/risk_classification2.pkl")

# Page setup
st.set_page_config(page_title="Risk Classification", page_icon="⚠️")
st.title("⚠️ Risk Classification Predictor")
st.markdown("Enter customer details to predict whether the insurance risk is **High** or **Low**.")

# User Inputs
customer_age = st.slider("Customer Age", 18, 100, 69)
annual_income = st.number_input("Annual Income (in USD)", value=99375.03, step=100.0)
property_age = st.slider("Property Age (in years)", 0, 50, 3)
claim_history = st.radio("Claim History", options=[0, 1], index=1, help="1 = Previous claim, 0 = No claim")
premium_amount = st.number_input("Premium Amount", value=552.0, step=10.0)
claim_amount = st.number_input("Claim Amount", value=4075.14, step=10.0)
fraudulent_claim = st.radio("Is it a Fraudulent Claim?", options=[0, 1], index=0)

# Encoded categorical fields
gender = st.selectbox("Gender", ["Male", "Female"])
gender_male = 1 if gender == "Male" else 0

policy_type = st.selectbox("Policy Type", ["Health", "Life", "Property"])
policy_type_health = 1 if policy_type == "Health" else 0
policy_type_life = 1 if policy_type == "Life" else 0
policy_type_property = 1 if policy_type == "Property" else 0

# Prepare input vector
input_data = np.array([[customer_age, annual_income, property_age, claim_history,
                        premium_amount, claim_amount, fraudulent_claim,
                        gender_male, policy_type_health, policy_type_life, policy_type_property]])

# Prediction
if st.button("Predict Risk Level"):
    prediction = model.predict(input_data)[0]
    risk = "High Risk" if prediction == 1 else "Low Risk"
    st.subheader(f"🛡️ Prediction: **{risk}**")

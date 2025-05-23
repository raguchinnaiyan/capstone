import streamlit as st
import joblib
import pandas as pd

# Load the trained pipeline model
model = joblib.load("C:/Users/ragu/capstone_pj/models/ridge_claim_model.pkl")

st.set_page_config(page_title="Insurance Claim Amount Prediction", layout="centered",page_icon="🧮")
st.title("🧮 Insurance Claim Amount Prediction")
st.markdown("Enter the customer and policy details to estimate the claim amount.")

# Input form
with st.form("claim_form"):
    customer_age = st.slider("Customer Age", 18, 100, 46)
    gender = st.selectbox("Gender", ["Female", "Male"])
    policy_type = st.selectbox("Policy Type", ["Health", "Life", "Property"])
    annual_income = st.number_input("Annual Income (₹)", min_value=0.0, value=79249.71)
    property_age = st.number_input("Property Age (years)", min_value=0, value=7)
    claim_history = st.selectbox("Has Previous Claims?", ["No", "Yes"])
    premium_amount = st.number_input("Premium Amount (₹)", min_value=0.0, value=356.0)
    fraudulent_claim = st.selectbox("Is Fraudulent Claim?", ["No", "Yes"])
    
    submitted = st.form_submit_button("Predict Claim Amount")

# Handle form submission
if submitted:
    # Convert categorical inputs
    gender_val = 1 if gender == "Male" else 0
    policy_map = {"Health": 0, "Life": 1, "Property": 2}
    policy_type_val = policy_map[policy_type]
    claim_history_val = 1 if claim_history == "Yes" else 0
    fraudulent_claim_val = 1 if fraudulent_claim == "Yes" else 0

    # Prepare DataFrame
    input_data = {
        "customer_age": customer_age,
        "gender": gender_val,
        "policy_type": policy_type_val,
        "annual_income": annual_income,
        "property_age": property_age,
        "claim_history": claim_history_val,
        "premium_amount": premium_amount,
        "fraudulent_claim": fraudulent_claim_val
    }

    input_df = pd.DataFrame([input_data])

    # Make prediction
    prediction = model.predict(input_df)[0]

    st.success(f"💰 Estimated Claim Amount: ₹{prediction:,.2f}")

import streamlit as st
import pandas as pd
import joblib

# Load your scaler and clustering model
scaler = joblib.load("C:/Users/ragu/capstone_pj/models/scaler_cs.pkl")
dbscan = joblib.load("C:/Users/ragu/capstone_pj/models/dbscan_model_cs.pkl")
cluster_names = {0: "Budget Conscious", 1: "Premium", 2: "Risk Aware", -1: "Unclassified"}  # example

# Dropdown values based on your chart
location_options = [
    "Mizoram", "Goa", "Rajasthan", "Sikkim", "West Bengal", "Uttar Pradesh", "Himachal Pradesh",
    "Manipur", "Gujarat", "Andaman and Nicobar Islands", "Tripura", "Nagaland", "Karnataka", 
    "Odisha", "Maharashtra", "Telangana", "Delhi", "Chandigarh", "Jharkhand", "Arunachal Pradesh", 
    "Tamil Nadu", "Dadra and Nagar Haveli", "Lakshadweep", "Bihar", "Daman and Diu", "Assam", 
    "Punjab", "Haryana", "Chhattisgarh", "Puducherry", "Uttarakhand", "Andhra Pradesh", "Kerala", 
    "Madhya Pradesh", "Meghalaya"
]
policy_type_map = {"Family": 0, "Group": 1, "Individual": 2, "Business": 3}
policy_category_map = {"Policy 1": 1, "Policy 2": 2, "Policy 3": 3, "Policy 4": 4}
    
# Streamlit UI
st.set_page_config(page_title="Customer Segmentation", layout="centered",page_icon="📊")
st.title(" 📊 Customer Segmentation")

age = st.number_input("Age", 18, 100, 30)
income_level = st.number_input("Income Level", 10000, 1000000, 50000)
coverage_amount = st.number_input("Coverage Amount", 10000, 1000000, 500000)
premium_amount = st.number_input("Premium Amount", 100, 10000, 1200)
policy_upgrades = st.number_input("Policy Upgrades", 0, 10, 1)
number_of_policies = st.number_input("Number of Policies", 1, 10, 2)

gender = st.radio("Gender", ["Male", "Female"])
gender_male = 1 if gender == "Male" else 0

location = st.selectbox("Location", location_options)
location_index = location_options.index(location)  # integer encoded location

occupation = st.selectbox("Occupation", [
    "Doctor", "Engineer", "Entrepreneur", "Lawyer", "Manager", "Nurse", "Salesperson", "Teacher"
])

# One-hot encode the selected occupation
occupations = {
    "occupation_Doctor": 0,
    "occupation_Engineer": 0,
    "occupation_Entrepreneur": 0,
    "occupation_Lawyer": 0,
    "occupation_Manager": 0,
    "occupation_Nurse": 0,
    "occupation_Salesperson": 0,
    "occupation_Teacher": 0,
}
occupations[f"occupation_{occupation}"] = 1

# Select Policy Type and Category
policy_type = st.selectbox("Policy Type", list(policy_type_map.keys()))
policy_category = st.selectbox("Policy Category", list(policy_category_map.keys()))

if st.button("Predict Cluster"):
    input_data = pd.DataFrame([{
        "age": age,
        "location": location_index,
        "income_level": income_level,
        "coverage_amount": coverage_amount,
        "premium_amount": premium_amount,
        "policy_upgrades": policy_upgrades,
        "number_of_policies": number_of_policies,
        "gender_Male": gender_male,
        **occupations
    }])

    scaled_data = scaler.transform(input_data)
    label = dbscan.fit_predict(scaled_data)[0]
    cluster_name = cluster_names.get(label, "Unknown")

    st.success(f"This customer belongs to the segment: **{cluster_name}**")

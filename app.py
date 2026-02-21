import streamlit as st
import pandas as pd
import joblib

# -------------------------------
# Load Model and Feature Schema
# -------------------------------

model = joblib.load("xgb_loan_model.joblib")
feature_order = joblib.load("feature_order.joblib")

# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(page_title="Loan Approval Predictor", layout="centered")

st.title("🏦 Loan Approval Prediction")
st.write("Enter applicant details below")

# -------------------------------
# User Inputs
# -------------------------------

age = st.number_input("Age", 18, 100, 30)
credit_score = st.number_input("Credit Score", 300, 900, 650)
credit_history_years = st.number_input("Credit History (Years)", 0, 50, 5)
income = st.number_input("Annual Income", min_value=0.0, value=50000.0)
loan_amount = st.number_input("Loan Amount", min_value=0.0, value=10000.0)
debt_to_income_ratio = st.number_input("Debt to Income Ratio", 0.0, 1.0, 0.3)
payment_to_income_ratio = st.number_input("Payment to Income Ratio", 0.0, 1.0, 0.2)
delinquencies_last_2yrs = st.number_input("Delinquencies (Last 2 Years)", 0, 50, 0)
defaults_on_file = st.number_input("Defaults on File", 0, 20, 0)

loan_intent = st.selectbox(
    "Loan Intent",
    ["Debt Consolidation", "Personal", "Education", "Medical", "Home Improvement", "Venture"]
)

# -------------------------------
# Prediction Button
# -------------------------------

if st.button("Predict"):

    # Initialize all features to 0
    input_data = {feature: 0 for feature in feature_order}

    # Fill numeric values
    input_data["age"] = age
    input_data["credit_score"] = credit_score
    input_data["credit_history_years"] = credit_history_years
    input_data["income"] = income
    input_data["loan_amount"] = loan_amount
    input_data["debt_to_income_ratio"] = debt_to_income_ratio
    input_data["payment_to_income_ratio"] = payment_to_income_ratio
    input_data["delinquencies_last_2yrs"] = delinquencies_last_2yrs
    input_data["defaults_on_file"] = defaults_on_file

    # Handle one-hot encoding
    intent_column = f"loan_intent_{loan_intent}"
    if intent_column in input_data:
        input_data[intent_column] = 1

    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])
    input_df = input_df[feature_order]

    # Predict
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    # Display result
    if prediction == 1:
        st.success(f"✅ Loan Approved (Confidence: {probability:.2%})")
    else:
        st.error(f"❌ Loan Rejected (Risk Score: {probability:.2%})")

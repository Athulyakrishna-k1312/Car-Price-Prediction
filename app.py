import streamlit as st
import pandas as pd
import joblib

# Load model and column names
model = joblib.load("model.pkl")
model_columns = joblib.load("model_columns.pkl")

st.title("🚗 Car Price Prediction")

st.write("Enter the car details below:")

year = st.number_input("Year", min_value=1990, max_value=2025, value=2018)

present_price = st.number_input("Present Price (Lakhs)", min_value=0.0)

kms_driven = st.number_input("Kilometers Driven", min_value=0)

owner = st.selectbox("Owner", [0, 1, 2, 3])

fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])

seller = st.selectbox("Seller Type", ["Dealer", "Individual"])

transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

if st.button("Predict Price"):

    input_data = {
        "Year": year,
        "Present_Price": present_price,
        "Kms_Driven": kms_driven,
        "Owner": owner,
        "Fuel_Type_Diesel": 0,
        "Fuel_Type_Petrol": 0,
        "Seller_Type_Individual": 0,
        "Transmission_Manual": 0
    }

    if fuel == "Diesel":
        input_data["Fuel_Type_Diesel"] = 1

    elif fuel == "Petrol":
        input_data["Fuel_Type_Petrol"] = 1

    if seller == "Individual":
        input_data["Seller_Type_Individual"] = 1

    if transmission == "Manual":
        input_data["Transmission_Manual"] = 1

    input_df = pd.DataFrame([input_data])

    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(input_df)

    st.success(f"Estimated Selling Price: ₹ {prediction[0]:.2f} Lakhs")
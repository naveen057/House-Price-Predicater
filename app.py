import streamlit as st
import joblib


def model_prediction(input_data):
    load_model = joblib.load('save_model.joblib')
    pred_sc = load_model.predict(input_data)
    return pred_sc


st.title("House Price Prediction")
st.subheader("Give features of the house you wish")

# Input fields for user input
bedrooms = st.number_input('No. of bedrooms in a house', min_value=1, max_value=10, value=3, step=1)
bathrooms = st.number_input('No. of bathrooms', min_value=1, max_value=10, value=2, step=1)
sqft_living = st.slider("Select the living area (in sqft):", min_value=500, max_value=1000, step=10)
sqft_lot = st.slider("Select the lot size (in sqft):", min_value=500, max_value=500000, value=7500, step=50)
floors = st.number_input("Enter no. of floors", min_value=1, max_value=3, value=1)
grade = st.slider("Select the house grade (1-10)", min_value=1, max_value=10, value=7)
zipcode = st.text_input("Enter the zipcode (numeric only)")

if zipcode:
    if not zipcode.isdigit():
        st.error("Zipcode must be numeric!")
    else:
        zipcode = int(zipcode)  

if st.button("Predict Price"):
    # Ensure zipcode is processed before prediction
    if isinstance(zipcode, int):
        import pandas as pd
        in_data = pd.DataFrame([[bedrooms, bathrooms, sqft_living, sqft_lot, floors, grade, zipcode]],
                       columns=['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'grade', 'zipcode'])

        st.write("Button clicked!\nRunning prediction...", model_prediction(in_data))

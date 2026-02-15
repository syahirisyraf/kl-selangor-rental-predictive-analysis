import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="Predictor", layout="wide")

# Load model and label encoders
model = joblib.load("model/random_forest_model.joblib")
label_encoders = joblib.load("model/label_encoders.joblib")

# Get location options grouped by region
df = pd.read_csv("data/mudah-apartment-kl-selangor-cleaned.csv")
locations_by_region = df.groupby("region")["location"].unique().to_dict()

st.title("Rental Price Predictor")
st.write("Fill in the property details below to predict the monthly rent.")

# Region and Location outside form for live filtering
col_region, col_location = st.columns(2)
with col_region:
    region = st.selectbox("Region", options=label_encoders["region"].classes_)
with col_location:
    location = st.selectbox("Location", options=sorted(locations_by_region[region]))

# Input form
with st.form("predictor_form"):
    col1, col2 = st.columns(2)

    with col1:
        property_type = st.selectbox("Property Type", options=label_encoders["property_type"].classes_)
        furnished = st.selectbox("Furnished", options=label_encoders["furnished"].classes_)
        size = st.number_input("Size (sq.ft)", min_value=100, max_value=10000, value=800, step=50)

    with col2:
        rooms = st.number_input("Rooms", min_value=1, max_value=10, value=3)
        bathroom = st.number_input("Bathroom", min_value=1, max_value=8, value=2)
        parking = st.number_input("Parking", min_value=0, max_value=10, value=1)

    col3, col4 = st.columns(2)
    with col3:
        facilities_count = st.slider("Facilities Count", min_value=0, max_value=14, value=5)
    with col4:
        additional_facilities_count = st.slider("Additional Facilities Count", min_value=0, max_value=6, value=2)

    submitted = st.form_submit_button("Predict Rent", use_container_width=True)

if submitted:
    # Encode categorical inputs using the same label encoders
    input_data = pd.DataFrame([{
        "region": label_encoders["region"].transform([region])[0],
        "location": label_encoders["location"].transform([location])[0],
        "property_type": label_encoders["property_type"].transform([property_type])[0],
        "rooms": rooms,
        "parking": parking,
        "bathroom": bathroom,
        "size (sq.ft)": size,
        "furnished": label_encoders["furnished"].transform([furnished])[0],
        "facilities_count": facilities_count,
        "additional_facilities_count": additional_facilities_count,
    }])

    # Predict (model outputs log scale, reverse with expm1)
    prediction_log = model.predict(input_data)[0]
    prediction = np.expm1(prediction_log)

    st.divider()
    st.subheader("Predicted Monthly Rent")
    st.metric(label="Estimated Rent", value=f"RM {prediction:,.0f}", border=True)
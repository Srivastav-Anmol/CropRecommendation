import streamlit as st
import pickle
with open('rf_model.pkl', 'rb') as file:
    model = pickle.load(file)
st.title("Crop Recommendation Application")
st.write("Please enter the values for the following fields:")
field_1 = st.number_input("Nitrogen Concentration", value=0.0)
field_2 = st.number_input("Phosphorus Concentration", value=0.0)
field_3 = st.number_input("Potassium Concentration", value=0.0)
field_4 = st.number_input("Temperature", value=0.0)
field_5 = st.number_input("Humidity", value=0.0)
field_6 = st.number_input("Ph", value=0.0)
field_7 = st.number_input("Rainfall", value=0.0)
if st.button("Submit"):
    input_data = [[field_1, field_2, field_3, field_4, field_5, field_6, field_7]]
    prediction = model.predict(input_data)[0].upper()
    st.write("The model prediction is:", prediction)


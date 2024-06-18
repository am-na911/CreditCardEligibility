import streamlit as st
import pandas as pd
import requests

def get_user_input():
    annual_income = st.number_input('Annual Income', min_value=0, value=50000)
    employed_days = st.number_input('Employed Days', min_value=0, value=3650)
    family_members = st.number_input('Family Members', min_value=0)
    gender = st.selectbox('Gender', ['Male',"female"])
    car_owner = st.selectbox('Car Owner', ['Yes', 'No'])
    property_owner = st.selectbox('Property Owner', ['Yes','No'])
    type_income = st.selectbox('Type of Income', ['Salaried', 'Business', 'Other'])
    education = st.selectbox('Education Level', ['High School', 'Bachelor', 'Master', 'PhD'])
    marital_status = st.selectbox('Marital Status', ['Single', 'Married', 'Divorced'])
    housing_type = st.selectbox('Housing Type', ['Rented', 'Owned', 'Mortgaged'])

    user_data = {
        'Annual_income': annual_income,
        'Employed_days': employed_days,
        'Family_Members': family_members,
        'GENDER': gender,
        'Car_Owner': car_owner,
        'Propert_Owner': property_owner,
        'Type_Income': type_income,
        'EDUCATION': education,
        'Marital_status': marital_status,
        'Housing_type': housing_type
    }
    
    return pd.DataFrame(user_data, index=[0])

# streamlit app
st.title('Credit CArd Eligibility Bot')
st.write("""
## Please provide the following details:
""")

# get user input
input_df = get_user_input()
st.write(input_df)

#prediction button
if st.button('Check Eligibility'):
    response = requests.post('http://127.0.0.1:5000/predict', json=input_df.to_dict(orient='records')[0])
    prediction = response.json()
    st.write(f"### Prediction: {'Eligible' if prediction['prediction'] == 1 else 'Not Eligible'}")
import streamlit as st
import pandas as pd
import joblib

# Load trained model

model = joblib.load('hospital_stay_model.pkl')

# Page configuration

st.set_page_config(
    page_title='Hospital Stay Prediction',
    layout='wide'
)

# Title

st.title('🏥 Hospital Stay Duration Prediction')

st.markdown(
    """
    Predict whether the patient will require:
    
    - 🟢 Short Stay
    - 🟡 Medium Stay
    - 🔴 Long Stay
    """
)

# Sidebar

st.sidebar.header('Patient Information')

# Inputs

Hospital_code = st.sidebar.number_input(
    'Hospital Code',
    min_value=1,
    max_value=50,
    value=10
)

Hospital_type_code = st.sidebar.selectbox(
    'Hospital Type Code',
    [0, 1, 2, 3, 4, 5, 6]
)

City_Code_Hospital = st.sidebar.number_input(
    'City Code Hospital',
    min_value=1,
    max_value=13,
    value=5
)

Hospital_region_code = st.sidebar.selectbox(
    'Hospital Region Code',
    [0, 1, 2]
)

Available_Extra_Rooms = st.sidebar.slider(
    'Available Extra Rooms in Hospital',
    0,
    20,
    3
)

Department = st.sidebar.selectbox(
    'Department',
    [0, 1, 2, 3, 4]
)

Ward_Type = st.sidebar.selectbox(
    'Ward Type',
    [0, 1, 2, 3, 4, 5]
)

Ward_Facility_Code = st.sidebar.selectbox(
    'Ward Facility Code',
    [0, 1, 2, 3, 4, 5]
)

Bed_Grade = st.sidebar.selectbox(
    'Bed Grade',
    [1, 2, 3, 4]
)

City_Code_Patient = st.sidebar.number_input(
    'City Code Patient',
    min_value=1,
    max_value=38,
    value=7
)

Type_of_Admission = st.sidebar.selectbox(
    'Type of Admission',
    [0, 1, 2]
)

Severity_of_Illness = st.sidebar.selectbox(
    'Severity of Illness',
    [0, 1, 2]
)

Visitors_with_Patient = st.sidebar.slider(
    'Visitors with Patient',
    0,
    20,
    3
)

Age = st.sidebar.selectbox(
    'Age Group',
    list(range(10))
)

Admission_Deposit = st.sidebar.number_input(
    'Admission Deposit',
    min_value=1000,
    max_value=20000,
    value=5000
)

# Feature Engineering

Severity_Visitors = (
    Severity_of_Illness *
    Visitors_with_Patient
)

Deposit_per_Visitor = (
    Admission_Deposit /
    (Visitors_with_Patient + 1)
)

# Create dataframe

input_data = pd.DataFrame({

    'Hospital_code': [Hospital_code],

    'Hospital_type_code': [Hospital_type_code],

    'City_Code_Hospital': [City_Code_Hospital],

    'Hospital_region_code': [Hospital_region_code],

    'Available Extra Rooms in Hospital': [
        Available_Extra_Rooms
    ],

    'Department': [Department],

    'Ward_Type': [Ward_Type],

    'Ward_Facility_Code': [Ward_Facility_Code],

    'Bed Grade': [Bed_Grade],

    'City_Code_Patient': [City_Code_Patient],

    'Type of Admission': [Type_of_Admission],

    'Severity of Illness': [Severity_of_Illness],

    'Visitors with Patient': [Visitors_with_Patient],

    'Age': [Age],

    'Admission_Deposit': [Admission_Deposit],

    'Severity_Visitors': [Severity_Visitors],

    'Deposit_per_Visitor': [Deposit_per_Visitor]
})

# Prediction

if st.button('Predict Stay Duration'):

    prediction = model.predict(input_data)[0]

    if prediction == 0:
        result = '🟢 Short Stay'

    elif prediction == 1:
        result = '🟡 Medium Stay'

    else:
        result = '🔴 Long Stay'

    st.success(f'Predicted Stay Duration: {result}')

    st.subheader('Patient Input Summary')

    st.dataframe(input_data)
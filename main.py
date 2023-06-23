import joblib
import streamlit as st
import pandas as pd

# Title and subtitle
st.title('Anomaly Detection from Network Traffic in IoT Devices')
st.markdown("**DATA 245 Group 5**")

idx2str = {0: 'DDoS Attacks',
           1: 'DoS Attacks',
           2: 'Mirai Attacks',
           3: 'Benign Traffic',
           4: 'Other Attacks',
           5: 'Reconnaissance',
           6: 'Malware and Exploits'}

def make_predict(data):
    # load model
    model = joblib.load('rf_model.sav')
    target = model.predict(data)
    print(int(target))
    return idx2str[int(target)]

# Create input fields for 10 features
feature_names = ['Number', 'Protocol Type', 'Header_Length', 'Tot sum', 'Magnitue', 'flow_duration', 'AVG', 'Min', 'Tot size', 'IAT'] 
inputs = []
for feature in feature_names:
    user_input = st.number_input(f'{feature}', step=0.5)
    inputs.append(user_input)

if st.button('Predict'):
    # Prepare the input data for prediction
    input_data = pd.DataFrame([inputs], columns=feature_names)
    prediction = make_predict(input_data)
    st.write(f"Attack Type: {prediction}")

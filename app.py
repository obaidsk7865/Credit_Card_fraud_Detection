import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('logisticRegression.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))


st.title('Credit_card_Fraud_Detection')

V1 = st.number_input('V1:')
V2 = st.number_input('V2:')
V3 = st.number_input('V3:')
V4 = st.number_input('V4:')
V5 = st.number_input('V4')
Amount = st.number_input('Amount:')

result=''
if st.button('Predict'):
    input = pd.DataFrame([[V1, V2, V3, V4, V5 ,Amount]], columns=['V1', 'V2', 'V3', 'V4', 'V5', 'Amount'])
    prediction = model.predict(input)
    if (prediction[0] == 0):
        result="legit"
    else:
        result="fraud"


st.success(result)

import streamlit as st
import requests

sepal_l = st.number_input('꽃받침의 길이는?')
sepal_w = st.number_input('꽃받침의 너비는?')
petal_l = st.number_input('꽃잎의 길이는?')
petal_w = st.number_input('꽃잎의 너비는?')

if st.sidebar.button('predict'):
    response = requests.post('http://127.0.0.1:5000/predict',
                            json=[sepal_l, sepal_w, petal_l, petal_w])
    st.write(response.text)
import streamlit as st
import requests
from os import environ

sepal_l = st.number_input('꽃받침의 길이는?')
sepal_w = st.number_input('꽃받침의 너비는?')
petal_l = st.number_input('꽃잎의 길이는?')
petal_w = st.number_input('꽃잎의 너비는?')
species = ['setosa', 'versicolor', 'virginica']

if st.sidebar.button('predict'):
    with st.spinner('Wait for it...'):
        # response = requests.post(f'http://127.0.0.1:5000/predict',
        response = requests.post(f'http://model:5000/predict',
        # response = requests.post(f'http://192.168.0.11:5000/predict',
        # response = requests.post(f'http://{environ["MY_PUBLIC_IP"]}:5000/predict',
                                json=[sepal_l, sepal_w, petal_l, petal_w])
        label = int(response.text)
        st.write(species[label])
    st.success('Done!')
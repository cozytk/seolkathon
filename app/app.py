import json
import requests
import streamlit as st

context = dict()
context['sentence'] = st.text_input('요약할 문장을 입력하시오.')

if st.sidebar.button('predict'):
    with st.spinner('Wait for it...'):
        # model: {DOCKER_IP}
        response = requests.post('http://model:5000/predict', json=json.dumps(context))
        result = json.loads(response.text)
        st.write(result['summary_text'])
    st.success('Done!')

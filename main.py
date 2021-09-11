import os
import streamlit as st
st.title("Gerador de Links diretos para Google Drive")
with st.form(key='myform'):
    url = st.text_input('Cole A Url Aqui')
    enviar = st.form_submit_button('Gerar')

    if enviar:
        try:
            lis = url.split('d/')
            u = lis[1]
            n = u.split('/view')
            nova_url = "https://drive.google.com/uc?export=download&id=" + n[0]
            st.text_input("Url com Link Direto",nova_url)
            st.success('Url Convertida Com Sucesso')
        except:
            st.error('A url tem que ser do Google Drive')





import streamlit as st
import requests
import pandas as pd
from app import URL_LOCAL, show_response_message

def delete_product():
    #with st.expander("Deletar Produto"):
        delete_id = st.number_input("ID do Produto para Deletar", min_value=0, format="%d")
        if st.button("Deletar Produto"):
            response = requests.delete(f"{URL_LOCAL}{delete_id}")
            #response = requests.delete(f"http://backend:8000/produtos/{delete_id}")
            #response = requests.delete(f"http://127.0.0.1:8000/produtos/{delete_id}")
            show_response_message(response)


delete_product()

st.page_link("app.py", label="Menu", icon="🏠")
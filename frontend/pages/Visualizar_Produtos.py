import streamlit as st
import requests
import pandas as pd
from app import URL_LOCAL, show_response_message


def visualization():
    #if st.button("Exibir Todos os Produtos"):
    response = requests.get(URL_LOCAL)
    #response = requests.get("http://backend:8000/produtos/")
    #response = requests.get("http://127.0.0.1:8000/produtos/")
    if response.status_code == 200:
        product = response.json()
        df = pd.DataFrame(product)

        df = df[
            [
                "id",
                "nome",
                "descricao",
                "preco",
                "categoria",
                "email_fornecedor",
                "created_at",
                "updated",
                "update_date"
            ]
        ]

        # Exibe o DataFrame sem o índice
        st.write(df.to_html(index=False), unsafe_allow_html=True)
    else:
        show_response_message(response)
visualization()

st.page_link("app.py", label="Menu", icon="🏠")
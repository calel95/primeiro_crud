import streamlit as st
import requests
import pandas as pd
from app import URL_LOCAL, show_response_message


def produto_detail():
    get_id = st.text_input("ID do Produto",placeholder=0)
    if st.button("Buscar Produto"):
        response = requests.get(f"{URL_LOCAL}{int(get_id)}")
        #response = requests.get(f"http://backend:8000/produtos/{get_id}")
        #response = requests.get(f"http://127.0.0.1:8000/produtos/{get_id}")
        if response.status_code == 200:
            product = response.json()
            df = pd.DataFrame([product])

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

produto_detail()
st.page_link("app.py", label="Menu", icon="🏠")
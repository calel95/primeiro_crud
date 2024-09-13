import streamlit as st
import requests
import pandas as pd
from app import URL_LOCAL, show_response_message


def upgrade_product():
    with st.form("update_product"):
        update_id = st.text_input("ID do Produto", placeholder=0)
        new_nome = st.text_input("Novo Nome do Produto")
        new_descricao = st.text_area("Nova Descrição do Produto")
        new_preco = st.number_input(
            "Novo Preço",
            value=None,
            placeholder="Novo Preço"
        )
        new_categoria = st.selectbox(
            "Nova Categoria",
            ["Eletrônico", "Eletrodoméstico", "Móveis", "Roupas", "Calçados"],
        )
        new_email = st.text_input("Novo Email do Fornecedor")

        update_button = st.form_submit_button("Atualizar Produto")

        if update_button:
            update_data = {}
            if new_nome:
                update_data["nome"] = new_nome
            if new_descricao:
                update_data["descricao"] = new_descricao
            if new_preco:
                update_data["preco"] = new_preco
            if new_email:
                update_data["email_fornecedor"] = new_email
            if new_categoria:
                update_data["categoria"] = new_categoria

            if update_data:
                response = requests.put(f"{URL_LOCAL}{int(update_id)}", json=update_data)
                #response = requests.put(f"http://backend:8000/produtos/{update_id}", json=update_data)
                #response = requests.put(f"http://127.0.0.1:8000/produtos/{update_id}", json=update_data)
                show_response_message(response)
            else:
                st.error("Nenhuma informação fornecida para atualização")

upgrade_product()

st.page_link("app.py", label="Menu", icon="🏠")
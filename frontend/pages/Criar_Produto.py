import streamlit as st
import requests
import pandas as pd
from app import URL_LOCAL, show_response_message

st.title("Criação de Produtos")


def create_product():

    #with st.expander("Adicionar um Novo Produto"):
    with st.form("new_product"):
        nome = st.text_input("Nome do Produto")
        descricao = st.text_area("Descrição do Produto")
        preco = st.text_input("Preço",placeholder="0")
        categoria = st.radio(
            "***Categoria***",
            ["Eletrônico", "Eletrodoméstico", "Móveis", "Roupas", "Calçados"],
        )
        email_fornecedor = st.text_input("Email do Fornecedor")
        submit_button = st.form_submit_button("Adicionar Produto")

        if submit_button:
            response = requests.post(
                #"http://127.0.0.1:8000/produtos/",
                #"http://backend:8000/produtos/",
                URL_LOCAL,
                json={
                    "nome": nome,
                    "descricao": descricao,
                    "preco": float(preco),
                    "categoria": categoria,
                    "email_fornecedor": email_fornecedor,
                },
            )
            show_response_message(response)

create_product()

st.page_link("app.py", label="Menu", icon="🏠")
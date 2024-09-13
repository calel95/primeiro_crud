import streamlit as st
import requests
import pandas as pd
from pages.Criar_Produto import create_product
from pages.Deletar_Produto import delete_product
from pages.Visualizar_Produtos import visualization
from pages.Detalhe_Produto import produto_detail
from pages.Atualizar_Produto import upgrade_product


URL_BACKEND = "http://backend:8000/produtos/"
URL_LOCAL = "http://127.0.0.1:8000/produtos/"

st.set_page_config(layout="wide")

st.image("logo.png", width=500)

st.title("Gerenciamento de Produtos")


# Função auxiliar para exibir mensagens de erro detalhadas
def show_response_message(response):
    if response.status_code == 200:
        st.success("Operação realizada com sucesso!")
    else:
        try:
            data = response.json()
            if "detail" in data:
                # Se o erro for uma lista, extraia as mensagens de cada erro
                if isinstance(data["detail"], list):
                    errors = "\n".join([error["msg"] for error in data["detail"]])
                    st.error(f"Erro: {errors}")
                else:
                    # Caso contrário, mostre a mensagem de erro diretamente
                    st.error(f"Erro: {data['detail']}")
        except ValueError:
            st.error("Erro desconhecido. Não foi possível decodificar a resposta.")

#st.set_page_config(layout="wide")
st.page_link("app.py", label="Menu", icon="🏠")
st.page_link("pages/Criar_Produto.py", label="Criar", icon="😀")
st.page_link("pages/Deletar_Produto.py", label="Deletar", icon="😭")
st.page_link("pages/Visualizar_Produtos.py", label="Visualizar", icon="👀")
st.page_link("pages/Atualizar_Produto.py", label="Atualizar", icon="😮")
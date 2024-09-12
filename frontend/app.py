import streamlit as st
import requests
import pandas as pd

URL_BACKEND = "http://backend:8000/produtos/"
URL_LOCAL = "http://127.0.0.1:8000/produtos/"

st.set_page_config(layout="wide")

#st.image("logo.png", width=200)

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


# Adicionar Produto
with st.expander("Adicionar um Novo Produto"):
    with st.form("new_product"):
        nome = st.text_input("Nome do Produto")
        descricao = st.text_area("Descrição do Produto")
        preco = st.number_input("Preço", min_value=0.01, format="%f")
        categoria = st.selectbox(
            "Categoria",
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
                    "preco": preco,
                    "categoria": categoria,
                    "email_fornecedor": email_fornecedor,
                },
            )
            show_response_message(response)
# Visualizar Produtos
with st.expander("Visualizar Produtos"):
    if st.button("Exibir Todos os Produtos"):
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

# Obter Detalhes de um Produto
with st.expander("Obter Detalhes de um Produto"):
    get_id = st.number_input("ID do Produto", min_value=1, format="%d")
    if st.button("Buscar Produto"):
        response = requests.get(f"{URL_LOCAL}{get_id}")
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

# Deletar Produto
with st.expander("Deletar Produto"):
    delete_id = st.number_input("ID do Produto para Deletar", min_value=1, format="%d")
    if st.button("Deletar Produto"):
        response = requests.delete(f"{URL_LOCAL}{delete_id}")
        #response = requests.delete(f"http://backend:8000/produtos/{delete_id}")
        #response = requests.delete(f"http://127.0.0.1:8000/produtos/{delete_id}")
        show_response_message(response)

# Atualizar Produto
with st.expander("Atualizar Produto"):
    with st.form("update_product"):
        update_id = st.number_input("ID do Produto", min_value=1, format="%d")
        new_nome = st.text_input("Novo Nome do Produto")
        new_descricao = st.text_area("Nova Descrição do Produto")
        new_preco = st.number_input(
            "Novo Preço",
            min_value=0.01,
            format="%f",
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
            if new_preco > 0:
                update_data["preco"] = new_preco
            if new_email:
                update_data["email_fornecedor"] = new_email
            if new_categoria:
                update_data["categoria"] = new_categoria

            if update_data:
                response = requests.put(f"{URL_LOCAL}{update_id}", json=update_data)
                #response = requests.put(f"http://backend:8000/produtos/{update_id}", json=update_data)
                #response = requests.put(f"http://127.0.0.1:8000/produtos/{update_id}", json=update_data)
                show_response_message(response)
            else:
                st.error("Nenhuma informação fornecida para atualização")
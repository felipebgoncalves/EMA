import streamlit as st
import psycopg2


# FUNÇÃO PARA CONEXÃO COM O BANCO DE DADOS
# @st.cache_resource
def conexao_db():
    # USUÁRIO POSTGRES - ACESSA TODOS OS BANCOS
    conn = psycopg2.connect(**st.secrets["postgres"])

    cur = conn.cursor()

    return cur

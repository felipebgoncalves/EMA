import streamlit as st
import psycopg2


# FUNÇÃO PARA CONEXÃO COM O BANCO DE DADOS
# @st.cache_resource
def conexao_db():
    # USUÁRIO POSTGRES - ACESSA TODOS OS BANCOS
#     conn = psycopg2.connect(**st.secrets["postgres"])
    conn = psycopg2.connect(host=st.secrets.db_credentials.host,
                            port=st.secrets.db_credentials.port,
                            username=st.secrets.db_credentials.username, 
                            password=st.secrets.db_credentials.password
                           )

    cur = conn.cursor()

    return cur

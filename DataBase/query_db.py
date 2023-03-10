import streamlit as st
import DataBase.conection_db as db


# FUNÇÃO PARA CONSULTAS NO BANCO DE DADOS
@st.cache_data(ttl=600)
def consulta_dados(sql_SELECT):
    # CONEXÃO AO DB E CRIAÇÃO DO CURSOR
    cur = db.conexao_db()

    # EXECUÇÃO DO COMANDO SQL
    cur.execute(sql_SELECT)

    recset = cur.fetchall()
    registros = []

    for rec in recset:
        registros.append(rec)

    return registros

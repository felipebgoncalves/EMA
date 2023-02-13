import streamlit as st
from PIL import Image

img = Image.open('logo_cepdec.png')
st.set_page_config(page_title="Cepdec", page_icon=img)

st.write("# Banco de Dados - EMA Cepdec! 👋")

st.sidebar.success("Selecione a opção desejada.")

st.markdown("""
                Página dedicada para visualização dos dados gerados pelas Estações Meteorológicas Automáticas (EMA)
                instaladas em 28 municípios do estado do Espírito Santo.
            
                **👈 Selecione umas das opções na barra lateral**
                """
            )



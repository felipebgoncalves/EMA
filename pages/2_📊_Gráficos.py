import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

st.set_page_config(page_title="Gráficos", page_icon="📊")

st.markdown("# Gráficos")
st.sidebar.title('Gráficos')

options = st.sidebar.radio('Selecione o gráfico que deseja visualizar:', ['Temperaturas',
                                                                          'Precipitação e '
                                                                          'Evapotranspiração Diária',
                                                                          'Rosa dos Ventos',
                                                                          'Precipitação'])

df = st.session_state['df']
st.header('testando session state')
st.dataframe(df)

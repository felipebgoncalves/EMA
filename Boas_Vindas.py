import streamlit as st
from PIL import Image
import folium
from streamlit_folium import st_folium

img = Image.open('logo_cepdec.png')
st.set_page_config(page_title="Cepdec", page_icon=img, layout='wide')

st.write("# Banco de Dados - EMA Cepdec!")

st.sidebar.success("Selecione a opção desejada.")

st.markdown("""
                Página dedicada para visualização dos dados gerados pelas Estações Meteorológicas Automáticas (EMA)
                instaladas em 28 municípios do estado do Espírito Santo.
            
                **👈 Selecione umas das opções na barra lateral**
                """
            )

st.markdown('O mapa indica a localização de todas as estações pertencentes à Cepdec')

mapa = folium.Map(location=[-19.504855745440523, -40.648548131522055], zoom_start=8)

folium.Marker([-18.549833, -40.991611],
              popup="EMA_ADN_01",
              tooltip="EMA_ADN_01"
              ).add_to(mapa)

folium.Marker([-21.161833, -41.564111],
              popup="EMA_API_01",
              tooltip="EMA_API_01"
              ).add_to(mapa)

folium.Marker([-19.797667, -40.274972],
              popup="EMA_ARA_01",
              tooltip="EMA_ARA_01",
              ).add_to(mapa)

folium.Marker([-19.059611, -41.02825],
              popup="EMA_ARN_01",
              tooltip="EMA_ARN_01",
              ).add_to(mapa)

folium.Marker([-20.927333, -41.185278],
              popup="EMA_ATV_01",
              tooltip="EMA_ATV_01",
              ).add_to(mapa)

folium.Marker([-20.627528, -41.197833],
              popup="EMA_CAS_01",
              tooltip="EMA_CAS_01",
              ).add_to(mapa)

folium.Marker([-18.574806, -39.760472],
              popup="EMA_COB_01",
              tooltip="EMA_COB_01",
              ).add_to(mapa)

folium.Marker([-19.487111, -40.58425],
              popup="EMA_COL_01",
              tooltip="EMA_COL_01",
              ).add_to(mapa)

folium.Marker([-20.772778, -41.672167],
              popup="EMA_GUC_01",
              tooltip="EMA_GUC_01",
              ).add_to(mapa)

folium.Marker([-20.791389, -40.794417],
              popup="EMA_ICO_01",
              tooltip="EMA_ICO_01",
              ).add_to(mapa)

folium.Marker([-19.792667, -40.855444],
              popup="EMA_ITG_01",
              tooltip="EMA_ITG_01",
              ).add_to(mapa)

folium.Marker([-21.032389, -40.915694],
              popup="EMA_ITP_01",
              tooltip="EMA_ITP_01",
              ).add_to(mapa)

folium.Marker([-18.9115, -40.061444],
              popup="EMA_JAG_01",
              tooltip="EMA_JAG_01",
              ).add_to(mapa)

folium.Marker([-19.768347, -40.337472],
              popup="EMA_JON_01",
              tooltip="EMA_JON_01",
              ).add_to(mapa)

folium.Marker([-19.8945, -41.054694],
              popup="EMA_LAT_01",
              tooltip="EMA_LAT_01",
              ).add_to(mapa)

folium.Marker([-20.425667, -40.677361],
              popup="EMA_MAF_01",
              tooltip="EMA_MAF_01",
              ).add_to(mapa)

folium.Marker([-21.065917, -41.377972],
              popup="EMA_MIS_01",
              tooltip="EMA_MIS_01",
              ).add_to(mapa)

folium.Marker([-19.231167, -40.829944],
              popup="EMA_PAN_01",
              tooltip="EMA_PAN_01",
              ).add_to(mapa)

folium.Marker([-18.229581, -40.020139],
              popup="EMA_PEC_01",
              tooltip="EMA_PEC_01",
              ).add_to(mapa)

folium.Marker([-20.831056, -40.743389],
              popup="EMA_PIU_01",
              tooltip="EMA_PIU_01",
              ).add_to(mapa)

folium.Marker([-19.262417, -40.337722],
              popup="EMA_RIB_01",
              tooltip="EMA_RIB_01",
              ).add_to(mapa)

folium.Marker([-20.091333, -40.531139],
              popup="EMA_SAL_01",
              tooltip="EMA_SAL_01",
              ).add_to(mapa)

folium.Marker([-20.19775, -40.21575],
              popup="EMA_SER_01",
              tooltip="EMA_SER_01",
              ).add_to(mapa)

folium.Marker([-19.729194, -40.653528],
              popup="EMA_SRC_01",
              tooltip="EMA_SRC_01",
              ).add_to(mapa)

folium.Marker([-20.673278, -40.99825],
              popup="EMA_VAR_01",
              tooltip="EMA_VAR_01",
              ).add_to(mapa)

folium.Marker([-20.419444, -40.468306],
              popup="EMA_VIA_01",
              tooltip="EMA_VIA_01",
              ).add_to(mapa)

folium.Marker([-18.607444, -40.692056],
              popup="EMA_VPA_01",
              tooltip="EMA_VPA_01",
              ).add_to(mapa)

folium.Marker([-19.006694, -40.383056],
              popup="EMA_VVA_01",
              tooltip="EMA_VVA_01",
              ).add_to(mapa)

output = st_folium(mapa,
                   width=700,
                   height=800,
                   returned_objects=["last_object_clicked"]
                   )

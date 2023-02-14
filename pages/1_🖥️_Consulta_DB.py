import time
from PIL import Image
import streamlit as st
from datetime import datetime
import pandas as pd
import pytz
from Utilities import select_ema, columns
from DataBase import query_db
from Utilities.download_CSV import convert_df


img = Image.open('database.png')
st.set_page_config(page_title='Consulta EMA', page_icon=img, layout='wide')

st.markdown('# Visualização dos dados das EMA')
st.sidebar.header('Filtro da Tabela de dados')

with st.sidebar:
    input_ema = st.selectbox('Selecione a Estação Meteorológica Automática', ['-----',
                                                                              'ADN_01 - Água Doce do Norte',
                                                                              'API_01 - Apiacá',
                                                                              'ARA_01 - Aracruz',
                                                                              'ARN_01 - Alto Rio Novo',
                                                                              'ATV_01 - Atílio Vivácqua',
                                                                              'CAS_01 - Castelo',
                                                                              'COB_01 - Conceição da Barra',
                                                                              'COL_01 - Colatina',
                                                                              'GUC_01 - Guaçuí',
                                                                              'ICO_01 - Iconha',
                                                                              'ITG_01 - Itaguaçú',
                                                                              'ITP_01 - Itapemirim',
                                                                              'JAG_01 - Jaguaré',
                                                                              'JON_01 - João Neiva',
                                                                              'LAT_01 - Laranja da Terra',
                                                                              'MAF_01 - Marechal Floriano',
                                                                              'MIS_01 - Mimoso do Sul',
                                                                              'PAN_01 - Pancas',
                                                                              'PEC_01 - Pedro Canário',
                                                                              'PIU_01 - Piúma',
                                                                              'RIB_01 - Rio Bananal',
                                                                              'SAL_01 - Santa Leopoldina',
                                                                              'SER_01 - Serra',
                                                                              'SRC_01 - São Roque do Canaã',
                                                                              'VAR_01 - Vargem Alta',
                                                                              'VIA_01 - Viana',
                                                                              'VPA_01 - Vila Pavão',
                                                                              'VVA_01 - Vila Valério'
                                                                              ])

    input_data_i = st.date_input('Insira a data inicial')
    input_hora_i = st.time_input('Insira a hora inicial - UTC (+ 03:00)')

    input_data_f = st.date_input('Insira a data final')
    input_hora_f = st.time_input('Insira a hora final - UTC (+ 03:00)')

    input_colunas = st.multiselect('Colunas deseja visualizar?', ['temp_int',
                                                                  'pressao_inst',
                                                                  'pressao_med',
                                                                  'pressao_max',
                                                                  'pressao_min',
                                                                  'temp_inst',
                                                                  'temp_med',
                                                                  'temp_max',
                                                                  'temp_min',
                                                                  'umid_rel_inst',
                                                                  'umid_rel_med',
                                                                  'umid_rel_max',
                                                                  'umid_rel_min',
                                                                  'rad_solar_glob_inst_LPPYRRA02',
                                                                  'rad_solar_glob_med_LPPYRRA02',
                                                                  'rad_solar_glob_max_LPPYRRA02',
                                                                  'rad_solar_glob_min_LPPYRRA02',
                                                                  'rad_solar_glob_inst_LPNET14',
                                                                  'rad_solar_glob_med_LPNET14',
                                                                  'rad_solar_glob_max_LPNET14',
                                                                  'rad_solar_glob_min_LPNET14',
                                                                  'rad_solar_reflet_inst',
                                                                  'rad_solar_reflet_med',
                                                                  'rad_solar_reflet_max',
                                                                  'rad_solar_reflet_min',
                                                                  'rad_iv_inst',
                                                                  'rad_iv_med',
                                                                  'rad_iv_max',
                                                                  'rad_iv_min',
                                                                  'rad_spf_inst',
                                                                  'rad_spf_med',
                                                                  'rad_spf_max',
                                                                  'rad_spf_min',
                                                                  'rad_sol_liq_inst',
                                                                  'rad_sol_liq_med',
                                                                  'rad_sol_liq_max',
                                                                  'rad_sol_liq_min',
                                                                  'temp_inst_NTC',
                                                                  'temp_med_NTC',
                                                                  'temp_max_NTC',
                                                                  'temp_min_NTC',
                                                                  'dir_vent_med',
                                                                  'dir_vent_max',
                                                                  'dir_vent_min',
                                                                  'vel_vent_med',
                                                                  'vel_vent_max',
                                                                  'vel_vent_min',
                                                                  'temp_solo_inst',
                                                                  'temp_solo_med',
                                                                  'temp_solo_max',
                                                                  'temp_solo_min',
                                                                  'umid_solo_inst',
                                                                  'umid_solo_med',
                                                                  'umid_solo_max',
                                                                  'umid_solo_min',
                                                                  'prec'
                                                                  ])

    input_button = st.button('Consultar')

if input_button:
    with st.spinner('Wait for it...'):
        time.sleep(2)

    input_ema = select_ema.seleciona_item(input_ema)

    if input_ema != '-----':

        input_data_i = input_data_i.strftime('%Y-%m-%d')
        input_hora_i = input_hora_i.strftime('%H:%M')
        input_data_f = input_data_f.strftime('%Y-%m-%d')
        input_hora_f = input_hora_f.strftime('%H:%M')

        data_hora_i = input_data_i + ' ' + input_hora_i + ':00'
        data_hora_f = input_data_f + ' ' + input_hora_f + ':00'

        data_hora_i = datetime.strptime(data_hora_i, '%Y-%m-%d %H:%M:%S')
        data_hora_f = datetime.strptime(data_hora_f, '%Y-%m-%d %H:%M:%S')

        if data_hora_f >= data_hora_i:

            data_hora_i = datetime.strftime(data_hora_i, '%Y-%m-%d %H:%M:%S')
            data_hora_f = datetime.strftime(data_hora_f, '%Y-%m-%d %H:%M:%S')

            sql = f"select * from {input_ema}_15m " \
                  f"where data_hora_utc between '{data_hora_i}' and '{data_hora_f}' " \
                  f"order by data_hora_utc asc "

            registros = query_db.consulta_dados(sql)

            df = pd.DataFrame(registros, columns=columns.colunas_df())

            if len(input_colunas) != 0:

                input_colunas.insert(0, 'data_hora_utc')
                input_colunas.insert(1, 'id_ema')
                input_colunas.insert(2, 'frequencia_ema')

                input_colunas = set(input_colunas)
                colunas = set(columns.colunas_df())

                colunas_df = list(colunas.difference(input_colunas))

                df.drop(columns=colunas_df, axis=1, inplace=True)

                df['data_hora_utc'] = pd.to_datetime(df['data_hora_utc'])

                df['data_hora_utc'] = df.set_index('data_hora_utc').index.tz_localize(pytz.utc) \
                    .tz_convert(pytz.timezone('America/Sao_Paulo'))

                df = df.set_index('data_hora_utc')

                # df['prec'] = df['prec'].astype(float)
                # df = df['prec'].groupby(pd.Grouper(freq='1D')).sum()

                st.write('A data/hora já foram convertidos para horário local - America/Sao_Paulo')

                st.dataframe(df)

                if input_button is not None:
                    st.session_state['df'] = df

                # CONVERSÃO DO DATAFRAME PARA ARQUIVO CVS E DISPONIBILIZADO PARA DOWNLOAD
                csv = convert_df(df)
                st.download_button(label="Download data as CSV",
                                   data=csv,
                                   file_name=f'{input_ema}.csv',
                                   mime='text/csv',
                                   )

            else:

                df['data_hora_utc'] = pd.to_datetime(df['data_hora_utc'])

                df['data_hora_utc'] = df.set_index('data_hora_utc').index.tz_localize(pytz.utc) \
                    .tz_convert(pytz.timezone('America/Sao_Paulo'))

                df = df.set_index('data_hora_utc')

                st.write('A data/hora já foram convertidos para horário local - America/Sao_Paulo')

                st.dataframe(df)

                if input_button is not None:
                    st.session_state['df'] = df

                # CONVERSÃO DO DATAFRAME PARA ARQUIVO CVS E DISPONIBILIZADO PARA DOWNLOAD
                csv = convert_df(df)
                st.download_button(label="Download data as CSV",
                                   data=csv,
                                   file_name=f'{input_ema}.csv',
                                   mime='text/csv',
                                   )

        else:

            st.warning('A data inicial deverá ser menor que a data final', icon="⚠️")

    else:

        st.warning('Selecione uma Estação Meteorológica Automática para realizar a consulta', icon="⚠️")




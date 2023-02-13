from datetime import datetime
import streamlit as st
import pandas as pd
import pytz
from Utilities import select_ema, columns
from DataBase import query_db
from Utilities.download_CSV import convert_df


def main_function(input_ema, input_data_i, input_hora_i, input_data_f, input_hora_f, input_colunas):
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

    return None

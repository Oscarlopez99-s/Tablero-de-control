import pandas as pd
import streamlit as st

url = 'https://github.com/Oscarlopez99-s/Repositorio-Oscar/raw/refs/heads/main/datos_generales_ficticios.csv' 
df = pd.read_csv(url, sep=';', encoding='utf-8')


print(df)


# Crear lista de las columnas de Interés
seleccion_columnas = ['FECHA_HECHOS','DELITO', 'ETAPA', 'FISCAL_ASIGNADO', 'DEPARTAMENTO', 'MUNICIPIO_HECHOS']
# Actualizo el dataframe -df- con las columnas de interés, ordenadas por fecha y reseteo el índice
df  = df[seleccion_columnas].sort_values(by='FECHA_HECHOS', ascending=True).reset_index(drop=True)

# Convierto la columna FECHA_HECHOS a formato fecha
df['FECHA_HECHOS'] = pd.to_datetime(df['FECHA_HECHOS'], errors='coerce')
# Extraigo solo la fecha (sin hora)
df['FECHA_HECHOS'] = df['FECHA_HECHOS'].dt.date

# CÁCULO DE MUNICIPIO CON MAS DELITOS
max_municipio = df['MUNICIPIO_HECHOS'].value_counts()
st.dataframe(max_municipio)
max_cantidad_municipio = df['MUNICIPIO_HECHOS'].value_counts().iloc[0]
st.write(f'Cant. Eventos: {max_cantidad_municipio}')

# CONSTRUIR LA PÁGINA
st.set_page_config(page_title="Dashboard de Delitos - Fiscalía", layout="centered")
st.header("Dashboard de Delitos - Fiscalía")
#st.markdown(f"<center><h2>Dashboard de Delitos - Fiscalía)



# max_cantidad_municipio = df['MUNICIPIO_HECHOS'].value.counts().iloc[0]

st.dataframe(df)




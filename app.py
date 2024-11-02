# pip install pandas altair streamlit
# streamlit run app.py

import pandas as pd
import altair as alt
import streamlit as st

# Función para cargar y procesar los datos
def load_and_prepare_data(file):
    # Cargar los datos
    data = pd.read_excel(file)

    # Limpiar y preparar los datos
    data['Peso'] = data['Peso'].str.replace('kg', '').str.replace(',', '.').astype(float)
    
    return data

# Configuración de la aplicación Streamlit
st.set_page_config(layout="wide")  # Configura la página para uso amplio de ancho

st.title('Evolución semanal del peso')

# Cargar el archivo de Excel
uploaded_file = st.file_uploader("Sube tu archivo de Excel", type="xlsx")

if uploaded_file is not None:
    # Llamar a la función para cargar y preparar los datos
    data = load_and_prepare_data(uploaded_file)

    # Crear el gráfico interactivo con Altair
    chart = alt.Chart(data).mark_line(point=True).encode(
        x='Fecha:T',
        y=alt.Y('Peso:Q', title='Peso (kg)', scale=alt.Scale(domain=[72, data['Peso'].max()])),
        tooltip=['Fecha:T', 'Peso:Q']
    ).properties(
        title='Evolución del Peso',
        width='container',  # Establecer el ancho al contenedor completo
        height=600  # Ajustar la altura a una más cómoda para pantalla completa
    ).interactive()

    # Mostrar el gráfico en Streamlit
    st.altair_chart(chart, use_container_width=True)


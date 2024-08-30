# Evolución Semanal del Peso

Este proyecto es una aplicación interactiva construida con Streamlit que permite visualizar la evolución semanal del peso mediante un gráfico lineal. La aplicación permite cargar un archivo de Excel con los datos y muestra un gráfico interactivo utilizando Altair.

## Requisitos

Antes de ejecutar la aplicación, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.x
- pandas
- altair
- streamlit
- openpyxl

Puedes instalar estas dependencias ejecutando los siguientes comandos en tu terminal:

```bash
pip install pandas
pip install altair
pip install streamlit
pip install openpyxl
```

# Ejecución de la Aplicación

## Para ejecutar la aplicación, sigue estos pasos:

1. Asegúrate de estar en el directorio donde se encuentra el archivo `app.py`.

2. Ejecuta el siguiente comando en tu terminal: 
    ```bash
    streamlit run app.py
    ```

3. Esto abrirá la aplicación en tu navegador web por defecto.
   
# Uso de la Aplicación
**1. Cargar Datos**: Al abrir la aplicación, podrás cargar un archivo de Excel (.xlsx) que contenga los datos de la evolución del peso. Asegúrate de que el archivo tenga una columna de "Peso" con los valores en formato [peso]kg y una columna de "Fecha" con las fechas correspondientes.

**2. Visualización**: Una vez cargado el archivo, la aplicación procesará los datos y generará un gráfico interactivo que muestra la evolución del peso a lo largo del tiempo.

# Estructura del Código
**1. `load_and_prepare_data(file)`:** Esta función carga los datos desde el archivo de Excel, limpia los datos de la columna "Peso" eliminando el texto "kg" y reemplazando las comas por puntos para convertirlos en valores numéricos.

**2. `st.set_page_config(layout="wide")`:** Configura el diseño de la página de la aplicación para un uso amplio del ancho.

**3. `st.file_uploader("Elige un archivo de Excel", type="xlsx")`:** Permite al usuario cargar el archivo de Excel.

**4. `alt.Chart(data).mark_line(point=True).encode(...)`:** Crea un gráfico lineal interactivo usando Altair, que muestra la evolución del peso con puntos en cada medición.

# Personalización

**1. Rango de Peso en el Gráfico:** El rango del eje Y en el gráfico se establece entre 72 kg y el valor máximo del peso en los datos. Puedes ajustar estos valores en el código si lo deseas.

**2. Dimensiones del Gráfico:** El gráfico tiene un ancho ajustado al contenedor y una altura de 600 píxeles. Puedes modificar estos valores para adaptar el gráfico a tus necesidades.

# Contribuciones

Si deseas contribuir a este proyecto, puedes realizar un fork y enviar un pull request con tus mejoras o sugerencias.
# Proyecto de Análisis de Crédito Financiero

Este proyecto aplica técnicas de ciencia de datos para predecir el riesgo crediticio de clientes utilizando un modelo KNN balanceado con SMOTE.

## Contenido del repositorio

- `credito_financiero.ipynb`: Notebook con el análisis exploratorio de datos y desarrollo del modelo.
- `hmeq.csv`: Conjunto de datos original.
- `knn_smote_model.pkl`: Modelo entrenado y serializado.
- `app.py`: Aplicación en Streamlit que permite hacer predicciones con nuevos datos.
- `requirements.txt`: Librerías necesarias para ejecutar el proyecto.

## Cómo ejecutar la app

1. Clona este repositorio

2. Instala dependencias
pip install -r requirements.txt

3. Ejecuta la app
streamlit run app.py


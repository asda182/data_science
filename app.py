import streamlit as st
import joblib
import numpy as np

st.title("Predicción de Riesgo de Crédito")

# Cargar modelo
modelo = joblib.load("knn_smote_model.pkl")

# Inputs numéricos
loan = st.number_input("Monto del Préstamo (LOAN)")
mortdue = st.number_input("Hipoteca Pendiente (MORTDUE)")
value = st.number_input("Valor de la Propiedad (VALUE)")
yoj = st.number_input("Años en el Trabajo (YOJ)")
derog = st.number_input("Historial Negativo (DEROG)")
delinq = st.number_input("Delincuencias (DELINQ)")
clage = st.number_input("Edad de la Cuenta más Antigua (CLAGE)")
ninq = st.number_input("Nuevas Cuentas (NINQ)")
clno = st.number_input("Cantidad de Cuentas (CLNO)")
debtinc = st.number_input("Relación Deuda/Ingreso (DEBTINC)")

# Variables categóricas one-hot
reason_homeimp = st.checkbox("¿Razón: Home Improvement?")
job_office = st.checkbox("Trabajo: Office")
job_other = st.checkbox("Trabajo: Other")
job_profexe = st.checkbox("Trabajo: ProfExe")
job_sales = st.checkbox("Trabajo: Sales")
job_self = st.checkbox("Trabajo: Self")

if st.button("Predecir"):
    entrada = np.array([[
        loan, mortdue, value, yoj, derog, delinq, clage, ninq, clno, debtinc,
        reason_homeimp, job_office, job_other, job_profexe, job_sales, job_self
    ]], dtype=float)

    pred = modelo.predict(entrada)
    resultado = "Pagará" if pred[0] == 0 else "No pagará"
    st.success(f"Resultado: {resultado}")

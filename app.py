# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 14:14:15 2024

@author: jperezr
"""

import streamlit as st
import pandas as pd
from scipy import stats

# Título de la aplicación
st.title("Análisis de Varianza (ANOVA) de Modelos de Focos LED")

# Sección de enunciado del ejercicio
st.header("Enunciado del Ejercicio")
st.write(
    """
    Una empresa fabricante de lámparas ensaya dos nuevos modelos de focos LED para uso comercial tratando de decidir entre ellos. 
    De momento se realizan las pruebas de vida útil tal como se muestra en la tabla a continuación. Se desea realizar una prueba 
    de ANOVA de un factor para comparar la vida útil entre los modelos de foco con un nivel de confianza del 95%.
    """
)

# Datos
data = {
    'Modelo 1': [8090, 8090, 8120, 8111, 8112, 8115, 8126, 8116, 8108, 8112],
    'Modelo 2': [7994, 8115, 7810, 8110, 7999, 7811, 8050, 8068, 7956, 8106]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Mostrar los datos
st.write("Datos de Vida Útil de los Modelos de Focos:")
st.write(df)

# Realizar ANOVA
f_value, p_value = stats.f_oneway(df['Modelo 1'], df['Modelo 2'])

# Valor crítico F para alfa = 0.05, df1 = 1, df2 = 18
alpha = 0.05
df1 = 1  # Grados de libertad entre grupos
df2 = len(df['Modelo 1']) + len(df['Modelo 2']) - 2  # Grados de libertad dentro de grupos
f_critical = stats.f.ppf(1 - alpha, df1, df2)

# Resultados del ANOVA
st.header("Resultados del ANOVA")
st.write(f"Valor F calculado: {f_value:.4f}")
st.write(f"Valor p: {p_value:.4f}")
st.write(f"Valor crítico F (α=0.05, df1={df1}, df2={df2}): {f_critical:.4f}")

# Interpretación
st.header("Interpretación")
if p_value < alpha:
    st.write("Se rechaza la hipótesis nula. Hay evidencia suficiente para afirmar que hay una diferencia significativa en la vida útil entre los dos modelos de focos.")
    if f_value > f_critical:
        st.write("El valor F calculado es mayor que el valor crítico F, confirmando la diferencia significativa.")
    else:
        st.write("El valor F calculado es menor o igual al valor crítico F, pero aún así se rechaza la hipótesis nula debido al valor p.")
else:
    st.write("No se rechaza la hipótesis nula. No hay evidencia suficiente para afirmar que hay una diferencia significativa en la vida útil entre los dos modelos de focos.")

# Sección de ayuda
st.sidebar.header("Ayuda")
st.sidebar.write(
    """
    Esta aplicación realiza un análisis de varianza (ANOVA) de un factor para comparar la vida útil entre dos modelos de focos LED. 
    El análisis ANOVA se utiliza para determinar si existen diferencias significativas en la vida útil de los dos modelos basándose 
    en los datos proporcionados.

    **Hipótesis:**
    - **Hipótesis nula (H0):** No hay diferencia significativa en la vida útil entre los dos modelos de focos LED. (Las medias de vida útil de ambos modelos son iguales.)
    - **Hipótesis alternativa (Ha):** Hay una diferencia significativa en la vida útil entre los dos modelos de focos LED. (Las medias de vida útil de los modelos son diferentes.)

    **Resultados del ANOVA:**
    - El valor F calculado y el valor p se comparan con el valor crítico F para decidir si se rechaza la hipótesis nula.
    - Si el valor p es menor que el nivel de significancia (α=0.05), se rechaza la hipótesis nula.
    - El valor crítico F se calcula para determinar el umbral para la comparación.

    Para más información sobre cómo interpretar los resultados del ANOVA, consulte la literatura estadística o un experto en análisis de datos.
    """
)

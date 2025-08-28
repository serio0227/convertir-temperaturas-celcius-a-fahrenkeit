import streamlit as st

# Título de la aplicación
st.title("Conversor de Grados Celsius a Fahrenheit")

# Campo de entrada para la temperatura en Celsius con formato corregido
celsius = st.number_input(
    "Ingrese la temperatura en grados Celsius:",
    value=0.0,
    step=0.1,
    format="%0.2f",  # Formato estándar para dos decimales
    min_value=-1000.0,  # Límite inferior razonable
    max_value=1000.0    # Límite superior razonable
)

# Botón para realizar la conversión
if st.button("Convertir"):
    try:
        # Fórmula de conversión: F = (C * 9/5) + 32
        fahrenheit = (celsius * 9/5) + 32
        # Mostrar el resultado con formato
        st.success(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f} °F")
    except Exception as e:
        # Manejo de errores (por si acaso)
        st.error(f"Ocurrió un error en la conversión: {str(e)}")

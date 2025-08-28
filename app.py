import streamlit as st

# Estilo CSS para decoración (fondo y colores)
st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff;  /* Fondo azul claro para la app */
    }
    .stButton>button {
        background-color: #4CAF50;  /* Botón verde */
        color: white;
    }
    .stSuccess {
        background-color: #dff0d8;  /* Resultado en verde claro */
    }
    </style>
    """, unsafe_allow_html=True)

# Título principal con emojis para decoración
st.markdown("<h1 style='text-align: center; color: #007BFF;'>🌡️ Conversor de Temperaturas Multi-Unidad 🌡️</h1>", unsafe_allow_html=True)

# Mensaje de bienvenida decorativo
st.markdown("**¡Bienvenido!** Convierte entre Celsius (°C), Fahrenheit (°F), Kelvin (K) y Rankine (°R) de forma fácil. Selecciona las unidades y presiona 'Convertir'. 🚀")

# Unidades disponibles
unidades = ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)", "Rankine (°R)"]

# Barra lateral para selecciones (decoración y organización)
with st.sidebar:
    st.header("Opciones de Conversión")
    unidad_entrada = st.selectbox("Unidad de Entrada:", unidades)
    unidad_salida = st.selectbox("Unidad de Salida:", unidades)
    st.markdown("---")  # Separador visual
    st.info("Elige unidades diferentes para convertir. Si son iguales, se muestra el mismo valor.")

# Dividir la interfaz en columnas para mejor layout (izquierda: entrada, derecha: salida)
col1, col2 = st.columns(2)

with col1:
    # Campo de entrada para el valor de temperatura
    valor = st.number_input(
        f"Ingrese la temperatura en {unidad_entrada}:",
        value=0.0,
        step=0.1,
        format="%0.2f",
        min_value=-10000.0,  # Límite amplio para Kelvin/Rankine
        max_value=10000.0
    )

# Botón para convertir (centrado)
if st.button("Convertir", key="convertir_btn"):
    try:
        # Función de conversión universal
        def convertir_temperatura(valor, entrada, salida):
            # Mapear unidades a abreviaturas para simplicidad
            mapa = {
                "Celsius (°C)": "C",
                "Fahrenheit (°F)": "F",
                "Kelvin (K)": "K",
                "Rankine (°R)": "R"
            }
            ent = mapa[entrada]
            sal = mapa[salida]
            
            # Convertir todo a Celsius primero
            if ent == "C":
                celsius = valor
            elif ent == "F":
                celsius = (valor - 32) * 5/9
            elif ent == "K":
                celsius = valor - 273.15
            elif ent == "R":
                celsius = (valor - 491.67) * 5/9
            
            # Convertir de Celsius a la unidad de salida
            if sal == "C":
                return celsius
            elif sal == "F":
                return (celsius * 9/5) + 32
            elif sal == "K":
                return celsius + 273.15
            elif sal == "R":
                return (celsius * 9/5) + 491.67
            
            return valor  # Si misma unidad

        # Realizar conversión
        resultado = convertir_temperatura(valor, unidad_entrada, unidad_salida)
        
        # Mostrar resultado en la columna derecha con decoración
        with col2:
            st.success(f"🌟 Resultado: {resultado:.2f} {unidad_salida}")
    except Exception as e:
        st.error(f"❌ Ocurrió un error: {str(e)}")

# Footer decorativo
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Creado con Streamlit | Soporta conversiones precisas con 2 decimales. ❄️🔥</p>", unsafe_allow_html=True)


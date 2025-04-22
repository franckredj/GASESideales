import streamlit as st

# Constante de los gases ideales
R = 0.0821  # atm·L/mol·K

st.title("Calculadora de la Ecuación de Gases Ideales")
st.markdown("**Ecuación:** PV = nRT")

# Selección de la variable a calcular
variable = st.selectbox(
    "¿Qué variable deseas calcular?",
    ("Presión (P)", "Volumen (V)", "Temperatura (T)", "Número de moles (n)")
)

# Funciones para calcular cada variable
def calcular_presion(n, T, V):
    return (n * R * T) / V

def calcular_volumen(n, T, P):
    return (n * R * T) / P

def calcular_temperatura(P, V, n):
    return (P * V) / (n * R)

def calcular_moles(P, V, T):
    return (P * V) / (R * T)

# Mostrar los campos según la variable seleccionada
if variable == "Presión (P)":
    n = st.number_input("Número de moles (mol)", min_value=0.0, step=0.1)
    T = st.number_input("Temperatura (K)", min_value=0.0, step=0.1)
    V = st.number_input("Volumen (L)", min_value=0.0, step=0.1)
    if st.button("Calcular Presión"):
        if V == 0:
            st.error("El volumen no puede ser cero.")
        else:
            P = calcular_presion(n, T, V)
            st.success(f"Presión: {P:.3f} atm")

elif variable == "Volumen (V)":
    n = st.number_input("Número de moles (mol)", min_value=0.0, step=0.1)
    T = st.number_input("Temperatura (K)", min_value=0.0, step=0.1)
    P = st.number_input("Presión (atm)", min_value=0.0, step=0.1)
    if st.button("Calcular Volumen"):
        if P == 0:
            st.error("La presión no puede ser cero.")
        else:
            V = calcular_volumen(n, T, P)
            st.success(f"Volumen: {V:.3f} L")

elif variable == "Temperatura (T)":
    n = st.number_input("Número de moles (mol)", min_value=0.0, step=0.1)
    V = st.number_input("Volumen (L)", min_value=0.0, step=0.1)
    P = st.number_input("Presión (atm)", min_value=0.0, step=0.1)
    if st.button("Calcular Temperatura"):
        if n == 0:
            st.error("El número de moles no puede ser cero.")
        else:
            T = calcular_temperatura(P, V, n)
            st.success(f"Temperatura: {T:.2f} K")

elif variable == "Número de moles (n)":
    T = st.number_input("Temperatura (K)", min_value=0.0, step=0.1)
    V = st.number_input("Volumen (L)", min_value=0.0, step=0.1)
    P = st.number_input("Presión (atm)", min_value=0.0, step=0.1)
    if st.button("Calcular Número de moles"):
        if T == 0:
            st.error("La temperatura no puede ser cero.")
        else:
            n = calcular_moles(P, V, T)
            st.success(f"Número de moles: {n:.3f} mol")

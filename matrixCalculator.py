import streamlit as st
import numpy as np

# Estilos CSS para mejorar el diseño
st.markdown(
    """
    <style>
        .encabezado {
            background-color: #d4edda; /* Verde suave */
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            font-size: 16px;
            font-weight: bold;
            color: #155724;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Encabezado
st.markdown('<div class="encabezado">INTEGRANTES: Iker Fonseca, Yohana Hidalgo, Isaac Lazo, Daniela Quijano<br> Profesora Jéssica Jiménez Moscoso | Proyecto - Algebra Lineal</div>', unsafe_allow_html=True)

# Título de la aplicación
st.title("Calculadora de Determinantes de Matrices")

# Sección: Información extra - Teoría sobre Determinantes
st.header("ℹ️ Información extra: ¿Qué es un determinante?")
st.write("""
El determinante de una matriz es un valor escalar que proporciona información clave sobre las propiedades de la matriz.
Se calcula mediante operaciones como la regla de Sarrus (para matrices 3x3) o el método de eliminación gaussiana.
         
**Definicion:**
""")

st.image("Determinante_Definicion.PNG", use_container_width=False, width=1200)

st.write("""**Propiedades clave:**
- Si el determinante es cero, la matriz es *singular* y no tiene inversa.
- El determinante cambia de signo si se intercambian filas.
- Multiplicar una fila por un número multiplica el determinante por ese número.
""")

# Sección: Información extra - Ejemplos de Determinantes
st.write("**Ejemplos:**")
st.image("Ejemplo1.jpg", caption="Ejemplo de matriz 2x2", use_container_width=False, width=350)

st.write("")

st.image("Ejemplo2.jpg", caption="Ejemplo de matriz 3x3", use_container_width=False, width=400)

# Instrucciones
st.subheader("📝 Instrucciones")
st.write("""
1. Ingresa el tamaño de la matriz (n x n).
2. Llena los elementos de la matriz.
3. Haz clic en **Calcular Determinante** para obtener el resultado y ver el paso a paso.
""")

# Input para el tamaño de la matriz
size = st.number_input("Ingresa el tamaño de la matriz (n x n):", min_value=1, value=2, step=1)

# Generar dinámicamente los campos de entrada para la matriz
matrix = []
for i in range(size):
    st.write(f"**Fila {i+1}**")
    cols = st.columns(size)
    row = [cols[j].number_input(f"Fila {i+1}, Columna {j+1}", value=0.0, key=f"row_{i}_col_{j}") for j in range(size)]
    matrix.append(row)

st.write("### 🧮 Matriz ingresada:")
st.write(np.array(matrix))

def show_steps(matrix):
    st.subheader("📊 Paso a paso para calcular el determinante:")
    try:
        matrix = np.array(matrix, dtype=float)
        n = matrix.shape[0]
        det = 1
        for i in range(n):
            pivot = matrix[i, i]
            st.write(f"- Pivote en posición ({i+1}, {i+1}): {pivot:.2f}")
            if pivot == 0:
                st.error("El pivote es cero, lo que indica que el determinante es cero.")
                return 0
            det *= pivot
            for k in range(i+1, n):
                factor = matrix[k, i] / pivot
                st.write(f"  - Eliminando elementos debajo del pivote usando factor {factor:.2f}")
                matrix[k] -= factor * matrix[i]
            st.write(f"  - Matriz tras la eliminación en la columna {i+1}:")
            st.write(matrix)
        return det
    except Exception as e:
        st.error(f"Error al mostrar los pasos: {e}")

# Botón para calcular el determinante
if st.button("Calcular Determinante"):
    try:
        matrix_array = np.array(matrix, dtype=float)
        if matrix_array.shape[0] != matrix_array.shape[1]:
            st.error("La matriz debe ser cuadrada (n x n).")
        else:
            determinant = show_steps(matrix_array)
            st.success(f"### ✅ El determinante de la matriz es: {determinant:.2f}")
    except Exception as e:
        st.error(f"Error al calcular el determinante: {e}")
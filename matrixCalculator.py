import streamlit as st
import numpy as np

# Título de la aplicación
st.title("Calculadora de Determinantes de Matrices")

# Descripción de la aplicación
st.write("""
### Instrucciones:
1. Ingresa el tamaño de la matriz (n x n).
2. Llena los elementos de la matriz.
3. Haz clic en **Calcular Determinante** para obtener el resultado y ver el paso a paso.
""")

# Input para el tamaño de la matriz
size = st.number_input(
    "Ingresa el tamaño de la matriz (n x n):",
    min_value=1,
    value=2,
    step=1
)

# Generar dinámicamente los campos de entrada para la matriz
matrix = []
for i in range(size):
    st.write(f"**Fila {i+1}**")
    cols = st.columns(size)
    row = []
    for j in range(size):
        element = cols[j].number_input(
            f"Fila {i+1}, Columna {j+1}",
            value=0.0,
            key=f"row_{i}_col_{j}"
        )
        row.append(element)
    matrix.append(row)

# Mostrar la matriz ingresada
st.write("### Matriz ingresada:")
st.write(np.array(matrix))

def show_steps(matrix):
    st.write("### Paso a paso para calcular el determinante:")
    try:
        matrix = np.array(matrix, dtype=float)
        n = matrix.shape[0]
        det = 1
        for i in range(n):
            pivot = matrix[i, i]
            st.write(f"- Tomando el pivote en la posición ({i+1}, {i+1}): {pivot:.2f}")
            if pivot == 0:
                st.error("El pivote es cero, lo que indica que el determinante es cero.")
                return 0
            det *= pivot
            for k in range(i+1, n):
                factor = matrix[k, i] / pivot
                st.write(f"  - Eliminando elementos debajo del pivote usando el factor {factor:.2f}")
                matrix[k] -= factor * matrix[i]
            st.write(f"  - Matriz tras la eliminación de la columna {i+1}:")
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
            st.success(f"### El determinante de la matriz es: {determinant:.2f}")
    except Exception as e:
        st.error(f"Error al calcular el determinante: {e}")
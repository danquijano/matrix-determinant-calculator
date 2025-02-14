import streamlit as st
import numpy as np

st.title("Determinantes de una Matriz | Calculadora")

st.write("""
### Ingresa la matriz a calcular
Ingresa el tamaño de la matriz (n x n) y luego llena sus elementos.
""")

# Input matrix size
size = st.number_input("Ingresa el tamaño de la matriz(n x n):", min_value=1, value=2, step=1)

# Dynamically generate input fields for the matrix
matrix = []
for i in range(size):
    st.write(f"**Row {i+1}**")
    cols = st.columns(size)
    row = []
    for j in range(size):
        element = cols[j].number_input(f"Row {i+1}, Col {j+1}", value=0.0, key=f"row_{i}_col_{j}")
        row.append(element)
    matrix.append(row)

# Display the matrix
st.write("### Tu matriz:")
st.write(np.array(matrix))

# Calculate determinant
if st.button("Calcular Determinante"):
    try:
        matrix_array = np.array(matrix)
        determinant = np.linalg.det(matrix_array)
        st.write(f"### Determinante: {determinant:.2f}")
    except:
        st.error("Matriz inválida. Por favor revise los datos.")
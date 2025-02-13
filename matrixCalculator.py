import streamlit as st
import numpy as np

st.title("Matrix Determinant Calculator")

st.write("""
### Enter your matrix
Input the size of your matrix (n x n) and then fill in the elements.
""")

# Input matrix size
size = st.number_input("Enter the size of the matrix (n x n):", min_value=1, value=2, step=1)

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
st.write("### Your Matrix:")
st.write(np.array(matrix))

# Calculate determinant
if st.button("Calculate Determinant"):
    try:
        matrix_array = np.array(matrix)
        determinant = np.linalg.det(matrix_array)
        st.write(f"### Determinant: {determinant:.2f}")
    except:
        st.error("Invalid matrix. Please check your input.")
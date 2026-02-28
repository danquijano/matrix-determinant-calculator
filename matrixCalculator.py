import streamlit as st
import numpy as np

# CSS styles for improved design
st.markdown(
    """
    <style>
        .header {
            background-color: #d4edda; /* Soft green */
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

# Header
st.markdown('<div class="header">TEAM MEMBERS: Iker Fonseca, Yohana Hidalgo, Isaac Lazo, Daniela Quijano<br> Professor Jéssica Jiménez Moscoso | Project - Linear Algebra</div>', unsafe_allow_html=True)

# Application title
st.title("Matrix Determinant Calculator")

# Section: Extra information - Theory about Determinants
st.header("ℹ️ Extra information: What is a determinant?")
st.write("""
The determinant of a matrix is a scalar value that provides key information about the matrix's properties.
It is calculated through operations such as Sarrus' rule (for 3x3 matrices) or the Gaussian elimination method.
         
**Definition:**
""")

st.image("Determinante_Definicion.PNG", use_container_width=False, width=1200)

st.write("""**Key properties:**
- If the determinant is zero, the matrix is *singular* and has no inverse.
- The determinant changes sign if rows are swapped.
- Multiplying a row by a number multiplies the determinant by that number.
""")

# Section: Extra information - Examples of Determinants
st.write("**Examples:**")
st.image("Ejemplo1.jpg", caption="Example of a 2x2 matrix", use_container_width=False, width=350)

st.write("")

st.image("Ejemplo2.jpg", caption="Example of a 3x3 matrix", use_container_width=False, width=400)

# Instructions
st.subheader("📝 Instructions")
st.write("""
1. Enter the size of the matrix (n x n).
2. Fill in the matrix elements.
3. Click **Calculate Determinant** to get the result and see the step-by-step process.
""")

# Input for matrix size
size = st.number_input("Enter the matrix size (n x n):", min_value=1, value=2, step=1)

# Dynamically generate input fields for the matrix
matrix = []
for i in range(size):
    st.write(f"**Row {i+1}**")
    cols = st.columns(size)
    row = [cols[j].number_input(f"Row {i+1}, Column {j+1}", value=0.0, key=f"row_{i}_col_{j}") for j in range(size)]
    matrix.append(row)

st.write("### 🧮 Entered matrix:")
st.write(np.array(matrix))

def show_steps(matrix):
    st.subheader("📊 Step-by-step determinant calculation:")
    try:
        matrix = np.array(matrix, dtype=float)
        n = matrix.shape[0]
        det = 1
        for i in range(n):
            pivot = matrix[i, i]
            st.write(f"- Pivot at position ({i+1}, {i+1}): {pivot:.2f}")
            if pivot == 0:
                st.error("The pivot is zero, which indicates the determinant is zero.")
                return 0
            det *= pivot
            for k in range(i+1, n):
                factor = matrix[k, i] / pivot
                st.write(f"  - Eliminating elements below the pivot using factor {factor:.2f}")
                matrix[k] -= factor * matrix[i]
            st.write(f"  - Matrix after elimination in column {i+1}:")
            st.write(matrix)
        return det
    except Exception as e:
        st.error(f"Error displaying steps: {e}")

# Button to calculate determinant
if st.button("Calculate Determinant"):
    try:
        matrix_array = np.array(matrix, dtype=float)
        if matrix_array.shape[0] != matrix_array.shape[1]:
            st.error("The matrix must be square (n x n).")
        else:
            determinant = show_steps(matrix_array)
            st.success(f"### ✅ The determinant of the matrix is: {determinant:.2f}")
    except Exception as e:
        st.error(f"Error calculating the determinant: {e}")

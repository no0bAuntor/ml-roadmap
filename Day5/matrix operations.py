import numpy as np

A = np.array([[4, 2, 6], [8, 10, 12], [-5, 3, 7]])
B = np.array([[12, 3, 0], [9, -4, 1], [2, 5, 1]])

# Multiplication
try:
    print(f"Matrix multiplication of A and B:\n{A@B}")
except ValueError as e:
    print(f"Error in matrix multiplication: {e}")

# Rank of a matrix
print(f"Rank of matrix A: {np.linalg.matrix_rank(A)}")

# Solve linear equation
b = np.array([4, 0, 36])
# Ax = b
print(f"x: \n{np.linalg.solve(A, b)}")

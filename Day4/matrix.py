import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

print(f"Addition of two matrices:\n{a+b}")
print(f"Subtraction of two matrices:\n{a-b}")

try:
    print(f"Multiplication of matrices:\n{a@b}")
except ValueError as e:
    print(f"Error: {e}. Matrices cannot be multiplied due to incompatible dimensions.")

print(f"transpose of matrix a:\n{a.T}")

c = np.array([[1, 2, 3], [4, 5, 6], [10, 8, 9]])
print(f"Determinant of matrix c:\n{np.linalg.det(c)}")

try:
    print(f"Inverse of matrix c:\n{np.linalg.inv(c)}")
except np.linalg.LinAlgError:
    print("Matrix c is singular and cannot be inverted.")


eigenvalues, eigenvectors = np.linalg.eig(c)
print(f"Eigenvalues of matrix c:\n{eigenvalues}")
print(f"Eigenvectors of matrix c:\n{eigenvectors}")


print(f"Rank of matrix c:\n{np.linalg.matrix_rank(c)}")
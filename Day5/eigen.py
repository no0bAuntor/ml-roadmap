import numpy as np

A=np.array([[4,0], [6, 7]])

eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues: ", eigenvalues)
print("Eigenvectors: \n", eigenvectors)
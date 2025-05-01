import numpy as np

a = np.array([1, 2, 3])
b = np.array([7, 8, 9])

print(f"Addition of two vectors:\n{a+b}")

print(f"Scaler multiplication of vector a:\n{2*a}")

print(f"Dot product of a and b vector are:\n {np.dot(a,b)}")

print(f"Norm of vector a is:\n {np.linalg.norm(a)}")

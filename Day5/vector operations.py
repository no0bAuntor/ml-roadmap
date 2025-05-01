import numpy as np

A = np.array([4, 1, -6])

B = np.array([7, 2, 3])


# Norm
print(f"Norm of vector A: {np.linalg.norm(A)}")

# Dot product
try:
    print(f"Dot product of vector A and B: {np.dot(A, B)}")
except ValueError as e:
    print(f"Error in dot product: {e}")

# Angle between two vectors
cosine_angle = np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))
angle = np.arccos(cosine_angle)
print(f"Angle between A and B in degree: {angle*180/np.pi}")

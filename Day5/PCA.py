import numpy as np
import matplotlib.pyplot as plt

# Original 3D data
data = np.array([[1, 2, 0],
                 [4, 6, 6],
                 [12, 8, 3]])

# Step 1: Center the data
data_centered = data - np.mean(data, axis=0)

# Step 2: Covariance matrix
cov_data = np.cov(data_centered.T)

# Step 3: Eigen decomposition
eigenvalues, eigenvectors = np.linalg.eig(cov_data)

# Sort by eigenvalue magnitude
sorted_indices = np.argsort(eigenvalues)[::-1]
eigenvectors = eigenvectors[:, sorted_indices]

# ----- 3D to 2D -----
projected_data_2D = data_centered @ eigenvectors[:, :2]
print("Projected Data (3D to 2D):", projected_data_2D)

# ----- 3D to 1D -----
projected_data_1D = data_centered @ eigenvectors[:, 0]
print("Projected Data (3D to 1D):", projected_data_1D)

# ==== Visualization ====

fig = plt.figure(figsize=(15, 5))

# Original 3D data
ax1 = fig.add_subplot(1, 3, 1, projection='3d')
ax1.scatter(data[:, 0], data[:, 1], data[:, 2], color='blue')
ax1.set_title('Original 3D Data')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

# Projected 2D data
ax2 = fig.add_subplot(1, 3, 2)
ax2.scatter(projected_data_2D[:, 0], projected_data_2D[:, 1], color='green')
ax2.set_title('Projected Data (3D → 2D)')
ax2.set_xlabel('PC1')
ax2.set_ylabel('PC2')

# Projected 1D data
ax3 = fig.add_subplot(1, 3, 3)
ax3.scatter(projected_data_1D, np.zeros_like(projected_data_1D), color='red')
ax3.set_title('Projected Data (3D → 1D)')
ax3.set_xlabel('PC1')
ax3.set_yticks([])

plt.tight_layout()
plt.show()

# Linear Algebra: Theory and Applications

## 📌 What is Linear Algebra?
Linear Algebra is the branch of mathematics concerning **vectors**, **matrices**, and **linear transformations**. It is the foundation of many fields including **Machine Learning**, **Computer Graphics**, and **Data Science**.

---

## 🧠 Core Concepts

### 1. **Scalars, Vectors, Matrices**
- **Scalar**: A single number (e.g., 5)
- **Vector**: A 1D array of numbers (e.g., [1, 2, 3])
- **Matrix**: A 2D array of numbers
- **Tensor**: Generalized matrix of higher dimensions

### 2. **Matrix Operations**
- Addition/Subtraction: Element-wise
- Scalar Multiplication: Multiply every element by a scalar
- Matrix Multiplication: Dot product of rows and columns
- Transpose: Flip matrix over its diagonal
- Inverse: A matrix `A` such that `A × A⁻¹ = I`
- Determinant: Scalar value that describes a matrix’s properties (e.g., invertibility)

### 3. **Vector Operations**
- Magnitude (Norm): Length of a vector
- Dot Product: `a · b = |a||b|cosθ`
- Cross Product: Vector perpendicular to two vectors (in 3D)

### 4. **Special Matrices**
- **Identity Matrix (I)**: Diagonal = 1, rest = 0
- **Diagonal Matrix**: Non-zero values only on diagonal
- **Symmetric Matrix**: `A = Aᵀ`
- **Orthogonal Matrix**: `A⁻¹ = Aᵀ`

---

## 🧮 Linear Equations
- A system of equations can be represented as:  
  **Ax = b**, where:
  - A: Coefficient matrix
  - x: Variable vector
  - b: Constant vector

- Solving methods:
  - Row Reduction (Gaussian elimination)
  - Matrix Inversion
  - LU Decomposition

---

## 📊 Applications in Machine Learning

### 🔸 1. **Data Representation**
- Features and samples are stored as matrices or tensors.
- Each row = sample, each column = feature.

### 🔸 2. **Model Training**
- Linear Regression: `y = Xw + b`
- Optimization algorithms (e.g., gradient descent) use vector calculus and matrix operations.

### 🔸 3. **Principal Component Analysis (PCA)**
- Reduces dimensionality using eigenvectors and eigenvalues of the covariance matrix.

### 🔸 4. **Neural Networks**
- Inputs, weights, and activations are handled via matrix multiplication.

### 🔸 5. **Computer Vision**
- Images = matrices of pixels.
- Filters in CNNs use convolution, a linear operation.

---

## 🛠️ Libraries in Python

- **NumPy**: Core library for linear algebra
- **SciPy**: Advanced linear algebra routines
- **TensorFlow / PyTorch**: For GPU-accelerated operations

---

## 📚 Key Takeaways

- Understanding linear algebra is **essential** for ML.
- Matrix and vector operations make models efficient.
- Concepts like eigenvalues, singular value decomposition (SVD), and projections are key to understanding how data behaves in high-dimensional spaces.

---

## ✏️ Further Topics (Explore Later)

- Eigen Decomposition
- Singular Value Decomposition (SVD)
- Projection Matrices
- Gram-Schmidt Process
- Moore–Penrose Pseudoinverse
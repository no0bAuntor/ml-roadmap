### 🧠 **Principal Component Analysis (PCA): Basic Information**

**Principal Component Analysis (PCA)** is a **dimensionality reduction** technique used in machine learning and statistics. It transforms a large set of variables into a smaller one that still contains most of the information in the original dataset.

---

### 📌 **Why Use PCA?**

* Reduce **computational cost** in ML models.
* **Visualize** high-dimensional data (e.g., 3D → 2D).
* Remove **correlated features**.
* **Denoise** data by ignoring less significant components.

---

### ⚙️ **How PCA Works (Step-by-Step)**

1. **Standardize the Data**

   * Subtract the mean from each feature to center the data.
   * Optionally scale features to have unit variance (especially for different units).

2. **Compute the Covariance Matrix**

   * Measures how features vary with each other.

3. **Eigen Decomposition**

   * Calculate **eigenvalues** and **eigenvectors** of the covariance matrix.
   * Eigenvectors are the **principal components**.
   * Eigenvalues show how much **variance** each principal component captures.

4. **Sort and Select Components**

   * Sort eigenvectors by descending eigenvalues.
   * Choose top *k* eigenvectors to form the **projection matrix**.

5. **Project the Data**

   * Multiply the original (centered) data with the projection matrix to get lower-dimensional data.

---

### 📊 Example in ML

| Use Case                 | PCA Benefit                                      |
| ------------------------ | ------------------------------------------------ |
| Image Compression        | Reduce pixel features while preserving key info. |
| Preprocessing for Models | Remove noise and reduce overfitting.             |
| Visualization            | Plot data in 2D/3D for understanding patterns.   |
| Speeding up training     | Fewer features → faster model training.          |

---

### 💡 PCA Limitations

* Assumes **linear relationships** between features.
* May discard features that are small in variance but important for prediction.
* Not ideal for **categorical data** unless encoded numerically.

---
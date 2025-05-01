# 📚 Mean and Variance in Machine Learning

## What is Mean?
- **Mean** is the **average value** of a set of numbers.
- It tells us the **central tendency** — where most values cluster.
- Used in ML for:
  - Understanding datasets.
  - Centering/normalizing data.
  - Finding biases in predictions.

### 🔹 Formula:
<!-- $$
\text{Mean} = \frac{\sum_{i=1}^{n} x_i}{n}
$$ -->
`Mean = (Sum of all values) / (Number of values)`

### 🔹 Example:
For `[2, 4, 6]`:  
<!-- Mean = $\frac{2 + 4 + 6}{3} = 4$ -->
`Mean = (2 + 4 + 6) ÷ 3 = 4`

---

## What is Variance?
- **Variance** measures **how spread out** numbers are from the mean.
- Key for:
  - Model **stability**.
  - Balancing **underfitting/overfitting**.
  - Feature scaling (e.g., KNN, SVM).

### 🔹 Formula:
<!-- $$
\text{Variance} = \frac{\sum_{i=1}^{n} (x_i - \text{Mean})^2}{n}
$$ -->
`Variance = Sum of [(each value - mean)²] / (Number of values)`

### 🔹 Example:
For `[2, 4, 6]` (Mean = 4):  
<!-- 
Variance = $\frac{(2-4)^2 + (4-4)^2 + (6-4)^2}{3} = \frac{4 + 0 + 4}{3} \approx 2.67$
-->
`Variance = [(2-4)² + (4-4)² + (6-4)²] ÷ 3 = (4 + 0 + 4) ÷ 3 ≈ 2.67`

---

# 🎯 Summary
- **Mean** = Center of the data.
- **Variance** = Spread around the center.
- **Critical** for data understanding, feature engineering, and model building.

> ✨ *"Mastering Mean and Variance is the first step toward ML wizardry."*

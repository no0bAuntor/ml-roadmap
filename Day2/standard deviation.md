# 📚 Standard Deviation in Machine Learning

## What is Standard Deviation?
- **Standard Deviation (σ)** measures the **amount of variation or dispersion** in a set of values.
- It tells us how **spread out** the data points are from the mean.
- A **low σ** means data points are close to the mean, while a **high σ** means they are widely spread.
- In Machine Learning, standard deviation is used for:
  - **Feature scaling** (normalization/standardization).
  - Detecting **outliers** in datasets.
  - Assessing **model uncertainty** (e.g., in ensemble methods).
  - Evaluating **data distribution** (e.g., in Gaussian models).

### 🔹 Formula:
<!-- $$
\sigma = \sqrt{\text{Variance}} = \sqrt{\frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}}
$$ -->
`σ = √(Variance) = √[ Σ(xᵢ - μ)² / N ]`  
where:
- `xᵢ` = each data point
- `μ` = mean of the data
- `N` = number of data points

### 🔹 Simple Example:
If numbers are `[2, 4, 6]`:
1. **Mean (μ)** = (2 + 4 + 6) / 3 = `4`
2. **Variance** = [(2-4)² + (4-4)² + (6-4)²] / 3 = `(4 + 0 + 4) / 3 ≈ 2.67`
3. **Standard Deviation (σ)** = √(2.67) ≈ `1.63`

---

# 🎯 Key Takeaways
- **Standard Deviation** = Square root of variance.
- Helps measure **data spread** and **consistency**.
- Used in **preprocessing, outlier detection, and model evaluation** in Machine Learning.

> ✨ *"Standard deviation is the ruler of variability—knowing it helps tame the chaos in data!"*
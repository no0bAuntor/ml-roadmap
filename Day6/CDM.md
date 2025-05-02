
---

# 📘 Cumulative Distribution Function (CDF)

## 📖 Theory

A **Cumulative Distribution Function (CDF)** gives the **cumulative probability** that a random variable $X$ is **less than or equal to** a value $x$:

$$
F(x) = P(X \leq x)
$$

### ✅ Key Properties:

* **Monotonically increasing**: CDF never decreases as $x$ increases.
* **Defined for all values**, even between discrete points.
* $\lim_{x \to \infty} F(x) = 1$
* For discrete variables, it's a **step function**; for continuous, it's smooth.

---

## 💡 Example

```python
import numpy as np
import matplotlib.pyplot as plt

# Sample data
data = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]
data_sorted = np.sort(data)

# Calculate CDF
cdf = np.arange(1, len(data_sorted) + 1) / len(data_sorted)

# Plot
plt.plot(data_sorted, cdf, marker='.', linestyle='none')
plt.xlabel('Value')
plt.ylabel('CDF(x)')
plt.title('CDF of Sample Data')
plt.grid(True)
plt.show()
```

📝 This CDF graph shows how the cumulative probability increases with each new data point.

---

## ⚙️ Applications in Machine Learning

1. **Anomaly Detection**

   * Detect if a value falls in a **rare tail** (e.g., < 5th percentile or > 95th percentile).

2. **Feature Engineering**

   * Use CDF to **normalize** data using quantiles or transform features into probability space.

3. **Fairness in ML**

   * Compare **CDFs across different groups** to detect bias in model outputs.

4. **ROC Curves**

   * ROC analysis compares the **CDF of true positives and false positives**.

5. **Sampling & Simulation**

   * Convert **uniform samples** into samples from other distributions using **inverse CDF**.

---

## 📌 Summary

* **CDF gives richer insights** than histograms or PMFs for comparing distributions.
* Used heavily in **model evaluation, data preprocessing, and fairness checks**.
* Easy to calculate from sorted data + ranks.

---

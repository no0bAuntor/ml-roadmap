# 📏 Regression Evaluation Metrics: MSE, RMSE, and R² Score

When training regression models (like Linear Regression), it's important to measure **how good the model's predictions are**. Here are three essential metrics to evaluate your model:

---

## 1️⃣ Mean Squared Error (MSE)

### 📘 Definition:
The **average of the squared differences** between predicted values and actual values.

### 🧮 Formula:
$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

Where:
- $y_i$ = actual value  
- $\hat{y}_i$ = predicted value  
- $n$ = number of samples

### 🔍 Interpretation:
- Lower MSE = better performance
- Penalizes **larger errors** more than smaller ones (because of squaring)

---

## 2️⃣ Root Mean Squared Error (RMSE)

### 📘 Definition:
The **square root of MSE**. It brings the error back to the same unit as the target variable.

### 🧮 Formula:
$$
\text{RMSE} = \sqrt{\text{MSE}} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
$$

### 🔍 Interpretation:
- More **intuitive** than MSE since it's in the same unit as the output (e.g., marks, price)
- Still penalizes large errors heavily

---

## 3️⃣ R² Score (Coefficient of Determination)

### 📘 Definition:
Measures the **proportion of variance** in the dependent variable that is predictable from the independent variable(s).

### 🧮 Formula:
$$
R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
$$

Where:
- $\bar{y}$ is the mean of actual values

### 🔍 Interpretation:
- R² = 1 → Perfect model (100% variance explained)
- R² = 0 → Model does no better than guessing the mean
- R² < 0 → Model performs worse than a horizontal line

---

## 🧠 Summary Table

| Metric | Good Value | Penalizes Large Errors | Unit of Output | Use Case              |
|--------|------------|------------------------|----------------|------------------------|
| MSE    | Lower      | ✅ Yes                 | Squared        | Pure error measurement |
| RMSE   | Lower      | ✅ Yes                 | Same as target | Easy to interpret      |
| R²     | Close to 1 | ❌ No                  | Unitless       | Variance explained     |

---

## 📌 In Python (scikit-learn):

```python
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
```

---

## 🧪 Example:
| Actual (y) | Predicted (ŷ) |
| ---------- | ------------- |
| 60         | 58            |
| 70         | 67            |
| 80         | 77            |


- **MSE** = 4.67
- **MAE** = 
- **$R^2$ Score** =0.98 
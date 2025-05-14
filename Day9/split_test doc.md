# ✂️ train_test_split Practice – Scikit-learn

## 📘 Purpose

This module is for practicing how to **split a dataset into training and testing sets** using `train_test_split()` from `scikit-learn`.

Splitting your data is a **critical step** in any ML project to:
- Train your model on one part of the data
- Test how well it generalizes to unseen data

---

## 📦 Tools & Libraries Used

- Python
- NumPy
- Pandas
- scikit-learn

---

## 🔄 train_test_split() – Overview

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

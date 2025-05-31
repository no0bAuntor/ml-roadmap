# 🔀 One-vs-Rest (OvR) Strategy – Multiclass Classification

## 📘 What is One-vs-Rest (OvR)?

**One-vs-Rest (OvR)** is a strategy used to extend binary classifiers to work with **multiclass classification problems**.

In OvR, for a problem with **n classes**, the algorithm builds **n separate binary classifiers**:
- Each one learns to distinguish **one class vs all others**.

---

## ⚙️ How It Works (Step-by-Step)

Let’s say you have 3 classes:  
`Class 0`, `Class 1`, and `Class 2`.

OvR will build:

1. **Classifier A**: Class 0 vs (Class 1 + Class 2)  
2. **Classifier B**: Class 1 vs (Class 0 + Class 2)  
3. **Classifier C**: Class 2 vs (Class 0 + Class 1)

Each classifier will output a **confidence score (probability)** for its own class.

✅ At prediction time, the model compares all classifiers and chooses the class with the **highest score**.

---

## 🧠 Real Example (Iris Dataset)

Suppose a Logistic Regression model is trained on:

- `Setosa` (0)
- `Versicolor` (1)
- `Virginica` (2)

OvR builds 3 classifiers:
- LogisticReg_0: Setosa vs [Versicolor, Virginica]
- LogisticReg_1: Versicolor vs [Setosa, Virginica]
- LogisticReg_2: Virginica vs [Setosa, Versicolor]

When given a new flower:
- Each classifier returns a score.
- Example:
  - Classifier 0 → 0.2
  - Classifier 1 → 0.6
  - Classifier 2 → 0.1

🟢 The model predicts class `1` (Versicolor), because it had the **highest probability**.

---

## 🧪 Advantages

| Benefit                | Description                                     |
|------------------------|-------------------------------------------------|
| Simple & Efficient     | Easy to implement using any binary classifier   |
| Scales well            | Works with many standard algorithms (like Logistic Regression, SVMs) |
| Interpretable          | Each classifier is trained independently        |

---

## ⚠️ Limitations

| Limitation             | Description                                     |
|------------------------|-------------------------------------------------|
| Conflicting predictions| Two classifiers may be confident at the same time |
| Imbalanced classes     | May be biased toward majority class             |
| Not ideal for correlated classes | OvR assumes independence between classifiers |

---

## 📌 OvR vs OvO (One-vs-One)

| Strategy     | Classifiers Built | Use Case                                  |
|--------------|-------------------|-------------------------------------------|
| One-vs-Rest  | `n` classifiers   | Default for Logistic Regression, fast     |
| One-vs-One   | `n(n-1)/2`        | Preferred in SVMs, more complex problems   |

---

## 📝 In scikit-learn

OvR is used **automatically** by many classifiers like `LogisticRegression`, `RidgeClassifier`, etc.

You can also use it manually:

```python
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression

model = OneVsRestClassifier(LogisticRegression())
model.fit(X_train, y_train)
```
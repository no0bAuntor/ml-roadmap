# 🌈 Multiclass Classification

## 📘 What is Multiclass Classification?

Multiclass classification is a type of **supervised learning** where the target (label) can belong to **more than two classes**.

Unlike **binary classification** (which predicts 0 or 1), multiclass classification predicts one of **three or more distinct classes**.

---

## 🧠 Examples:

| Problem                                 | Classes                          |
|----------------------------------------|----------------------------------|
| Iris Flower Classification             | Setosa, Versicolor, Virginica   |
| Handwritten Digit Recognition (MNIST)  | 0 through 9                     |
| Weather Prediction                     | Sunny, Cloudy, Rainy, Snowy     |
| Type of Disease Diagnosis              | Flu, Cold, Allergy, COVID-19    |

---

## ⚙️ Algorithms That Support Multiclass Classification

Most classification algorithms support multiclass either directly or using strategies:

- **Logistic Regression** (with One-vs-Rest)
- **Decision Trees**
- **Random Forests**
- **K-Nearest Neighbors**
- **Support Vector Machines (One-vs-One / OvR)**
- **Neural Networks (Softmax Output Layer)**

---

## 🧰 Multiclass Strategies in scikit-learn

### 🔹 One-vs-Rest (OvR) (default for Logistic Regression)

- Trains one binary classifier per class.
- For each test sample, all classifiers vote.
- Class with **highest score wins**.

### 🔹 One-vs-One (OvO)

- Trains classifiers for **every pair of classes**.
- More computationally expensive, used in SVMs.

---

## 🧪 Evaluation Metrics for Multiclass Classification

| Metric         | Description                                            |
|----------------|--------------------------------------------------------|
| Accuracy       | Overall correct predictions                            |
| Confusion Matrix | Shows correct and incorrect predictions by class     |
| Precision      | How many predicted for class X were actually correct   |
| Recall         | How many actual class X samples were correctly found   |
| F1 Score       | Balance between precision and recall                   |

> Use `classification_report()` from scikit-learn to see these metrics.

---

## 📊 Iris Dataset Example (3-class problem)

- Features: Sepal/petal length and width
- Classes:
  - `0` = Setosa
  - `1` = Versicolor
  - `2` = Virginica

Model output will predict one of these three classes using Logistic Regression (or any classifier).

---

## ✅ Summary

| Feature             | Binary Classification   | Multiclass Classification    |
|---------------------|-------------------------|-------------------------------|
| Output labels       | 2 (e.g., 0 or 1)         | 3+ classes                    |
| Evaluation          | Accuracy, Precision, Recall | Same, extended to multiple classes |
| Common Use Cases    | Spam detection, fraud     | Flower type, digit, emotion  |

---

> 🎯 **Multiclass classification** is the foundation of many real-world applications — from diagnosing diseases to identifying images, sounds, and patterns.


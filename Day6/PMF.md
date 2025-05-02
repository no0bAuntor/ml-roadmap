
---

# 📘 Probability Mass Function (PMF)

## 📖 Theory

A **Probability Mass Function (PMF)** is a function that gives the **probability of discrete outcomes**. It describes the probability distribution of a **discrete random variable**, assigning a probability to each possible value.

* The PMF of a random variable $X$, denoted as $P(X = x)$, satisfies:

  $$
  \sum P(X = x_i) = 1
  $$
* PMFs are only defined for **discrete variables** (e.g., coin tosses, dice rolls, word counts).
* Each probability must satisfy $0 \leq P(X = x) \leq 1$

---

## 💡 Example

Simulating the PMF of rolling a fair 6-sided die:

```python
from collections import Counter

rolls = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6]
counts = Counter(rolls)
total = len(rolls)

pmf = {val: freq / total for val, freq in counts.items()}
print(pmf)
```

**Output:**

```python
{1: 0.083, 2: 0.167, 3: 0.083, 4: 0.25, 5: 0.083, 6: 0.333}
```

📝 The PMF tells us the empirical probability of each die face based on the observed data.

---

## ⚙️ Applications in Machine Learning

1. **Naive Bayes Classifier**

   * PMFs estimate the likelihood $P(x_i | y)$ for each feature given the class.
   * Especially used for text classification, spam filtering, and sentiment analysis.

2. **Language Models (e.g., n-grams)**

   * Estimate $P(w_i | w_{i-1}, ..., w_{i-n})$ from word frequency counts.

3. **Recommendation Systems**

   * PMFs model the probability of users liking certain items (from rating distributions).

4. **Sampling & Synthetic Data Generation**

   * Discrete sampling from PMFs is used to generate synthetic data (for bootstrapping, GANs, etc.).

---

## 📌 Summary

* PMFs are essential for modeling and reasoning about **discrete probabilities**.
* They are foundational in **Bayesian models**, **text processing**, and **classification**.
* Easy to implement using `Counter` in Python, and very interpretable.

---

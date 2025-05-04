# 📊 Bayes Theorem & Naive Bayes Classifier

## 🔍 What is Bayes Theorem?

Bayes Theorem is a fundamental concept in probability theory that describes the probability of an event, based on prior knowledge of conditions that might be related to the event.

### 🔣 Formula:

$
P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}
$

- **P(A|B)**: Posterior probability (probability of hypothesis A given data B)
- **P(B|A)**: Likelihood (probability of data B given hypothesis A)
- **P(A)**: Prior probability of hypothesis A
- **P(B)**: Total probability of data B

---

## 🤖 What is Naive Bayes Classifier?

Naive Bayes is a **probabilistic machine learning algorithm** based on Bayes Theorem, with a strong (naive) assumption that **features are independent** given the class.

Despite the assumption being rarely true, Naive Bayes often performs surprisingly well, especially in text classification problems.

---

## 📘 Example (Manual):

Let's say we're classifying SMS as "spam" or "ham".

Training data:

| Message             | Class |
|---------------------|-------|
| "free money now"    | spam  |
| "call now"          | spam  |
| "hi how are you"    | ham   |
| "let's meet tomorrow"| ham   |

We want to classify: `"free call now"`

Using Naive Bayes, we:

1. Calculate prior probabilities:  
   - P(spam) = 2/4 = 0.5  
   - P(ham) = 2/4 = 0.5

2. Tokenize and count words by class.

3. Apply Laplace smoothing to avoid 0 probabilities.

4. Calculate posterior probabilities using:
$$
\log P(\text{class}) + \sum \log P(\text{word}|\text{class})
$$

5. Choose class with highest posterior score.

---

## 🛠 Applications in Machine Learning

Naive Bayes is widely used in the following areas:

- ✉️ **Spam filtering** – Classify emails as spam or ham.
- 💬 **Sentiment analysis** – Positive or negative sentiment.
- 📄 **Document categorization** – News, sports, politics, etc.
- 🧬 **Medical diagnosis** – Predict disease likelihood from symptoms.
- 🕵️‍♂️ **Fraud detection** – Detect abnormal transactions.

---

## 🧪 Pros and Cons

### ✅ Pros:
- Simple and fast.
- Works well with small datasets.
- Performs well on text classification.

### ❌ Cons:
- Assumes feature independence.
- Not ideal for features that are highly correlated.

---

## 🧾 How to Use in Code?

We can implement it:
- 📦 From scratch (educational purposes).
- ⚙️ Using libraries like `scikit-learn` for real applications.

```python
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

X = ["free money now", "call now", "hi how are you", "let's meet tomorrow"]
y = ["spam", "spam", "ham", "ham"]

vectorizer = CountVectorizer()
X_counts = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_counts, y)

test = vectorizer.transform(["free call now"])
print(model.predict(test))  # Output: ['spam']

import math
from collections import defaultdict

class NaiveBayesClassifier:
    def __init__(self):
        self.class_counts = defaultdict(int)
        self.word_counts = defaultdict(lambda: defaultdict(int))
        self.vocab = set()
        self.total_docs = 0

    def tokenize(self, text):
        return text.lower().split()

    def train(self, data):
        for message, label in data:
            self.total_docs += 1
            self.class_counts[label] += 1
            for word in self.tokenize(message):
                self.word_counts[label][word] += 1
                self.vocab.add(word)

    def predict(self, message):
        words = self.tokenize(message)
        class_scores = {}

        for label in self.class_counts:
            # Start with log prior
            log_prob = math.log(self.class_counts[label] / self.total_docs)
            total_words = sum(self.word_counts[label].values())
            vocab_size = len(self.vocab)

            for word in words:
                word_freq = self.word_counts[label][word] + 1  # Laplace smoothing
                word_prob = word_freq / (total_words + vocab_size)
                log_prob += math.log(word_prob)

            class_scores[label] = log_prob

        return max(class_scores, key=class_scores.get)

# Sample usage
if __name__ == "__main__":
    data = [
        ("free money now", "spam"),
        ("call now", "spam"),
        ("hi how are you", "ham"),
        ("let's meet tomorrow", "ham")
    ]

    clf = NaiveBayesClassifier()
    clf.train(data)

    test_messages = ["free call now", "how are you", "win money", "let's call now"]
    for msg in test_messages:
        prediction = clf.predict(msg)
        print(f"Message: '{msg}' => Predicted: {prediction}")
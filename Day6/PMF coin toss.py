import random
import matplotlib.pyplot as plt
from collections import Counter

# Simulate 1000 coin toss
coin_flips = [random.choice(["Heads", "Tails"]) for _ in range(1000)]

# Calculate PMF
flip_counts = Counter(coin_flips)
print(flip_counts)
total_flips = len(coin_flips)
pmf = {flip: count / total_flips for flip, count in flip_counts.items()}
print(f"PMF: {pmf}")

# plot PMF
plt.bar(pmf.keys(), pmf.values(), color=['skyblue', 'wheat'])
plt.title("PMF of Coin Toss")
plt.xlabel("Outcome")
plt.ylabel("Probability")

plt.show()
# The code simulates tossing a coin 10 times and prints the result of each toss.
import random

outcome=["Heads", "Tails"]
head=0
tail=0

for x in range(10):
    toss=random.choice(outcome)
    print(f"Toss{x+1}: {toss}")
    if toss=="Heads":
        head+=1
    else:
        tail+=1
print(f"Total Heads: {head}")        
print(f"Total Tails: {tail}")        
'''
# 📚 Python Sets: A Complete Guide

## What is a Set?
- A **set** is an **unordered**, **mutable** collection of **unique** elements
- Does **not maintain insertion order**
- Cannot contain duplicate values
- Optimized for membership testing (faster than lists)
- Can store only **hashable** types (immutable types like int, float, str, tuple)

### 🔹 Syntax:
my_set = {item1, item2, item3}  # Curly braces
empty_set = set()                # NOT {} (that's a dict)
'''

# ---
# Key Features of Sets
# 1. **Uniqueness**: Automatically removes duplicates
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)  # Output: {1, 2, 3}

# 2. **Unordered**: No index positions
# print(numbers[0])  # TypeError: 'set' object is not subscriptable

# 3. **Mutable**: Can add/remove items
# 4. **Mathematical Operations**: Union, intersection, difference etc.

'''
## Common Operations
'''

### 1️⃣ Create a Set
empty_set = set()               # Correct way
fruits = {"apple", "banana", "cherry"}
mixed = {1, "hello", 3.14, (1, 2)}  # Can contain tuples
# invalid = {[1, 2]}           # TypeError: unhashable type 'list'

### 2️⃣ Add Items
colors = {"red", "green"}
colors.add("blue")               # Add single item
colors.update(["yellow", "orange"])  # Add multiple items

### 3️⃣ Remove Items
colors.discard("red")          # Safe remove (no error if missing)
colors.remove("green")         # Raises KeyError if missing
colors.pop()                   # Removes arbitrary item (Front item in Python)
colors.clear()                 # Empty the set

### 4️⃣ Set Operations
a = {1, 2, 3}
b = {2, 3, 4}

print(a | b)   # Union: {1, 2, 3, 4}
print(a & b)   # Intersection: {2, 3}
print(a - b)   # Difference (in a not b): {1}
print(a ^ b)   # Symmetric difference: {1, 4}

### 5️⃣ Membership Testing
if "apple" in fruits:
    print("Found!")

'''
### 6️⃣ Set Methods
| Method               | Description                         | Example                     |
|----------------------|-------------------------------------|-----------------------------|
| add(x)               | Adds single element x               | fruits.add("mango")         |
| update(iterable)     | Adds multiple elements              | fruits.update(["kiwi", "pear"]) |
| remove(x)            | Removes x (raises error if missing) | fruits.remove("apple")      |
| discard(x)           | Removes x (no error if missing)     | fruits.discard("apple")     |
| pop()                | Removes arbitrary element           | fruits.pop()                |
| clear()              | Removes all elements                | fruits.clear()              |
| union(s)             | Returns union of sets               | a.union(b)                  |
| intersection(s)      | Returns intersection                | a.intersection(b)           |
| difference(s)        | Returns elements in a not in b      | a.difference(b)             |
| symmetric_difference(s)| Returns elements in either but not both | a.symmetric_difference(b) |
| issubset(s)          | Checks if all elements are in s     | a.issubset(b)               |
| issuperset(s)        | Checks if contains all elements of s| a.issuperset(b)             |
'''

# ---
# Advanced Use Cases

### 1️⃣ Removing List Duplicates
names = ["Alice", "Bob", "Alice", "Charlie"]
unique_names = list(set(names))  # ['Charlie', 'Alice', 'Bob']

### 2️⃣ Frozenset (Immutable Set)
immutable_set = frozenset([1, 2, 3])
# immutable_set.add(4)  # AttributeError

### 3️⃣ Set Comprehension
squares = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}

### 4️⃣ Finding Shared/Distinct Elements
recipes = {"pizza", "pasta", "salad"}
my_meals = {"pizza", "burger"}
common = recipes & my_meals  # {"pizza"}

'''
# 🎯 Summary
- **Unique Elements**: Automatic duplicate removal
- **Fast Lookups**: Optimized for membership tests
- **Mathematical Operations**: Built-in set algebra
- **Mutable But Unordered**: Can modify but can't index
- **Memory Efficient**: Than lists for unique collections

> ✨ "Sets are Python's mathematical gift for efficient uniqueness operations!"
'''

# ---
# Set vs List vs Tuple Cheat Sheet
'''
Feature       | Set             | List            | Tuple
--------------|-----------------|-----------------|-----------------
Ordered       | ❌ No           | ✔️ Yes          | ✔️ Yes
Mutable       | ✔️ Yes          | ✔️ Yes          | ❌ No
Duplicates    | ❌ No           | ✔️ Yes          | ✔️ Yes
Use Case      | Unique items    | Ordered sequence| Fixed data
Membership    | O(1) super fast | O(n) slow       | O(n) slow
'''
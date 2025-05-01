'''
# 📚 Python Tuples: A Complete Guide

## What is a Tuple?
- A **tuple** is an **immutable**, **ordered** collection of items (elements).
- Allows **duplicate** values.
- Can store **mixed data types** (int, float, string, etc.).
- Faster than lists for fixed data.

### 🔹 Syntax:
my_tuple = (item1, item2, item3)  # Parentheses (optional for >1 item)
single_item_tuple = (42,)          # Comma required for single item
'''

# ---
# Key Features of Tuples
# 1. **Immutable**: Cannot be modified after creation
coordinates = (10, 20)
# coordinates[0] = 5  # TypeError: 'tuple' object does not support item assignment

# 2. **Ordered**: Items have fixed index (starts at 0)
# 3. **Lightweight**: More memory efficient than lists for fixed data

'''
## Common Operations
'''

### 1️⃣ Create a Tuple
empty_tuple = ()
numbers = (1, 2, 3, 4)
mixed = (1, "hello", 3.14, True)
single_item = ("lonely",)  # Note trailing comma
no_parentheses = 5, 6, 7   # Valid tuple (parentheses optional)

### 2️⃣ Access Items
colors = ("red", "green", "blue")
print(colors[1])     # Output: "green" (index 1)
print(colors[-1])    # Output: "blue" (negative index)

### 3️⃣ Slicing (Extract Sub-Tuples)
letters = ('a', 'b', 'c', 'd', 'e')
print(letters[1:4])   # Output: ('b', 'c', 'd') (index 1 to 3)
print(letters[:3])    # Output: ('a', 'b', 'c') (start to index 2)
print(letters[2:])    # Output: ('c', 'd', 'e') (index 2 to end)

### 4️⃣ Tuple Unpacking
point = (3, 4)
x, y = point  # x=3, y=4

### 5️⃣ Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
combined = tuple1 + tuple2  # (1, 2, 3, 4)

'''
### 6️⃣ Tuple Methods
| Method       | Description                          | Example                     |
|--------------|--------------------------------------|-----------------------------|
| count(x)     | Returns occurrences of x            | numbers.count(2)            |
| index(x)     | Returns first index of x            | colors.index("green")       |
'''

# ---
# Advanced Use Cases

### 1️⃣ As Dictionary Keys
locations = {
    (35.68, 139.76): "Tokyo",
    (40.71, -74.01): "New York"  # Valid because tuples are immutable
}

### 2️⃣ Function Return Values
def get_dimensions():
    return 1920, 1080  # Implicit tuple
width, height = get_dimensions()

### 3️⃣ Named Tuples (from collections module)
from collections import namedtuple
Person = namedtuple('Person', ['name', 'age'])
p = Person("Alice", 30)
print(p.name)  # Output: "Alice"

### 4️⃣ Tuple Comprehension
# Actually creates a generator, need to convert to tuple
squares = tuple(x**2 for x in range(5))  # (0, 1, 4, 9, 16)

'''
# 🎯 Summary
- **Immutable & Ordered**: Secure fixed data with index access
- **Memory Efficient**: Better performance than lists for static data
- **Versatile**: Dictionary keys, function returns, multiple assignments
- **Safe**: Prevents accidental modification of data

> ✨ "When you need an immutable sequence, tuples are your Pythonic fortress!"
'''

# ---
# Tuple vs List Cheat Sheet
'''
Feature        | Tuple            | List
--------------|------------------|-----------------
Mutability    | Immutable        | Mutable
Syntax        | () or items,     | []
Memory        | Less             | More
Speed         | Faster iteration | Slower
Use Case      | Fixed data       | Dynamic data
'''
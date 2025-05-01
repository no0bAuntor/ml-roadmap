'''
# 📚 Python Dictionaries: A Complete Guide

## What is a Dictionary?
- A **dictionary** is a **mutable**, **unordered** collection of key-value pairs
- Keys must be **unique** and **hashable** (immutable types like int, float, str, tuple)
- Values can be any Python object
- Optimized for **fast lookups** by key (O(1) time complexity)

### 🔹 Syntax:
my_dict = {key1: value1, key2: value2}  # Curly braces with key:value pairs
empty_dict = {}                         # Or dict()
'''

# ---
# Key Features of Dictionaries
# 1. **Key-Value Pairs**: Store data as paired elements
student = {"name": "Alice", "age": 24, "courses": ["Math", "Physics"]}

# 2. **Dynamic**: Can grow/shrink as needed
student["gpa"] = 3.8  # Add new key-value pair

# 3. **Unordered**: Until Python 3.7+, insertion order is now preserved
# (But still considered "unordered" in principle)

'''
## Common Operations
'''

### 1️⃣ Create a Dictionary
empty_dict = {}
person = {"name": "John", "age": 30}
mixed_keys = {1: "one", "two": 2, (1,2): "tuple key"}

# Using dict() constructor
another_dict = dict(name="Alice", age=25)  # Keys become strings automatically

### 2️⃣ Access Values
print(person["name"])          # "John" - raises KeyError if missing
print(person.get("age"))       # 30 - returns None if missing
print(person.get("address", "N/A"))  # "N/A" (default if key missing)

### 3️⃣ Modify Dictionary
person["age"] = 31            # Update existing key
person["city"] = "Boston"     # Add new key-value pair
person.update({"age": 32, "job": "Engineer"})  # Multiple updates

### 4️⃣ Remove Items
del person["city"]            # Remove key (raises KeyError if missing)
age = person.pop("age")       # Remove and return value
person.clear()                # Empty the dictionary

### 5️⃣ Dictionary Views
keys = person.keys()          # View of all keys
values = person.values()      # View of all values
items = person.items()        # View of key-value pairs (as tuples)

'''
### 6️⃣ Dictionary Methods
| Method               | Description                         | Example                      |
|----------------------|-------------------------------------|------------------------------|
| get(key[, default])  | Safe value access                   | person.get("name")           |
| pop(key[, default])  | Remove and return value             | person.pop("age")            |
| update(other_dict)   | Merge dictionaries                  | person.update({"age": 32})   |
| setdefault(key, val) | Get value, set default if missing   | person.setdefault("city", "NY") |
| fromkeys(seq[, val]) | Create dict from sequence of keys   | dict.fromkeys(["a", "b"], 0) |
| copy()               | Shallow copy                        | new_dict = person.copy()     |
'''

# ---
# Advanced Use Cases

### 1️⃣ Dictionary Comprehension
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

### 2️⃣ Nested Dictionaries
employees = {
    "manager": {"name": "Alice", "age": 35},
    "developer": {"name": "Bob", "age": 28}
}
print(employees["manager"]["name"])  # "Alice"

### 3️⃣ Merging Dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = dict1 | dict2  # {'a': 1, 'b': 3, 'c': 4}

### 4️⃣ Default Values with defaultdict
from collections import defaultdict
word_counts = defaultdict(int)  # Default to 0 for missing keys
word_counts["hello"] += 1       # Automatically handles missing keys

### 5️⃣ Ordered Dictionaries
from collections import OrderedDict
ordered = OrderedDict([("a", 1), ("b", 2)])  # Preserves insertion order

'''
# 🎯 Summary
- **Key-Value Storage**: Ideal for labeled data
- **Fast Lookups**: O(1) time complexity for access
- **Flexible**: Mix of data types in values
- **Powerful Methods**: Comprehensive API for manipulation
- **Python's Swiss Army Knife**: Used everywhere from JSON to class attributes

> ✨ "Dictionaries are Python's version of a real-world dictionary - fast lookups by unique keys!"
'''

# ---
# Dictionary vs Other Types Cheat Sheet
'''
Feature        | Dictionary      | List            | Set             | Tuple
--------------|----------------|-----------------|-----------------|-----------------
Ordered       | ✔️ (Python 3.7+)| ✔️ Yes          | ❌ No           | ✔️ Yes
Mutable       | ✔️ Yes          | ✔️ Yes          | ✔️ Yes          | ❌ No
Indexed       | By keys         | By position      | ❌ No           | By position
Duplicates    | Keys: ❌ No     | ✔️ Yes          | ❌ No           | ✔️ Yes
              | Values: ✔️ Yes  |                 |                 |
Use Case      | Labeled data    | Ordered sequence| Unique items    | Fixed data
'''
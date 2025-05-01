'''
# 📚 Python Lists: A Complete Guide

## What is a List?
- A **list** is a **mutable**, **ordered** collection of items (elements).  
- Allows **duplicate** values.  
- Can store **mixed data types** (int, float, string, etc.).  

### 🔹 Syntax:
my_list = [item1, item2, item3]   # Square brackets
'''

# ---
# Key Features of Lists
# 1. **Mutable**: Items can be **modified** after creation.
my_list = [1, 2, 3]
my_list[0] = "new_value"  # Changes the first item

# 2. **Ordered**: Items have a **fixed index** (starts at `0`).
# 3. **Dynamic**: Size **grows/shrinks** as items are added/removed.

'''
## Common Operations  
'''

### 1️⃣ Create a List
empty_list = []  
numbers = [1, 2, 3, 4]  
mixed = [1, "hello", 3.14, True]  

### 2️⃣ Access Items
fruits = ["apple", "banana", "cherry"]  
# print(fruits[1])    # Output: "banana" (index 1)  
# print(fruits[-1])   # Output: "cherry" (negative index = last item)  

### 3️⃣ Modify Items
fruits[0] = "avocado"  # Replaces "apple" with "avocado"  

### 4️⃣ Add Items
fruits.append("orange")      # Adds to the end  
fruits.insert(1, "mango")    # Inserts at index 1  

### 5️⃣ Remove Items
fruits.remove("banana")  # Removes first occurrence  
fruits.pop(1)            # Removes item at index 1  
del fruits[0]            # Deletes item at index 0  

### 6️⃣ Slicing (Extract Sub-Lists)
numbers = [0, 1, 2, 3, 4, 5]  
# print(numbers[1:4])   # Output: [1, 2, 3] (index 1 to 3)  
# print(numbers[:3])    # Output: [0, 1, 2] (start to index 2)  
# print(numbers[2:])    # Output: [2, 3, 4, 5] (index 2 to end)  

'''
### 7️⃣ List Methods
| Method       | Description                          | Example                      |
|--------------|--------------------------------------|------------------------------|
| `append(x)`  | Adds `x` to the end                  | `fruits.append("kiwi")`      |
| `extend(L)`  | Adds all items from list `L`         | `fruits.extend(["pear", "grape"])` |
| `sort()`     | Sorts the list in place              | `numbers.sort()`             |
| `reverse()`  | Reverses the list                    | `fruits.reverse()`           |
| `count(x)`   | Returns occurrences of `x`           | `fruits.count("apple")`      |
| `copy()`     | Returns a shallow copy               | `new_list = fruits.copy()`   |
'''

# ---
# Advanced Use Cases  

### 1️⃣ List Comprehension (Compact Creation)
squares = [x**2 for x in range(5)]  # Output: [0, 1, 4, 9, 16]  

### 2️⃣ Nested Lists (2D Lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  
# print(matrix[1][2])  # Output: 6 (2nd row, 3rd column)  

### 3️⃣ Iterate Over a List
for fruit in fruits:  
    print(fruit)  

'''
# 🎯 Summary  
- **Mutable & Ordered**: Modify items, keep insertion order.  
- **Flexible**: Store any data type, resize dynamically.  
- **Powerful Methods**: Sort, slice, reverse, and more.  
- **Essential for Data Handling**: Used in loops, algorithms, and ML data prep.  

> ✨ *"Mastering lists unlocks the power of efficient data manipulation in Python!"*  
'''
# Python Data Structures Revision
# This file includes List, Tuple, Set, and Dictionary
# The goal is to revise all core collection types in one place.

# =========================================================
# 1. LIST
# =========================================================

# A list is an ordered, mutable, duplicate-friendly collection.
# Written with square brackets [].

numbers = [10, 20, 30, 40]
print("List:", numbers)
print(numbers[0])
print(numbers[1:3])
print(len(numbers))
numbers.append(50)
print(numbers)
numbers.insert(2, 25)
print(numbers)
numbers.remove(20)
print(numbers)
print(numbers.pop())
print(numbers)
print(sorted(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Example problem 1: find even numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8]
even = [x for x in nums if x % 2 == 0]
print(even)

# Example problem 2: remove duplicate values
items = [1, 2, 2, 3, 4, 4, 5]
unique_items = list(set(items))
print(unique_items)

# =========================================================
# 2. TUPLE
# =========================================================

# A tuple is an ordered, immutable collection.
# Written with parentheses ().

point = (10, 20)
print("Tuple:", point)
print(point[0])
print(point[1])
print(point.count(10))
print(point.index(20))

# Tuple unpacking
x, y = point
print(x, y)

# Example problem 1: find second largest
values = (9, 4, 12, 7, 15)
sorted_values = sorted(values)
print(sorted_values[-2])

# Example problem 2: return multiple values from a function

def student_info():
    return ('Aman', 21, 'Delhi')

name, age, city = student_info()
print(name, age, city)

# =========================================================
# 3. SET
# =========================================================

# A set is an unordered collection of unique elements.
# Written with curly braces {}.

myset = {1, 2, 3, 4, 4, 5}
print("Set:", myset)
myset.add(6)
print(myset)
myset.remove(3)
print(myset)
print(2 in myset)

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 | set2)   # union
print(set1 & set2)   # intersection
print(set1 - set2)   # difference

# Example problem 1: remove duplicates
arr = [1, 2, 2, 3, 4, 4, 5]
unique = set(arr)
print(unique)

# Example problem 2: common elements in two lists
list1 = ['apple', 'banana', 'orange']
list2 = ['banana', 'grape', 'apple']
common = set(list1) & set(list2)
print(common)

# =========================================================
# 4. DICTIONARY
# =========================================================

# A dictionary stores data as key-value pairs.
# Written with curly braces {} using key: value.

student = {
    'name': 'Aman',
    'age': 21,
    'course': 'Python'
}
print("Dictionary:", student)
print(student['name'])
print(student.get('age'))
student['city'] = 'Delhi'
print(student)
student['age'] = 22
print(student)
student.pop('course')
print(student)
print(student.keys())
print(student.values())
print(student.items())

# Example problem 1: count characters in a string
text = 'banana'
frequency = {}
for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1
print(frequency)

# Example problem 2: merge two dictionaries
person1 = {'name': 'Aman', 'age': 21}
person2 = {'city': 'Delhi', 'course': 'Python'}
merged = {**person1, **person2}
print(merged)

# =========================================================
# Comparison between all four data structures
# =========================================================

print("\nComparison:")
print("List -> ordered, mutable, allows duplicates")
print("Tuple -> ordered, immutable, allows duplicates")
print("Set -> unordered, mutable, unique values only")
print("Dictionary -> key-value pairs, mutable, keys are unique")

# =========================================================
# Quick summary
# =========================================================

# Use list when you need ordered values and duplicate items.
# Use tuple when values should not change.
# Use set when you need unique values and fast membership test.
# Use dictionary when you need key-value mapping.



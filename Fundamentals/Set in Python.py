# Set in Python is a collection of unique items that are unordered and mutable.
# Sets are written with curly braces {}.
# Sets do not allow duplicate values.
# Sets cannot be accessed by index like lists.
# Sets are useful when we need unique values and fast membership checks.

# ---------------------------
# Beginner concepts
# ---------------------------

myset = {1, 2, 3, 4, 'apple', 'banana'}
print(myset)
print(type(myset))

numbers = {1, 2, 2, 3, 3, 4}
print(numbers)     # duplicates are removed automatically

myset = {'a', 'b', 'c'}
print(myset)       # order is not guaranteed

# print(myset[0])  # This will raise an error because set is not indexable

# ---------------------------
# Add and update
# ---------------------------

myset = {'apple', 'banana'}
myset.add('orange')
print(myset)

myset.update(['grape', 'mango'])
print(myset)

# ---------------------------
# Remove and pop
# ---------------------------

myset = {'apple', 'banana', 'grape'}
myset.remove('banana')
print(myset)

myset.discard('mango')        # no error even if value is absent
print(myset)

print(myset.pop())            # removes and returns a random item
print(myset)

myset.clear()                 # remove all items
print(myset)

# ---------------------------
# Membership check
# ---------------------------

myset = {'apple', 'banana', 'grape'}
print('apple' in myset)
print('mango' in myset)

# ---------------------------
# Set operations
# ---------------------------

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))

# ---------------------------
# Set comprehension
# ---------------------------

squares = {x * x for x in range(1, 6)}
print(squares)

letters = {'a', 'b', 'c'}
upper_letters = {ch.upper() for ch in letters}
print(upper_letters)

# ---------------------------
# Frozen set
# ---------------------------

frozen = frozenset({1, 2, 3, 4})
print(frozen)
# frozen.add(5)   # this will raise an error because frozenset is immutable

# ---------------------------
# Important advanced concepts
# ---------------------------

# 1. Sets are unordered.
# 2. They store unique values only.
# 3. They are faster than lists for membership checks.
# 4. They support mathematical operations like union and intersection.
# 5. They are useful for removing duplicates and comparing collections.

# ---------------------------
# Example problems
# ---------------------------

# Problem 1: Remove duplicates from a list
items = [1, 2, 2, 3, 4, 4, 5]
unique_items = set(items)
print(unique_items)

# Problem 2: Find common elements between two lists
list1 = ['apple', 'banana', 'orange']
list2 = ['banana', 'grape', 'apple']
common = set(list1) & set(list2)
print(common)

# Problem 3: Find students who are present in both groups
group_a = {'Aman', 'Riya', 'John'}
group_b = {'John', 'Neha', 'Aman'}
present_in_both = group_a & group_b
print(present_in_both)

# ---------------------------
# Real-life use of sets
# ---------------------------
# Sets are used in tasks like:
# - removing duplicates
# - checking if a value exists
# - comparing two groups of data
# - performing mathematical set operations

# Example:
students_a = {'Aman', 'Riya', 'John'}
students_b = {'John', 'Neha', 'Aman'}
print(students_a | students_b)  # union
print(students_a & students_b)  # intersection

# Summary:
# A set is an unordered collection of unique elements.
# It is useful for membership checks, removing duplicates, and set-based logic.
# It is different from a list because it does not keep duplicates and cannot be indexed.
# List in Python is a collection of items that are ordered and mutable.
# Lists are written with square brackets [].
# Lists allow duplicate items.
# Lists can hold different data types.
# Lists are one of the most commonly used data structures in Python.

# ---------------------------
# Beginner concepts
# ---------------------------

mylist = [1, 2, 3, 5, 'apple', 'dog', True, False, 'apple']
print(type(mylist))
print(type(mylist[5]))
print(type(mylist[2]))
print(type(mylist[7]))

print(mylist[5])                 # accessing the 6th item in the list
print(mylist[0:4])               # slicing from index 0 to 3
print(mylist[-1])                # last item
print(mylist[-3])                # third last item
print(mylist[2:])                # slicing from index 2 to the end
print(len(mylist))               # length of list

print('apple' in mylist)         # check if value exists
print('car' in mylist)
print(mylist.count('apple'))     # count occurrences
print(mylist.index('apple'))     # first index of 'apple'

# ---------------------------
# Add / insert / remove / pop
# ---------------------------

mylist.append('banana')          # add at the end
print(mylist)

mylist.insert(2, 'cat')          # insert at a specific position
print(mylist)

mylist.remove('dog')             # removes first match
print(mylist)

mylist.pop()                     # removes last item
print(mylist)

mylist.extend(['grape', 'orange'])  # add multiple items
print(mylist)

# ---------------------------
# Sort, reverse, min, max, sum
# ---------------------------

mylist1 = [1, 2, 3, 5, 9, 4, 6, 7, 8]
mylist1.sort()                   # sort ascending
print(mylist1)

mylist.reverse()                 # reverse the order of mylist
print(mylist)

print(min(mylist1))              # minimum value
print(max(mylist1))              # maximum value
print(sum(mylist1))              # sum of all numbers

# ---------------------------
# Copy, clear and nested list
# ---------------------------

copy_list = mylist.copy()        # copy list
print(copy_list)

mylist.clear()                   # remove all items
print(mylist)

nested = [[1, 2], [3, 4], [5, 6]]
print(nested[1][0])              # access inner list element

# ---------------------------
# List comprehension
# ---------------------------

squares = [x * x for x in range(1, 6)]
print(squares)

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)

# ---------------------------
# Important advanced properties
# ---------------------------

# 1. Lists are mutable meaning they can be changed after creation.
# 2. They keep order.
# 3. They allow duplicates.
# 4. They are useful for storing multiple related values.
# 5. They support slicing and list comprehension.

# ---------------------------
# Example problems
# ---------------------------

# Problem 1: Find all even numbers in a list
nums = [10, 15, 22, 31, 44, 55]
result = [n for n in nums if n % 2 == 0]
print(result)

# Problem 2: Remove duplicate values from a list
items = [1, 2, 2, 3, 4, 4, 5]
unique_items = list(set(items))
print(unique_items)

# Problem 3: Find the second largest number
numbers = [8, 4, 12, 6, 15]
max_num = max(numbers)
numbers.remove(max_num)
second_largest = max(numbers)
print(second_largest)

# ---------------------------
# Real-life use of lists
# ---------------------------
# Lists are used to store shopping items, student marks, names, countries, etc.
# Example:
student_names = ['Aman', 'Riya', 'John']
print(student_names)
student_names.append('Neha')
print(student_names)

# Summary:
# A list is an ordered, mutable, duplicate-friendly collection of values.
# It is very useful for storing multiple related values and working with loops.
# It supports many built-in methods and is one of the core Python data structures.
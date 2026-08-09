# Tuples in Python is a collection of items that are ordered and immutable.
# Tuples are written with round brackets ().
# Tuples allow duplicate items.
# Tuples can hold different data types.
# Unlike lists, tuples cannot be changed after creation.
# Tuples are commonly used for fixed data and safe values.

# ---------------------------
# Beginner concepts
# ---------------------------

mytuple = (1, 2, 3, 5, 'apple', 'dog', True, False, 'apple')
print(type(mytuple))
print(type(mytuple[5]))
print(type(mytuple[2]))
print(type(mytuple[7]))

print(mytuple[5])             # access item by index
print(mytuple[0])             # first element
print(mytuple[0:4])           # slicing
print(mytuple[-1])            # last item
print(mytuple[-3])            # third last item
print(mytuple[2:])            # from index 2 to end
print(len(mytuple))           # length of tuple

print('apple' in mytuple)     # check membership
print('car' in mytuple)
print(mytuple.count('apple')) # count duplicates
print(mytuple.index('apple')) # first matching index

# ---------------------------
# Tuple packing and unpacking
# ---------------------------

point = (10, 20)
x, y = point
print(x)
print(y)

# ---------------------------
# tuple methods
# ---------------------------

print(mytuple)
print(mytuple[:3])
print(mytuple[::-1])          # reverse the tuple

mytuple1 = (1, 2, 3, 5, 9, 4, 6, 7, 8)
print(sorted(mytuple1))       # returns a sorted list
print(min(mytuple1))          # minimum value
print(max(mytuple1))          # maximum value
print(sum(mytuple1))          # sum of values

# ---------------------------
# Immutability concept
# ---------------------------

# Tuples are immutable, so these operations are not allowed:
# mytuple.append('banana')
# mytuple.remove('dog')
# mytuple.pop()
# mytuple[0] = 10

# But we can convert it to a list, modify it, and convert it back
mylist = list(mytuple)
mylist.append('banana')
mytuple = tuple(mylist)
print(mytuple)

# ---------------------------
# Nested tuples
# ---------------------------

student = ('Aman', (90, 85, 88))
print(student[0])
print(student[1][2])

# ---------------------------
# Advanced concepts
# ---------------------------

# 1. Tuples are safer than lists because they cannot be accidentally changed.
# 2. They are useful for constant values or fixed records.
# 3. They can be used for multiple return values from a function.
# 4. They are hashable, so they can be used as keys in dictionaries.

# Example: function returning multiple values

def get_person():
    return ('Aman', 21, 'Delhi')

name, age, city = get_person()
print(name, age, city)

# ---------------------------
# Example problems
# ---------------------------

# Problem 1: Find the second largest number in a tuple
numbers = (8, 4, 12, 6, 15)
sorted_nums = sorted(numbers)
print(sorted_nums[-2])

# Problem 2: Count how many times a value appears
marks = (90, 85, 90, 78, 90)
print(marks.count(90))

# Problem 3: Unpack values from a tuple
student_info = ('Riya', 20, 'Mumbai')
name, age, city = student_info
print(name, age, city)

# ---------------------------
# Real-life use of tuples
# ---------------------------
# Tuples are used to store fixed data such as:
# - coordinates (x, y)
# - RGB color values (255, 0, 0)
# - database records
# - function return values

color = (255, 0, 0)
print(color)

# Summary:
# A tuple is an ordered, immutable collection of values.
# It is useful when you want data that should not change.
# It supports indexing, slicing, unpacking, and safe fixed-data storage.

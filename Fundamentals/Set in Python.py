# Set in Python is a collection of unique items that are unordered and mutable.
# Sets are written with curly braces.
# Sets do not allow duplicate values.
# Sets cannot be accessed by index like lists.

myset = {1, 2, 3, 4, "apple", "banana"}
print(myset)
print(type(myset))

numbers = {1, 2, 2, 3, 3, 4}
print(numbers)   # {1, 2, 3, 4} 

myset = {"a", "b", "c"}
print(myset)     # order may be different every time

myset = {"apple", "banana", "grape"}

#print(myset[0])  # This will raise an error

myset = {"apple", "banana"}
myset.add("orange") #add an item to the set
print(myset)

myset = {"apple", "banana"}
myset.update(["grape", "mango"]) #add multiple items to the set
print(myset)

myset = {"apple", "banana", "grape"}
myset.remove("banana") #remove an item from the set
print(myset)

myset = {"apple", "banana", "grape"}
myset.discard("mango")  # no error even if item is not present
print(myset) 

myset = {"apple", "banana", "grape"}
print(myset.pop())   # removes and returns a random item
print(myset)

myset = {"apple", "banana"}
myset.clear() #clear all items from the set
print(myset)   # set()

myset = {"apple", "banana", "grape"}

print("apple" in myset)   # True
print("mango" in myset)   # False

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))          # {1, 2, 3, 4, 5, 6}
print(set1.intersection(set2))   # {3, 4}
print(set1.difference(set2))     # {1, 2}
print(set1.symmetric_difference(set2))  # {1, 2, 5, 6}

# Set in Python is a collection of unique items that are unordered and mutable.
# Sets are written with curly braces.
# Sets do not allow duplicate values.

myset = {1, 2, 3, "apple", "dog", True}
print(myset)

print(len(myset))        # length of the set
print("apple" in myset)  # check if an item exists

myset.add("banana")      # add one item
print(myset)

myset.update(["grape", "orange"])  # add multiple items
print(myset)

myset.remove("dog")      # remove an item
print(myset)

myset.discard("mango")   # safely remove item if present
print(myset)

print(myset.pop())       # removes and returns a random item
print(myset)

myset.clear()            # remove all items
print(myset)

students_a = {"Aman", "Riya", "John"}
students_b = {"John", "Neha", "Aman"}

print(students_a | students_b)   # union
print(students_a & students_b)   # intersection

my_list = [1, 2, 2, 3]
my_set = {1, 2, 2, 3}

print(my_list)  # [1, 2, 2, 3]
print(my_set)   # {1, 2, 3}
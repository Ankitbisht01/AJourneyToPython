# Dictionary in Python is a collection of key-value pairs.
# Dictionaries are written with curly braces {}.
# Each item is stored as key: value.
# Keys must be unique.
# Values can be of any data type.
# Dictionaries are ordered in Python 3.7+.
# Dictionaries are mutable (we can change them after creation).

# ---------------------------
# Beginner concepts
# ---------------------------

student = {
    'name': 'Aman',
    'age': 21,
    'course': 'Python',
    'is_student': True,
    'marks': [80, 90, 95]
}

print(type(student))
print(student)
print(student['name'])
print(student['age'])
print(student.get('course'))
print(student.get('city', 'Not found'))

print(student.keys())
print(student.values())
print(student.items())
print(len(student))
print('name' in student)
print('Aman' in student.values())

# ---------------------------
# Adding and updating values
# ---------------------------

student['city'] = 'Delhi'
print(student)

student['age'] = 22
print(student)

# ---------------------------
# Removing values
# ---------------------------

student.pop('course')
print(student)

student.popitem()
print(student)

student.clear()
print(student)

# ---------------------------
# Nested dictionaries
# ---------------------------

student_details = {
    'student1': {'name': 'Aman', 'age': 21},
    'student2': {'name': 'Riya', 'age': 20},
    'student3': {'name': 'John', 'age': 23}
}

print(student_details)
print(student_details['student1']['name'])
print(student_details['student2']['age'])

# ---------------------------
# Dictionary comprehension
# ---------------------------

squares = {x: x * x for x in range(1, 6)}
print(squares)

names = ['Aman', 'Riya', 'John']
name_lengths = {name: len(name) for name in names}
print(name_lengths)

# ---------------------------
# Copying and merging
# ---------------------------

original = {'a': 1, 'b': 2}
copy_dict = original.copy()
print(copy_dict)

new_dict = dict(original)
print(new_dict)

dict1 = {'name': 'Aman', 'age': 21}
dict2 = {'city': 'Delhi', 'course': 'Python'}
merged = dict1 | dict2
print(merged)

merged2 = {**dict1, **dict2}
print(merged2)

# ---------------------------
# Updating with another dictionary
# ---------------------------

dict1.update({'city': 'Mumbai', 'age': 22})
print(dict1)

# ---------------------------
# Setdefault and from list of tuples
# ---------------------------

person = {'name': 'Riya'}
person.setdefault('city', 'Delhi')
print(person)

items = [('name', 'Aman'), ('age', 21), ('city', 'Delhi')]
d = dict(items)
print(d)

# ---------------------------
# Looping through dictionary
# ---------------------------

marks = {'Aman': 90, 'Riya': 85, 'John': 95}
for student_name, score in marks.items():
    print(student_name, score)

for key in marks:
    print(key)

for value in marks.values():
    print(value)

# ---------------------------
# Advanced real-world usage
# ---------------------------

student_record = {
    'name': 'Aman',
    'roll_no': 101,
    'subjects': ['Math', 'Science'],
    'result': {'math': 90, 'science': 95}
}

print(student_record)
print(student_record['subjects'])
print(student_record['result']['math'])

# ---------------------------
# Example problems
# ---------------------------

# Problem 1: Count frequency of characters in a string
text = 'banana'
frequency = {}
for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1
print(frequency)

# Problem 2: Store marks of students
marks_dict = {'Aman': 88, 'Riya': 92, 'John': 75}
print(marks_dict['Riya'])
print(max(marks_dict.values()))

# Problem 3: Merge two employee dictionaries
employee1 = {'name': 'Aman', 'age': 21}
employee2 = {'city': 'Delhi', 'department': 'IT'}
employee = {**employee1, **employee2}
print(employee)

# ---------------------------
# Important notes
# ---------------------------

# 1. Dictionary stores data as key-value pairs.
# 2. Keys must be unique.
# 3. Keys are usually strings or numbers.
# 4. Dictionaries are mutable and fast for lookup.
# 5. They are perfect for storing records, settings, and structured data.

# Summary:
# A dictionary is an unordered but key-based collection used for mapping values to identifiers.
# It is one of the most powerful and widely used data structures in Python.
# Example: student records, employee data, configuration settings, JSON-like data.
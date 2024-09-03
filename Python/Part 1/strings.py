####### STRINGS #######

# Basics
print('hello in single quotes')
print("hello in double quotes")
print('hello in single quotes, with "double quotes" inside')

# Indexing
my_string = "University of Engineering"
print(my_string[3])

# Slicing
print(my_string[2:6:2])

print(my_string.upper())
print(my_string.capitalize())
print(my_string.lower())
print(my_string.split())

# String Interpolation
name = "John"
age = 30
print(f"Hello, my name is {name} and I am {age} years old")

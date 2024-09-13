# INHERITANCE

# Base Class
class Animal:

    def __init__(self):
        print("Animal Created")

    def whoAmI(self):
        print("I am an animal")

    def eat(self):
        print("I eat various things")

# Derived Class
class Dog(Animal):
    def __init__(self):
        print("Dog Created")

    def eat(self):
        print("I eat dog food")

    def bark(self):
        print("I bark")

myDog = Dog()
# Function from BASE Class
myDog.whoAmI()  # Output: I am an animal
# Function from DERIVED Class
myDog.eat()  # Output: I eat dog food
myDog.bark() 

# SPECIAL FUNCTIONS

class Book:

    def __init__(self,title,author,pages) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("The Book is Destoyed")
        

b = Book("Python", "Guido van Rossum", 200)
print(b)
print(len(b))
del b

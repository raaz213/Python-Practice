#Creating Class and Object

# Using Object method
class Person:
    def __init__(self, name, age):  # constructor
        self.name = name            # data/properties
        self.age = age 
    def display_info(self):         #method/function
        print(f"Name: {self.name}\nAge: {self.age}")
# creating an object      
p = Person("John", 30)
p.display_info()

# Using __Str__() function
#The __str__() function controls what should be returned when the class object is represented as a string.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}"
p = Person("John", 30)
print(p)
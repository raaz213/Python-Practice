# Example 1
class Animal:
    def sound(self):
        print("The animal makes a sound")
class Dog(Animal):
    def bark(self):
        print("The dog barks")
        
d = Dog()
d.sound()  # from parent
d.bark()  # from child

# Example 2
class Person:
    def __init__(self, name, age):  # constructor
        self.name = name            # data/properties
        self.age = age 
    def display_info(self):         #method/function
        print(f"Name: {self.name}\nAge: {self.age}")

class Student(Person):
    def __init__(self, name, age, college):
        super().__init__(name, age)  # call the constructor of the parent class
        self.college = college
    def display_college(self):
        print("College: ",self.college)
        
s = Student("John", 20, "TU")
s.display_info() # Inherited from Person class
s.display_college() # Specific to Student class
            

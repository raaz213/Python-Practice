class Dog:
    def sound(self):
        print("Bark")
class Cat:
    def sound(self):
        print("Meow")
        
d = Dog()
c = Cat()
d.sound()
c.sound()  

# Or you can do using for loop to display the sound of all the animals
class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

for animal in [Dog(), Cat()]:
    animal.speak()
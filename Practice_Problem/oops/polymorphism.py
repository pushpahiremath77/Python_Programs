class Animal:
    def sound(self):
        return "Animal"

class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return "Mew"
    

animals = Dog()

print(animals.sound())

# for animal in animals:
#     print(animal.sound())

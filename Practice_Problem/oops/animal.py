class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("barking")

class Cat(Animal):
    def sound(self):
        super().sound()
        print("meow")

c1 = Cat()
c1.sound()

c2 = Dog()
c2.sound()

print(Dog.mro())
print(Cat.mro())
print(Animal.mro())



class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = (self.phy+self.chem+self.math)/3

stu1 = Student(87,90,98)
print(stu1.percentage)
        
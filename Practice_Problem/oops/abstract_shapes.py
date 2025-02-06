from abc import ABC , abstractmethod

#Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

#concrete class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
rect = Rectangle(4, 5)
print("Area:", rect.area())
print("Perimeter:",rect.perimeter())
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.__year = year

    def start(self):
        print(f"The {self.model} is starting...")

    def get_year(self):
        return self.__year
    
    def set_year(self,year):
        self.__year = year



car1 = Car("Toyota","Corolla",2020)
#print(car1.__year)
car1.start()
print(car1.get_year())
car1.set_year(2025)
print(car1.get_year())






class Vehicle:
    def __init__(self,model,year):
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle starting...")

    def stop(self):
        print("Vehicle stoping...")

class Car(Vehicle):

    def break_apply(self):
        print("Break applied")

    def start(self):
        
        print("Car starting...")
        super().start()

    def stop(self):
        print("Car stoping...")

c1 = Car("Merce",2025)
c1.start() 
super(Car)


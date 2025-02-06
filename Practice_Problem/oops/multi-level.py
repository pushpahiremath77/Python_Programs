# class Car:
#     def start(self):
#         print("Car started")

#     def stop(self):
#         print("Car stopped")

# class Toyato(Car):
#     def __init__(self,name):
#         self.name = name

# class Fortune(Toyato):
#     def clutch(self):
#         print("Clutch applied")
        
# car2 = Fortune("xyz")

# #properties inherited from both Car class & Toyato class
# car2.start()
# car2.stop()
# print(car2.name)
# car2.clutch()


from abc import ABC,abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def sta(self):
        print("Car started")
        

car1 = Car()
car1.sta()




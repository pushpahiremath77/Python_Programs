class Car:

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

class Toyato(Car):

    def __init__(self,name):
        self.name = name

car1 = Toyato("abc")

#methods inherited from parent class Car
car1.start()
car1.stop()
print(car1.name)
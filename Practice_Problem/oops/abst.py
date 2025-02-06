from abc import ABC, abstractmethod

class Appliance(ABC):  # Abstract class
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing machine is now ON.")

    def turn_off(self):
        print("Washing machine is now OFF.")

class Refrigerator(Appliance):
    def turn_on(self):
        print("Refrigerator is now ON.")

    def turn_off(self):
        print("Refrigerator is now OFF.")

# Using the appliances
washer = WashingMachine()
fridge = Refrigerator()

washer.turn_on()  # Output: Washing machine is now ON.
fridge.turn_off()  # Output: Refrigerator is now OFF.

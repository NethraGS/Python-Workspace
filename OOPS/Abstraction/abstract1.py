from abc import ABC, abstractmethod


class Vehicle(ABC): 
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def drive(self):
        # We leave this empty because every vehicle drives differently
        pass

# 2. Subclasses (Must implement the abstract methods)
class PetrolCar(Vehicle):
    def drive(self):
        print(f"{self.brand} is burning fuel to move.")

class ElectricCar(Vehicle):
    def drive(self):
        print(f"{self.brand} is using battery power to move.")

# --- The "Strictness" Test ---

# try_vehicle = Vehicle("Generic") 
# ^ This would throw an ERROR: "Can't instantiate abstract class Vehicle"

my_petrol = PetrolCar("Toyota")
my_petrol.drive()
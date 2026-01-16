# Base class
class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"{self.brand}: Vroom vroom! (Engine roaring)")


# Child class 1
class ElectricCar(Car):
    def drive(self):
        print(f"{self.brand}: ... (Silent electric hum)")


# Child class 2
class Truck(Car):
    def drive(self):
        print(f"{self.brand}: Rumble rumble! (Heavy diesel engine)")


garage = [
    Car("Toyota"),
    ElectricCar("Tesla"),
    Truck("Ford")
]

for vehicle in garage:
    vehicle.drive()

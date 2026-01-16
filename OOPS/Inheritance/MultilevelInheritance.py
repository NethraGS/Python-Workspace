class Vehicle: #level 1
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.brand} is now driving!")

class Car(Vehicle): #level 2
    def __init__(self, brand, color, fuel_type):
        super().__init__(brand, color)
        self.fuel_type = fuel_type

    def car_info(self):
        print(f"Fuel type: {self.fuel_type}")

class ElectricCar(Car): #level 3
    def __init__(self, brand, color, fuel_type, battery_capacity):
        super().__init__(brand, color, fuel_type)
        self.battery_capacity = battery_capacity

    def battery_info(self):
        print(f"Battery capacity: {self.battery_capacity} kWh")

my_car = ElectricCar("Mercedes-Benz", "Black", "Electric", 75)

print(my_car.brand)
print(my_car.color)
print(my_car.fuel_type)

my_car.drive()
my_car.car_info()
my_car.battery_info()


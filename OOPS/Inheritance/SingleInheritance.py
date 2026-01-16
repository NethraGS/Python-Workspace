class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.brand} is now driving!")

class Car(Vehicle):
    def __init__(self, brand, color):
        super().__init__(brand, color)

    def car_type(self):
        print("This is a car")


my_car = Car("Toyota", "Red")

print(my_car.brand)
print(my_car.color)

my_car.drive()
my_car.car_type()

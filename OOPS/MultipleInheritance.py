# Parent class 1
class Calling:
    def feature1(self):
        print("Calling feature")

class playing():
    def feature(self):
        print("Playing feature")

# Parent class 2
class Camera:
    def feature2(self):
        print("Camera feature")


# Child class (Multiple Inheritance)
class SmartPhone(Calling, Camera, playing):
    def explore(self):
        print("Exploring features of SmartPhone")

phone = SmartPhone()
phone.feature()
phone.explore()
phone.playing()

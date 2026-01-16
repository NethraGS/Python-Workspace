# Parent class 1
class Calling:
    def calling_feature(self):
        print("Calling feature")


# Parent class 2
class Playing:
    def playing_feature(self):
        print("Playing feature")


# Parent class 3
class Camera:
    def camera_feature(self):
        print("Camera feature")


# Child class (Multiple Inheritance)
class SmartPhone(Calling, Playing, Camera):
    def explore(self):
        print("Exploring features of SmartPhone")


phone = SmartPhone()

phone.calling_feature()
phone.playing_feature()
phone.camera_feature()
phone.explore()

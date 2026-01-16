class Animal:
    # Constructor
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(self.name, "says", self.sound)


# Creating objects
dog = Animal("Dog", "Bark")
cat = Animal("Cat", "Meow")

# Calling methods
dog.make_sound()
cat.make_sound()

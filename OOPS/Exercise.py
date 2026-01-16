class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(self.name, "says", self.sound)


dog = Animal("Dog", "Bark")
cat = Animal("Cat", "Meow")


dog.make_sound()
cat.make_sound()

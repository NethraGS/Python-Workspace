
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal makes a sound")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)  

    def speak(self):
        print(self.name, "says Bark")



class Cat(Animal):
    def __init__(self, name):
        super().__init__(name) 

    def speak(self):
        print(self.name, "says Meow")



dog = Dog("Dog")
cat = Cat("Cat")


dog.speak()
cat.speak()

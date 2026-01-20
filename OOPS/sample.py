class animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound

    def make_sound(self):
        print(self.name+" makes "+self.sound)

dog=animal("spy","bark")
dog.make_sound()
cat=animal("tom","meow")
cat.make_sound()
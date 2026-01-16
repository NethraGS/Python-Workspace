def __init__(self, name, age,twitter_handle="abc"):
        self.name = name
        self.age = age
        self.__twitter_handle = twitter_handle  # private attribute
        self._password = "default_password"  # protected attribute

def get_twitter_handle(self):
    return self.__twitter_handle
def set_twitter_handle(self, handle):
    self.__twitter_handle = handle
def greet(self):
    return f"Hello, my name is {self.name} and I am {self.age} years old."
class Computer:
   
    def show_details(self):
        return f"details of phone"

p1=Computer()
print(p1.show_details())  

class Demo:
    def __new__(cls):
        print("Creating object")
        return super().__new__(cls)

    def __init__(self):
        print("Initializing object")

obj = Demo()
print("hello")


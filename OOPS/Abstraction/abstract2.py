from abc import ABC, abstractmethod
class Person(ABC): 

    @abstractmethod
    def doSomething(self):
        pass

class Student(Person):
    def doSomething(self):
        print("Student is studying.")

class Employee(Person):
    def doSomething(self):
        print("Employee is working.")

p1=Student();
p1.doSomething();
p2=Employee();
p2.doSomething();
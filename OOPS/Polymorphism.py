class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_details(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}" 
class Coder(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    def get_details(self):
        self.salary += 10000  # Coders get a bonus
        return f"Employee Name: {self.name}, Salary: {self.salary}, Programming Language: {self.programming_language}" 
class Designer(Employee): 
    def __init__(self, name, salary, design_tool):
        super().__init__(name, salary)
        self.design_tool = design_tool
    def get_details(self):
        self.salary += 5000  # Designers get a bonus
        return f"Employee Name: {self.name}, Salary: {self.salary}, Design Tool: {self.design_tool}"

Employees=[Employee("Alice", 70000), Coder("Bob", 90000, "Python"), Designer("Charlie", 80000, "Photoshop")]

for emp in Employees:
    print(emp.get_details())
class Employee:

    def __init__(self,id=None,name=None,salary=None):
        self.id=id
        self.name=name
        self.salary=salary

    def show(self):
        print(f"ID: {self.id}, Name: {self.name}, Salary: {self.salary}")
    
emp1=Employee(101,"Neo",30000)
emp2=Employee(102,"Trinity",35000)
emp3=Employee(103,"Morpheus",40000)
emp4=Employee(104,"Cypher",25000)
emps={emp1.id:emp1,emp2.id:emp2,emp3.id:emp3,emp4.id:emp4}
emp5=Employee(105,"Smith",45000)
flag=False
for emp in emps:
    if(emps[emp].id==emp5.id):
        print("Already Exists")
        flag=True
        break
if not flag:
    emps.update({emp5.id:emp5})

for emp in emps.values():
    emp.show()
 

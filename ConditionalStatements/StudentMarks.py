name=input("Enter name:")

marks = int(input("Enter your marks: "))
print("Hi {name} Your Grades are:")
if(marks>70 and marks<=100):
    print("woah!,You passed with Distinction")
elif(marks>=50 and marks<=70):
    print("Grade B")
elif(marks>=40 and marks<50):
    print("Grade C")
else:
    print("uhmm,Sorry You Failed")
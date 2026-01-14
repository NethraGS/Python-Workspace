try:
    num=int(input("Enter a number: "))
    print("line2")
    print(10/num)
    print("phase1 done")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
finally:
    print("Execution completed.")
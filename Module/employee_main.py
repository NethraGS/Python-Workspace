"""
Salary Calculator for employees based on designation and leave days.
"""

import logging
import employee_utility

base_salary = int(input("Enter the base salary: "))
designation = input("Enter the designation (Coder/Designer/Manager): ")
leave_days = int(input("Enter the number of leave days taken: "))
if(leave_days < 0):
    logging.error("Leave days cannot be negative.")
    exit(1)


total_salary = employee_utility.final_salary(base_salary, designation, leave_days)
print(f"The final salary is: {total_salary}")

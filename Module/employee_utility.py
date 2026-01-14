"""
Calculate employee salary  Module based on designation and leaves taken.
"""


def calculate_leaves(salary, leave_days):

    """
    Docstring for calculate_leaves

    :param salary: Description
    :param leave_days: Description
    """
    if leave_days > 15:
        deduction = (salary / 30) * (leave_days - 15)
    else:
        deduction = 0
    return deduction


def calculate_salary(base_salary, bonuses, deductions):

    """
    Docstring for calculate_salary

    :param base_salary: Description
    :param bonuses: Description
    :param deductions: Description
    """
    total_salary = base_salary + bonuses - deductions
    return total_salary


def calculate_bonus(designation, base_salary):

    """
    Docstring for calculate_bonus

    :param designation: Description
    :param base_salary: Description
    """
    if designation == "Coder":
        bonus = 10 / 100 * base_salary
    elif designation == "Designer":
        bonus = 15 / 100 * base_salary
    elif designation == "Manager":
        bonus = 5 / 100 * base_salary
    else:
        bonus = 0
    return bonus


def final_salary(base_salary, designation, leave_days):

    """
    Docstring for final_salary

    :param base_salary: Description
    :param designation: Description
    :param leave_days: Description
    """
    deductions = calculate_leaves(base_salary, leave_days)
    bonuses = calculate_bonus(designation, base_salary)
    total_salary = calculate_salary(base_salary, bonuses, deductions)
    return total_salary

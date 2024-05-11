#Scenario: You have a dataset containing information about employee salaries. You need to calculate the total salary expense for each department.
#Task: Write a Python script using lists and tuples to aggregate the salary data by department and calculate the total expense for each department.

# Sample dataset containing employee salaries with format (name, department, salary)
employee_data = [
    ("Harsha", "HR", 50000),
    ("Suresh", "IT", 60000),
    ("Harish", "HR", 55000),
    ("Balaji", "IT", 62000),
    ("Charlie", "Finance", 70000),
    ("Dev", "Finance", 72000)
]
# Dictionary to store total expenses for each department
department_expenses = {}

# Iterate through the employee data to aggregate expenses
for name, department, salary in employee_data:
    if department in department_expenses:
        department_expenses[department] += salary
    else:
        department_expenses[department] = salary

# Print the total expenses for each department
for department, expense in department_expenses.items():
    print(f"Total expense for {department} : {expense}")

from employees import FullTimeEmployee, PartTimeEmployee

employees = [
    FullTimeEmployee("Ahmed", 101, 8000),
    PartTimeEmployee("Sara", 102, 80, 50),
    FullTimeEmployee("Khalid", 103, 12000),
]
total = 0
for employee in employees:
    employee.display_info(end=" ")                # same line as the salary
    salary = employee.calculate_salary()
    print(f"Salary: {salary} SAR")
    total = total + salary

print(f"Total Salaries: {total} SAR")
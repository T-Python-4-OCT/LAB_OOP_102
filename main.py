from employee import FullTimeEmployee, PartTimeEmployee

def money(value):
    return int(value) if value == int(value) else round(value, 2)


employees = [
    FullTimeEmployee("Ahmed", 101, 8000),
    PartTimeEmployee("Sara", 102, 80, 50),
    FullTimeEmployee("Khalid", 103, 12000),
]

total = 0
for emp in employees:
    salary = emp.calculate_salary()
    emp.display_info()
    print(f"Salary: {money(salary)} SAR")
    total += salary

print(f"Total Salaries: {money(total)} SAR")
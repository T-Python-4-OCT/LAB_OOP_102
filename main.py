
from employee import FullTimeEmployee, PartTimeEmployee


employee1 = FullTimeEmployee("Ahmed", 101, 8000)
employee2 = PartTimeEmployee("Sara", 102, 80, 50)
employee3 = FullTimeEmployee("Khalid", 103, 12000)


employees = [employee1, employee2, employee3]


total_salaries = 0

for employee in employees:
    employee.display_info()
    total_salaries += employee.calculate_salary()

print(f"Total Salaries: {total_salaries:g} SAR")

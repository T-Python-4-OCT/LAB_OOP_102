from employee import FullTimeEmployee, PartTimeEmployee

employees = [
    FullTimeEmployee("Ahmed", 101, 8000),
    PartTimeEmployee("Sara", 102, 80, 50),
    FullTimeEmployee("Khalid", 103, 12000),
]

total_salaries = 0

for emp in employees:
  emp.display_info()
  salary = emp.calculate_salary()
  print(f"Salary: {salary} SAR")
  total_salaries += salary

print(f"Total Salaries: {total_salaries} SAR")
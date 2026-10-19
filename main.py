from full import FullTimeEmployee, PartTimeEmployee


emp1 = FullTimeEmployee("Ahmed", 101, 8000)
emp2 = PartTimeEmployee("sara", 102, 80, 50)
emp3 = FullTimeEmployee("Khalid", 103, 12000)


employees = [emp1, emp2, emp3]


total_salaries = 0

for employee in employees:
    employee.display_info()
    total_salaries += employee.calculate_salary()


print(f"Total Salaries: {total_salaries} SAR")
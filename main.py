from Employees import FullTimeEmployee, PartTimeEmployee

employees = [
    FullTimeEmployee("Ahmed", 101, 8000),
    PartTimeEmployee("Sara", 102, 80, 50),
    FullTimeEmployee("Khalid", 103, 12000),
]

total = 0
for emp in employees:                     
    emp.display_info(end=" ")
    salary = emp.calculate_salary()        
    print(f"Salary: {salary} SAR")
    total += salary

print(f"Total Salaries: {total} SAR")

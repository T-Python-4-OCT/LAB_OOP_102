from employees import  Employee,FullTimeEmployee, PartTimeEmployee

ahmed = FullTimeEmployee("Ahmed", 101, 8000)
sara = PartTimeEmployee("Sara", 102, 80, 50)
khalid = FullTimeEmployee("Khalid", 103, 12000)

employees = [ahmed, sara, khalid]  

total = 0

for emp in employees:
    salary = emp.calculate_salary()
    print(f"Employee: {emp.name} ID: {emp.get_employee_id()} Salary: {salary} SAR")
    total += salary

print(f"Total Salaries: {total} SAR")
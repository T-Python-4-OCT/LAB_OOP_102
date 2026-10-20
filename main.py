
from emp import FullTimeEmployee, PartTimeEmployee

#Create objects
muath=FullTimeEmployee("Muath", 101, 10000)
sara=PartTimeEmployee("Sara", 102, 50, 80)
khalid=FullTimeEmployee("Khalid", 103, 12000)

employees=[muath, sara, khalid]
total_salaries = 0
for employee in employees:
    salary = employee.calculate_salary()

    print(
        f"Employee: {employee.name} "
        f"ID: {employee.get_employee_id()} "
        f"Salary: {salary} SAR"
    )

    total_salaries += salary
    
    
    
print(f"Total Salaries: {total_salaries} SAR")

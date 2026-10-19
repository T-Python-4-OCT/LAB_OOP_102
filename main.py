
from employee import FullTimeEmployee, PartTimeEmployee


# Create employee objects
employees = [
    FullTimeEmployee("Ahmed", 101, 8000),
    PartTimeEmployee("Sara", 102, 80, 50),
    FullTimeEmployee("Khalid", 103, 12000)
]

# Calculate total salaries
total_salaries = 0

for employee in employees:
    salary = employee.calculate_salary()

    print(
        f"Employee: {employee.name} "
        f"ID: {employee.get_employee_id()} "
        f"Salary: {salary:g} SAR"
    )

    total_salaries += salary

print(f"Total Salaries: {total_salaries:g} SAR")
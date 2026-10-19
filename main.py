from full_time_employee import FullTimeEmployee
from part_time_employee import PartTimeEmployee
from payroll import process_payroll

try:
    employees = [
        FullTimeEmployee(f"Ahmed", 101, 8000),
        PartTimeEmployee("Sara", 102, 80, 50),
        FullTimeEmployee("Khalid", 103, 12000),
    ]
except ValueError as error:
    print("Invalid data:", error)
    employees = []

total = process_payroll(employees)
print(f"Total Salaries: {total} SAR")
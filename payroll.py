def process_payroll(employees):
    total = 0
    for emp in employees:
        emp.display_info()
        salary = emp.calculate_salary()  # works for any Employee type
        print(f"Salary: {salary} SAR")
        total += salary
    return total
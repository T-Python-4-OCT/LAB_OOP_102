from employee import Employee, FullTimeEmployee, PartTimeEmployee
def main():
    employee1 = FullTimeEmployee("Ahmed", 101, 8000)
    employee2 = PartTimeEmployee("Sara", 102, 80, 50)
    employee3 = FullTimeEmployee("Khalid", 103, 12000)

    employees = [employee1, employee2, employee3]

    total_salaries = 0

    print("=== Employee Records & Salary Payout ===")
    for employee in employees:
        employee.display_info()
        employee.pay_salary()
        total_salaries += employee.calculate_salary()
        print("-" * 40)

    print(f"Total Salaries: {total_salaries:,} SAR\n")

    print("=== Testing Abstraction & Constraints ===")
    try:
        invalid_employee = Employee("Fahad", 999)
    except TypeError as e:
        print(f"Caught expected error: {e}")

    try:
        employee1.__transfer_funds(8000)
    except AttributeError:
        print("Private method __transfer_funds successfully restricted")

if __name__ == "__main__":
    main()
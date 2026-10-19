from full_time_employee import FullTimeEmployee
from part_time_employee import PartTimeEmployee

def main():
    try:
        employees = [
            FullTimeEmployee("Ahmed", 10198654, 8000),
            PartTimeEmployee("Sara", 10256789, 80, 40),
            FullTimeEmployee("Khalid", 103667822, 12000),
        ]
    except ValueError as e:
        print(f"Validation error: {e}")
        return

    total = 0

    for emp in employees:
        emp.display_info()
        salary = emp.calculate_salary()
        print(f"Salary: {salary} SAR")
        total += salary

    print(f"Total Salaries: {total} SAR")


if __name__ == "__main__":
    main()
from employee import FullTimeEmployee, PartTimeEmployee


def main():
    ahmed = FullTimeEmployee("Ahmed", 101, 8000)
    sara = PartTimeEmployee("Sara", 102, 80, 50)
    khalid = FullTimeEmployee("Khalid", 103, 12000)

    employees = [ahmed, sara, khalid]

    total_salary = 0

    for employee in employees:
        salary = employee.calculate_salary()

        print(
            f"Employee: {employee.name} "
            f"ID: {employee.get_employee_id()} "
            f"Salary: {salary} SAR"
        )

        total_salary += salary

    print(f"Total Salaries: {total_salary} SAR")


if __name__ == "__main__":
    main()

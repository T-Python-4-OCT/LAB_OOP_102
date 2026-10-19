from employee import FullTimeEmployee, PartTimeEmployee


def main():
    ahmed = FullTimeEmployee("Ahmed", 101, 8000)
    sara = PartTimeEmployee("Sara", 102, 80, 50)
    khalid = FullTimeEmployee("Khalid", 103, 12000)

    employees = [ahmed, sara, khalid]

    total = 0

    for employee in employees:
        salary = employee.calculate_salary()
        employee.display_info(end=" ")
        print("Salary:", salary, "SAR")
        total = total + salary

    print("Total Salaries:", total, "SAR")


if __name__ == "__main__":
    main()
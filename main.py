from employee import FullTimeEmployee, PartTimeEmployee


def main():
  employees = [
      FullTimeEmployee("Ahmed", 101, 8000),
      PartTimeEmployee("Sara", 102, hours_worked=80, hourly_rate=50),
      FullTimeEmployee("Khalid", 103, 12000),
  ]

  total_salaries = 0

  for emp in employees:
    emp.display_info()
    salary = emp.calculate_salary()
    total_salaries += salary
    print(f"Salary: {int(salary)} SAR")

  print(f"Total Salaries: {int(total_salaries)} SAR")


if __name__ == "__main__":
  main()
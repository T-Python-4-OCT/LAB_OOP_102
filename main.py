from employee import FullTimeEmployee, PartTimeEmployee

def main():
    # Create employee objects
    employees = [
        FullTimeEmployee("Mohammed", 101, 10000),
        PartTimeEmployee("Norah", 150, 90, 70),
        FullTimeEmployee("Nawaf", 103, 12000)
    ]

    total_salaries = 0.0

    # Single loop to display info, calculate/display salary, and accumulate total
    for emp in employees:
        emp.display_info(end=" ")
        salary = emp.calculate_salary()
        
        # Format salary without decimal places if it's a whole number
        salary_display = int(salary) if salary.is_integer() else salary
        print(f"Salary: {salary_display} SAR")
        
        total_salaries += salary

    total_display = int(total_salaries) if total_salaries.is_integer() else total_salaries
    print(f"Total Salaries: {total_display} SAR")

if __name__ == "__main__":
    main()

"""Employee management: builds employees, prints salaries and the total."""
 
from employees import FullTimeEmployee, PartTimeEmployee
 
 
def fmt(amount):
    """Show 8000 instead of 8000.0, but keep real decimals like 8000.5."""
    return f"{amount:g}" if amount == int(amount) else f"{amount:.2f}"
 
 
def main():
    employees = [
        FullTimeEmployee("Ahmed", 101, 8000),
        PartTimeEmployee("Sara", 102, 80, 50),
        FullTimeEmployee("Khalid", 103, 12000),
    ]
    print("________________________________")
    total = 0
    for emp in employees:
        emp.display_info(end=" ")
        salary = emp.calculate_salary()
        print(f"Salary: {fmt(salary)} SAR")
        total += salary
    print("_________________________________") 
    print(f"Total Salaries: {fmt(total)} SAR")
    print("_________________________________") 
 
if __name__ == "__main__":
    main()

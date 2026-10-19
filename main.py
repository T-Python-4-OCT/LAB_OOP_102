from employee import FullTimeEmployee, PartTimeEmployee



#          💰 EMPLOYEE SALARY SYSTEM 💰


print("\n✨ = EMPLOYEE SALARY SYSTEM = ✨\n")


# 👥 Create employees
abdulrahman = FullTimeEmployee("Abdulrahman", 101, 8000)
amal = PartTimeEmployee("Amal", 102, 80, 50)
mohammed= FullTimeEmployee("Mohammed", 103, 12000)


# 📋 Store all employees in one list
employees = [abdulrahman, amal,mohammed ]


# 💰 Calculate total salaries
total_salaries = 0

for employee in employees:
    employee.display_info()

    salary = employee.calculate_salary()

    print(f"Salary: {salary:g} SAR 💰")

    total_salaries += salary


print("\n✨ ========================== ✨")
print(f"💰 Total Salaries: {total_salaries:g} SAR")
print("✨ ============================ ✨")
print("\n🎉 Thank you for using the system!")
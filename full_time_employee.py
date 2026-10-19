from employee import Employee
from validators import check_non_negative


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = check_non_negative(monthly_salary, "Monthly salary")

    def calculate_salary(self):
        return self.monthly_salary
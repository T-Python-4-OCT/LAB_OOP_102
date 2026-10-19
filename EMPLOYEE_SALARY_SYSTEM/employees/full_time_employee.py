import math

from employees.employee import Employee


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)

        if (
            isinstance(monthly_salary, bool)
            or not isinstance(monthly_salary, (int, float))
            or not math.isfinite(monthly_salary)
            or monthly_salary < 0
        ):
            raise ValueError("Monthly salary must be a non-negative finite number.")

        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

        
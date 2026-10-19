from employee import Employee

class FullTimeEmployee(Employee):
    """Employee with a fixed monthly salary."""

    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        if not isinstance(monthly_salary, (int, float)) or isinstance(monthly_salary, bool) or monthly_salary <= 0:
            raise ValueError("Monthly salary must be a positive number.")
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary
from employee import Employee


class FullTimeEmployee(Employee):

    def __init__(self, name: str, employee_id: int, monthly_salary: float):
        super().__init__(name, employee_id)

        if monthly_salary < 0:
            raise ValueError("Monthly salary cannot be negative")

        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):

    def __init__(self, name: str, employee_id: int, hours_worked: int, hourly_rate: float):
        super().__init__(name, employee_id)

        if hours_worked < 0:
            raise ValueError("Hours worked cannot be negative")

        if hourly_rate < 0:
            raise ValueError("Hourly rate cannot be negative")

        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate
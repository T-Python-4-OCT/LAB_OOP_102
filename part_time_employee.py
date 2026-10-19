from employee import Employee

class PartTimeEmployee(Employee):
    """Employee paid by the hour."""

    def __init__(self, name, employee_id, hours_worked, hourly_rate):
        super().__init__(name, employee_id)
        if not isinstance(hours_worked, (int, float)) or isinstance(hours_worked, bool) or hours_worked < 0:
            raise ValueError("Hours worked must be a non-negative number.")
        if not isinstance(hourly_rate, (int, float)) or isinstance(hourly_rate, bool) or hourly_rate <= 0:
            raise ValueError("Hourly rate must be a positive number.")
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate
import math

from employees.employee import Employee


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hours_worked, hourly_rate):
        super().__init__(name, employee_id)

        if (
            isinstance(hours_worked, bool)
            or not isinstance(hours_worked, (int, float))
            or not math.isfinite(hours_worked)
            or not 0 <= hours_worked <= 744
        ):
            raise ValueError("Hours worked must be between 0 and 744.")

        if (
            isinstance(hourly_rate, bool)
            or not isinstance(hourly_rate, (int, float))
            or not math.isfinite(hourly_rate)
            or hourly_rate < 0
        ):
            raise ValueError("Hourly rate must be a non-negative finite number.")

        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate
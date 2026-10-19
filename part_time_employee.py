from employee import Employee
from validators import check_non_negative


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hours_worked, hourly_rate):
        super().__init__(name, employee_id)
        self.hours_worked = check_non_negative(hours_worked, "Hours worked")
        self.hourly_rate = check_non_negative(hourly_rate, "Hourly rate")

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate
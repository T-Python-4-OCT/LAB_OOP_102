from abc import ABC, abstractmethod  # abstract base class

def check_text(value, field):
    if not isinstance(value, str) or value.strip() == "":
        raise ValueError(f"{field} must be a non-empty text")
    return value.strip()


def check_number(value, field, allow_zero=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be a number")
    if value < 0 or (value == 0 and not allow_zero):
        raise ValueError(f"{field} must be a positive number")
    return value


class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = check_text(name, "Name")
        if isinstance(employee_id, bool) or not isinstance(employee_id, int) or employee_id <= 0:
            raise ValueError("Employee ID must be a positive whole number")
        self.__employee_id = employee_id          # private attribute

    def get_employee_id(self):
        return self.__employee_id

    def display_info(self, end="\n"):
        print(f"Employee: {self.name} ID: {self.get_employee_id()}", end=end)

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = check_number(monthly_salary, "Monthly salary")

    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hours_worked, hourly_rate):
        super().__init__(name, employee_id)
        self.hours_worked = check_number(hours_worked, "Hours worked", allow_zero=True)
        self.hourly_rate = check_number(hourly_rate, "Hourly rate")

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate
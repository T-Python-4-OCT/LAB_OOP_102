from abc import ABC, abstractmethod
import math


MAX_MONTHLY_SALARY = 20000


def _validate_amount(value, field_name):
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(value)
        or value < 0
    ):
        raise ValueError(f"{field_name} must be a finite, non-negative number.")


def _validate_salary(value):
    _validate_amount(value, "Salary")
    if value > MAX_MONTHLY_SALARY:
        raise ValueError(
            f"Salary must not exceed {MAX_MONTHLY_SALARY} SAR per month."
        )


class Employee(ABC):
    def __init__(self, name, employee_id):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        if any(character.isdigit() for character in name):
            raise ValueError("Name must not contain numbers.")
        if type(employee_id) is not int or employee_id <= 0:
            raise ValueError("Employee ID must be a positive integer.")

        self.name = name.strip()
        self.__employee_id = employee_id

    def get_employee_id(self):
        return self.__employee_id

    def display_info(self):
        print(f"Employee: {self.name} ID: {self.get_employee_id()}", end=" ")

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        _validate_salary(monthly_salary)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        _validate_salary(self.monthly_salary)
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hours_worked, hourly_rate):
        super().__init__(name, employee_id)
        _validate_amount(hours_worked, "Hours worked")
        _validate_amount(hourly_rate, "Hourly rate")
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        _validate_salary(self.calculate_salary())

    def calculate_salary(self):
        salary = self.hours_worked * self.hourly_rate
        _validate_salary(salary)
        return salary

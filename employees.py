"""Employee classes for the Employee Salary System."""

from abc import ABC, abstractmethod
from numbers import Real


def _validate_name(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Name must be a non-empty string.")
    return value.strip()


def _validate_positive_int(value, field):
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{field} must be a positive integer.")
    return value


def _validate_non_negative_number(value, field):
    if isinstance(value, bool) or not isinstance(value, Real) or value < 0:
        raise ValueError(f"{field} must be a number greater than or equal to 0.")
    return value


class Employee(ABC):
    """Abstract parent class for all employees."""

    def __init__(self, name, employee_id):
        self.name = name 
        self.__employee_id = _validate_positive_int(employee_id, "Employee ID")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = _validate_name(value)

    def get_employee_id(self):
        return self.__employee_id

    def display_info(self, end="\n"):
        print(f"Employee: {self.name} ID: {self.get_employee_id()}", end=end)

    @abstractmethod
    def calculate_salary(self):
        """Every employee type must define how its salary is calculated."""


class FullTimeEmployee(Employee):
    """Receives a fixed monthly salary."""

    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary           

    @property
    def monthly_salary(self):
        return self._monthly_salary

    @monthly_salary.setter
    def monthly_salary(self, value):
        self._monthly_salary = _validate_non_negative_number(value, "Monthly salary")

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    """Paid by hours worked * hourly rate."""

    def __init__(self, name, employee_id, hours_worked, hourly_rate):
        super().__init__(name, employee_id)
        self.hours_worked = hours_worked                   
        self.hourly_rate = hourly_rate                    

    @property
    def hours_worked(self):
        return self._hours_worked

    @hours_worked.setter
    def hours_worked(self, value):
        self._hours_worked = _validate_non_negative_number(value, "Hours worked")

    @property
    def hourly_rate(self):
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value):
        self._hourly_rate = _validate_non_negative_number(value, "Hourly rate")

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate



    #MohammedAlnsafi
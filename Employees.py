from abc import ABC, abstractmethod


class Employee(ABC):
    """Abstract parent class for all employees."""

    def __init__(self, name, employee_id):
        self.name = name                    
        self.__employee_id = self._validate_id(employee_id) 

    @staticmethod
    def _validate_id(employee_id):
        if not isinstance(employee_id, int) or isinstance(employee_id, bool) or employee_id <= 0:
            raise ValueError("employee_id must be a positive integer")
        return employee_id

    @staticmethod
    def _validate_number(value, field, allow_zero=False):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError(f"{field} must be a number")
        if value < 0 or (value == 0 and not allow_zero):
            raise ValueError(f"{field} must be {'zero or ' if allow_zero else ''}greater than zero")
        return value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("name must be a non-empty string")
        self.__name = value.strip()

    def get_employee_id(self):
        return self.__employee_id

    def display_info(self, end="\n"):
        print(f"Employee: {self.name} ID: {self.__employee_id}", end=end)

    @abstractmethod
    def calculate_salary(self):
        """Every subclass must implement this."""


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary

    @property
    def monthly_salary(self):
        return self.__monthly_salary

    @monthly_salary.setter
    def monthly_salary(self, value):
        self.__monthly_salary = self._validate_number(value, "monthly_salary")

    def calculate_salary(self):
        return self.__monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hours_worked, hourly_rate):
        super().__init__(name, employee_id)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    @property
    def hours_worked(self):
        return self.__hours_worked

    @hours_worked.setter
    def hours_worked(self, value):
        self.__hours_worked = self._validate_number(value, "hours_worked", allow_zero=True)

    @property
    def hourly_rate(self):
        return self.__hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value):
        self.__hourly_rate = self._validate_number(value, "hourly_rate")

    def calculate_salary(self):
        return self.__hours_worked * self.__hourly_rate
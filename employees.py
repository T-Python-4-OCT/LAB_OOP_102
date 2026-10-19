from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, name, employee_id):
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(employee_id, int) or employee_id <= 0:
            raise ValueError("Employee ID must be a positive number.")

        self.name = name
        self.__employee_id = employee_id

    def get_employee_id(self):
        return self.__employee_id

    def display_info(self):
        print(f"Employee: {self.name} ID: {self.__employee_id}", end=" ")

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):

    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self.set_monthly_salary(monthly_salary)

    def get_monthly_salary(self):
        return self.__monthly_salary

    def set_monthly_salary(self, monthly_salary):
        if not isinstance(monthly_salary, (int, float)) or monthly_salary <= 0:
            raise ValueError("Monthly salary must be a positive number.")
        self.__monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.__monthly_salary


class PartTimeEmployee(Employee):

    def __init__(self, name, employee_id, hours_worked, hourly_rate):
        super().__init__(name, employee_id)
        self.set_hours_worked(hours_worked)
        self.set_hourly_rate(hourly_rate)

    def get_hours_worked(self):
        return self.__hours_worked

    def set_hours_worked(self, hours_worked):
        if not isinstance(hours_worked, (int, float)) or hours_worked < 0:
            raise ValueError("Hours worked must be zero or more.")
        self.__hours_worked = hours_worked

    def get_hourly_rate(self):
        return self.__hourly_rate

    def set_hourly_rate(self, hourly_rate):
        if not isinstance(hourly_rate, (int, float)) or hourly_rate <= 0:
            raise ValueError("Hourly rate must be a positive number.")
        self.__hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.__hours_worked * self.__hourly_rate

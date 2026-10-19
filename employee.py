from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, employee_id):
        if not isinstance(name, str) or len(name.strip()) < 4:
            raise ValueError("Name must be at least 4 characters")
        if not isinstance(employee_id, int) or employee_id <= 0:
            raise ValueError("Employee ID must be a positive integer")

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
        if not isinstance(monthly_salary, (int, float)) or not 0 < monthly_salary <= 20000:
            raise ValueError("Salary must be a number between 1 and 20000")
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hours_worked, hourly_rate):
        super().__init__(name, employee_id)
        if not isinstance(hours_worked, (int, float)) or not 0 <= hours_worked <= 160:
            raise ValueError("Hours must be a number between 0 and 160")
        if not isinstance(hourly_rate, (int, float)) or not 0 < hourly_rate <= 200:
            raise ValueError("Rate must be a number between 1 and 200")
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate
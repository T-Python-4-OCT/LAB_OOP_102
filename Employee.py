from abc import ABC, abstractmethod
class Employee(ABC):

    def __init__(self, name, employee_id):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name cannot be empty")

        if not isinstance(employee_id, int) or isinstance(employee_id, bool) or employee_id <= 0:
            raise ValueError("Invalid employee ID")

        self.name = name
        self.__employee_id = employee_id

    def get_employee_id(self):
        return self.__employee_id

    def display_info(self):
        print(f"Employee: {self.name} ID: {self.get_employee_id()}")

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):

    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)

        if not isinstance(monthly_salary, (int, float)) or isinstance(monthly_salary, bool) or monthly_salary < 0:
            raise ValueError("Invalid monthly salary")

        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):

    def __init__(self, name, employee_id, hours_worked, hourly_rate):
        super().__init__(name, employee_id)

        if not isinstance(hours_worked, (int, float)) or isinstance(hours_worked, bool) or not 0 <= hours_worked <= 744:
            raise ValueError("Invalid hours worked")

        if not isinstance(hourly_rate, (int, float)) or isinstance(hourly_rate, bool) or hourly_rate < 0:
            raise ValueError("Invalid hourly rate")

        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

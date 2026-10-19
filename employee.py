from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name: str, employee_id: int):
        if not name.strip():
            raise ValueError("Employee name cannot be empty")

        if employee_id <= 0:
            raise ValueError("Employee ID must be positive")

        self.name = name
        self.__employee_id = employee_id

    def get_employee_id(self):
        return self.__employee_id

    def display_info(self):
        salary = self.calculate_salary()
        print(f"Employee: {self.name} ID: {self.get_employee_id()} {salary} SAR")

    @abstractmethod
    def calculate_salary(self):
        pass
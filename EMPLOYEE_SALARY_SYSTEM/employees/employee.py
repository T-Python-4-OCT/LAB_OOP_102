from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, employee_id):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Employee name cannot be empty.")

        if (
            isinstance(employee_id, bool)
            or not isinstance(employee_id, int)
            or employee_id <= 0
        ):
            raise ValueError("Employee ID must be a positive integer.")

        self.name = name.strip()
        self.__employee_id = employee_id

    def get_employee_id(self):
        return self.__employee_id



    def display_info(self):
        print(f"Employee: {self.name} ID: {self.get_employee_id()}")

    @abstractmethod
    def calculate_salary(self):
        pass





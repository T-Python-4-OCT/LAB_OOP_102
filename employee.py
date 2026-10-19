from abc import ABC, abstractmethod
from validators import check_name, check_id


class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = check_name(name)
        self.__employee_id = check_id(employee_id)  # private

    def get_employee_id(self):
        return self.__employee_id

    def display_info(self):
        print(f"Employee: {self.name} ID: {self.get_employee_id()}", end=" ")

    @abstractmethod
    def calculate_salary(self):
        pass
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.__employee_id = employee_id

    def get_employee_id(self):
        return self.__employee_id

    def display_info(self):
        print(f"Employee:{self.name},ID:{self.get_employee_id()}")

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id,monthly_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

    

class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hours_worked, hourly_rate):
        super().__init__(name, employee_id)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

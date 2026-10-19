
from abc import ABC, abstractmethod



#        💼 EMPLOYEE SALARY SYSTEM 💼


class Employee(ABC):

    def __init__(self, name, employee_id):
        # Validation
        if not name:
            raise ValueError("Employee name cannot be empty.")

        if not isinstance(employee_id, int) or employee_id <= 0:
            raise ValueError("Employee ID must be a positive number.")

        self.name = name
        self.__employee_id = employee_id

    def get_employee_id(self):
        return self.__employee_id

    def display_info(self):
        print(
            f"Employee: {self.name} "
            f"ID: {self.get_employee_id()}",
            end=" "
        )

    @abstractmethod
    def calculate_salary(self):
        pass



#             👨‍💼 FULL-TIME EMPLOYEE


class FullTimeEmployee(Employee):

    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)

        if monthly_salary <= 0:
            raise ValueError("Monthly salary must be greater than 0.")

        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary



#             👨‍💻 PART-TIME EMPLOYEE


class PartTimeEmployee(Employee):

    def __init__(self, name, employee_id, hours_worked, hourly_rate):
        super().__init__(name, employee_id)

        if hours_worked <= 0:
            raise ValueError("Hours worked must be greater than 0.")

        if hourly_rate <= 0:
            raise ValueError("Hourly rate must be greater than 0.")

        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate
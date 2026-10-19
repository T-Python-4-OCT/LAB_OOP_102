from abc import ABC, abstractmethod

MAX_MONTHLY_SALARY = 100000
MAX_HOURLY_RATE = 300
MAX_HOURS_WORKED = 300


class Employee(ABC):
    def __init__(self, name, employee_id):
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("Name must be a non-empty text.")
        if not name.replace(" ", "").isalpha():
            raise ValueError("Name must contain letters only (no numbers or symbols).")
        if not isinstance(employee_id, int) or employee_id <= 0:
            raise ValueError("ID must be a whole number greater than zero.")

        self.name = name
        self.__employee_id = employee_id

    def get_employee_id(self):
        return self.__employee_id

    def display_info(self, end="\n"):
        print("Employee:", self.name, "ID:", self.__employee_id, end=end)

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        if not isinstance(monthly_salary, (int, float)) or monthly_salary <= 0:
            raise ValueError("Monthly salary must be a number greater than zero.")
        if monthly_salary > MAX_MONTHLY_SALARY:
            raise ValueError(f"Monthly salary cannot be more than {MAX_MONTHLY_SALARY} SAR.")

        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hours_worked, hourly_rate):
        super().__init__(name, employee_id)
        if not isinstance(hours_worked, (int, float)) or hours_worked < 0:
            raise ValueError("Hours worked must be a number (0 or more).")
        if hours_worked > MAX_HOURS_WORKED:
            raise ValueError(f"Hours worked cannot be more than {MAX_HOURS_WORKED} per month.")
        if not isinstance(hourly_rate, (int, float)) or hourly_rate <= 0:
            raise ValueError("Hourly rate must be a number greater than zero.")
        if hourly_rate > MAX_HOURLY_RATE:
            raise ValueError(f"Hourly rate cannot be more than {MAX_HOURLY_RATE} SAR.")

        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate
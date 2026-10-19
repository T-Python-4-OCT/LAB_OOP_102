class Employee:
    def __init__(self, name: str, employee_id: int):
        if not name:
            raise ValueError("Name cannot be empty")

        if employee_id <= 0:
            raise ValueError("Employee ID must be positive")

        self.name = name
        self.__employee_id = employee_id

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id: int):
        if employee_id <= 0:
            raise ValueError("Employee ID must be positive")
        self.__employee_id = employee_id

    def display_info(self):
        print(f"Employee: {self.name} ID: {self.get_employee_id()}")

    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement calculate_salary")


class FullTimeEmployee(Employee):
    def __init__(self, name: str, employee_id: int, monthly_salary: float):
        super().__init__(name, employee_id)

        if monthly_salary < 0:
            raise ValueError("Salary cannot be negative")

        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name: str, employee_id: int, hours_worked: float, hourly_rate: float):
        super().__init__(name, employee_id)

        if hours_worked < 0:
            raise ValueError("Hours cannot be negative")

        if hourly_rate < 0:
            raise ValueError("Hourly rate cannot be negative")

        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate
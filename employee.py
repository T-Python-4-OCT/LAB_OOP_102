from abc import ABC, abstractmethod

class Employee(ABC):
    """Abstract base class representing a generic employee."""
    
    def __init__(self, name: str, employee_id: int):
        self.name = name
        self.__employee_id = employee_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Employee name must be a non-empty string.")
        self._name = value.strip()

    def get_employee_id(self) -> int:
        """Returns the private employee ID."""
        return self.__employee_id

    def display_info(self, end: str = ""):
        """Prints the employee's name and ID."""
        print(f"Employee: {self.name} ID: {self.__employee_id}", end=end)

    @abstractmethod
    def calculate_salary(self) -> float:
        """Abstract method to calculate employee salary."""
        pass


class FullTimeEmployee(Employee):
    """Represents a full-time employee with a fixed monthly salary."""

    def __init__(self, name: str, employee_id: int, monthly_salary: float):
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary

    @property
    def monthly_salary(self) -> float:
        return self._monthly_salary

    @monthly_salary.setter
    def monthly_salary(self, value: float):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Monthly salary must be a non-negative number.")
        self._monthly_salary = float(value)

    def calculate_salary(self) -> float:
        return self._monthly_salary


class PartTimeEmployee(Employee):
    """Represents a part-time employee paid based on hours worked and hourly rate."""

    def __init__(self, name: str, employee_id: int, hours_worked: float, hourly_rate: float):
        super().__init__(name, employee_id)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    @property
    def hours_worked(self) -> float:
        return self._hours_worked

    @hours_worked.setter
    def hours_worked(self, value: float):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Hours worked must be a non-negative number.")
        self._hours_worked = float(value)

    @property
    def hourly_rate(self) -> float:
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value: float):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Hourly rate must be a non-negative number.")
        self._hourly_rate = float(value)

    def calculate_salary(self) -> float:
        return self._hours_worked * self._hourly_rate

from abc import ABC, abstractmethod


class Employee(ABC):

  def __init__(self, name: str, employee_id: int):
    if not name.strip():
      raise ValueError("Name cannot be empty.")
    if employee_id <= 0:
      raise ValueError("Employee ID must be a positive integer.")

    self.name = name
    self.__employee_id = employee_id    

  def get_employee_id(self):
    return self.__employee_id

  def display_info(self):
    print(f"Employee: {self.name} ID: {self.__employee_id}", end=" ")

  @abstractmethod
  def calculate_salary(self):
    pass


class FullTimeEmployee(Employee):

  def __init__(self, name: str, employee_id: int, monthly_salary: float):
    super().__init__(name, employee_id)
    if monthly_salary < 0:
      raise ValueError("Monthly salary cannot be negative.")
    self.monthly_salary = monthly_salary

  def calculate_salary(self):
    return self.monthly_salary


class PartTimeEmployee(Employee):

  def __init__(
      self, name: str, employee_id: int, hours_worked: float, hourly_rate: float
  ):
    super().__init__(name, employee_id)
    if hours_worked < 0 or hourly_rate < 0:
      raise ValueError("Hours worked and hourly rate cannot be negative.")
    self.hours_worked = hours_worked
    self.hourly_rate = hourly_rate

  def calculate_salary(self):
    return self.hours_worked * self.hourly_rate
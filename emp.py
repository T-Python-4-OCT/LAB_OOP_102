from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self,name,employee_id):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name cannot be empty")

        if isinstance(employee_id, bool) or not isinstance(employee_id, int) or employee_id <= 0:
            raise ValueError("Employee ID must be a positive integer")
        
        
        self.name=name
        self.__employee_id=employee_id
        
    def get_employee_id(self):
        return self.__employee_id
    
    def display_info(self):
        print(f"Employee: {self.name} ID: {self.get_employee_id()}")        
 
    @abstractmethod
    def calculate_salary(self):
        pass
    

class FullTimeEmployee(Employee):
    def __init__(self,name,employee_id,monthly_salary):
        if isinstance(monthly_salary, bool) or not isinstance(monthly_salary, (int, float)) or monthly_salary <= 0:
           raise ValueError("Monthly salary must be a positive number")

        
        
        super().__init__(name,employee_id)
        self.monthly_salary=monthly_salary
    def calculate_salary(self):
        return self.monthly_salary
        






class PartTimeEmployee(Employee):  
    def __init__(self,name,employee_id,hours_worked,hourly_rate):
        if isinstance(hours_worked, bool) or not isinstance(hours_worked, (int, float)) or hours_worked < 0:
           raise ValueError("Hours worked cannot be negative")

        if isinstance(hourly_rate, bool) or not isinstance(hourly_rate, (int, float)) or hourly_rate <= 0:
           raise ValueError("Hourly rate must be a positive number")
        
        super().__init__(name,employee_id)
        self.hourly_rate=hourly_rate
        self.hours_worked=hours_worked
        
        
    def calculate_salary(self):
        return self.hourly_rate*self.hours_worked










      
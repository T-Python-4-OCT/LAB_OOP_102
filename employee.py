
class Employee:
    def __init__(self, name, employee_id):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Employee name must be a non-empty string.")

        if (isinstance(employee_id, bool)
            or not isinstance(employee_id, int)
            or not 100 <= employee_id <= 999 ):
            raise ValueError("Employee ID must be exactly 3 digits.")
            

        self.name = name.strip()
        self.__employee_id = employee_id

    def get_employee_id(self):
        return self.__employee_id

    def display_info(self):
        print(f"Employee: {self.name} "
            f"ID: {self.get_employee_id()} "
            f"Salary: {self.calculate_salary():g} SAR")
            

    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement calculate_salary().")
            


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)

        if (isinstance(monthly_salary, bool)
            or not isinstance(monthly_salary, (int, float))
            or monthly_salary < 0):
            raise ValueError("Monthly salary must be a non-negative number.")

        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hours_worked, hourly_rate):
        super().__init__(name, employee_id)

        if (isinstance(hours_worked, bool)
            or not isinstance(hours_worked, (int, float))
            or not 0 <= hours_worked <= 744):
            
            raise ValueError("Hours worked must be between 0 and 744 per month.")

        if (isinstance(hourly_rate, bool)
            or not isinstance(hourly_rate, (int, float))
            or hourly_rate < 0):
            
            raise ValueError("Hourly rate must be a non-negative number.")

        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

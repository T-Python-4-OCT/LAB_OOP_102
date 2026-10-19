class Employee:

    def __init__(self, name, employee_id):
        # Prevent creating an object directly from Employee
        if type(self) is Employee:
            raise TypeError("Employee is abstract and cannot be instantiated directly.")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(employee_id, int) or isinstance(employee_id, bool) or employee_id <= 0:
            raise ValueError("Employee ID must be a positive integer.")

        self.name = name.strip()
        self.__employee_id = employee_id 

    def get_employee_id(self):
        return self.__employee_id

    def display_info(self):
        print(f"Employee: {self.name}  ID: {self.__employee_id}", end=" ")

    def calculate_salary(self):
        """Must be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement calculate_salary().")
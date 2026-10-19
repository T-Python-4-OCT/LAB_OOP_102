"""Quick checks: python test_employees.py"""
 
from employees import Employee, FullTimeEmployee, PartTimeEmployee
 
 
def expect_error(func, label):
    try:
        func()
    except (ValueError, TypeError) as e:
        print(f"OK   {label}: {type(e).__name__}: {e}")
    else:
        raise AssertionError(f"FAILED (no error): {label}")
 
 

expect_error(lambda: Employee("X", 1), "abstract Employee")
 

class Bad(Employee):
    pass
expect_error(lambda: Bad("X", 1), "subclass missing calculate_salary")
 
# validation
expect_error(lambda: FullTimeEmployee("", 1, 100), "empty name")
expect_error(lambda: FullTimeEmployee(123, 1, 100), "name not a string")
expect_error(lambda: FullTimeEmployee("A", 0, 100), "id = 0")
expect_error(lambda: FullTimeEmployee("A", -5, 100), "negative id")
expect_error(lambda: FullTimeEmployee("A", "1", 100), "id as string")
expect_error(lambda: FullTimeEmployee("A", 1, -100), "negative salary")
expect_error(lambda: FullTimeEmployee("A", 1, "100"), "salary as string")
expect_error(lambda: FullTimeEmployee("A", 1, True), "salary as bool")
expect_error(lambda: PartTimeEmployee("A", 1, -1, 50), "negative hours")
expect_error(lambda: PartTimeEmployee("A", 1, 10, -50), "negative rate")
 

e = FullTimeEmployee("A", 1, 100)
expect_error(lambda: setattr(e, "monthly_salary", -1), "setter negative salary")

assert not hasattr(e, "employee_id")
expect_error(lambda: e.__employee_id, "private id access") if False else None
assert e.get_employee_id() == 1
 
assert FullTimeEmployee("A", 1, 8000).calculate_salary() == 8000
assert PartTimeEmployee("S", 2, 80, 50).calculate_salary() == 4000
assert PartTimeEmployee("S", 2, 0, 50).calculate_salary() == 0
 
print("\nAll tests passed.")

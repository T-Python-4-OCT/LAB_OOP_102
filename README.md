# Employee Salary System

## Scenario

A company wants to develop a simple system to calculate employee salaries.

The company has two types of employees:

- Full-Time Employee: Receives a fixed monthly salary.
- Part-Time Employee: Gets paid based on the number of hours worked.

Your task is to build this system using Python OOP.

## Requirements

### Part 1 — A Parent (Abstract) Employee Class

Create a parent class called `Employee` with:

Attributes:

- `name`: Employee's name.
- `employee_id`: A private attribute storing the employee's ID.

Methods:

- `get_employee_id()`: Returns the employee's ID.
- `display_info()`: Prints the employee's name and ID.
- `calculate_salary()`: An abstract method that subclasses must implement.

### Part 2 — Employee Types

Create two classes that inherit from `Employee`.

1\. FullTimeEmployee

- Additional attribute: `monthly_salary`.
- Implements `calculate_salary()` to return the fixed monthly salary.

2\. PartTimeEmployee

- Additional attributes: `hours_worked` and `hourly_rate`.
- Implements `calculate_salary()` to return `hours_worked * hourly_rate`.

### Part 3 — Employee Management

Create three employee objects:

| Name   | Type      | Salary details    |
| ------ | --------- | ----------------- |
| Ahmed  | Full-Time | 8,000 SAR/month   |
| Sara   | Part-Time | 80 hours × 50 SAR |
| Khalid | Full-Time | 12,000 SAR/month  |

Store all employees in a list.

Use a single loop to:

1. Display each employee's information.
2. Calculate and display their salary using `calculate_salary()`.
3. Calculate the total salaries of all employees.

## Expected Output

CONSOLE
```
Employee: Ahmed ID: 101 Salary: 8000 SAR
Employee: Sara ID: 102 Salary: 4000 SAR
Employee: Khalid ID: 103 Salary: 12000 SAR
Total Salaries: 24000 SAR
```

## Rules

- Use encapsulation and any needed OOP principles.
- Arrange your code in at least 2 files.
- Do validation to make sure values are acceptable. Names must be non-empty and
  must not contain numbers; employee IDs must be positive integers; salary,
  hours worked, and hourly rates must be finite, non-negative numbers. Monthly
  salary per employee must not exceed 20,000 SAR.

## Files

- `employees.py` defines the abstract `Employee` class and its employee types.
- `LAB_OOP_02.py` creates the sample employees and prints their salaries.

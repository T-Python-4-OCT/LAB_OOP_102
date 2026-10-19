import unittest
from employee import FullTimeEmployee, PartTimeEmployee

class TestEmployeeSystem(unittest.TestCase):
    
    def test_full_time_employee(self):
        emp = FullTimeEmployee("Ahmed", 101, 8000)
        self.assertEqual(emp.name, "Ahmed")
        self.assertEqual(emp.get_employee_id(), 101)
        self.assertEqual(emp.monthly_salary, 8000)
        self.assertEqual(emp.calculate_salary(), 8000)

    def test_part_time_employee(self):
        emp = PartTimeEmployee("Sara", 102, 80, 50)
        self.assertEqual(emp.name, "Sara")
        self.assertEqual(emp.get_employee_id(), 102)
        self.assertEqual(emp.hours_worked, 80)
        self.assertEqual(emp.hourly_rate, 50)
        self.assertEqual(emp.calculate_salary(), 4000)

    def test_validation_name(self):
        with self.assertRaises(ValueError):
            FullTimeEmployee("", 101, 8000)
        with self.assertRaises(ValueError):
            PartTimeEmployee("   ", 102, 10, 10)

    def test_validation_salary(self):
        with self.assertRaises(ValueError):
            FullTimeEmployee("Ahmed", 101, -500)

    def test_validation_hours_and_rate(self):
        with self.assertRaises(ValueError):
            PartTimeEmployee("Sara", 102, -10, 50)
        with self.assertRaises(ValueError):
            PartTimeEmployee("Sara", 102, 10, -50)

if __name__ == "__main__":
    unittest.main()

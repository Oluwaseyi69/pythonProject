import unittest

from ibrahim.employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.employee = Employee(123,"seyi","operations",45,4)

    def test_emp_salary(self):
        self.employee.calculate_emp_salary(5)
        self.assertEquals(50, self.employee.get_salary(5))

    def test_that_emp_salary_cannot_be_negative(self):
        self.employee.negative_salary(-4)
        self.assertEquals(0, self.employee.get_salary(0))

    # def test_that_employee_details(self):
    #     employee = Employee(1, "seyi","operations", 45, 4)
    #     self.assertRaises(self.employee.emp_details(),employee)

    def test_print_employee_details(self):
        emp = Employee(123, "seyi","operations", 45, 4)
        emp.emp_assign_department("IT")
        emp.calculate_emp_salary(50)
        emp.emp_details()


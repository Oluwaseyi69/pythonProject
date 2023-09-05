from random import random

from ibrahim.employee_exceptions import InvalidHour


class  Employee:
    def __init__(self, generate_id, name, department, hourly_rate, number_of_worked):
        # self.employee_details = None
        # self.salary = 0
        self.__emp_id = generate_id
        self.__emp_name = name
        self.__emp_department = department
        self.hourly_rate = 10
        self.number_of_worked = number_of_worked

    def calculate_emp_salary(self, number_of_hours_worked):
        self.salary = self.hourly_rate * number_of_hours_worked
        if number_of_hours_worked >= 0:
            return self.salary

        else:
            raise InvalidHour("Enter a valid hour")

    def negative_salary(self, number_of_hours_worked):
        # self.salary = self.hourly_rate * number_of_hours_worked
        if number_of_hours_worked <= 0:
            return 0
        else:
            raise InvalidHour("Enter a valid hour")



    def get_salary(self, number_of_hours_worked):
        return  self.hourly_rate * number_of_hours_worked



    def emp_assign_department(self, emp_department):
        self.__emp_department = emp_department

    def emp_details(self):
        print(f""" 
                    Employee Id: {self.__emp_id}
                    Employee Name: {self.__emp_name}
                    Employee Department: {self.__emp_department}
                    Employee Worked Hours:  {self.number_of_worked}
                    Employee Salary:${self.calculate_emp_salary(4)}
        """)

    def generate_id(self):
        return ''.join(str(random.randint(0, 9))
                       for _ in range(6))

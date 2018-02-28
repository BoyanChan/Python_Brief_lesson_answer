class Employee:
    def __init__(self, first_name, last_name, salary=''):
        self.fn = first_name
        self.ln = last_name
        if salary:
            self.salary = int(salary)
        else:
            self.salary = int(0)

    def give_raise(self, salary=5000):
        self.salary += salary


import unittest


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_Epe = Employee("A", "B")

    def test_no_salary(self):
        self.assertEqual(self.my_Epe.salary, 0)

    def test_5000_salary(self):
        self.my_Epe.give_raise()
        self.assertEqual(self.my_Epe.salary, 5000)

    def test_100_salary(self):
        self.my_Epe.give_raise(100)
        self.assertEqual(self.my_Epe.salary, 100)


unittest.main()


class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # or Employee.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first,last,pay= emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Employee('test', 'user', 50000)
emp2 = Employee('neeli', 'mishra', 60000)

import datetime
my_date = datetime.date(2016,7,11)
print(Employee.is_workday(my_date))

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-80000'
# emp_str_3 = 'Jane-Doe-90000'
#
# new_emp1 = Employee.from_string(emp_str_1)
# new_emp2 = Employee.from_string(emp_str_2)

# print(new_emp1.email)
# print(new_emp1.pay)

#Employee.raise_amount = 1.05
# emp1.set_raise_amount(1.05)
#
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)






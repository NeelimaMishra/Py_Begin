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

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay) # other way to write this is Employee.__init__(self,first,last,pay)
        self.prog_lang = prog_lang

class Managers(Employee):

    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())

dev_1 = Developer('test', 'user', 50000, "python")
dev_2 = Developer('neeli', 'mishra', 60000, "java")

mgr_1 = Managers('soe','smith',80000, [dev_1])

#print(isinstance(mgr_1, Developer))
#print(issubclass(Managers, Employee))
#print(issubclass(Managers, Developer))
print(issubclass(Developer, Employee))
# mgr_1.add_emp(dev_1)
# print(mgr_1.print_emps())
# mgr_1.remove_emp((dev_1))
# print(mgr_1.print_emps())

# print(dev_1.email)
# print(dev_1.prog_lang)

#print(help(Developer))








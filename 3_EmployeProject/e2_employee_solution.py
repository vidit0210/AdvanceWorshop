#inherittance

class Employee:

    raise_amount =1.10

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'

    def get_fullname(self):
        return self.first + self.last

    def apply_raise(self):
         return self.pay *self.raise_amount



class Developer(Employee):
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self,first,last,pay,employees = None):
        super().__init__(first,last,pay)
        self.employees = employees

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

    def print_employee(self):
        for emp in self.employees:
            print('-->',emp.get_fullname())


d1 = Developer('Vidit','Shah',1000,'Python')

print(d1.prog_lang)

m1=Manager('Rock','Shah',100,[d1])

print(m1.print_employee())
print(m1.add_emp('d2'))
print(m1.print_employee())
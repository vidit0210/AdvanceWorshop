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




e1=Employee('Vidit','Shah',1000)
print(e1.get_fullname())
print(e1.email)
print(e1.pay)
print(e1.apply_raise())
e1.raise_amount =2
print((e1.apply_raise()))
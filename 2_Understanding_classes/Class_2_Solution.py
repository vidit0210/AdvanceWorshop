class Student:

    def __init__(self, fname, lname, rollno):
        self.fname = fname
        self.lname = lname
        self.rollno = rollno

    def email(self):
        print('Your email id is :', self.fname + '.' + self.lname + '@somaiya.edu')


s1 = Student('Vidit', 'Shah', '45')
print(s1.fname)
print(s1.lname)
print(s1.rollno)

print(s1.email())
# Inheritance
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


"""class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)"""


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def pri(self):
        print(self.firstname + ' ' + self.lastname + ' ' + str(self.graduationyear))


x = Student("Mike", "Olsen", 2019)
x.pri()
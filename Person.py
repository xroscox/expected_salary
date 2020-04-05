class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        self.ssid = ""

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.student_id = None
        self.graduationyear = year


x = Student("Mike", "Olsen", 2020)
x.printname()
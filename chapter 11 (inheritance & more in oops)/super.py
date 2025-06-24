class Person:
    def __init__(self):
        print("initializing a person....\n")

    country = "india"

    def takebreath(self):
        print("i am breathing....")

class Employee:
    company = "honda"
    def __init__(self):
        super().__init__()
        print("initializing a employee....\n")

    def getsalary(self):
        print(f"salary is {self.salary}")

    def takebreath(self):

        print("i am an employee so i am luckily breathing...")

class programmer(Employee):
    company = "fiverr"
    country = "india"

    def __init__(self):
        #super().__init__()
        print("initializing a programer....\n")

    def getsalary(self):
        print(f"no salary to programmer")

    def takebreath(self):
        super().takebreath()
        print("i am an programmer so i am breathing++...")

#p = Person()
#p.takebreath()

#e = Employee()
'''e.takebreath()
'''
pr = programmer()
#pr.takebreath()
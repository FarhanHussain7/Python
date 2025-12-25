class Person:
    country = "india"

    def takebreath(self):
        print("i am breathing....")

class Employee:
    company = "honda"

    def getsalary(self):
        print(f"salary is {self.salary}")

    def takebreath(self):
        print("i am an employee so i am luckily breathing...")

class programmer(Employee):
    company = "fiverr"
    country = "india"

    def getsalary(self):
        print(f"no salary to programmer")

    def takebreath(self):
        print("i am an programmer so i am breathing++...")

p = Person()
p.takebreath()
#print(p.company)---- # it will through an error beacuse person doesnot have an company
e = Employee()
e.takebreath()
print(e.company)
pr = programmer()
pr.takebreath()
print(pr.company)
print(pr.country)


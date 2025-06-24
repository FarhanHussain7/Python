class Employee:
    company = "visa"
    eCode = 120

class Freelancer:
    company = "fiverr"
    level = 1

    def upgradelevel(self):
        self.level = self.level + 1

class Programmer(Employee, Freelancer):# if user want print(p.company) than only first class(employee) give there comapny name 
    name = "rohit"

p = Programmer()
p.upgradelevel()
print(p.company)
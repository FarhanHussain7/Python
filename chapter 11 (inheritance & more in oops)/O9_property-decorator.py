class Employee:
    company = "bharat gas"
    salary = 4500
    salarybonus = 500
    #totalsalary = 5000

    @property
    def totalsalary(self):
        return self.salary + self.salarybonus
    
    @totalsalary.setter
    def totalsalary(self, val):
        self.salarybonus = val - self.salary


e = Employee()
print(e.totalsalary)
e.totalsalary = 5000
print(e.salary)
print(e.salarybonus)


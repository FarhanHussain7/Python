class Employee:
    company = "camel"
    salary = 100
    location = "delhi"

    #def changesalary(self, sal):
        #s
    @classmethod    
    def changesalary(cls, sal):
        cls.salary = sal


e = Employee()
print(e.salary)
e.changesalary(454)
print(e.salary)
print(Employee.salary)
class Employee:
    company = "google"
    def getsalary(self):
        print("salary for this employee working in {self.company} is {self.salary}")

harry = Employee()
harry.salary = 10000
harry.getsalary() #Employee.getsalary(harry)
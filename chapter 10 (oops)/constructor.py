class Employee:
    company = "google"
    
    def __init__(self, name, salary, submit):
        self.name = name
        self.salary = salary
        self.submit = submit
        print("employee is created")
    
    def getdetailse(self):
        print("the name of the employee is ",self.name)
        print("the salary of the employee is {self.salary}")
        print("the submit of the employee is {self.submit}")
    def getsalary(self):
        print("salary for this employee working in {self.company} is {self.salary}")
    
    @staticmethod # this methods is a decorader to mark greet as a static method
    def greet():
        print("good morning, sir")
    @staticmethod
    def time():
        print("time is 9am in morning")
harry = Employee("harry", 100, "youtube")
harry.getdetailse()
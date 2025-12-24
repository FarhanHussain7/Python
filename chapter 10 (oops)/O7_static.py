class Employee:
    @staticmethod # this methods is a decorader to mark greet as a static method
    def greet():
        print("good morning, sir")
    @staticmethod
    def time():
        print("time is 9am in morning")
harry = Employee()
harry.greet() #Employee.greet()
harry.time()
class Employee:
    company = "google"
    salary = 100
    
    def __init__(self,age):
        self.age = age # instance attribute

    def show(self): # instance method - it will target to object
        print(f"How are you {self.age}")

    @classmethod # class method - it will target to class 
    def hello(cls):
        print("you are in class method ")

    @staticmethod #static method - 
    def static():
        print("How are you sir ")

obj = Employee(89)

obj.show()
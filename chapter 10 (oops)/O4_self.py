# self is dedicated to object so it hadle the function 

class Employee:

    company = "google"
    def getsalary(self):
        print("salary for this employee working in {self.company} is {self.salary}")

harry = Employee()
harry.salary = 10000
harry.getsalary() #Employee.getsalary(harry)


class Factory:
    # Constructor 
    def __init__(self,material,zip, pocket):
        self.material = material
        self.zip = zip
        self.pocket = pocket
    
    def show(self):
        print(f"Your product has :{self.material} {self.zip} {self.pocket}")


reebok = Factory("leather", 3, 2)

print(reebok.material)

campus = Factory("nylon",4,5)

print(campus.pocket)

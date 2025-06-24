class Employee:
    company = "google"

    def showDetails(self):
        print("this is an employee")

class programmer(Employee):
    language = "python"
    company = "youtube"
    
    def getlanguage(self):
        print("the language is {self.language}")
    
    def showDetails(self):
        print("this is an programer")


e = Employee()
e.showDetails()
print(e.company)
p = programmer()
p.showDetails()
print(p.company)
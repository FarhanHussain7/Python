class Employee:
    company = "google" #class attribute

harry = Employee()
rajani = Employee()
harry.salary = 300 # instance attributes
rajani.salary = 400 # instance attributes

print(harry.company)
print(rajani.company)
Employee.company = "youtube"
print(harry.company)
print(rajani.company)
print(harry.salary)
print(rajani.salary)
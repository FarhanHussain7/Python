class Employee:
    company = "google"
    salary = 100
    

harry = Employee()
rajani = Employee()
# creating instance attributes salary for both the object
'''harry.salary = 300 # instance attributes
rajani.salary = 400 # instance attributes
'''
print(harry.salary)
print(rajani.salary)
#print(rajani.address)# this line through an error because address is not present in class 
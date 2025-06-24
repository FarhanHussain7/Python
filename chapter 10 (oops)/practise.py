# creata a class programmer for storing info

'''class Programmer:
    company = "microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product
    def getinfo(self):
        print(f"the name of the programmer is {self.name} and the product is {self.product}")

harry = Programmer("harry", "skype")
alka = Programmer("alka", "github")
harry.getinfo()
alka.getinfo()
'''
# write a class calculator capable of finding spaces , cube , and square number
'''class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"the value of {self.number} square is {self.number **2}")

    def squareroot(self):
        print(f"the value of {self.number} square root is {self.number **0.5}")

    def cube(self):
        print(f"the value of {self.number} cube is {self.number **3}")


a = Calculator(7)
a.square()
a.squareroot()
a.cube()
'''
# write a class with class attribute, 
'''class sample:
    a = "harry"

obj = sample()
obj.a = "viky"
#sample.a = "vikky" ----(attribute) when we want to change name then it can be use and change attribute in instance attribute
print(sample.a)
print(obj.a)
'''
#add a static method in problem 2 to greet the user hello

'''class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"the value of {self.number} square is {self.number **2}")

    def squareroot(self):
        print(f"the value of {self.number} square root is {self.number **0.5}")

    def cube(self):
        print(f"the value of {self.number} cube is {self.number **3}")
    @staticmethod    
    def greet():
        print("*****hello there welcome to the best calculator of the world*****")

a = Calculator(1)
a.greet()
a.square()
a.squareroot()
a.cube()
'''

# write a class train which has methods to book a ticket, get status(no. of sets)and get fare info

'''class Train:
    def __init__(self, name, fare, seats):
        self.name = name 
        self.fare = fare
        self.seats = seats 
    def getstatus(self):
        print("*********")
        print(f"the num of the train is {self.name}")
        print(f"the seats available in the train are {self.seats}")
        print("**********")
        
    def fareInfo(self):
        print(f"the price of the ticket is: rs {self.fare}")
    def bookticket(self):
        if(self.seats>0):
            print(f"your ticket has been booked, your seat number {self.seats}")
            self.seats = self.seats - 1
        else:
            print("sorry train is full, try tatkal")
    def cancleticket(self, seats):
        pass

intercity = Train("intercity express: 1457654", 98, 2)
intercity.getstatus()
intercity.bookticket()
intercity.bookticket()
intercity.bookticket()
intercity.getstatus()
intercity.fareInfo()
'''
# can you change the self parameter inside a class to something else (say 'harry').try change self

class sample:
    def __init__(slf, name):
        slf.name = name
        
obj = sample("harry")
print(obj.name)








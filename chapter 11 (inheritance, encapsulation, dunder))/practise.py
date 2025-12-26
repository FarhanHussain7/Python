#create a class e-2 victor and use it to creta another class representing 3-d vector
'''class C2dvec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"
        

class C3Dvac(C2dvec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v2d = C2dvec(1, 3)
v3d = C3Dvac(1, 9, 7)
print(v2d)
print(v3d)
'''
# create a class pets from aa claas animal 
'''class Animals:
    animalttype =  "mammal"

class pets:
    color = "white"

class dog:
    @staticmethod
    def bark():
        print("bow bow")

d = dog()
d.bark()
'''

# create a class of employee and add salary and increment properties 
'''class Employee:
    salary = 1000
    increment = 1.5
    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sal):
        self.increment = sal/self.salary

e = Employee()
print(e.salaryAfterIncrement)

print(e.increment)
e.salaryAfterIncrement = 2000
print(e.increment)
'''

# write a class complex to represed complex number, along with overload operator + and *
'''class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i
    def __add__(self, c):
        return complex(self.real + c.real, self.imaginary + c.imaginary)
        
    def __mul__(self, c):
        mulReal = self.real*c.real - self.imaginary*c.imaginary
        mulImg = self.real*c.imaginary + self.imaginary*c.real
        return Complex(mulReal, mulImg)
    
    def __str__(self):
        if self.imaginary<0:
            return f"{self.real} - {-self.imaginary}i"
        else:
            return f"{self.real} + {self.imaginary}i"

c1 = Complex(3, 2)
c2 = Complex(1, 7)
print(c1 + c2)
print(c1 * c2)        
'''

# write a class vector representing a vector of n dimension. overload with + and * 
'''class vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]
    
    def __add__(self, vec2):
        newlist = []
        for i in range(len(self.vec)):
            newlist.append(self.vec[i] * vec2.vec[i])
        return vector(newlist)
    
    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum
    
v1 = vector([1, 4, 6])
v2 = vector([1, 6, 9])
print(v1+v2)
print(v1*v2)
'''

# wrie __str__ methods to print the vector as 7i + 8j + 10k
class vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"
       
v1 = vector([1, 4, 6])
v2 = vector([1, 6, 9])
print(v1)
print(v2)

#overide the __len__ () methods on vector of problem 5 to display the dimension of the vector 
class vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]
    
    def __add__(self, vec2):
        newlist = []
        for i in range(len(self.vec)):
            newlist.append(self.vec[i] * vec2.vec[i])
        return vector(newlist)
    
    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum
    
    def __len__(self):
        return len(self.vec)
    
v1 = vector([1, 4, 6])
v2 = vector([1, 6, 9])
print(len(v1))
print(len(v2))









        

    
     
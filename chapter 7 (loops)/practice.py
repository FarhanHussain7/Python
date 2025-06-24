# write a program of multiplication table 

'''num = int(input("enter the number\n"))

for i in range(1, 11):
  #  print(str(num) + "x" + str(i) + "=" + str(i*num))#--> simple string 
     print(f"{num}X{i}={num*i}")#--> F string 
'''

# write a program to greet all the person names stored in l1 and start with S

'''l1 =["harry", "sohan", "sachin", "rahul"]

for name in l1:
     if name.startswith("s"):
          print("hello " + name)
'''
# write program with while loop to print a table
'''num = int(input("ENter the number"))
i = 1
while (i<=10):
     print(str(num) + "x" + str(i) + "=" +str(i*num))
     i = i + 1
'''

# write a program to print a prime number

'''num = int(input("enter the number: "))
prime = True
for i in range(2, num):
     if(num%i == 0 and num!=2):
          prime = False
          break
if prime:
     print("this number is prime")
else:
     print("this number is not prime")
          
'''
# write a program to find the sum of first n natural number using while loop




#write a program to print factorial
# n! = 1 x 2 x 3 x ..........xn
# 5! = 1 x 2 x 3 x 4 x 5
'''
num = int(input("enter the number: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i 
print(f"the factorial of this {num} is {factorial}")
'''

# print the star pattern
'''
n = 4

for i in range(4):
    print("*" * (i+1))
'''
# print a star(*) pyramid structure
n = 8
for i in range(8):
    print(" " * (n-i-1), end="")# '''these three print formula is only for single line
    print("*" * (2*i+1), end="")#--> the (end="") is used to don't print spacing
    print(" " * (n-i-1))
    
# write a program to print the star structure in square formation

for i in range(3):
    print("*")



# write a program  to print a table in reseverse order

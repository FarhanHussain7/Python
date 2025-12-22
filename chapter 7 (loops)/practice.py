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
for i in range(10,1,-2):
    print(i)

# Check given number is prime or not
num = int(input("enter the number: "))
count = 0
for i in range(1, num+1):
    if num % i == 0:
        count = count + 1
if count == 2:
    print("this number is prime")
else:
    print("this number is not prime")

# Print Fibonacci series up to n terms
n = int(input("Enter the number of terms: "))          
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b 

# Find the sum of digits of a number
num = int(input("Enter a number: "))
sum_of_digits = 0
while num > 0:
     digit = num % 10
     sum_of_digits += digit
     num //= 10     
print("Sum of digits:", sum_of_digits)

# Check if a number is palindrome
num = int(input("Enter a number: "))    
original_num = num
reversed_num = 0         
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
if original_num == reversed_num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

# check number is  perfect number 
num = int(input("Enter a number: "))
sum = 0 
for i in range(1,num):
    if num%1 == 0 :
        sum += i 

if sum == num:
    print("Number is perfect number ")
else:
    print("Number is not perfect number ")

# print all the armstrong number between 1 to n
n = int(input("Enter the upper limit: "))   
for num in range(1, n + 1):
    order = len(str(num))
    sum_of_powers = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** order
        temp //= 10
    if sum_of_powers == num:
        print(num)

# print all the digit character in a string and special character
s = input("Enter a string: ")
digits = ""
char = ""
special_characters = ""
for i in s:
    if i.isdigit():
        digits += i
    elif i.isalpha():
        char += i
    else:
        special_characters += i 
    
print("Digits:", digits)
print("Characters:", char)  
print("Special Characters:", special_characters)


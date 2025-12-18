# there are two type of Conversion 
'''
1. Implicit typecasting
 - It is done by language own self

2 - Explicit typecasting
 - It is done by the user
 int()
 float()
 complex()
 str()
 tuple()
 set()
 dict()
 bool()
'''

a = "6774" # a number can be a string if number has doblue comma
a = int(a)# it can change the string into a integer value but it can change only number not the alphabet
print(type(a))
print(a + 6)

# input function
a = input("enter your name: ") # if you put "farhan" the input user print farhan
a = int(a)# if i give any number to input than i have change string into integer(if possible)
print(type(a))
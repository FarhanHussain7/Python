# '''
# autthor: FARHAN
# licencedd to: abc company
# *****thank you******
# '''
# import os # method of comment
# print("hello world")   


# Count nuber of characters in a string
string=input ("enter string: ")
dict={}

for ch in string:
    if ch in dict:
        dict[ ch]+=1
    else:
        dict[ ch]=1
        
print ("your elements :")
for am in dict:
    print("the count of elements ",am," is ",dict[am])

b="A"
print(ord(b))

c=65
print(chr(c))
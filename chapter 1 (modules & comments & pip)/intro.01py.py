# '''
# autthor: FARHAN
# licencedd to: abc company
# *****thank you******
# '''
# import os # method of comment
# print("hello world")   


string=input ("enter string:")
dict={}

for ch in string:
    if ch in dict:
        dict[ ch]+=1
    else:
        dict[ ch]=1
        
print ("your elements :")
for am in dict:
    print("the count of elements",am,"is",dict[am])
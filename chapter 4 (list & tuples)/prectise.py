#write the program to print seven fruits in list
'''f1 = input("enter the fruit number 1: ") 
f2 = input("enter the fruit number 2: ") 
f3 = input("enter the fruit number 3: ") 
f4 = input("enter the fruit number 4: ") 
f5 = input("enter the fruit number 5: ") 
f6 = input("enter the fruit number 6: ") 
f7 = input("enter the fruit number 7: ")'''

#myfruitlist = [f1, f2, f3, f4, f5, f6, f7]
#print(myfruitlist)


# write a program to print the six marks of a student
'''m1 = int(input("enter marks for student number 1: "))
m2 = int(input("enter marks for student number 2: "))
m3 = int(input("enter marks for student number 3: "))
m4 = int(input("enter marks for student number 4: "))
m5 = int(input("enter marks for student number 5: "))
m6 = int(input("enter marks for student number 6: "))

mylist = [m1, m2, m3, m4, m5, m6]
mylist.sort()
print(mylist)'''

#sum a list with 4 numder
'''a = [2,5,66,5]
print(a[0]+a[1]+a[2]+a[3])'''

# count the number of zero in tuples
# a = (7, 0, 8, 0, 0, 9)

# print(a.count(0))

# print the postive and negitive numbers in a list
'''a = [2, -7, 5, -9, 4, -2, 1, -6]
pos = []    
neg = []
for i in a:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)
print("positive numbers are: ", pos)
print("negitive numbers are: ", neg)'''
# write a program to print the sum of all the numbers in a list
'''a = [2, 5, 6, 8, 4]
s = 0
for i in a:
    s = s + i
print("the sum of all the numbers in a list is: ", s)'''

# write a program to print the average of all the numbers in a list
'''a = [2, 5, 6, 8, 4]
s = 0
for i in a:
    s = s + i       
avg = s / len(a)
print("the average of all the numbers in a list is: ", avg)'''

# write a program to print the largest number in a list
'''a = [2, 5, 66, 8, 4]
largest = a[0]
for i in a:
    if i > largest:
        largest = i
print("the largest number in a list is: ", largest)'''

# write a program to print the smallest number in a list
'''a = [2, 5, 66, 8, 4]
smallest = a[0]
for i in a:
    if i < smallest:
        smallest = i    
print("the smallest number in a list is: ", smallest)'''
# write a program to print the second largest number in a list
a = [2, 5, 66, 8, 4]
a.sort()
print("the second largest number in a list is: ", a[-2])
print("the second largest number in a list is: ", a[a.index(max(a))-1])


# write a program to print the second smallest number in a list
'''a = [2, 5, 66, 8, 4]
a.sort()
print("the second smallest number in a list is: ", a[1])'''
# write a program to print the reverse of a list
'''a = [2, 5, 66, 8, 4]
a.reverse()
print("the reverse of a list is: ", a)'''
# write a program to print the list after removing duplicates
'''a = [2, 5, 66, 8, 4, 5, 2, 8]
b = []
for i in a:
    if i not in b:
        b.append(i)     
print("the list after removing duplicates is: ", b)'''


# write a program to print the list after merging two lists
'''a = [2, 5, 66]
b = [8, 4, 5]
c = a + b
print("the list after merging two lists is: ", c)'''
# write a program to print the list after multiplying each element by 2
'''a = [2, 5, 66, 8, 4]
b = []
for i in a:
    b.append(i * 2)
print("the list after multiplying each element by 2 is: ", b)'''

# write a program to print the list after squaring each element
'''a = [2, 5, 66, 8, 4]
b = []
for i in a:
    b.append(i ** 2)
print("the list after squaring each element is: ", b)'''
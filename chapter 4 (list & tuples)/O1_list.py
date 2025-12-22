#create a list using []
a = [1,2,3,4,56,6]
#print the list using rint()function
print(a)

#acces using index using a[0], a[1], a[2]
print(a[2])


#change the value of list using 
a[0] =22
print(a)

#we can create a list with items of different types
c = [66,"farhan",False,6.9]
print(c)


#list slicing
friends = ["farhah","rohit","vikash","deepak",45]
# [start:end-1:step]
print(friends[0:4])
print(friends[-4:]) 


# list methods

l1 = [2,3,56,75,45,89]
#l1.sort()--->> foorr  sorts the list in accending order
#l1.reverse()-->.ffor reversee print
#l1.append(66)-->.useing for adding new number oor vaalue 
#l1.insert(2,444)-->insert 444 at index 2
#l1.pop(3)-->deleteing or poping any value at index 3
l1.remove(56)#--> for removing any value
print(l1)
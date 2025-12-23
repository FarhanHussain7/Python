'''def readfile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"file {filename} is not found")

readfile("1.txt")
readfile("2.txt")
readfile("3.txt")
'''

#write a program to print third, fifth and seventh element from a list using enumerator function

'''l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index, item in enumerate(1):
    if index==2 or index==4 or index==6:
     # print(index, item)
       print(f"the  {index + 1}th element is {item}")
'''
# write a list comprehension to print a list which content the multiplication table of a user enterd
'''num = int(input("enter your number: "))

table = [num*i for i in range(1, 11)]
print(table)'''

# write a program to display a/b where a and b are integer. if b=0, display infinite by handling the zerodivisionerror.

'''a = int(input("enter number a : "))
b = int(input("enter number b : "))

try:
    print(a/b)
except:
    print("infinite")
'''
# store the multiplication table genrated in problem 3 in a file named table.txt
num = int(input("enter your number: "))

table = [num*i for i in range(1, 11)]
print(table)
with open("1tables.txt","a")as f:
    f.write(str(table))
    f.write('\n')
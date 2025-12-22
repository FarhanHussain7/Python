fruits = ['banana', 'watermelon', 'grapes', 'mangos']

#for item in fruits:
 #   print(item)


# range function
# range is used to generate a sequence of numbers 
# range(start, stop, step)
# in range function stop is exclusive and start is inclusive it means it will include start but will not include stop
# step is optional it is used to define the increment value
# by default step is 1
# by default start is 0
# range(1,20,2)
# 1,3,5,7,9,11,13,15,17,19
for i in range(1, 8):
    print(i)

# for loop with else 
for i in range(10): # it can define the number of rows
    print(i)
else:
    print("this is inside else of for")

# input in range 
num = int(input("enter the number: "))

for i in range(1, num+1):
    print(i)

for i in range(10,0,-1):
    print("Reverse loop ", i)

for i in range(-5,-16,-1):
    print(" Negtive value loop ", i)

# Define the range for the multiplication table
rows = 10
columns = 10

# Nested for loop to create the multiplication table
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        # Print the product of i and j, formatted to align the columns
        print(f"{i * j:4}", end=" ")
    # Move to the next line after each row is printed
    print()


# Print a table 
for i in range(5,51,5):
    print(i)

n = int(input("Enter a number to print its multiplication table: "))

for i in range(n,(n*10)+1,n):
    print(i)

# Print char of a String 
string = "HelloWorld"

for i in range(len(string)):
    print(string[i])

for char in range(string):
    print(char)
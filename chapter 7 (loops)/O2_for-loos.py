fruits = ['banana', 'watermelon', 'grapes', 'mangos']

#for item in fruits:
 #   print(item)


# range function

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
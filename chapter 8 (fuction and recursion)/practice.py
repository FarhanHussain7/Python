# write a progam to find the maximum number 
def maximum(num1, num2, num3):
    if (num1>num2):
        if (num1>num3):
            return num1
        else:
            return num3
    else:
        if (num2>num3):
            return num2
        else:
            return num3
m = maximum(88, 45, 67)
print("the value of the maximum is " + str(m))

# write a program to change celceis in fernhiet temprature
def farh(cel):
    return (cel *(9/5)) + 32

c = 0 
f = farh(c)
print("farhreheit temprature is " + str(f))

# write a program to print() fuction in one line output with end

print("hello", end=" ") #--> end is connect the line 
print("how", end=" ")
print("are", end=" ")
print("you", end=" ")

# write a progarm to sum of natural number by useing recursion
'''n! = (n-1)! * n
sum(n) = sum(n-1) + n
'''

#write a program to print a star structure
n = 6
for i in range(n):
    print("*" * (n-i)) 

# write a program to convert the inche in meter 
#later

# 
def remove_and_split(string, word):
    newstr = string.replace(word, "")
    return newstr.strip()

this = "      harry is a good"
n = remove_and_split(this, "harry")
print(n)

# write a ython function to print multiplication table of given number



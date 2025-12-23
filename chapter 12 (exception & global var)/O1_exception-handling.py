# Exception handling in Python 
# try, except, else, finally
# multiple except blocks
# Objective: Learn how to handle exceptions in Python using try, except, else, and finally blocks.
# Exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions.
# Common exceptions include ValueError, TypeError, ZeroDivisionError, etc.
# The try block contains code that might raise an exception.
# The except block contains code that runs if an exception occurs in the try block.

try:
    a = int(input("enter a number: "))
    c = 1/a
    print(c)
except ValueError as e :
    print("please enter a valid number")
    
except ZeroDivisionError as e :
    print("make sure you are not dividung by 0")
    
else:
    print("this code is executed only when there is no exception")
finally:
    print("thanks for using this code")
# finally block is always executed no matter what


# Raising exceptions manually using raise keyword
# Objective: Learn how to raise exceptions manually in Python using the raise keyword.
age = int(input("enter your age: "))

if age < 18 :
    raise ValueError("age cannot be less than 18")
else:
    print("you are eligible to vote")


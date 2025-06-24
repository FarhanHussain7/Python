try:
    a = int(input("enter a number: "))
    c = 1/a
    print(c)
except ValueError as e :
    print("please enter a valid number")
    
except ZeroDivisionError as e :
    print("make sure you are not dividung by 0")
    
print("thanks for using this code")


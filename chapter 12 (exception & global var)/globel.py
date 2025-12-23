# Global variable is a variable that is defined outside of any function and can be accessed from any function within the same module.
# Local variable is a variable that is defined within a function and can only be accessed within that function.

a = 30 #global varieable
def func1():
    global a 
    print(f"print statement 1 : {a}")
    a = 8 #local variable if global keyword is not used
    print(f"print statement 2 : {a}")

func1()
print(f"print statement 3 : {a}")
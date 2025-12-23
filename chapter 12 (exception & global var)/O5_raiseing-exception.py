def Increment(num):
    try:
        return int(num) + 1
    except :
        raise ValueError("this is not good - farhan")
    
a = Increment(333)
print(a)
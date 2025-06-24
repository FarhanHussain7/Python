try:
    i = int(input("enter the number: "))
    c = 1/i
except Exception as e:
    print(e)
else:
    print("we were sucessfull")
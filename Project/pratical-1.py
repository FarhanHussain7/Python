# making a program for a kirana store 
sum = 0
while(True):
    userinput = input("enter the price or press q to quit: \n")
    if (userinput!='q'):
     sum = sum + int(userinput)
     print(f"order total so far {sum}")

    else:
      print("")
      print(f"your bill total is {sum}. thanks for shoppng with us")
      break
    
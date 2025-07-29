'''age = int(input("enter your age: "))
if(age>33 and age>45):# if both true them outcome is true
    print("you can work with us")
else:
    print("you can not work with us")
'''

age = int(input("entr your age :"))
if(age>34 or age>56):# if any one condition is true them outcome will come in true
    print("you can work with us")
else:
    print("you can not work with us")

if(age>18 and age<50):# in this case both condition should be true then it will give resul
    print("Yes he can apply")
elif(age==40):
    print("his age is 40")
else:
    print("not apply")
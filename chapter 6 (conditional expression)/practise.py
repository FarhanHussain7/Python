# wite a program to find greatest f four number 
'''num1 = int(input("enter number 1:"))
num2 = int(input("enter number 2:"))
num3 = int(input("enter number 3:"))
num4 = int(input("enter number 4:"))

if(num1>num4):
    f1 = num1
else:
    f1 = num4
if(num2>num3):
    f2 = num2
else:
    f2 = num3
    if(f1>f2):
        print(str(f1) + "is greatest")
    else:
        print(str(f2) + "is greatest")
'''
# write a program to print student pass or not
'''sub1 = int(input("enter first subject\n"))
sub2 = int(input("enter second subject\n"))
sub3 = int(input("enter third subject\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail because you have less than 33 marks")

elif(sub1+sub2+sub3)/3 <40:
    print("you are fail due to total percentage less than 40")
else:
    print("cngratulation! you passed the exam")
'''
#write a program to find spam text------

'''text  = input("enter the text\n")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("this text is spam")
else:
    print("this text is not spam")
'''
# write a program to find the charecter length-----
'''name = input("enter the name\n")
if(len(name)==10):
    print("true")
else:
    print("false")
'''

# 
'''names = ["rohit", "shiv", "deepak", "viaksh", "jatin" ]
name = input("enter the name to check\n")

if name in names:
    print("your name is present in the list")
else:
    print("your name is not present in the list")
'''

#write a progarm to defin the grade according to it marks

'''marks = int(input("enter your marks\n"))

if marks>=90:
    grade = "EX"
elif marks>=80:
    grade = "a"
elif marks>=70:
    grade = "b"
elif marks>=60:
    grade = "c"
elif marks>=50:
    grade = "d"
else:
    grade = "fail"


print("your grade is " + grade)
'''
#
post = input("enter the post\n")

if "harry" in post:
    print("yes")
elif "HARRY" in post:
    print("yes")
else:
    print("NO")
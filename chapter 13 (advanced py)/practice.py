# create two virtual enviroment , install few packages in the first one. how do you create a similer enviroment in the second one

# write a program to input name, marks and phone number of a student and format it using the format function like below;
'''name = input("enter your name: ")
marks = input("enter your marks: ")
phone = input("enter your phone number: ")

template = "the name of the student is {}, his marks are {}, and phone number is {} "
output = template.format(name, marks, phone)
print(output)'''

# write a list contains the multiplication table of 7 . write a program to convert it to a vertical string of same number(7/14)
'''l = [str(i*7) for i in range(1, 11)]
print(l)

verticaltable = "\n".join(l)
print(verticaltable)
'''
# write a program to filter a list of number which are divisble by 5

'''l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 78, 56, 89, 99, 65]

a = filter(lambda a : a%5==0, l)
print(list(a))
'''
# write a program to find the maximum of the number in a list using the reduce function
'''from functools import reduce
l = [3, 8, 4, 2, 5]

a =reduce(max, l)
print(a)'''

# ran pip freeze for the system interpretor take the contains and create a similar virtualenv.

# explore the flask module and create a web server using flask & python
from flask import Flask 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'HELLO, WORLD!'

if __name__ == "__main__":
    app.run(debug=True)




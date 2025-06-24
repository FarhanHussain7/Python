def percent(marks): # def is a function it can simple put a line which is reptet many time
    p = ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
    return p

marks1 = [45, 56, 78, 88]
percentage1 = percent(marks1)

marks2 = [43, 57, 98, 58]
percentage2 = percent(marks2)
print(percentage1, percentage2)

# example question
def greet(name):
    print("good day, "+ name)


def mysum(num1, num2):
    return num1 + num2

greet("farhan")
s = mysum(12, 67)
print(s)
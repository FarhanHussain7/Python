class number:
    def __init__(self, num):
        self.num = num

    def __mul__(self, num2):
        print("lets multiply")
        return self.num * num2.num

n1 = number(5)
n2 = number(4)
#sum = n1 + n2
mul = n1 * n2
print(sum)   
print(mul)  
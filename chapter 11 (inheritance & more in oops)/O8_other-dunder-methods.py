class Number:
    def __init__(self, num):
        self.num = num

    def __mul__(self, num2):
        print("lets multiply")
        return self.num * num2.num
    
    def __str__(self):# str is a dunder methods(useing for single number)
        return f"decimal number: {self.num}"
    
    def __len__(self):# len function for showing lenght of number
        return 1
        

n = Number(9)
print(n)
print(len(n))
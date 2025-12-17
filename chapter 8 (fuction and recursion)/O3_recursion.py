# n! = 1 * 2 * 3 * ......*n
'''
n = 5
product =  1
for i in range(n):
    product = product * (i+1)
print(product)
'''

def factorial_iter(n):
    product = 1
    for i in range(n):
      product = product * (i+1)
    return product


def factorial_recursive(n):
   if n == 1 or n ==0:
      return 1
   return n * factorial_recursive(n-1)


#f = factorial_iter(5) # In this calling funtion run only for one single time and run for loop inside 
f = factorial_recursive(5) # In this calling function keep calling itself again and again if give parameter is greater than 1
print(f)



    
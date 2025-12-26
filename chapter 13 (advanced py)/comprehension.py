# Comprehension function work with list tuples and set 
# It will used to do complex calculation in single line 

m = [[2,6,4], [7,1,9], [8,5,3]]
#  [num (all value save inside num after runing nested loop )]
flat = [num for row in m for num in row]
flat.sort()
print(flat)  # [1,2,3,4,5,6,7,8,9]

# var(list) =[element(i) ] :- i will save every element with is satisfy the if condition  
list = [i for i in range(1,21) if i%2 == 0]
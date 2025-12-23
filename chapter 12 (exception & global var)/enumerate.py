# Objective: Learn how to use the enumerate function in Python to get index-value pairs from an iterable.
# The enumerate() function adds a counter to an iterable and returns it as an enumerate object.

list1 = [4, 34, 2, False, 6.4, "farhan"]
'''index = 0
for item in list1:
    print(item, index)
    index +=1'''

for index, item in enumerate(list1):
    print(item, index)
a = [3, 4, 3, 7, 8, 2, 9, 8, 4, 2, 5, 7, 9]
'''b = []
for item in a:
    if item%2==0:
        b.append(item)

print(b)'''
# shortcut to write the same
b = [i for i in a if i%2==0]
print(b)
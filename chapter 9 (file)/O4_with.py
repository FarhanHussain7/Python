# with function is close by itself , this function is automatically open and close

with open('another.txt', 'r') as f:# read can help to read file
    a = f.read()

with open('another.txt', 'w') as f:# write function is used write the content 
    a = f.write("me")
print(a)
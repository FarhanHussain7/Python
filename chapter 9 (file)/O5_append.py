# Append is used to add content to the end of the file without overwriting existing content
# It will create the file if it does not exist
# a is mode use to append the content in file

file = open('another.txt', 'a')# open file in append mode
file.write("\nThis line is appended.")# append content to the file  
file.close()
file = open('another.txt', 'r')
content = file.read()   
print(content)
file.close()

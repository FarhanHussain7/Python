a = 34 
b = "farhan's"
#b = 'farhan'---> string cab be easly write in this types also
#b = '''farhan is going 
 # to market today'''
print(a,b)
print(type(b))


greeting = "good morning,"
name = "farhan"
# print(type(name))
#concatenating two string by adding them
c = greeting + name
print(c)

#index framing and slicing string
name = "farhan"
#print(name[0]) for index framing 
#print(name[0:])#  for slicing [0:4] last value is alway e
c = name[-3:-1]
print(c)

#string function
story = '''onc upon a time a boy name is kaif he is a very 
kind guy'''
#print(story[0:]) --> this is example of slicing



# types of string function
print(len(story))# --> first type

print(story.endswith("guy"))#-->Second type(answer is true or false)

print(story.count("o"))#-->third type(counting string and single alphabet)

print(story.capitalize())#-->forth type(use for capital letter to first strating word)
print(story.find("kaif"))#-->fifth type (useing for find the postion number of string)
print(story.replace("kaif","jihan"))#-->sixth type (useing for replaceing the string word)

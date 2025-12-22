# --> dictionary is a key value pair data structure
# --> dictionary is mutable means we can change its values
# --> dictionary is unordered means it does not maintain the order of elements
# --> dictionary is defined by curly braces {}
# example of dictionary

mydict = {
    "fast" : "in a quick manner",
    "harry" : "a coder",
    "marks" : [1,3, 4],
    "anotherdict" : {'harry' : 'player'}
}

print(mydict['fast'])
print(mydict['harry'])
mydict['marks'] = [43, 65]#-->it can change esily
print(mydict['marks'])

print(mydict['anotherdict']['harry'])
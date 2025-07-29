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
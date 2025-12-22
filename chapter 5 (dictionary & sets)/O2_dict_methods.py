mydict = {
    "fast" : "in a quick manner",
    "harry" : "a coder",
    "marks" : [1,3, 4],
    "anotherdict" : {'harry' : 'player'},
    1 : 2
}

#there are four type of methods of dictionary

# first methods
print(mydict.keys())#-->keys is methods of dictionary
print(type(mydict.keys()))
print(list(mydict.keys()))
print(list(mydict.values()))#-->Values is also a method

# second methods
print(mydict.items())#-> it can print (key , values) for all the content of the dictionary

#third methods
# update the dictionary by adding keys,values pairs  from updatedict
updatedict = {
    "deepak" : "vikash",
    "rohit" : "friend"
}
mydict.update(updatedict)

print(mydict)  
# fourth methods
print(mydict.get("harry"))
print(mydict["harry"])
# example for showing differnerce btw .get and [] syntax methods
print(mydict.get("harry2"))#-->if harry2 is not present in dictionary then he print none
print(mydict["harry2"])#-->but in case if harry2 is not present in dictionary then this give an error

for i in mydict.values():
    print(i) #--> it will print all the keys of dictionary

# create a dictionary from two lists
d1 = {10:100, 20:200, 30:300}
d2 = {40:400, 50:500, 60:600}

for i in d2.items():
    d1[i] = d2[i]

print(d1)
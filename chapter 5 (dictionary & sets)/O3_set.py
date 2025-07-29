a = {1, 3, 4, 5, 1,}#--> sets is a collection of non-repetitive elements

print(type(a))
print(a)

#important - this syntax will create an empty dictionary and not an empty set
b = {} #--> this is a empty dictionary
print(type(b))

c = set()#-->this is a syntax of printing empty set
print(type(c))

#adding values in an empty set
c.add(4)
c.add(5)
#if user add same value then set wil ignor them because it cannot print repetitive value 
c.add(4)
c.add(5)
#c.add([4, 5, 6])-->list can change its value so it cannot works in sets
#c.add({4, 5, 6})-->dictionary also change it values and keys so it cannot suitable for sets
c.add((4, 5, 6))#-->tupels are not changed after assign so it can works in sets

print(c)

# methods of sets 
#first methods
print(len(c))
# second
c.remove(5)# rmeove 5 from set c
#c.remove(15)# when 15 is not present in set c then it gives error
print(c)

# third methods
print(c.pop())
print(c)


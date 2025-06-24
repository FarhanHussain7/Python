# use open function to read the content of file 
f = open('sample.txt', 'r')
data = f.read(5)# how many charecter are read
print(data)
f.close()
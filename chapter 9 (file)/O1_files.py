# use open function to read the content of file 
f = open('python/chapter 9 (file)/sample.txt', 'r')
data = f.read()# Read all content of file
print(data)
f.close()


f = open('python/chapter 9 (file)/sample.txt', 'r')
data = f.read(5)# how many charecter are read
print(data)
f.close()
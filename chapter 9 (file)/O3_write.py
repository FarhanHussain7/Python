# Write content to a file using write() function 
# w is mode use to write the content in file
# write will overwrite the existing content in the file


f = open('another.txt', 'w')# open() function create a new text file with name another.txt
f.write("please write this to the file")# cntent save in another.txt file
f.close()

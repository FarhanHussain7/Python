# print a program with input function
'''name = input("enter your name\n")
print("good afternoon, "+ name)'''

# program for letter templates
letter = '''dear <|name|>,
greeting from abc company
you are selected!

date:<|date|>
'''
name = input("enter your name\n")
date = input("enter date\n")
letter = letter.replace("<|name|>", name)
letter = letter.replace("<|date|>", date)
#print(letter)

# detect the double spacing
st = "this is a string with double  spacing "
#doublespace = st.find("  ")
#print(doublespace)

# replacing double space with single spaces

st = st.replace("  "," ")
print(st)


# write a letter by escape squence

letter = "dear sir. i m very happy today ! thanks"
print(letter)
format_letter = "dear sir.\n\t i\'m very happy today !\n thanks"
print(format_letter) 
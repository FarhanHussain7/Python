#
'''
f = open('poem.txt')
t = f.read()
if 'twinkle' in t:
    print("twinkle is present")
else:
    print("twinkle is not present")
f.close()
'''

#
'''def game():
    return 67
score = game()
with open('hiscore.txt') as f:
    hiscorestr = f.read()
if hiscorestr=='':
    with open('hiscore.txt', "w") as f:   
        f.write(str(score))
elif int(hiscorestr)<score:
    with open('hiscore.txt', "w") as f:   
        f.write(str(score))
'''


#
'''for i in range(2, 21):
    with  open(f"tables/multiplication_table_of_{i}", "w") as f:
      for j in range(1, 11):
        f.write(f"{i}x{j}={i*j}\n")
        
'''

#
'''with open("sample.txt") as f:
    content = f.read()

content = content.replace("donkey", "$%@$^#")

with open("sample.txt", "w") as f:
     f.write(content)
'''
#
 


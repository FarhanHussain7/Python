# we are going to write a program to genrates a random number and ask the user to guses it ?
import random
randnumber = random.randint(1, 100)
#print(randnumber)

userguess = None
guesses = 0

while(userguess != randnumber):
    userguess = int(input("enter your guess: "))
    guesses +=1
    if(userguess==randnumber):
        print("you guessed it right!")
    else:
        if(userguess>randnumber):
            print("you guessed it wrong! enter a smaller number")
        else:
            print("you guessed it wrong! enter a larger number")

print(f"you guessed the number in {guesses} guesses")
with open("hiscore1.txt", "r") as f:
    hiscore1 = int(f.read())

if(guesses<hiscore1):
    print("you have just broken the high score!")
    with open("hiscore1.txt", "w") as f:
        f.write(str(guesses))

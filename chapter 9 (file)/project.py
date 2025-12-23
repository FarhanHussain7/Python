
from pathlib import Path


def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items} ")


def createfile():
    try:
        readfileandfolder()
        name = input("Please tell you file name : ")
        p = Path(name)
        if not p.exists():
            with open(p,'w') as fs:
                data = input("Write your Message in file : ")
                fs.write(data)

                print(f"FILE CREATED SUCCESSFULLY")
        else:
            print("this file already exists")
    except Exception as err:
        print(f"An error occured as {err}")


def readfile():
    try:
        readfileandfolder()
        name = input("Which file you want to read ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            
            print("Readed Successfully")
    except Exception as err:
        print("An Error occred ", err)

           


print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")


check = int(input("Enter your Choice : "))

if check == 1:
    createfile()
elif check ==2:
    readfile()

else:
    print("enter a valid choice")

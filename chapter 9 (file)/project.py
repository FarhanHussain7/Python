
from pathlib import Path
import os

# def readfileandfolder():
#     path = Path('')
#     items = list(path.rglob('*'))
#     for i, items in enumerate(items):
#         print(f"{i+1} : {items} ")

# def readfileandfolder():
#     path = Path(r"C:\Users\HP\New folder\python\chapter 9 (file)")
#     items = list(path.rglob('*'))   # recursive
#     for i, item in enumerate(items, start=1):
#         print(f"{i} : {item}")


from pathlib import Path
import os

def readfileandfolder():
    # Explicitly set the path to your "chapter 9 (file)" directory
    path = Path(r"C:\Users\HP\New folder\python\chapter 9 (file)")
    
    # List only files/folders inside this directory
    items = list(path.iterdir())   # use iterdir() instead of rglob('*') for non-recursive
    for i, item in enumerate(items, start=1):
        print(f"{i} : {item}")

from pathlib import Path

def createfile():
    try:
        readfileandfolder()
        name = input("Please tell your file name : ")

        # Prevent user from escaping the folder
        if "\\" in name or "/" in name:
            print("❌ Invalid file name. Do not include paths.")
            return

        base_path = Path(r"C:\Users\HP\New folder\python\chapter 9 (file)")
        p = base_path / name

        if not p.exists():
            with open(p, 'w') as fs:
                data = input("Write your Message in file : ")
                fs.write(data)
            print("============= FILE CREATED SUCCESSFULLY =============")
        else:
            print("⚠️ This file already exists")
    except Exception as err:
        print(f"An error occurred: {err}")

def readfile():
    try:
        readfileandfolder()
        name = input("Which file you want to read ")
        p = Path(r"C:\Users\HP\New folder\python\chapter 9 (file)")/name
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            
            print("========== Readed Successfully ===============")
    except Exception as err:
        print("An Error occred ", err)


def updatefile():
    try:
        readfileandfolder()
        name = input("tell me which file you want to update ")
        p = Path(r"C:\Users\HP\New folder\python\chapter 9 (file)")/name
        if p.exists() and p.is_file():
            print("Press 1 for change the name of the file : -")
            print("Press 2 for overwriting the data of your file :- ")
            print("Press 3 for appending content of your file :- ")

            res = int(input("Enter your response: -"))
            if res == 1:
                name2 = input("Name of your file :- ")
                p2 = p.parent / name2
                p.rename(p2)

            if res == 2:
                with open(p, 'w') as fs:
                    data = input("Write your overwrite data :- ")
                    fs.write(data)

            if res == 3:
                with open(p, 'a') as fs:
                    data = input("Write your append data :- ")
                    fs.write(data)
        else:
            print("File not exists")

        print(" ============= UPDATE SUCCESSFULLY ===============")
    except Exception as err:
        print("An error occur ", err)
        
def deletefile():
    try:
        readfileandfolder()
        name = input("Which file you want to delete : ")
        p = Path(r"C:\Users\HP\New folder\python\chapter 9 (file)")/name
        if p.exists() and p.is_file():
            os.remove(p)
        else:
            print("File not Exists")
        
        print("============ DELETE SUCCEFULLY ==============")
    except Exception as err:
        print("An error occur ", err)
 
flag = True
while(flag):
        
    print("Press 1 for creating a file")
    print("Press 2 for reading a file")
    print("Press 3 for updating a file")
    print("Press 4 for deleting a file")
    print("press 5 for exit ")


    try:
        check = int(input("Enter your Choice : "))
    except ValueError:
        print("❌ Please enter a number between 1–5")
        continue

    if check == 1:
        createfile()
    elif check == 2:
        readfile()
    elif check == 3:
        updatefile()
    elif check == 4:
        deletefile()
    elif check == 5:
        flag = False
    else:
        print("Enter a valid choice")

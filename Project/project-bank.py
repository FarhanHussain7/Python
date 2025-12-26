import json
import random
import string
from pathlib import Path

class Bank:
    database = 'python/Project/data.json'
    data = []

    @classmethod
    def load_data(cls):
        """Load existing accounts from file into cls.data"""
        db_path = Path(cls.database)
        if db_path.exists():
            try:
                with db_path.open('r', encoding='utf-8') as fs:
                    cls.data = json.load(fs)
                    if not isinstance(cls.data, list):
                        cls.data = []
            except json.JSONDecodeError:
                cls.data = []
        else:
            cls.data = []

    @classmethod
    def __update(cls):
        """Write all accounts back to file"""
        Path(cls.database).parent.mkdir(parents=True, exist_ok=True)
        with open(cls.database, 'w', encoding='utf-8') as fs:
            json.dump(cls.data, fs, ensure_ascii=False, indent=2)

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        token = alpha + num + spchar
        random.shuffle(token)
        return "".join(token)

    def __init__(self):
        Bank.load_data()   # load previous accounts when object is created

    def Createaccount(self):
        info = {
            "name": input("Enter your name :- "),
            "age": int(input("Enter your age :- ")),
            "email": input("Enter your email :- "),
            "pin": int(input("Enter your PIN :- ")),
            "accountNo": Bank.__accountgenerate(),  # cleaner key name
            "balance": 0
        }
        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry! You cannot create your account")
            return

        print("Account has been created successfully")
        for k, v in info.items():
            print(f"{k} : {v}")
        print("Please remember your account number")

        # Append new account to existing list
        Bank.data.append(info)
        Bank.__update()

    def depositemoney(self):
        account_number = input("Enter your account number :- ")
        pin = int(input("Enter your PIN :- "))
        amount = int(input("Enter amount to deposit :- "))

        # Find matching account
        for customer in Bank.data:
            if customer.get("accountNo") == account_number and customer.get("pin") == pin:
                if amount <= 0:
                    print("Deposit amount must be positive.")
                    return
                customer["balance"] += amount
                Bank.__update()
                print(f"Deposited {amount}. New balance: {customer['balance']}")
                return

        print("Invalid account number or PIN.")

# --- Menu driver ---
if __name__ == "__main__":
    user = Bank()
    print("press 1 for creating an account")
    print("press 2 for depositing the money in the bank")
    print("press 3 for withdrawing the money")
    print("press 4 for details")
    print("press 5 for updating the details")
    print("press 6 for deleting your account")

    try:
        check = int(input("Enter your choice :- "))
    except ValueError:
        print("Invalid choice.")
    else:
        if check == 1:
            user.Createaccount()
        elif check == 2:
            user.depositemoney()
        else:
            print("Option not implemented yet.")

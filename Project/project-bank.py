import json
import random
import string
from pathlib import Path


class Bank:
    database = 'python/Project/data.json'
    data = []

    # ---------------- Utility Methods ----------------
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
        """Generate random account number"""
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        token = alpha + num + spchar
        random.shuffle(token)
        return "".join(token)

    def __init__(self):
        Bank.load_data()   # load previous accounts when object is created

    # ---------------- Account Operations ----------------
    def create_account(self):
        try:
            info = {
                "name": input("Enter your name :- "),
                "age": int(input("Enter your age :- ")),
                "email": input("Enter your email :- "),
                "pin": int(input("Enter your PIN (4 digits) :- ")),
                "accountNo": Bank.__accountgenerate(),
                "balance": 0
            }
        except ValueError:
            print("Invalid input. Please enter numeric values for age and PIN.")
            return

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry! You cannot create your account (must be 18+ and PIN must be 4 digits).")
            return

        print("\n✅ Account has been created successfully")
        for k, v in info.items():
            print(f"{k} : {v}")
        print("⚠️ Please remember your account number\n")

        Bank.data.append(info)
        Bank.__update()

    def deposit_money(self):
        accnumber = input("Enter your account number :- ")
        try:
            pin = int(input("Enter your PIN :- "))
            amount = int(input("Enter amount to deposit :- "))
        except ValueError:
            print("Invalid input. PIN and amount must be numbers.")
            return

        for customer in Bank.data:
            if customer.get("accountNo") == accnumber and customer.get("pin") == pin:
                if amount <= 0 or amount > 20000:
                    print("Deposit amount must be between 1 and 20000.")
                    return
                customer["balance"] += amount
                Bank.__update()
                print(f"✅ Deposited {amount}. New balance: {customer['balance']}")
                return

        print("❌ Invalid account number or PIN.")

    def withdraw_money(self):
        accnumber = input("Enter your account number :- ")
        try:
            pin = int(input("Enter your PIN :- "))
        except ValueError:
            print("Invalid PIN format.")
            return

        userData = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userData:
            print("❌ No account found.")
            return

        try:
            amount = int(input("Enter withdrawal amount :- "))
        except ValueError:
            print("Invalid amount.")
            return

        if amount > userData[0]['balance']:
            print("❌ Insufficient balance.")
        else:
            userData[0]['balance'] -= amount
            Bank.__update()
            print(f"✅ Withdrawn {amount}. Remaining balance: {userData[0]['balance']}")

    def show_details(self):
        accnumber = input("Enter your account number :- ")
        try:
            pin = int(input("Enter your PIN :- "))
        except ValueError:
            print("Invalid PIN format.")
            return

        userData = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userData:
            print("❌ No account found.")
            return

        print("\n📋 Account Details:")
        for k, v in userData[0].items():
            print(f"{k} : {v}")

    def update_details(self):
        accnumber = input("Enter your account number :- ")
        try:
            pin = int(input("Enter your PIN :- "))
        except ValueError:
            print("Invalid PIN format.")
            return

        userData = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userData:
            print("❌ No account found.")
            return

        print("\nAge, account number and Balance cannot be changed.")
        print("Fill your details or leave blank to keep old values.")

        newdata = {
            "name": input("Enter new name or press Enter: "),
            "email": input("Enter new email or press Enter: "),
            "pin": input("Enter new PIN or press Enter: ")
        }

        if newdata['name'] == "":
            newdata["name"] = userData[0]['name']
        if newdata['email'] == "":
            newdata['email'] = userData[0]['email']
        if newdata['pin'] == "":
            newdata["pin"] = userData[0]['pin']
        else:
            try:
                newdata['pin'] = int(newdata['pin'])
            except ValueError:
                print("Invalid PIN format. Keeping old PIN.")
                newdata['pin'] = userData[0]['pin']

        newdata['age'] = userData[0]['age']
        newdata['accountNo'] = userData[0]['accountNo']
        newdata['balance'] = userData[0]['balance']

        userData[0].update(newdata)
        Bank.__update()
        print("✅ Details updated successfully.")

    def delete_account(self):
        accnumber = input("Enter your account number :- ")
        try:
            pin = int(input("Enter your PIN :- "))
        except ValueError:
            print("Invalid PIN format.")
            return

        userData = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userData:
            print("❌ No account found.")
            return

        check = input("Press Y to confirm deletion or N to cancel: ").lower()
        if check == 'y':
            Bank.data.remove(userData[0])
            Bank.__update()
            print("✅ Account deleted successfully.")
        else:
            print("❌ Deletion cancelled.")


# ---------------- Menu Driver ----------------
if __name__ == "__main__":
    user = Bank()
    options = {
        1: user.create_account,
        2: user.deposit_money,
        3: user.withdraw_money,
        4: user.show_details,
        5: user.update_details,
        6: user.delete_account
    }

    while True:
        print("\n--- Bank Menu ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Show Account Details")
        print("5. Update Account Details")
        print("6. Delete Account")
        print("q. Quit")

        choice = input("Enter your choice :- ").strip().lower()

        if choice == 'q':
            print("👋 Exiting... Thank you for using the Bank system.")
            break

        try:
            choice = int(choice)
            action = options.get(choice)
            if action:
                action()
            else:
                print("❌ Invalid option.")
        except ValueError:
            print("❌ Invalid choice. Please enter a number or 'q' to quit.")
import json
import random
import string
from pathlib import Path
import streamlit as st


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
        Bank.load_data()


# ---------------- Streamlit UI ----------------
def main():
    st.title("🏦 Simple Bank System")
    st.sidebar.title("Menu")
    choice = st.sidebar.radio(
        "Select an option",
        ["Create Account", "Deposit Money", "Withdraw Money",
         "Show Account Details", "Update Account Details", "Delete Account"]
    )

    bank = Bank()

    if choice == "Create Account":
        st.subheader("Create a New Account")
        name = st.text_input("Enter your name")
        age = st.number_input("Enter your age", min_value=0, step=1)
        email = st.text_input("Enter your email")
        pin = st.text_input("Enter your PIN (4 digits)", type="password")

        if st.button("Create Account"):
            if age < 18 or len(pin) != 4 or not pin.isdigit():
                st.error("Must be 18+ and PIN must be 4 digits.")
            else:
                info = {
                    "name": name,
                    "age": age,
                    "email": email,
                    "pin": int(pin),
                    "accountNo": Bank.__accountgenerate(),
                    "balance": 0
                }
                Bank.data.append(info)
                Bank.__update()
                st.success("Account created successfully!")
                st.json(info)

    elif choice == "Deposit Money":
        st.subheader("Deposit Money")
        accnumber = st.text_input("Enter your account number")
        pin = st.text_input("Enter your PIN", type="password")
        amount = st.number_input("Enter amount to deposit", min_value=1, max_value=20000)

        if st.button("Deposit"):
            for customer in Bank.data:
                if customer["accountNo"] == accnumber and customer["pin"] == int(pin):
                    customer["balance"] += amount
                    Bank.__update()
                    st.success(f"Deposited {amount}. New balance: {customer['balance']}")
                    break
            else:
                st.error("Invalid account number or PIN.")

    elif choice == "Withdraw Money":
        st.subheader("Withdraw Money")
        accnumber = st.text_input("Enter your account number")
        pin = st.text_input("Enter your PIN", type="password")
        amount = st.number_input("Enter withdrawal amount", min_value=1)

        if st.button("Withdraw"):
            for customer in Bank.data:
                if customer["accountNo"] == accnumber and customer["pin"] == int(pin):
                    if amount > customer["balance"]:
                        st.error("Insufficient balance.")
                    else:
                        customer["balance"] -= amount
                        Bank.__update()
                        st.success(f"Withdrawn {amount}. Remaining balance: {customer['balance']}")
                    break
            else:
                st.error("Invalid account number or PIN.")

    elif choice == "Show Account Details":
        st.subheader("Account Details")
        accnumber = st.text_input("Enter your account number")
        pin = st.text_input("Enter your PIN", type="password")

        if st.button("Show"):
            for customer in Bank.data:
                if customer["accountNo"] == accnumber and customer["pin"] == int(pin):
                    st.json(customer)
                    break
            else:
                st.error("No account found.")

    elif choice == "Update Account Details":
        st.subheader("Update Account Details")
        accnumber = st.text_input("Enter your account number")
        pin = st.text_input("Enter your PIN", type="password")

        if st.button("Fetch Account"):
            for customer in Bank.data:
                if customer["accountNo"] == accnumber and customer["pin"] == int(pin):
                    st.write("Age, account number and balance cannot be changed.")
                    new_name = st.text_input("Enter new name", value=customer["name"])
                    new_email = st.text_input("Enter new email", value=customer["email"])
                    new_pin = st.text_input("Enter new PIN (4 digits)", value=str(customer["pin"]))

                    if st.button("Update"):
                        if new_pin.isdigit() and len(new_pin) == 4:
                            customer["name"] = new_name
                            customer["email"] = new_email
                            customer["pin"] = int(new_pin)
                            Bank.__update()
                            st.success("Details updated successfully.")
                        else:
                            st.error("PIN must be 4 digits.")
                    break
            else:
                st.error("No account found.")

    elif choice == "Delete Account":
        st.subheader("Delete Account")
        accnumber = st.text_input("Enter your account number")
        pin = st.text_input("Enter your PIN", type="password")

        if st.button("Delete"):
            for customer in Bank.data:
                if customer["accountNo"] == accnumber and customer["pin"] == int(pin):
                    Bank.data.remove(customer)
                    Bank.__update()
                    st.success("Account deleted successfully.")
                    break
            else:
                st.error("No account found.")


if __name__ == "__main__":
    main()

# Do this to run this project 
# (.venv) PS C:\Users\HP\New folder\python\project> streamlit run bank_app.py
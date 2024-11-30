def load_accounts():
    accounts = {}
    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                account_number, pin, balance = line.strip().split("|")
                accounts[account_number] = {"pin": pin, "balance": float(balance)}
    except FileNotFoundError:
        print("Error: accounts.txt not found.")
    except Exception as e:
        print(f"Unexpected error while loading accounts: {e}")
    return accounts

def save_accounts(accounts):
    try:
        with open('accounts.txt', 'w') as file:
            for account_number, data in accounts.items():
                file.write(f"{account_number}|{data['pin']}|{data['balance']}\n")
    except Exception as e:
        print(f"Unexpected error while saving accounts: {e}")


def authenticate(accounts):
    account_number = input("Enter account number: ")
    pin = input("Enter PIN: ")
    if account_number in accounts and accounts[account_number]["pin"] == pin:
        return account_number
    else:
        print("Invalid account number or PIN.")
        return None

def check_balance(account_number, accounts):
    try:
        return accounts[account_number]["balance"]
    except KeyError:
        print("Error: Account not found.")
        return None

def deposit(account_number, accounts):
    try:
        amount = float(input("Enter deposit amount: "))
        accounts[account_number]["balance"] += amount
        save_accounts(accounts)
    except ValueError:
        print("Invalid deposit amount. Please enter a valid number.")
    except KeyError:
        print("Error: Account not found.")
    except Exception as e:
        print(f"Unexpected error during deposit: {e}")

def withdraw(account_number, accounts):
    try:
        amount = float(input("Enter withdrawal amount: "))
        balance = accounts[account_number]["balance"]
        if amount <= balance:
            accounts[account_number]["balance"] -= amount
            save_accounts(accounts)
        else:
            print("Insufficient funds.")
    except ValueError:
        print("Invalid withdrawal amount. Please enter a valid number.")
    except KeyError:
        print("Error: Account not found.")
    except Exception as e:
        print(f"Unexpected error during withdrawal: {e}")

def change_pin(account_number, accounts):
    try:
        new_pin = input("Enter the new pin: ")

        if not new_pin.isdigit() or len(new_pin) != 4:
            print("Error: PIN must be a 4-digit number.")
            return
        
        accounts[account_number]['pin'] = new_pin
        save_accounts(accounts)
        print("PIN successfully updated.")
    except Exception as e:
        print(f"Unexpected error while changing PIN: {e}")


def create_account(accounts):
    try:
        account_number = input("Enter a new account number:")
        if not account_number.isdigit() or len(account_number) != 5:
            print("Error: account number must be a 5-digit number.")
            return
        
        if account_number in accounts:
            print("Error: Account number already exists.")
            return
        
        pin = input("Enter a 4-digit PIN: ")
        if not pin.isdigit() or len(pin) != 4:
            print("Error: PIN must be a 4-digit number.")
            return
        initial_balance = 0
        accounts[account_number] = {"pin": pin, "balance": initial_balance}
        save_accounts(accounts)
        print(f"Account {account_number} successfully created.")
    except Exception as e:
        print(f"Unexpected error while creating account: {e}")

accounts = load_accounts()
print(accounts)
account_number = authenticate(accounts)

if account_number:
    while True:
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change Pin")
        print("5. Create Account")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
                print(f"Balance: {check_balance(account_number, accounts)}")
        elif choice == "2":
            deposit(account_number, accounts)
        elif choice == "3":
            withdraw(account_number, accounts)
        elif choice == "4":
            change_pin(account_number, accounts)
        elif choice == "5":
            create_account(accounts)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

else:
    print("authentification failed.")



def show_balance(balance):
    print(f"Current balance {balance}")

def deposit(balance):
    amount = input("Enter amount to deposit: ")
    return print("Current Balance $:", balance + float(amount))

def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    return print("Current Balance $:", balance + float(amount))

def logout(name):
    print(f"Goodby {name}")
    

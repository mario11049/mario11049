balances =[]
def deposit(amount):
    with open("money.txt", "r") as file:
        balance = int(file.read())
    balance += amount
    with open("money.txt", "w") as file:
        file.write(str(balance))
    print(f"₹{amount} recieved successfully!!!")
def withdraw(amount):
    with open("money.txt", "r") as file:
        balance = int(file.read())
        if balance < amount:
            print("insufficient balance!!!")
        else:
            with open("money.txt", "w") as file:
                balance -= amount
                file.write(str(balance))
            print(f"${amount} withdrawn successfully!!!")
def check_balance():
    with open("money.txt", "r") as file:
        balance = int(file.read())
    print(f"your current balance is: ${balance}")
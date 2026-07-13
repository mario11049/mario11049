from bank import deposit, withdraw, check_balance
def main():
    while True:
       print("=" * 25)
       print("welcome to our bank!!!")
       print("=" * 25)
       print("selcect choice")
       print("1.fetch balance")
       print("2.deposite money")
       print("3.wihdraw money")
       print("4.exit")
       choice = int(input("enter your choice(1-4): "))

       if choice == 1:
            check_balance()
       elif choice == 2:
           amount = int(input("entert the amount you need to deposite: "))
           deposit(amount)
       elif choice == 3:
            amount = int(input("entert the amount you need to withdraw: "))
            withdraw(amount)
       elif choice == 4:       
           print("=" * 30)
           print("Thanks or using our bank!!!")
           print("=" * 30)
           break
       else:
           print("invalid choice!!!")
           
     
if __name__ == "__main__":
    main()

class bank:
    def __init__(self, amount):
        self._amount = None
        self.amount = amount
        print(f"amount is {self.amount}")
    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self, amount):
        if amount < 0:
            raise ("amount not sufficient!!")
        self._amount = amount
def main():
    bank = get_amount()
def get_amount():
    amount = int(input("enter the amount: "))
    return bank(amount)
if __name__ == "__main__":
    main()
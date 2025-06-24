class BankAccount:
    def __init__(self):
        self.__balance = 0  # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount()
acc.deposit(1000)
print("Balance:", acc.get_balance())

# OR simply you can do like this
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

a1 = BankAccount(1000)
print(a1.get_balance())


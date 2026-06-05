class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)

account.deposit(500)
account.withdraw(200)

print("Current Balance:", account.get_balance())

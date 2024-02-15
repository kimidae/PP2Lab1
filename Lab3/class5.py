class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited amount {amount} to the account. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew amount {amount} from the account. Current balance: {self.balance}")
        else:
            print("Insufficient funds")

account = BankAccount("Siller", 0)
account.deposit(1000)
account.withdraw(500)
account.withdraw(1000)

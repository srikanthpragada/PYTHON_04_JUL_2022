class Account:
    minbal = 10000

    @staticmethod
    def getminbal():
        return Account.minbal

    # Constructor
    def __init__(self, acno, ahname):
        # Object Attributes
        self.acno = acno
        self.ahname = ahname
        self.balance = 0

    # Methods
    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - Account.minbal >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds!")


a1 = Account(1, "Larry")
a1.deposit(10000)
a1.withdraw(5000)
print(a1.get_balance())


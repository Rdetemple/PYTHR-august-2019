class BankAccount:
    interest_rate = 0.01
    accounts = []

    def __init__(self):
        '''Important message '''
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print('Get a job!')
        else:
            self.balance -= amount

    @classmethod
    def create(cls):
        b = cls()
        __class__.accounts.append(b)
        return b

    @classmethod
    def total_funds(cls):
        total = 0
        for account in cls.accounts:
            total += account.balance
        return total

    @classmethod
    def add_interest(cls):
        total = 0
        for account in cls.accounts:
            account.balance = account.balance + (account.balance * cls.interest_rate)
                # balance + (balance * 0.01)

def main():

    my_account = BankAccount.create()
    your_account = BankAccount.create()
    print(my_account.balance) #==> 0
    print(BankAccount.total_funds()) #==> 0
    my_account.deposit(200)
    your_account.deposit(1000)
    print(my_account.balance) #==> 200
    print(your_account.balance) #==> 1000
    print(BankAccount.total_funds()) #==> 1200
    BankAccount.add_interest()
    print(my_account.balance) #==> 202.0
    print(your_account.balance) #==> 1010.0
    print(BankAccount.total_funds()) #==> 1212.0
    my_account.withdraw(50)
    print(my_account.balance) #==> 152.0
    print(BankAccount.total_funds()) #==> 1162.0


main()

class vampire:

    coven = []

    def __init__(self):
        '''Important message '''
        self.drank_blood_today = False
        self.in_coffin = False

    def drink_blood(self):
        self.drank_blood_today = True

    def go_home(self):
        self.in_coffin = True

    @classmethod
    def create(cls):
        b = cls()
        __class__.coven.append(b)
        return b

    @classmethod
    def sunrise(cls):
        for vampire in cls.coven:
            if not vampire.drank_blood_today or not vampire.in_coffin:
                cls.coven.remove(vampire)

    @classmethod
    def sunset(cls):
        for vampire in cls.coven:
            vampire.in_coffin = False
            vampire.drank_blood_today = False
def main():

    vampire1 = vampire.create()
    vampire2 = vampire.create()
    vampire1.drink_blood()
    vampire2.drink_blood()
    vampire1.go_home()
    vampire.sunrise()
    print(len(vampire.coven))
    vampire.sunset()
    vampire1.go_home()
    vampire.sunrise()
    print(len(vampire.coven))



    # # print(my_account.balance) #==> 0
    # # print(BankAccount.total_funds()) #==> 0
    # my_account.deposit(200)
    # your_account.deposit(1000)
    # print(my_account.balance) #==> 200
    # print(your_account.balance) #==> 1000
    # print(BankAccount.total_funds()) #==> 1200
    # BankAccount.add_interest()
    # print(my_account.balance) #==> 202.0
    # print(your_account.balance) #==> 1010.0
    # print(BankAccount.total_funds()) #==> 1212.0
    # my_account.withdraw(50)
    # print(my_account.balance) #==> 152.0
    # print(BankAccount.total_funds()) #==> 1162.0
    #

main()

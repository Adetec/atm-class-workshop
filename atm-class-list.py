class ATM:
    def __init__(self, bank_name, balance):
        self.bank_name = bank_name
        self.balance = balance
        self.withdrawals_list = []

    def get_current_balance(self):
        print("Current balance = " + str(self.balance))

    def give_money(self, request):
        notes = [100, 50, 10, 5]
        for note in notes:
            while request >= note:
                request -= note
                print("give " + str(note))
        if request % 5 != 0:
            print('give ' + str(request) + ' pieces')
            request = 0

    def get_new_balance(self):
        print("new balance: " + str(self.balance))

    def withdraw(self, request):

        self.get_current_balance()

        if request > self.balance:
            print("Can't give you all this money !!")

        elif request < 0:
            print("More than zero plz!")

        else:
            self.withdrawals_list.append(request)
            self.balance -= request
            self.give_money(request)
            self.get_new_balance()

        return self.balance

    def show_withdrawals(self):
        for withdrawal in self.withdrawals_list:
            print("withdrawal: " + str(withdrawal))


balance1 = 500
balance2 = 1000

atm1 = ATM("Smart Bank", balance1)
atm2 = ATM("Baraka Bank", balance2)

atm1.withdraw(700)
atm1.withdraw(300)

atm2.withdraw(500)
atm2.withdraw(250)

atm2.show_withdrawals()

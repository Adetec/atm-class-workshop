class ATM:
    def __init__(self, bank_name, balance):
        self.bank_bame = bank_name
        self.balance = balance

    def withdraw(self, request):
        print("Current balance = ", self.balance)
        result = self.balance

        if request > self.balance:
            print("Can't give you all this money !!")

        elif request < 0:
            print("More than zero plz!")

        else:
            while request > 0:

                if request >= 100:
                    request -= 100
                    print("give 100")

                elif request >= 50:
                    request -= 50
                    print("give 50")

                elif request >= 10:
                    request -= 10
                    print("give 10")

                elif request >= 5:
                    request -= 5
                    print("give 5")

                elif request < 5:
                    print("give " + str(request))
                    request = 0

            result = self.balance - request

        return result


balance1 = 500
balance2 = 1000

atm1 = ATM("Smart Bank", balance1)
atm2 = ATM("Baraka Bank", balance2)

atm1.withdraw(700)
atm1.withdraw(300)

atm2.withdraw(500)
atm2.withdraw(250)

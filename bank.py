class bankAccount():
    def __init__(self, money):
        self.money = money
        print('you have Rs.', self.money, 'in your bank account')

    def withdraw(self, amount):
        self.money = self.money - amount
        print('you withdrew Rs.', amount)
        print('now you have Rs.', self.money, 'in your account')

    def deposit(self, depoAmount):
        self.money = self.money + depoAmount
        print('you deposited Rs.', depoAmount)
        print('now you have Rs.', self.money, 'in your account')
    
money = int(input("How much money do you want to start with in your bank account? \n"))
bank1 = bankAccount(money)
withdrawal = int(input("How much money do you want to withdraw from your bank account? \n"))
bank1.withdraw(withdrawal)
depo = int(input("How much money do you want to deposit in your bank account? \n"))
bank1.deposit(depo)

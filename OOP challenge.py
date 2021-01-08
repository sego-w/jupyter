# Python Course OOP Challenge

class Bank:
    def __init__(self,ownerarg,balancearg):
        self.owner = ownerarg
        self.balance = balancearg
    def deposit(self,deposit_amount):
        self.deposit = deposit_amount
        self.balance = self.balance + deposit_amount
    def withdrawal(self,withdraw_amount):
        self.withdraw = withdraw_amount
        self.balance = self.balance - withdraw_amount
exampl1 = Bank("John Cena", 1000000)
exampl1.deposit(13024)
print(f"The owner of the account is {exampl1.owner()}, with a balance of ${exampl1.balance()}"
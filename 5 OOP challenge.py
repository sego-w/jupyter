# Python Course OOP Challenge

class Bank:
    def __init__(self,ownerarg,balancearg=0):
        self.owner = ownerarg
        self.balance = balancearg
    def deposit(self,deposit_amount):
       # self.deposit = deposit_amount
        self.balance = self.balance + deposit_amount
        print(f"The new balance is {self.balance}")
    def withdrawal(self,withdraw_amount):
       # self.withdraw = withdraw_amount
        if withdraw_amount <= self.balance:
            self.balance = self.balance - withdraw_amount
        else:
            print("Error lolz")
        print(f"The new balance is {self.balance}")
    def __str__(self):
        return f"The owner of the account is {exampl1.owner()}, with a balance of ${exampl1.balance()}"
exampl1 = Bank("John Cena", 1000000)
exampl1.withdrawal(500)
# print()
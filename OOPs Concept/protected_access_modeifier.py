class Account:
    _amount=0
    def deposit(self,add):
        self._amount+=add
    def debit(self,sub):
        self._amount-=sub
    def printAmount(self):
        print(self._amount)
class User(Account):
    def calculateTax(self):
        tax=self._amount * 0.2
        print(tax)


u1=User()
u1.deposit(100)
u1.printAmount
u1.debit(50)
u1.printAmount
u1=calculateTax()
# print(b1.amount)  ------>     # Will throw error

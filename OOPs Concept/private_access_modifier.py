class Account:
    __amount=0
    def deposit(self,add):
        self.__amount+=add


    def debit(self,sub):
        self.__amount-=sub

    def printAmount(self):
        print(self.__amount)

b1=Account()
b1.deposit(100)
# print(b1.amount)  ------>     # Will throw error
b1.debit(50)
b1.printAmount
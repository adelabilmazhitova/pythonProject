####1problems
# class Bank():
#     def __init__(self):
#         self.balance=0
#     def deposit(self):
#         s=int(input('vvedite sum- '))
#         self.balance+=s
#
#     def withdraw(self):
#         sum=int(input('scoliko nado- '))
#         if self.balance>=sum:
#             self.balance-=sum
#             print('withdrawal successfully completed')
#             print('ostatok', self.balance)
#         else:
#             print('no money withdrawal')
# B=Bank()
# B.deposit()
# B.withdraw()
###############2problem
class Money():
    def __init__(self, num, amount, cur):
        self.num = num
        self.amount = amount
        self.cur = cur
    def to_tenge (self):
        if(self.cur == "usd"):
            return self.num*self.amount*472
        elif (self.cur == "euro"):
            return self.num*self.amount*457
        elif (self.cur=="rub"):
            return self.num*self.amount*8
        elif(self.cur=="tenge"):
            return self.num*self.amount
        else:
            print('NO, error this command')
class Wallet():
    def __init__(self,sum):
        self.money=[]
        self.money.append(Money.get(sum))
    def get(self, a):
        print(self.money[a])
    def add(self,b):
        self.money[b]
    def __str__(self):
        return self.money
a=Money(40,20,"usd")
b=Money(25,20,"euro")
c=Money(27,20,"rub")
d=Money(30,20,"tenge")
sum=Wallet(a)
sum.add(b)
sum.add(c)
sum.add(d)

d=[a.to_tenge(),b.to_tenge(),c.to_tenge(),d.to_tenge()]
print(sum.__str__())





class Account:

    def __init__(self,balance,acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"was debited")
        print("Total balance:",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"was credited")
        print("Total balance:",self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1 = Account(10000,123)
acc1.debit(5000)
acc1.credit(2000)
print("Balance amount:",acc1.get_balance())
        


from abc import ABC, abstractmethod
class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2



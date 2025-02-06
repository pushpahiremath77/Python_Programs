# How would you design a class to manage bank accounts where
# the account balance should only be accessed or modified through specific methods
class bank:
    def __init__(self,accno,accbalance,accname):
        self.accno = accno
        self.accbalance = accbalance
        self.accname =accnamed
class Account:

    def __init__(self,acc_no,passwd):
        self.acc_no = acc_no
        self.__passwd = passwd

    def reset_passwd(self):
        print(self.__passwd)

    def __hello(self):
        print("Hello Pushpa!")

    def welcome(self):
        self.__hello()
   
acc1 = Account(1234,"abcd")
print(acc1.acc_no)
acc1.reset_passwd()
acc1.welcome()
#acc1.__hello()
        


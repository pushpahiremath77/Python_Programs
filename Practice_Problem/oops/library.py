class Bank:
    b_name = "Syndicate"
    b_id = "123"

    def __init__(self):
        self.accounts = []
        self.next_acc_no = 1

    def create_account(self, customer):
        customer.acc_no = self.next_acc_no
        self.accounts.append(customer)
        self.next_acc_no += 1
        print(f"Account created with account number {customer.acc_no}")

    def display_info(self):
        if self.accounts:
            print("Accounts details")
            for acc in self.accounts:
                print(f"{acc.acc_no} ==> {acc.name}, {acc.age}, {acc.city}, {acc.balance}")

    def withdraw_amount(self, acc, amount):
        acc.balance -= amount
        return acc.balance
    
    def deposite_amount(self, acc, amount):
        acc.balance += amount
        return acc.balance

class Customer:
    def __init__(self, name, age, city, balance):
        self.name = name
        self.age = age
        self.city = city
        self.balance = balance
        self.acc_no = None

    def check_balance(self):
        print(f"{self.balance}")

if __name__ == "__main__":
    bank = Bank()

    acc1 = Customer("Pushpa", 22, "Vijayapura", 10000)
    acc2 = Customer("Disha", 23, "Goa", 5000)
    bank.create_account(acc1)
    bank.create_account(acc2)
    bank.display_info()

    bank.withdraw_amount(acc1, 5000)
    acc1.check_balance()

    bank.deposite_amount(acc1, 2000)
    acc1.check_balance()

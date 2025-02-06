import random

class Bank:
    b_name = "Syndicate"
    b_id = "123"

    def __init__(self):
        self.accounts = []

    def generate_unique_account_number(self):
        while True:
            acc_no = random.randint(1, 99)
            if acc_no not in self.accounts:
                return acc_no
        
    def create_account(self, customer):
        customer.acc_no = self.generate_unique_account_number()
        self.accounts.append(customer)
        print(f"Account created with account number {customer.acc_no}")


    def display_info(self):
        if self.accounts:
            print("Accounts details")
            for acc in self.accounts:
                print(f"{acc.acc_no} ==> {acc.name}, {acc.age}, {acc.city}, {acc.balance}")

    def withdraw_amount(self, acc, amount):
        acc.balance -= amount
        print(f"{acc.name} has withdrawn amount {amount}")
    

    def deposite_amount(self, acc, amount):
        acc.balance += amount
        print(f"{acc.name} has deposited amount {amount}")

class Customer:
    def __init__(self, name, age, city, balance):
        self.name = name
        self.age = age
        self.city = city
        self.balance = balance
        self.acc_no = None

    def check_balance(self):
        print(f"Remained amount in Account: {self.balance}")

if __name__ == "__main__":
    bank = Bank()
    
    acc1 = Customer("Pushpa", 22, "Vijayapura", 10000)
    acc2 = Customer("Disha", 23, "Goa", 5000)
    acc3 = Customer("Ankitha",22,"Bangalore",20000)
    acc4 = Customer("Viju",21,"Belagavi",50000)


    bank.create_account(acc1)
    bank.create_account(acc2)
    bank.create_account(acc3)
    bank.create_account(acc4)

    bank.display_info()

    bank.withdraw_amount(acc1, 5000)
    acc1.check_balance()

    bank.deposite_amount(acc1, 2000)
    acc1.check_balance()

    # bank.withdraw_amount(acc2,100)
    # acc2.check_balance()

    # bank.deposite_amount(acc2,1000)
    # acc2.check_balance()



class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"
    
    def display_elements(self):
        if not self.is_empty():
            return self.stack
        else:
            return "Stack is empty"
    
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"
    
    def is_empty(self):
        return len(self.stack) == 0

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.display_elements())  # Output: [10, 20, 30]
print(stack.top())               # Output: 30
print(stack.pop())               # Output: 30
print(stack.display_elements())  # Output: [10, 20]
print(stack.is_empty())          # Output: False















class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def display_elements(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            for item in self.stack:
                print(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

# Example usage
stack1 = Stack()
stack1.push(10)
stack1.push(20)
stack1.push(30)

print("Elements in stack:")
stack1.display_elements()

print("\nPop operation:")
stack1.pop()

print("\nElements in stack after pop:")
stack1.display_elements()

print("\nTop element in stack:")
print(stack1.top())












def validate_brackets(string):
    stack = []  
    brackets = {'(': ')', '{': '}', '[': ']'} 
    
    for char in string:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    
    return len(stack) == 0

string = input("Enter string: ")

# Call the function and print the result
result = validate_brackets(string)
print(result)

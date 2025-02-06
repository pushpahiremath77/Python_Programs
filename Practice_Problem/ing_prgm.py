
def add_ing(s):

    if len(s)<3:
        return s
    elif s[-3:]=="ing":
        return s +"ly"
    else:
        return s +"ing"

s = input("Enter a string:")
result = add_ing(s)
print(result)

















class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None
    
    def is_empty(self):
        return not self.stack

def validate_brackets(brackets):
    stack = Stack()

    bracket_pairs = {'(': ')', '{': '}', '[': ']'}
    
    for char in brackets:
        if char in bracket_pairs: 
            stack.push(char)
        elif char in bracket_pairs.values():  
            if stack.is_empty() or bracket_pairs[stack.pop()] != char:
                return False
   
    return stack.is_empty()

# Get user input
user_input = input("Enter a string with brackets: ")

# Validate brackets and print the result
if validate_brackets(user_input):
    print("True")
else:
    print("False")








class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

def validate_brackets(brackets):
    stack = Stack()
    # Dictionary to match opening and closing brackets
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in brackets:
        if char in '({[':  # If it's an opening bracket, push to stack
            stack.push(char)
        elif char in ')}]':  # If it's a closing bracket
            # Check if the stack is empty or if the top doesn't match
            if stack.is_empty() or stack.pop() != bracket_pairs[char]:
                return False
    
    # If the stack is empty, all brackets are properly closed
    return stack.is_empty()

# Take user input as a string of brackets
user_input = input("Enter a string of brackets: ")

# Call the function and print the result
print(validate_brackets(user_input))






def validate_brackets(brackets):
    stack = []

    bracket_pairs = {')': '(', '}': '{', ']': '['}
    
    for char in brackets:
        # If the character is one of the opening brackets, push it to the stack
        if char in '({[':
            stack.append(char)
        # If it's a closing bracket, check if the stack is not empty and if it matches the last opened one
        elif char in ')}]':
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()
    
    # If stack is empty, all brackets are properly closed
    return len(stack) == 0

# Take user input as a string of brackets
user_input = input("Enter a string of brackets: ")

# Call the function and print the result
print(validate_brackets(user_input))

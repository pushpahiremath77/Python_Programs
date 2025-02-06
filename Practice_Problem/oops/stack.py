
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
        return not self.stack  

    def top_element(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

stack1 = Stack()
stack1.push(10)
stack1.push(20)
stack1.push(30)

print("Elements in stack:")
stack1.display_elements()

print("\nTop element in stack:")
print(stack1.top_element())

print("\nAfter Pop the top element")
stack1.pop()
stack1.display_elements()













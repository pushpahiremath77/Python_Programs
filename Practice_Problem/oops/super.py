# class Parent:
#     def __init__(self,text):
#         self.text=text

#     def print_message(self):
#         print("Welcome!")

# class Child(Parent):
#     def __init__(self, text):
#         #super().__init__(text)
#         self.text = text

#         super().print_message()

# a1 = Child("Hi")
# a1.print_message()
# print(a1.text)       

class A:
    def display(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")
        super().display()

class C(A):
    def display(self):
        print("Class C")
        super().display()

class D(B, C):
    def display(self):
        print("Class D")
        super().display()

    

d = D()
d.display()


print(D.mro())



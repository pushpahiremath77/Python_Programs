# def swap(a,b):
#     temp=a
#     a=b
#     b=temp
#     return a,b

# a=int(input("a:"))
# b=int(input("b:"))
# print(f"Swapped: {swap(a,b)}")


# def swap(a,b):
#     a,b=b,a
#     return a,b

# a=int(input("a:"))
# b=int(input("b:"))
# print(f"Swapped: {swap(a,b)}")

def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b

a=int(input("a:"))
b=int(input("b:"))
print(f"Swapped: {swap(a,b)}")
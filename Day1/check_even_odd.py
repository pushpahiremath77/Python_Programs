# def check_even_odd(n):
#     if n%2==0:
#         print(f"{n} is even")
#     else:
#         print(f"{n} is odd")

# n=int(input("Enter a number:"))
# check_even_odd(n)


def check_even_odd(n):
    match n%2:
        case 0:
            return "Even"
        case 1:
            return "odd"

n=int(input("Enter a number:"))
print(f"{check_even_odd(n)}")
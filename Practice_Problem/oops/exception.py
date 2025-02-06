try:
    num = int(input("Enter a number:"))
    result = 10/num
    print(f"Result:{result}")

except ZeroDivisionError:
    print("Zero is not allowed")

except ValueError:
    print("Invalid type")




def check_positive(num):
    if num<0:
        raise ValueError("Number must be positive")
    return num

try:
    number = check_positive(5)

except ValueError as a:
    print(a)
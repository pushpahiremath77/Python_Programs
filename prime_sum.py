def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def sum_of_prime(a,b):
    sum=0
    for i in range(a,b+1):
        if is_prime(i):
            sum=sum+i
    return sum

a=int(input("Enter first number:"))
b=int(input("Enter last number:"))

print(f"sum is:{sum_of_prime(a,b)}")
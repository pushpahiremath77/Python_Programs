def is_prime(n):
    if n==1 or n==2:
        return n
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def prime_decorator(func):
    def print_prime(n):
        for i in range(1,func(n)):
            if is_prime(i):
                print(i)        
    return print_prime

@prime_decorator
def prime_num(n):
    return n
prime_num(10)


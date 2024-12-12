# num = int(input("Enter a number:"))
# if(num<2):
#     print("It's not a prime number")
# else:
#     is_prime = True
#     for i in range(2,num):
#         if num%i==0:
#             is_prime=False
#             break
        
#     if is_prime:
#         print(f"{num} is Prime number")
#     else:
#         print(f"{num} is not Prime number")











def is_prime(n):
    if n<2:
        return False
    
    # for i in range(2,n):
    #     if n%i==0:
    #         return False
    # return True

    i=2
    while(i<n):
        if n%i==0:
            return False
        i+=1
    return True



n=int(input("Enter a number:"))
if is_prime(n):
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")











def prime_number(n):
    for num in range(2,n+1):
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num,end=" ")

n=int(input("Enter number to print prime numbers:"))

prime_number(n)


    


  

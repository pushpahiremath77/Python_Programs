# for num in range(1,51):
#     if num%5 == 0 or num%7==0:
#         print(num)

# num = 1
# while(num<51):
#     if num%5==0 or num%7==0:
#         print(num)
#     num+=1


# for i in range(1500,2701):
#     if i%7==0 and i%5==0:
#         print(i,end=" ")

# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print('*',end=" ")
#     print(' ')




for i in range(1,51):
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0 and i%5==0:
        print("FizzBuzz")
    print(i)
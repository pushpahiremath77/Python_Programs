
n=int(input("Enter a number to reverse:"))
temp=n
reverse=0

for i in str(n):
    remainder=n%10
    reverse=reverse*10+remainder
    n=n//10
print(f"Reversed number of {temp} is --> {reverse}")


# i=1
# while n!=0:
#     remainder=n%10
#     reverse=reverse*10+remainder
#     n=n//10
# print(f"Reversed number of {temp} is {reverse}")



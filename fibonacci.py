
# n = int(input("Enter number of terms:"))
# a=0
# b=1
# print("Fibonacci series:")
# for i in range(n):
#     print(a,end=" ")
#     sum=a+b
#     a=b
#     b=sum

print("Using for loop")
a=0
b=1
for i in range(10):
    print(a,end=" ")
    sum=a+b
    a=b
    b=sum
print()

print("Using while loop")
a=0
b=1
i=0
while(i<10):
    print(a,end=" ")
    sum=a+b
    a=b
    b=sum
    i+=1
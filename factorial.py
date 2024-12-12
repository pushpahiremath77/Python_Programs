#for loop
fact =1
for i in range(1,6):
    fact=fact*i
    print(fact)

#while loop
# fact=1
# i=1
# while i<=10:
#     fact=fact*i
#     print(fact)
#     i+=1

#Find factorial of specific number
# n=int(input("Enetr a number:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

n=int(input("Enetr a number:"))
fact=1
i=1
while(i<n+1):
    fact=fact*i
    i+=1
print(fact)
n = 123
n = str(n)
string = ""
for num in n:
    string=num + string
print(string)



reverse = 0
n=-456
negative = n<0
n = abs(n)
while n>0:
    digit = n%10
    reverse = reverse*10 + digit
    n=n//10

if negative:
    reverse = -reverse

print(reverse)





list1 =  [1, 2, 3, 4, 5]
list1.sort(reverse=True)
print(list1)



list1 =  [1, 2, 3, 4, 5]
print(list1[::-1])



list1 =  [1, 2, 3, 4, 5]
list2 = []
for i in range(len(list1)-1,-1,-1):
    list2.append(list1[i])
print(list2)

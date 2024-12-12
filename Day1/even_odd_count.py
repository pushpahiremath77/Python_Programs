num = (1,2,3,4,5,6,7,8,9)
count_odd = 0
count_even = 0
# for i in num:
#     if i % 2 ==0:
#         count_even+=1
#     #else:
#     count_odd+=1

i=0
while(i<len(num)):
    if num[i]%2==0:
        count_even+=1
    else:
        count_odd+=1
    i+=1

print("count of even numbers:",count_even)
print("count of odd numbers:",count_odd)

# n = 5
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end=" ")
#     print()


str1 = "fahat"
dict1 = {}
for char in str1:
    if char in dict1:
        dict1[char] += 1
    else:
        dict1[char] = 1
count = 0
for count in dict1.values():
    if count > 1:
        count += 1

print(count)

# print(len(str))
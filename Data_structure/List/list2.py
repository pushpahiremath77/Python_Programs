list1 = [1,2,3,4,5,6,2,3,1,7,4,2]
list2 = [11,12,13,14,15]
list1.extend(list2)
print(f"Concated :{list1}")

list1.sort(reverse=True)
print(f"Sorted descending:{list1}")

item = 4
list1.append(item)
print(list1)

list1.pop(2)
print(list1)

for i in range(len(list1)):
    print(list1[i],end=" ")

print()
list1.reverse()
print(list1)

count = list1.count(2)
print(count)

new = list1[2:7]
print(new)

list2 = ['D','i','s','h','a','p','u','s','h','p','a']
list2 = list2[::-1]
print(list2)

new_1 = []
for i in range(len(list2)-1,0,-1):
    new_1.append(list2[i])
print(new_1)

pali_list = [1,2,3,4,3,2,1] 
if pali_list == pali_list[::-1]:
    print("Given list is palindrome")
else:
    print("Given list is not palindrome")

#Move zeros to end of list
list1 = [0,1,0,3,0,12,0]
for num in list1:
    if num == 0:
        list1.remove(num)
        list1.append(num)
print(list1)


#Move zeros to beginning of list
list1 = [0,1,0,3,0,12,0,-1]
for item in list1:
    if item!=0:
        list1.remove(item)
        list1.append(item)
print(list1)



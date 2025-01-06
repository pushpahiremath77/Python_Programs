def two_product(list1,n):
    result =[]
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i]*list1[j]==n:
                result.append(list1[i])
                result.append(list1[j])
    return result

list1 = [1, 2, 3, 4, 13, 5]
num = 39
result = two_product(list1,num)
print(result)
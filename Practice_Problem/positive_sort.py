def positive_sort(list1):
    positives = sorted([num for num in list1 if num>0])
    pos_index = 0
    result = []
    for num in list1:
        if num>0:
            result.append(positives[pos_index])
            pos_index+=1
        else:
            result.append(num)
    return result
 
list1 = [6, 3, -2, 5, -8, 2, -2]
result = positive_sort(list1)
print(result)
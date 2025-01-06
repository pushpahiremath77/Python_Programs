def list_of_multiples(n,length):
    list1 = []
    for i in range(1,length+1):
        list1.append(n*i)
    return list1

result = list_of_multiples(12,10)
print(result)
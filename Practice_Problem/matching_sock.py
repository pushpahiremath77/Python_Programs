def matching_sock(list1):
    pairs = 0
    sock_count = {}
    for item in list1:
        if item not in sock_count:
            sock_count[item]=1
        else:
            sock_count[item]+=1

    for count in sock_count.values():
        pairs += count//2
    return pairs

list1 = [10, 20, 20, 10, 10, 30, 50, 10, 20]
result = matching_sock(list1)
print(result)
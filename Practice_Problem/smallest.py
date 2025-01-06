#Largest
list1 = [7, 4, 6, 3, 9, 1]
list1.sort()
k=1
print(list1[-k])



#smallest 
list1 = [7, 4, 6, 3, 9, 1]
list1.sort(reverse=True)
k=1
print(list1[-k])



#kth smallest
def kth_smallest(list1,k):
    for _ in range(k):
        min_val = min(list1)
        list1.remove(min_val)
    return min_val

list1 = [7, 4, 6, 3, 9, 1]
k=3
result = kth_smallest(list1[:],k)
print(f"{k}rd smallest is :{result}")




#kth largest
def kth_largest(list1,k):
    for _ in range(k):
        max_val = max(list1)
        list1.remove(max_val)
    return max_val

list1 = [7, 4, 6, 3, 9, 1]
k=3
result = kth_largest(list1[:],k)
print(f"{k}rd largest is :{result}")
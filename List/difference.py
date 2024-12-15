def list_difference(lst1, lst2):
    return list(set(lst1) - set(lst2))

lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 4, 5, 6, 7]
print("Difference between lists:", list_difference(lst1, lst2))

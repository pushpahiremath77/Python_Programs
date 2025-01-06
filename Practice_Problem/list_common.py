def sum_common(lst1,lst2,lst3):
    union = set(lst1) & set(lst2) & set(lst3)
    return sum(union)


lst1 = [1, 2, 3] 
lst2 = [5, 3, 2]
lst3 = [7, 3, 2]
union = sum_common(lst1,lst2,lst3)
print(union)


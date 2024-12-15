def remove_duplicates(list1):
    list1 = list(set(list1))
    print("List after removing duplicates--->",list1)

list1 = [1, 2, 2, 3, 4, 4, 5]
remove_duplicates(list1)
















# def remove_duplicates(list1):
#     return [list(x) for x in set(tuple(x) for x in list1)]

# list1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# print("New list without duplicates:", remove_duplicates(list1))
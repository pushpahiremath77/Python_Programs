def common_element(list1, list2):
    # for item in list1:
    #     if item in list2:
    #         return True
    # return False

    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 3, 9, 4, 10]

print("Common elements:", common_element(list1, list2))